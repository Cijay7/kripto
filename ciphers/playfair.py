class PlayfairCipher:
    def __init__(self, key):
        self.key = key
        self.matrix = self.create_matrix(key)

    def create_matrix(self, key):
        # Create a 5x5 matrix for the Playfair Cipher
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        key = ''.join(sorted(set(key), key=key.index)) # Remove duplicates while maintaining order
        key += ''.join(filter(lambda x: x in alphabet, alphabet))
        key = key.replace('J', 'I')  # Replace J with I
        return [list(key[i:i+5]) for i in range(0, 25, 5)]

    def display_matrix(self):
        for row in self.matrix:
            print(' '.join(row))

    def encrypt(self, plaintext):
        # Implement the encryption algorithm here
        pass

    def decrypt(self, ciphertext):
        # Implement the decryption algorithm here
        pass
