excelente = 0
ruim = 0

# Para fazer a pesquisa com 10 pessoas durante um teste,
# troque 50 por 10 na linha abaixo.(fiz isso pela praticidade de não precisar digitar 50 vezes;)
total_pessoas = 10

for numero in range(total_pessoas):
    print("\nEntrevistado", numero + 1)

    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Digite 1, 2 ou 3: "))

    if opiniao == 1:
        excelente = excelente + 1
        print("Obrigado", nome, "pela resposta!")
    elif opiniao == 2:
        print("Obrigado", nome, "pela resposta!")
    elif opiniao == 3:
        ruim = ruim + 1
        print("Obrigado", nome, "pela resposta!")
    else:
        print("Opção inválida. Essa resposta não foi contada.")

print("\nResultado da pesquisa:")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
print("Quantidade de respostas BOM:", total_pessoas - excelente - ruim)
