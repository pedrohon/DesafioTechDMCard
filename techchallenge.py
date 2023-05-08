import time

# Aqui está a função que verifica se a expressão está correta ou incorreta, por isso, "ci"
def ci(x):
    x = x.strip()
    expressao = list(x)

    # verifica se a linha é vazia. Incluí também o /n, pois, pode ser uma linha vazia após ou entre linhas

    # por fim, se não há parenteses na expressão, ela já é dada como verdadeira
    if not "(" in x and not ")" in x:
        return True
    
    # a partir dessa condição, iniciei, as verificações caractere a caractere
    else:
        # "p" para associar a ideia de "parenteses"
        p = 0
        for c in expressao:
            # comparo o elemento "c" com o símbolo "("
            if c == "(":
                p = p + 1
            # se ele for verdadeiro, somo 1 na variavel "p"

            # se o primeiro não for verdadeiro, comparo o elemento "c" com o símbolo ")"
            elif c == ")":
                p = p - 1
                # se "p" for negativo, há mais ")" do que "("
                if p < 0:
                    return False

            # para qualquer outro caractere, ele verifica se há mais ")" do que "("
            else:
                if p < 0:
                    return False

        # retorna falso se p ≠ de 0
            # se for maior possui mais "(" do que ")"
            # se for menor possui mais ")" do que "("
        return p == 0


caminho = input("Digite o nome do arquivo: ")

antes = time.time()

# aqui é definido o arquivo que será verificado
with open(caminho, "r") as expressoes:

    # nesse passo, atribui a uma variavel "texto" o conteudo do arquivo recebido em forma de lista
    texto = expressoes.readlines()
    
    # chama o arquivo "resultado.txt", caso não exista, será criado
    with open("resultado.txt", "w") as resultado:

        '''
        para armazenar se a expressão está correta ou incorreta, criei a lista "conteudo"
        verifico se o a expressao é verdadeira ou falsa, e faço a atribuição nessa lista
        '''
        conteudo = []
        for e in texto:
            if ci(e):
                conteudo.append("correct")
            else:
                conteudo.append("incorrect")

        # por fim, imprimo no arquivo "resultado" linha a linha os elementos da lista conteudo
        resultado.writelines('\n'.join(conteudo))
    
depois = time.time()
print("Demorou: ", (depois - antes), "seg")