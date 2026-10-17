def lerLinhas(l):
    # Dicionário para agrupar registros por CPF
    cpfes = {}

    i = 0
    while i < len(l):
        # Ignora linhas vazias
        if not l[i].strip():
            i += 1
            continue

        # Identifica em qual posição o CPF se encontra com base na estrutura
        if "Título" in l[i]:
            if i + 3 < len(l):
                # Pega o texto do CPF e divide pelo ponto (.) para pegar o primeiro bloco
                partes_cpf = l[i + 3].split('.')
                i += 5
            else:
                break
        else:
            if i + 2 < len(l):
                partes_cpf = l[i + 2].split('.')
                i += 4
            else:
                break

        # Tenta converter o primeiro bloco do CPF para inteiro
        try:
            inicio_cpf = int(partes_cpf[0])
        except (IndexError, ValueError):
            inicio_cpf = 0

        # Cria a estrutura do eleitor
        eleitor = {"inicio_cpf": partes_cpf}

        # Agrupa pelo início do CPF
        if inicio_cpf not in cpfes:
            cpfes[inicio_cpf] = []
        cpfes[inicio_cpf].append(eleitor)

    # Exibe os resultados após processar todas as linhas
    print("\n" + "=" * 40 + "\n")
    print("Inícios de CPF encontrados:")

    i = 0

    for inicio_cpf in sorted(cpfes.keys()):
        if (i%6 == 0):
            print("\n")

        if inicio_cpf < 10:
            print(f"00{inicio_cpf}",end="  ")
        elif inicio_cpf < 100: 
            print(f"0{inicio_cpf}",end="  ")
        else:
            print(f"{inicio_cpf}",end="  ")
        i+=1


def eleitores():
    print(
        "Insira os registros abaixo.\n"
        "Para encerrar a entrada e gerar o relatório, digite 'sair' e dê Enter:\n"
    )

    linhas = []
    try:
        while True:
            linha = input()
            if linha.strip().lower() == "sair":
                break
            linhas.append(linha)
    except EOFError:
        pass

    if linhas:
        lerLinhas(linhas)


if __name__ == "__main__":
    eleitores()