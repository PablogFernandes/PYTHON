from hashlib import sha256

usuario_padrao = "c6fcb8c1b253b876428aed7fda470f9dc19fe36a5c1b5664c3819d39d156b4f0"
senha_padrao = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"

usuario_digitado = input("digite seu usuário: ").encode("ascii")
senha_digitado = input("digite sua senha: ").encode("ascii")
usuario_digitado = sha256(usuario_digitado).hexdigest()
senha_digitado = sha256(senha_digitado).hexdigest()

if senha_digitado == senha_padrao and usuario_digitado == usuario_padrao:
    print("bem vindo ao curso FATEC")
else:
    print("senha ou usuário incorreto")