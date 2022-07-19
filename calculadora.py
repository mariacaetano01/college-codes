'''
PROBLEMA PROPOSTO
Construir uma função que resolva uma equação polinomial de quinto grau a partir do método
de verificação e refinnamento proposto durante as aulas.
    • Faça a busca no intervalo de -20 até 20, com incrementos de 0,5
    • Use o critério de convegência tomando m = 6

ENTRADAS
Para escolher quais serão os 6 coeficientes da equação, pegue as três primeira letras do
seu primeeiro e último nome (Tabela registrada no Clasroom)
    • nome = Maria Fernanda Caetano
    • M = 1.65
    • A = -3.510
    • R = 0.571
    • C = -17.1
    • A = -3.510
    • E = 11.18

SAÍDAS
    • A equação formada, conforme orientado na tabela #OK
    • Os intervalos da primeira etapa do método #OK
    • As soluções encontradas e asociadas a cada intervalo
    • O gráfico da iteração vs. o erro |xi-x(i-1)|
'''

import matplotlib.pyplot


def funcao(x):
    # funcao com base nos critérios do exercício
    return(1.65*(x**5)) + (-3.510*(x**4)) + (0.571*(x**3)) + (-17.1*(x**2)) + (-3.510*x) + 11.18


def contador(inicial, final, incremento):
    # O contador vai definir um intervalo de x para calcular y

    contador = 0
    while inicial <= final:
        contador += 1
        inicial += incremento
    return contador


def valores_de_y(inicial, contador, incremento):
    # Os valores de y representam os valores de f(x) a serem usados no identificador

    lista_y = []
    lista_x = []
    x = inicial
    for _ in range(contador):
        # valores dos coeficientes conforme tabela no Classroom
        y = funcao(x)
        lista_y.append(y)
        lista_x.append(x)
        x += incremento
    return [lista_x, lista_y]


def identificador(listas):
    # O identificador consiste em encontrar mudança de sinais entre os
    # resultados da equação

    lista_valores_x = listas[0]
    lista_valores_y = listas[1]
    intervalos_a = []
    intervalos_b = []
    for pos, _ in enumerate(lista_valores_y):
        if pos > 0:
            if (lista_valores_y[pos] < 0 and lista_valores_y[(pos-1)] > 0) or (lista_valores_y[pos] > 0 and lista_valores_y[(pos-1)] < 0):
                intervalos_a.append(lista_valores_x[pos-1])
                intervalos_b.append(lista_valores_x[pos])

    intervalos = tuple(zip(intervalos_a, intervalos_b))
    intervalos = list(map(list, intervalos))
    return intervalos


def refinador(intervalos):
    # O refinador consiste em diminuir cada intervalo até atender o critério
    # de convergência e encontrar a aproximação da raiz da equação

    raizes = []
    erro = []
    iteracao = []
    contador = i = 0

    for _ in intervalos:
        intervalo = intervalos[contador]
        x = intervalo[0]
        y1 = funcao(x)
        x = intervalo[1]
        y2 = funcao(x)
        if y2 < y1:
            intervalo = [intervalo[1], intervalo[0]]
        while abs((intervalo[0]) - (intervalo[1])) > 10**(-6):
            x = (intervalo[0]+intervalo[1])/2  # x = media in while
            y = funcao(x)
            if y < 0:
                intervalo[0] = x
            if y > 0:
                intervalo[1] = x
            iteracao.append(i)
            i += 1
            erro.append(abs((intervalo[0]) - (intervalo[1])))
        raizes.append(x)
        contador += 1
    return raizes,erro,iteracao


def main():
    print('EQUAÇÃO POLINOMIAL: MARIA CAETANO')
    print('y = (1,65*(x^5)) + (-3,510*(x^4)) + (0,571*(x^3))+ (-17,1*(x^2)) + (-3,510*x) + 11,18')
    print('')

    valor_inicial = -20
    valor_final = 20
    incremento = 0.5

    print('INTERVALOS COM MUDANÇA DE SINAL:')
    intervalo_de_contagem = contador(valor_inicial, valor_final, incremento)
    valores = valores_de_y(valor_inicial, intervalo_de_contagem, incremento,)
    identifica = identificador(valores)
    print(identifica)
    print(' ')

    print('RAÍZES REFINADAS DA FUNÇÃO:')
    refina,erro,iteracao = refinador(identifica)
    print(refina)
    print(' ')

    # print('GRÁFICO VALORES DE X vs VALORES DE Y')
    # matplotlib.pyplot.plot(valores[0],valores[1])
    # matplotlib.pyplot.show()

    print ('GRÁFICO INTERCÇÃO vs. ERRO (TODOS INTERVALOS')
    print ('Cada pico do gráfico representa um novo intervalo')
    matplotlib.pyplot.title ('GRÁFICO INTERAÇÃO vs. ERRO')
    matplotlib.pyplot.xlabel("Quantidade de Iterações")
    matplotlib.pyplot.ylabel("Erro = |xi-x(i-1)|")
    matplotlib.pyplot.plot(iteracao,erro)
    matplotlib.pyplot.show()

if __name__ == "__main__":
    main()
