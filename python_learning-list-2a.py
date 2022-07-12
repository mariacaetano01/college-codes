# Lista de exercícios - Condições

def maior3(a, b, c):

        #receba 3 valores e retorna o maior deles
        #argumento: a (float) = primeiro valor;
        #argumento: b (float) = segundo valor;
        #argumento: c (float) = terceiro valor;
        #retorna: float, o maior entre os 3 valores.
   
    if a > b and a >c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def menor3(a, b, c):

        #recebe 3 valores e retorna o menor deles;
        #argumento: a (float) = primeiro valor;
        #argumento: b (float) = segundo valor;
        #argumento:  (float) = terceiro valor;
        #retorna: float, menor entre os 3 valores.

    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


def testa_lados(a, b, c):

        #receba 3 lados de um triângugo;
        #informe se os valores podem ser um triângulo;
        #indique, se sim, se é um triângulo isóceles, equilátero ou escaleno;
        #argumento: a (float) = primeiro lado;
        #argumento: b (float) = segundo lado;
        #argumento: c (float) = terceiro lado;
        #retorna: string, texto indicando resultado
        #confomidade com testes no final desse arquivo.
                #se a soma de dois lados não é maior ou igual ao terceiro
                #então não forma triângulo;
                #três lados iguauis: equiláetro
                #três lados diferentes: escaleno
                #dois lados igual e um diferente: isósceles

    if not (a+b>c and a+c>b and b+c>a):
        return "Não forma um triângulo"

    elif a==b and a==c and b==c:
        return "Triângulo equilátero"    
    elif a==b and a!=c and b!=c:
        return "Triângulo isósceles"
    elif b==c and b!=a and c!=a:
        return "Triângulo isósceles"
    elif a==c and a!=b and c!=b:
        return "Triângulo isósceles"
    else:
        return "Triângulo escaleno"

def ano_bissexto(ano):

        #determine se é um ano bissexto ou não;
        #argumento: ano(int) = texto formato 4 digitos;
        #retorna: bool true/false caso seja bissexto ou não.
            #o ano é bissexto caso seja divisível por 4;
            #se for um ano centenário (ex: 1900, 2000), deve ser divisível por 400;
    

    if ano % 4 != 0 or (ano % 400 != 0 and ano % 100 == 0):
        return False
    else:
        return True


def maior_dia_do_mes(mes, ano):

            #retorna ultimo dia do mes para um determinado ano e mes;
            #os valores possíveis são: 28,29,30,31;
            #devem ser considerados os anos bissextos;
            #uma função separar para dizer se é ano bissexto;
            #argumento: mes(int) = mes formato 2 digitos;
            #agumento: ano(int) = ano formato 4 digitos;
            #retorna: valor int indicando ultimo dia valido no mes/ano;
    
    ano = ano_bissexto (ano) 

    if mes == 2 and ano == True:
        return 29
    elif mes == 2 and ano == False:
        return 28
    elif mes == 1:
        return 31
    elif mes == 3:
        return 31
    elif mes == 4:
        return 30
    elif mes == 5:
        return 31
    elif mes == 6:
        return 30
    elif mes == 7:
        return 31
    elif mes == 8:
        return 31
    elif mes == 9:
        return 30
    elif mes == 10:
        return 31
    elif mes == 11:
        return 30
    elif mes == 12:
        return 31
    elif mes > 12:
        return 0

def data_valida(data):

        #recebe uma string no formato dd/mm/aaaa;
        #informa bool indicando se data é valida ou não;
        #verifica sem ano é bissexto + outros detalhes;
        #conferir testes no final do arquivo para + detalhes;
        #argumento: data (string) = data formato "dd/mm/aaaa"
        #retorna: bool true/false, indicando se é valido ou não

    dia,mes,ano = data.split ('/')
    dia_numero = int(dia)
    mes_numero = int(mes)
    ano_numero = int(ano)
    quantidade = maior_dia_do_mes (mes_numero,ano_numero)

    if quantidade == 0:
        return False
    elif mes_numero < 1 or mes_numero > 12 or mes_numero == 00:
        return False
    elif dia_numero == 00 or mes_numero == 00 or ano_numero == 0000:
        return False
    elif dia_numero < 1 or dia_numero > quantidade:
        return False
    elif ano_numero == 0000:
        return False
    else:
        return True


def baskara(a, b, c):
    from math import sqrt
        #calcule as raizes de uma equação de 2º grau;
        #ax2 + bx + c;
            #se o usuário informar valor a = 0 é equação de 1º grau;
            #se o delta calculado for negativo, a equanção é imaginária:
                #devolva tupla vazia;
            #se o delta calculado = 0, só tem uma raiz real:
                #devolva uma tupla de elemento único;
            #se o delta for positivo, a equação possui 2 raizes reais:
                #devolva uma tupla de 2 elementos;
        #argumento: a (float) = valor a da equação;
        #argumento: b (float) = valor b da equação;
        #argumento: c (float) = valor c da equação;
        #retorna: tupla de float contando os valores das raízes
        #sendo uma raíz, duas rapizes ou tupla vazia caso não tenha raíz.

    if a == 0:
        return (-c / b,)

    delta = b**2 - 4 * a * c
    if delta < 0:
        return ()
    elif delta == 0:
        return ((-b + sqrt(delta)) / 2,)
    else:
        return ((-b + sqrt(delta)) / 2, (-b - sqrt(delta)) / 2)
    
    
def acrescimo_nota_bb(nota_sozinho, nota_com_ajuda):
    
        #recebe uma nota do LITTLE BROTHER antes de receber ajuda e a nota
        #depois que o BIG BROTHER ajudou e retorna acrescimo que o BIG BROTHER
        #receberá em sua nota pela ajuda;
        #o acréscinmo pe de 1/4 da diferença das notas (se for positivo);
        #argumento: nota_sozinho(float) = a nota que o aluino tirou sem ajuda;
        #argumento: nota_com_ajuda(float) = " após ter sido ajudado;
        #retorna: float = acréscimo da nota obtido pelo aluno que ajudou

    BIG_BROTHER = ((nota_com_ajuda) - (nota_sozinho))/4

    if nota_com_ajuda < nota_sozinho:
        return 0
    if nota_com_ajuda> nota_sozinho:
        return round(BIG_BROTHER,1)
 


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = "\033[31m%s" % ("Falhou")
    else:
        prefixo = "\033[32m%s" % ("Passou")
        acertos += 1
    print(
        "%s Esperado: %s \tObtido: %s\033[1;m" % (prefixo, repr(esperado), repr(obtido))
    )


def main():

    print("Maior de 3 valores:")
    test(maior3(a=1, b=2, c=3), 3)
    test(maior3(a=1.01, b=1.1, c=1.02), 1.1)
    test(maior3(a=0, b=-1, c=-2), 0)
    test(maior3(a=-100, b=0, c=100), 100)


    print("Menor de 3 valores:")
    test(menor3(a=1, b=2, c=3), 1)
    test(menor3(1.01, 1.02, 1.1), 1.01)
    test(menor3(0, -1, -2), -2)
    test(menor3(-100, 0, 100), -100)

    print("Triângulos:")
    test(testa_lados(7, 1, 2), "Não forma um triângulo")
    test(testa_lados(7, 2, 1), "Não forma um triângulo")
    test(testa_lados(1, 7, 2), "Não forma um triângulo")
    test(testa_lados(1, 2, 7), "Não forma um triângulo")
    test(testa_lados(2, 1, 7), "Não forma um triângulo")
    test(testa_lados(2, 7, 1), "Não forma um triângulo")
    test(testa_lados(2, 2, 2), "Triângulo equilátero")
    test(testa_lados(3, 3, 3), "Triângulo equilátero")
    test(testa_lados(2, 3, 4), "Triângulo escaleno")
    test(testa_lados(2, 4, 3), "Triângulo escaleno")
    test(testa_lados(3, 4, 2), "Triângulo escaleno")
    test(testa_lados(3, 2, 4), "Triângulo escaleno")
    test(testa_lados(2, 3, 3), "Triângulo isósceles")
    test(testa_lados(3, 2, 2), "Triângulo isósceles")
    test(testa_lados(3, 3, 2), "Triângulo isósceles")
    test(testa_lados(3, 2, 3), "Triângulo isósceles")

    print("Ano bissexto:")
    test(ano_bissexto(1000), False)
    test(ano_bissexto(1200), True)
    test(ano_bissexto(1004), True)
    test(ano_bissexto(1040), True)
    test(ano_bissexto(2012), True)
    test(ano_bissexto(2014), False)

    print("Maior dia do mês:")
    test(maior_dia_do_mes(1, 2014), 31)
    test(maior_dia_do_mes(3, 2014), 31)
    test(maior_dia_do_mes(4, 2014), 30)
    test(maior_dia_do_mes(5, 2014), 31)
    test(maior_dia_do_mes(6, 2014), 30)
    test(maior_dia_do_mes(7, 2014), 31)
    test(maior_dia_do_mes(9, 2014), 30)
    test(maior_dia_do_mes(10, 2014), 31)
    test(maior_dia_do_mes(11, 2014), 30)
    test(maior_dia_do_mes(12, 2014), 31)
    test(maior_dia_do_mes(2, 2014), 28)
    test(maior_dia_do_mes(2, 2016), 29)

    print("Valida datas:")
    test(data_valida(data="01/01/2014"), True)
    test(data_valida(data="31/01/2014"), True)
    test(data_valida(data="00/00/0000"), False)
    test(data_valida(data="30/04/2014"), True)
    test(data_valida(data="31/04/2014"), False) #linha 5
    test(data_valida(data="30/09/2014"), True)
    test(data_valida(data="31/09/2014"), False) #linha 7
    test(data_valida(data="30/06/2014"), True)
    test(data_valida(data="31/06/2014"), False) #linha 9
    test(data_valida(data="30/11/2014"), True)
    test(data_valida(data="31/11/2014"), False) #linha 11
    test(data_valida(data="32/01/2014"), False) #linha 12
    test(data_valida(data="01/01/0000"), False) #linha 13
    test(data_valida(data="01/13/2014"), False)
    test(data_valida(data="01/00/2014"), False)
    test(data_valida(data="29/02/2014"), False) #linha 16
    test(data_valida(data="29/02/2016"), True)

    print("Báskara:")
    test(baskara(1, 4, 4), (-2.0,))
    test(baskara(1, 5, 4), (-1.0, -4.0))
    test(baskara(0, 4, 2), (-0.5,))
    test(baskara(4, 4, 4), ())

    print("Acréscimo BB:")
    test(acrescimo_nota_bb(1, 10), 2.2)
    test(acrescimo_nota_bb(7, 6), 0.0)
    test(acrescimo_nota_bb(0, 10), 2.5)
    test(acrescimo_nota_bb(6.9, 7.1), 0.0)

if __name__ == "__main__":
    main()
    print(
        "\n%d Testes, %d Ok, %d Falhas: Nota %.1f"
        % (total, acertos, total - acertos, float(acertos * 10) / total)
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
