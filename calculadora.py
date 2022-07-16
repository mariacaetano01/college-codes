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

def contador(inicial, final, incremento):
    # O contador vai definir um intervalo de x para calcular y

    contador = 0
    while inicial <= final:
        contador += 1
        inicial += incremento
    return contador


def valores_de_y(inicial, contador, incremento):
    # Os valores de y representam os valores de f(x) a serem
    # usados no identificador

    lista_y = []
    lista_x = []
    x = inicial
    for _ in range(contador):
        # valores dos coeficientes conforme tabela no Classroom
        y = (1.65*(x**5)) + (-3.510*(x**4)) + (0.571*(x**3)) + \
            (-17.1*(x**2)) + (-3.510*x) + 11.18
        lista_y.append(y)
        lista_x.append(x)
        x += incremento
    return lista_y


def identificador(lista_y):
    # O identificador consiste em encontrar mudança de sinais entre os
    # resultados da equação

    lista_valores_y = lista_y
    intervalos_1 = []
    intervalos_2 = []
    for pos, _ in enumerate(lista_valores_y):
        if (lista_valores_y[pos] < 0 and lista_valores_y[(pos-1)] > 0) or (lista_valores_y[pos] > 0 and lista_valores_y[(pos-1)] < 0):
            intervalos_1.append(lista_valores_y[pos-1])
            intervalos_2.append(lista_valores_y[pos])

    del intervalos_1[0]
    del intervalos_2[0]
    intervalos = zip(intervalos_1, intervalos_2)
    return list(intervalos)


def refinador(intervalos):
    # O refinador consiste em diminuir cada intervalo até atender o
    # critério de convergência e encontrar a aproximação da raiz da
    # equação
    return 'Ainda não esá pronto'


def main():
    print('EQUAÇÃO POLINOMIAL: MARIA CAETANO')
    print('y = (a*(x^5)) + (b*(x^4)) + (c*(x^3)) + (d*(x^2)) + (e*x) + f')
    print('y = (1,65*(x^5)) + (-3,510*(x^4)) + (0,571*(x^3))+ (-17,1*(x^2)) + (-3,510*x) + 11,18')
    print('')

    valor_inicial = -20
    valor_final = 20
    incremento = 0.5
    intervalo_de_contagem = contador(valor_inicial, valor_final, incremento)

    valores = valores_de_y(valor_inicial, intervalo_de_contagem, incremento)
    identifica = identificador(valores)
    print('INTERVALOS COM MUDANÇA DE SINAL:')
    print(identifica)
    print(' ')


if __name__ == "__main__":
    main()

