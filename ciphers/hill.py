import numpy as np

class HillCipher:
    def __init__(self, key):
        self.key = key
        self.key_matrix = self.create_matrix(key)
        self.inverse_key_matrix = self.modulus_inverse(self.key_matrix)

    def create_matrix(self, key):
        # Convert the key string into a matrix
        key_length = int(len(key) ** 0.5)
        return np.array([[ord(key[i * key_length + j]) % 26 for j in range(key_length)] for i in range(key_length)])

    def modulus_inverse(self, matrix):
        # Find the inverse of the key matrix modulo 26
        det = int(np.round(np.linalg.det(matrix)))
        det_inv = self.modular_inverse(det, 26)
        matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % 26
        return matrix_mod_inv

    def modular_inverse(self, a, m):
        # Extended Euclidean Algorithm to find modular inverse
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

    def encrypt(self, plaintext):
        # Encryption logic here
        ... # Implementation to be filled in

    def decrypt(self, ciphertext):
        # Decryption logic here
        ... # Implementation to be filled in