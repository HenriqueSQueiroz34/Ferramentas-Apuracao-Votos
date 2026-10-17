analise = input("Qual o texto que deseja contar (Dica: se tiver um caracter que separa, coloca também)? ")

print( 
      "Insira os registros abaixo.\n"
      "Para encerrar a entrada e gerar o relatório, digite 'sair' e dê Enter:\n"
  )

contador=0

try:
    while True:
      linha = input()
      # Verifica se a linha é 'sair'
      if linha.strip().lower() == "sair":
        break
      if analise in linha:
        contador +=1

except EOFError:
    pass

print("Contador total: ",contador)