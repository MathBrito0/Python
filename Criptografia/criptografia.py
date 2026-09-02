from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import time

inicio = time.time()

# chave DES (8 bytes = 64 bits, sendo 56 efetivos)
chave = get_random_bytes(8)

# mensagem
mensagem = b"Mensagem secreta"

# criptografar
cipher = DES.new(chave, DES.MODE_CBC)
cifrado = cipher.encrypt(pad(mensagem, DES.block_size))

print("IV:", cipher.iv)
print("Cifrado:", cifrado)

# descriptografar
cipher_dec = DES.new(chave, DES.MODE_CBC, iv=cipher.iv)
decifrado = unpad(cipher_dec.decrypt(cifrado), DES.block_size)

fim = time.time()

bench = fim - inicio

print("Decifrado:", decifrado.decode())
print({bench})



#------------------------------------------









from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import time

inicio = time.time()

# chave (16 ou 24 bytes)
chave = DES3.adjust_key_parity(get_random_bytes(24))

# mensagem
mensagem = b"Mensagem secreta"

# criptografar
cipher = DES3.new(chave, DES3.MODE_CBC)
cifrado = cipher.encrypt(pad(mensagem, DES3.block_size))

print("IV:", cipher.iv)
print("Cifrado:", cifrado)

# descriptografar
cipher_dec = DES3.new(chave, DES3.MODE_CBC, iv=cipher.iv)
decifrado = unpad(cipher_dec.decrypt(cifrado), DES3.block_size)

fim = time.time()

bench = fim - inicio

print("Decifrado:", decifrado.decode())
print({bench})








#-----------------------------------------------











from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import time

inicio = time.time()

# chave (16, 24 ou 32 bytes)
chave = get_random_bytes(32)

# mensagem
mensagem = b"Mensagem secreta"

# criptografar
cipher = AES.new(chave, AES.MODE_CBC)
cifrado = cipher.encrypt(pad(mensagem, AES.block_size))

print("IV:", cipher.iv)
print("Cifrado:", cifrado)

# descriptografar
cipher_dec = AES.new(chave, AES.MODE_CBC, iv=cipher.iv)
decifrado = unpad(cipher_dec.decrypt(cifrado), AES.block_size)

fim = time.time()

bench = fim - inicio

print("Decifrado:", decifrado.decode())
print({bench})







#--------------------------------------





from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import time

inicio = time.time()


# ==============================
# 1. Gerar chaves (ECC)
# ==============================
alice_private = ec.generate_private_key(ec.SECP256R1())
alice_public = alice_private.public_key()


bob_private = ec.generate_private_key(ec.SECP256R1())
bob_public = bob_private.public_key()


# ==============================
# 2. Segredo compartilhado
# ==============================
alice_shared = alice_private.exchange(ec.ECDH(), bob_public)
bob_shared = bob_private.exchange(ec.ECDH(), alice_public)


# ==============================
# 3. Derivar chave AES
# ==============================
key = HKDF(
algorithm=hashes.SHA256(),
length=32,
salt=None,
info=b'ecdh'
).derive(alice_shared)


# ==============================
# 4. Criptografia AES
# ==============================
iv = os.urandom(12) # ideal para GCM


cipher = Cipher(algorithms.AES(key), modes.GCM(iv))
encryptor = cipher.encryptor()


message = b"Mensagem com ECDH + AES"
ciphertext = encryptor.update(message) + encryptor.finalize()


tag = encryptor.tag


print("Cifrado:", ciphertext)


# ==============================
# 5. Descriptografia
# ==============================
cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag))
decryptor = cipher.decryptor()


plaintext = decryptor.update(ciphertext) + decryptor.finalize()

fim = time.time()

bench = fim - inicio

print("Decifrado:", plaintext)
print({bench})






#--------------------------------------------







# Necessário a biblioteca Cryptography
# pip install cryptography


from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import time

inicio = time.time()


# 1. Gerar chaves
private_key = rsa.generate_private_key(
  public_exponent=65537,
  key_size=8192
)


public_key = private_key.public_key()


# 2. Mensagem
message = b"Oi, segredo!"


# 3. Criptografar (chave pública)
ciphertext = public_key.encrypt(
  message,
  padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
  )
)


# 4. Descriptografar (chave privada)
plaintext = private_key.decrypt(
  ciphertext,
  padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
  )
)

fim = time.time()

bench = fim - inicio

print("Original:", message)
print("Decifrado:", plaintext)
print({bench})
