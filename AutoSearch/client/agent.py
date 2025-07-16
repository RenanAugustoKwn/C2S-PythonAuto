def conversar():
    print("Olá! Estou aqui pra te ajudar a encontrar um carro!")
    filtros = {}
    
    marca = input("De qual marca você procura? ").strip()
    if marca: filtros['marca'] = marca

    cor = input("Tem alguma cor preferida? ").strip()
    if cor: filtros['cor'] = cor

    combustivel = input("Tipo de combustível (Gasolina, Etanol, Flex)? ").strip()
    if combustivel: filtros['combustivel'] = combustivel

    ano = input("Ano aproximado ou exato? ").strip()
    if ano: filtros['ano'] = ano

    return filtros
