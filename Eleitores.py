def zonas(t):
  partes = t.split("|")
  zonaparte = ""
  for p in partes:
    if "Zona" in p:
      zonaparte = p
      break
  zona = int(zonaparte.split(":")[1].strip())
  return zona


def lerLinhas(l):
  # Eleitores por zona
  zonaele = {}

  i = 0
  while i < len(l):
    # Linhas vazias
    if not l[i].strip():
      i += 1
      continue

    if "Título" in l[i]:
      if i + 4 < len(l):
        titulo = l[i + 1]
        cpf = l[i + 2]
        nasc = l[i + 3]
        nome = l[i + 4]
        i += 5
      else:
        break
    else:
      if i + 3 < len(l):
        titulo = l[i]
        cpf = l[i + 1]
        nasc = l[i + 2]
        nome = l[i + 3]
        i += 4
      else:
        break

    try:
      zona = zonas(titulo)
    except (IndexError, ValueError):
      zona = 0

    eleitor = {
        "titulo": titulo,
        "cpf": cpf,
        "nascimento": nasc,
        "nome": nome,
    }

    if zona not in zonaele:
      zonaele[zona] = []
    zonaele[zona].append(eleitor)

  # Exibe os resultados apenas APÓS processar todas as linhas
  print("\n" + "=" * 40 + "\n")
  for zona in sorted(zonaele.keys()):
    print(f"------------------- Zona: {zona} -------------------")
    for eleitor in zonaele[zona]:
      print("Título de eleitor:")
      print(eleitor["titulo"])
      print(eleitor["cpf"])
      print(eleitor["nascimento"])
      print(eleitor["nome"])
      print()


def eleitores():
  print(
      "Insira os registros abaixo.\n"
      "Para encerrar a entrada e gerar o relatório, digite 'sair' e dê Enter:\n"
  )

  linhas = []
  try:
    while True:
      linha = input()
      # Verifica se a linha é 'sair'
      if linha.strip().lower() == "sair":
        break
      linhas.append(linha)
  except EOFError:
    pass

  # Processa e imprime tudo após o término da digitação
  if linhas:
    lerLinhas(linhas)


if __name__ == "__main__":
  eleitores()