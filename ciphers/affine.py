class AffineCipher:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        if self.gcd(a, 26) != 1:
            raise ValueError("a must be coprime to 26")

    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                x = ord(char.lower()) - ord('a')
                encrypted_char = (self.a * x + self.b) % 26
                ciphertext += chr(encrypted_char + ord('a'))
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        a_inverse = self.mod_inverse(self.a, 26)
        for char in ciphertext:
            if char.isalpha():
                y = ord(char.lower()) - ord('a')
                decrypted_char = (a_inverse * (y - self.b)) % 26
                plaintext += chr(decrypted_char + ord('a'))
            else:
                plaintext += char
        return plaintext

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def mod_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1
