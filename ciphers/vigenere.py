class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword

    def encrypt(self, plaintext):
        encrypted = ""
        keyword_repeated = self._repeat_keyword(plaintext)
        for p, k in zip(plaintext, keyword_repeated):
            if p.isalpha():
                offset = ord(k) - ord('A')
                if p.islower():
                    encrypted += chr((ord(p) - ord('a') + offset) % 26 + ord('a'))
                else:
                    encrypted += chr((ord(p) - ord('A') + offset) % 26 + ord('A'))
            else:
                encrypted += p  # Non-alpha characters are added directly
        return encrypted

    def decrypt(self, ciphertext):
        decrypted = ""
        keyword_repeated = self._repeat_keyword(ciphertext)
        for c, k in zip(ciphertext, keyword_repeated):
            if c.isalpha():
                offset = ord(k) - ord('A')
                if c.islower():
                    decrypted += chr((ord(c) - ord('a') - offset) % 26 + ord('a'))
                else:
                    decrypted += chr((ord(c) - ord('A') - offset) % 26 + ord('A'))
            else:
                decrypted += c  # Non-alpha characters are added directly
        return decrypted

    def _repeat_keyword(self, text):
        keyword_length = len(self.keyword)
        keyword_repeated = (self.keyword * (len(text) // keyword_length + 1))[:len(text)].upper()
        return keyword_repeated
