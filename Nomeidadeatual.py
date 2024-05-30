idadeatual = False

while not idadeatual:

   print("Insira seu nome completo:")
   print("Insira sua data de nascimento (apenas o ano):")

   try:

       nome = input("Nome: ")
    
       if not nome.replace(" ", "").isalpha():
           raise ValueError("O nome deve conter apenas letras")

       ano = int(input("Ano de nascimento: "))

       if (ano >= 1922) and (ano <= 2021):
           res = 2022 - ano

           idadeatual = True

           print("Nome:", nome, "Idade:", res)

       else:
           print("Informe corretamente o ano de nascimento (entre 1922 e 2021)")

   except ValueError as e:
       print(e)
