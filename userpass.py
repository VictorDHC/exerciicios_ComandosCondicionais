user = input("Qual seu usuário?: ")
passw = input("Qual sua senha?: ")
if user == "admin" and passw == "1234":
    print("Sucesso. ")
elif user == "convidado":
    print("Acesso Restrito")
else:
    print("Acesso Negado")
