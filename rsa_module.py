from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Random import new as Random
from base64 import b64encode
from base64 import b64decode

class RSA_Cipher:
  def generate_key(self,key_length):
    assert key_length in [1024,2048,4096]
    rng = Random().read
    self.key = RSA.generate(key_length,rng)

  def encrypt(self,data):
    plaintext = b64encode(data.encode())
    rsa_encryption_cipher = PKCS1_OAEP.new(self.key)
    ciphertext = rsa_encryption_cipher.encrypt(plaintext)
    return b64encode(ciphertext).decode()

  def decrypt(self,data):
    ciphertext = b64decode(data.encode())
    rsa_decryption_cipher = PKCS1_OAEP.new(self.key)
    plaintext = rsa_decryption_cipher.decrypt(ciphertext)
    return b64decode(plaintext).decode()
