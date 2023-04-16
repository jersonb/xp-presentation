def soma(valor1, valor2):
    return valor1 + valor2

assert soma(1, 1) == 2

def exibe_mensagem(valor):
    return len(valor) > 5

assert exibe_mensagem("123456")
assert not exibe_mensagem("12345")