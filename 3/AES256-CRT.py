import pyaes
import hashlib



class AES256:

    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()  # The key must be 256 bits
        self.iv = 27928000841356984726233357955409624076659936569171526749940232512655365051623

    def encrypt(self, pt):
        aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.iv))
        ct = aes.encrypt(pt)
        return ct

    def decrypt(self, ct):
        aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.iv))
        pt = aes.decrypt(ct)
        return pt


if __name__ == '__main__':

	plain_text = "H" * 300
	print("plain text: ", plain_text, "  len: ", len(plain_text))


	test = AES256("TEST")
	cipher_text = test.encrypt(plain_text)
	print("cipher text: ", cipher_text, "  len: ", len(cipher_text))  # length of cipher text == length of plain text
