def conversar():
    print("Procurar Carro!")
    filtros = {}
    
    marca = input("Qual a marca do carro que voce deseja? ").strip()
    if marca: filtros['marca'] = marca

    cor = input("Qual a cor? ").strip()
    if cor: filtros['cor'] = cor

    combustivel = input("Tipo de combustível (Gasolina, Etanol, Flex)? ").strip()
    if combustivel: filtros['combustivel'] = combustivel

    ano = input("Ano aproximado ou exato? ").strip()
    if ano: filtros['ano'] = ano

    return filtros
