print("bem vindo, cadastre-se")
print("======================")

usuario = input("digite seu nome de usurario: ").lower
senha = input("digite sua senha: ")

print("cadastro realizado com sucesso")
deseja_fazer_login = input("deseja fazer login? (s/n) ")

if deseja_fazer_login == "s":


  for i in range(3):
    usuario_local = input("digite seu nome de usurario: ")
    senha_local = input("digite sua senha: ")



    if usuario_local == usuario and senha == senha_local:
        print("acesso permitido")
        break

    elif ((usuario_local != usuario) or (senha != senha_local)) and (i == 2):
       print("tentativas esgotadas")
       break

    elif usuario_local != usuario or senha != senha_local:
        print(f"usuario ou senha incorretos, restam {(2 - i)}  tente novamente")
