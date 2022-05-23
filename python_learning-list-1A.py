#Lista de Exercícios 1A - variáveis e operadores

#recebe dois valores e devolve a soma deles
def somainteiros (a,b):
    s = a + b
    return s

#recebe valor em metro e devolve em mm
def mmm (m):
    mm = m * 1000
    return mm

#recebe distância e velocidade e devolve tempo para percorrer
def tempoparapercorrer (km,v):
    horas = (km / v) 
    return round (horas,2)

#recebe salário e aumento em % e devolve novo salário
def novosalário (atual,porcento):

    x = (atual * porcento) / 100
    y = atual + x
    return round(y,2)

#recebe valor e % de desconto e devolve novo valor
def valordesconto (preço,desconto):
    valor = (desconto/100) * preço
    novo = preço - valor
    return round(novo,2)

#recebe uma data com dias, horas, minutos e segundos e devolve total em seg
def diasparasegundos (d,h,m,s):
    seg = (d * 86400) + (h * 3600) + (m * 60) + s
    return seg

#receve valor em Celsius e devole em Fahrenheit
def CparaF(c):
    fah = c * 1.8 + 32
    return round(fah,2)

#recebe valor em Fahrenheit e devolve em Celsius
def FparaC(f):
    cel = (f - 32) / 1.8
    return round(cel,2)

#recebe dias que o carro ficou alugado e km rodados e devolve valor a pagar
def valoraluguel (dias,km):
    valordia = 60
    valorkm = 0.15
    v = dias * valordia + km * valorkm
    return v

#recebe anos fumados e cigarros fumados por dia e devolve dias perdidos
def diasperdidos (anos,cigarros):

    diasnoano = 365
    minutosporcigarro = 10

    dias = anos * diasnoano * cigarros * minutosporcigarro
    total = dias // 1440
    return total

#eleva dois a 10 e devolve quantidade de algarismos
def doiselevadoadez ():

    valor = len(str(2 ** 10000))
    return valor

#recebe notas, gera media e diz se o aluno esta aprovado ou reprovado
def aprova (prova1,prova2,exercicio1,exercicio2):

    pesoprova = 7
    pesoex = 3

    parcial1 = (prova1 * pesoprova) + (exercicio1 * pesoex)
    parcial11 = parcial1 / 10
    parcial2 = (prova2 * pesoprova) + (exercicio2 * pesoex) 
    parcial22 = parcial2 / 10
    mediaaluno = (parcial11 + parcial22) / 2

    if mediaaluno == 7:
        mediaaluno = True
    elif mediaaluno > 7:
        mediaaluno = True
    else:
        mediaaluno = False
    
    return mediaaluno

#recebe horas trabalhadas e valor por hora e devolve salário liq
def salarioliquido (valorhora,horas):

    salariobruto = horas * valorhora

    perc_inss = 8 / 100
    perc_ir = 11 / 100
    perc_sindicato = 5 / 100

    inss = salariobruto * perc_inss
    ir = salariobruto * perc_ir
    sindicato = salariobruto * perc_sindicato
    descontos = inss + ir + sindicato 

    salarioliquido = salariobruto - descontos

    return round(salarioliquido)

#recebe quantidade de ovos e arredonda para quantidade de duzias
def duzias (unidades):
    from math import ceil

    duzia = ceil(unidades / 12)
    return duzia

#recebe m2 de cobertura a pintar e devolve quantas latas de tinta comprar
def latasdetinta(m2):

    capacidadelata = 3 * 18
    latas = m2 // capacidadelata
    if m2 % capacidadelata:
        latas +=  1 
    
    return latas

#recebe número e decompoe 
def decompornumero (num):
    
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    return c,d,u

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = f"\033[31m{'Falhou'}"
    else:
        prefixo = f"\033[32m{'Passou'}"
        acertos += 1
    print(f"{prefixo} Esperado: {esperado} \tObtido: {obtido}\033[1;m")


def main():
    print("Soma dois inteiros:")
    test(somainteiros(0, 0), 0)
    test(somainteiros(-1, 0), -1)
    test(somainteiros(1, 1), 2)
    test(somainteiros(0, -1), -1)
    test(somainteiros(10, 10), 20)
    test(somainteiros(-10, -10), -20)
    test(somainteiros(-10, 20), 10)

    print("Metros para milimetros:")
    test(mmm(0), 0)
    test(mmm(1), 1000)
    test(mmm(1.8), 1800)
    test(mmm(1.81), 1810)

    print(
        "Tempo gasto para percorrer um distancia a uma velocidade"
        "constante(linha reta):"
    )
    test(tempoparapercorrer(1330, 20), 66.50)
    test(tempoparapercorrer(1000, 100), 10.00)
    test(tempoparapercorrer(1000, 123), 8.13)
    test(tempoparapercorrer(100000, 201), 497.51)

    print("Aumento salarial baseado na porcentagem de aumento:")
    test(novosalário(1330, 20), 1596.00)
    test(novosalário(1000, 0), 1000.00)
    test(novosalário(1000.10, 123), 2230.22)
    test(novosalário(0.0, 200), 0.00)

    print("Desconto do preco atual baseado na porcentagem do desconto:")
    test(valordesconto(1330, 20), 1064.00)
    test(valordesconto(1000, 0), 1000.00)
    test(valordesconto(1000.10, 5.5), 945.09)
    test(valordesconto(0.0, 200), 0.00)

    print("Dias,horas,minutos e segundos para segundos:")
    test(diasparasegundos(0, 0, 0, 0), 0)
    test(diasparasegundos(0, 0, 0, 1), 1)
    test(diasparasegundos(0, 0, 0, 30), 30)
    test(diasparasegundos(0, 0, 1, 0), 60)
    test(diasparasegundos(0, 0, 1, 1), 61)
    test(diasparasegundos(0, 1, 0, 0), 3600)
    test(diasparasegundos(0, 0, 60, 0), 3600)
    test(diasparasegundos(1, 0, 0, 0), 86400)
    test(diasparasegundos(1, 1, 1, 1), 90061)
    test(diasparasegundos(0, 23, 59, 59), 86399)
    test(diasparasegundos(10, 20, 59, 1), 939541)

    print("Celsius para Fahrenheit:")
    test(CparaF(0), 32.00)
    test(CparaF(100), 212.00)
    test(CparaF(30), 86.00)
    test(CparaF(300), 572.00)
    test(CparaF(-100), -148.00)
    test(CparaF(1), 33.80)

    print("Fahrenheit para Celsius:")
    test(FparaC(32), 0)
    test(FparaC(212), 100)
    test(FparaC(30), -1.11)
    test(FparaC(300), 148.89)
    test(FparaC(-100), -73.33)
    test(FparaC(1), -17.22)

    print("Preco a pagar pelo aluguel do carro:")
    test(valoraluguel(10, 100), 615.00)
    test(valoraluguel(13, 133), 799.95)
    test(valoraluguel(1, 0), 60.00)
    test(valoraluguel(3, 79), 191.85)

    print("Total de dias que perdeu de viver por ter fumados:")
    test(diasperdidos(10, 10), 253)
    test(diasperdidos(13, 13), 428)
    test(diasperdidos(0, 110), 0)
    test(diasperdidos(3, 79), 600)

    print("Calcula a quantidade de algarismos que há em dois elevado a dez mil:")
    test(doiselevadoadez(), 3011)

    print("Média final:")
    test(aprova(10, 10, 0, 0), True)
    test(aprova(0, 0, 10, 10), False)
    test(aprova(10, 10, 10, 10), True)
    test(aprova(0, 0, 5, 0), False)
    test(aprova(8.0, 7.0, 9.0, 8.0), True)

    print("Salário líquido:")
    test(salarioliquido(10, 80), 608)
    test(salarioliquido(100, 30), 2280)
    test(salarioliquido(2.5, 300), 570)
    test(salarioliquido(5, 120), 456)

    print("Dúzias:")
    test(duzias(12), 1)
    test(duzias(24), 2)
    test(duzias(11), 1)
    test(duzias(23), 2)

    print("Latas de tinta:")
    test(latasdetinta(10), 1)
    test(latasdetinta(100), 2)
    test(latasdetinta(560), 11)
    test(latasdetinta(50001), 926)

    print("Decompor número:")
    test(decompornumero(326), (3, 2, 6))
    test(decompornumero(320), (3, 2, 0))
    test(decompornumero(310), (3, 1, 0))
    test(decompornumero(305), (3, 0, 5))
    test(decompornumero(300), (3, 0, 0))
    test(decompornumero(100), (1, 0, 0))
    test(decompornumero(101), (1, 0, 1))
    test(decompornumero(311), (3, 1, 1))
    test(decompornumero(111), (1, 1, 1))
    test(decompornumero(12), (0, 1, 2))
    test(decompornumero(25), (0, 2, 5))
    test(decompornumero(20), (0, 2, 0))
    test(decompornumero(10), (0, 1, 0))
    test(decompornumero(21), (0, 2, 1))
    test(decompornumero(11), (0, 1, 1))
    test(decompornumero(16), (0, 1, 6))
    test(decompornumero(1), (0, 0, 1))
    test(decompornumero(7), (0, 0, 7))


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
