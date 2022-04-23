from hashlib import sha256

cpf = b"1232456789-10"
print(cpf)
cpf = sha256(cpf)
print(cpf.hexdigest())
