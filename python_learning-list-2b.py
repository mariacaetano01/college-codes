# Lista de exercícios - Condições (Adicional)

from math import ceil

def situacao_aluno(nota1, nota2, nota3, faltas, aulas_ministradas):
    #A média do aluno é dada pela média aritmética simples entre as 3 notas.
    #Se o aluno tiver mais de 25% de faltas, está automaticamente reprovado 
    #por faltas (RF). Se ele tiver média abaixo de 7.0, está em Exame Final.
    #Se tiver média acima de 7.0 e frequencia igual ou superior a 75% está 
    #aprovado (AP).

    #Args:
        #nota1 (float): 1a nota
        #nota2 (float): 2a nota
        #nota3 (float): 3a nota
        #faltas (int): número de faltas
        #aulas_ministradas (int): quantidade de aulas ministradas
    #Returns:
    #string: a situação do aluno

    media = (nota1+nota2+nota3) / 3
    frequencia = (faltas*100) / aulas_ministradas

    if media >= 7 and frequencia <= 25:
        return ('AP')
    elif media < 7 and frequencia <= 25:
        return ('EF')
    else:
        return ('RF')

def aumento_preco(preco):
    #Calcula o aumento do preço, baseado no seguinte critério:
    # - até 280 (inclusive): aumento de 20%
    # - até 700 (inclusive): aumento de 15%
    # - até 1500 (inclusive): aumento de 10%
    # - acima de 1500: aumento de 5%

    # Argumentos: preco (float) =  o preço atual do produto

    # Retorna: tupla de floats: preco atual, percentual de aumento, 
    # valor do aumento e novo preço, todos com duas casas decimais.

    if preco <= 280:
        aumento = preco*(20/100) 
        porcento = 20
        novo_valor = preco + aumento
    elif preco <= 700:
        aumento = preco*(15/100)
        porcento = 15
        novo_valor = preco + aumento
    elif preco <= 1500: 
        aumento = preco*(10/100)
        porcento = 10
        novo_valor = preco + aumento
    else:
        aumento =  preco*(5/100)
        porcento = 5
        novo_valor = preco + aumento
    
    return (preco, porcento, aumento, novo_valor)


def idade_canina(idade_humana, porte_do_cao):
    # É sabido que os caẽs amadurecem mais rapidamente do que os seres
    # humanos (na verdade, alguns serem humanos parecem nunca amadurecer).
    # Calcule sua idade canina, baseada nos seguintes fatores:
        #cães de porte pequeno: fator 5;
        #cães de porte médio: fator 6;
        #cães grandes: fator 7.
    # Argumentos:
        #idade_humana (int): a idade do ser humano
        #porte_do_cao (string): um texto informando o porte do cão (veja os testes para detalhes)
    # Retorna:
        #int: a idade canina do ser humano

    fator_p = 5
    fator_m = 6
    fator_g = 7

    if porte_do_cao == "pequeno":
        return int(idade_humana/fator_p) 
    elif porte_do_cao == "medio":
        return int(idade_humana/fator_m) 
    elif porte_do_cao == "grande":
        return int(idade_humana/fator_g)

def aumento_salario(salario):

    # Calcule o aumento de salário de acordo com a seguinte tabela:
    # - até 1 SM(inclusive): aumento de 20%
    # - de 1 até 2 SM(inclusive): aumento de 15%
    # - de 2 até 5 SM(inclusive): aumento de 10%
    # - acima de 5 SM: aumento de 5%
         # Salário mínimo para referência: R$ 724,00

    # Argumentos: salario (float) =  o salario atual
    # Retorna: float = novo salário, com duas casas decimais.

    salario_min = 724.00

    if salario <= salario_min:
        return (((salario*20)/100)+salario)
    elif salario <= (2*salario_min):
        return (((salario*15)/100)+salario)
    elif salario <= (5*salario_min):
        return (((salario*10)/100)+salario)
    else:
        return round ((((salario*5)/100)+salario),2)



def nota_para_conceito(nota):

    # Converta a nota para conceito, conforme a tabela abaixo:
    # Nota                     Conceito
    # Entre 10.0 e 9.0            A
    # Entre 8.9 e 8.0             B
    # Entre 7.9 e 7.0             C
    # Entre 6.9 e 6.0             D
    # Entre 5.9 e zero            E

    # Argumento nota(float) =  a nota, com 1 casa decimal
    # Retorna: string = o conceito correspondente

    if 0 <= nota <= 5.9:
        return 'E'
    elif 6 <= nota <= 6.9:
        return 'D'
    elif 7 <= nota <= 7.9:
        return 'C'
    elif 8 <= nota <= 8.9:
        return 'B'
    else:
        return 'A'


def imc(peso, altura):

    # Escreva uma função que calcula o índice de massa corporal (imc = peso / altura ** 2),
    # de acordo com a seguinte tabela:

    # imc <= 18.5: "Subpeso"
    # imc <= 25.0: "Normal"
    # imc <= 30.0: "Sobrepeso"
    # imc > 30: "Obeso"

    # Argumentos: peso (float) =  peso em Kg
    # Argumentos: altura (float): altura em metros
    # Retorna: string =  índice de massa corporal

    divisao = peso / (altura*altura)

    if divisao <= 18.5:
        return 'Subpeso'
    elif 18.5 < divisao <= 25:
        return 'Normal'
    elif 25 < divisao <= 30:
        return 'Sobrepeso'
    else:
        return 'Obeso' 


def converte_hora_24_para_12(horario):

    #Recebe um horário no formato 24 horas e retorna no
    #formato 12 horas (am/pm).
        # - am: antes do meio-dia
        #pm: depois do meio-dia
    #Para detalhes, consulte:
    # https://pt.wikihow.com/Converter-o-Hor%C3%A1rio-do-Formato-24h-Para-12h

    # Argumento: horario (string) =  um horário no formato 24 horas
    # Retorna: string = horario no formato 12 horas (am/pm)

    hora,minuto = horario.split(':')
    hora = int(hora)

    if 1 <= hora < 12:
        return (f'{hora}:{minuto} am')
    elif 12 == hora:
        return (f'{hora}:{minuto} pm')
    elif 12 < hora <= 23:
        return (f'{hora-12}:{minuto} pm')
    elif hora == 00:
        return (f'{hora+12}:{minuto} am')

def converte_hora_12_para_24(horario):

    # Recebe um horário no formato 12 horas (am/pm) e retorna no formato 24 horas.
        # - am: antes do meio-dia
        # - pm: depois do meio-dia
    # Para detalhes, consulte:
    # https://pt.wikihow.com/Converter-o-Hor%C3%A1rio-do-Formato-24h-Para-12h

    # Argumento: horario (string) = um horário no formato 12 horas (am/pm)
    # Retorna: string = horario no formato 24 horas

    hora,minuto = horario.split(':')
    minuto,parte = minuto.split(' ')
    hora = int(hora)

    if parte == 'pm' and hora != 12:
        return (f'{hora+12}:{minuto}')
    elif parte == 'pm' and hora == 12:
        return (f'{hora}:{minuto}')
    elif (parte == 'am' and hora != 12) and hora < 10:
        return (f'0{hora}:{minuto}')
    elif (parte == 'am' and hora != 12) and hora > 10:
        return (f'{hora}:{minuto}')
    elif parte == 'am' and hora == 12:
        return (f'00:{minuto}')
    else:
        return 'algo deu errado'



def conta_combustivel(qtde_litros, tipo_combustivel, tipo_pagamento):
    
    #O posto Tabajara está vendendo combustíveis com a seguinte tabela de preços:
        #a. Tabela de preços
            #Alcool: R$ 3,159
            #Gasolina: R$ 3,739
            #Diesel: 3,090
    #b. Se o pagamento for feito à vista ou débito, o cliente recebe um desconto 
        #de 10% sobre o valor total
    #c. Escreva um função que leia o número de litros vendidos, o tipo de 
        #combustível (gasolina, álcool, diesel), e o tipo de pagamento 
        #(à vista, débito, crédito), calcule e devolva o valor total da compra.

    # Args:
        #qtde_litros (float): quantidade de litros vendida
        #tipo_combustivel (string): uma letra indicando o tipo de combustível
        #tipo_pagamento (string): uma letra, indicando o tipo de pagamento

    # Returns:
        #float: o valor a ser pago, com duas casas decimais

    preco_a = round((qtde_litros*3.159),2)
    preco_g = round((qtde_litros*3.739),2)
    preco_d = round((qtde_litros*3.090),2)
    desconto_a = round(((preco_a*10)/100),2)
    desconto_g = round(((preco_g*10)/100),2)
    desconto_d = round(((preco_d*10)/100),2)

    if tipo_combustivel == 'a':
        if tipo_pagamento == 'v' or tipo_pagamento == 'd':
            return round((preco_a - desconto_a),2)
        else:
            return preco_a
    elif tipo_combustivel == 'g':
        if tipo_pagamento == 'v' or tipo_pagamento == 'd':
            return round((preco_g - desconto_g),2)
        else:
            return preco_g
    elif tipo_combustivel == 'd':
            if tipo_pagamento == 'v' or tipo_pagamento == 'd':
                return round((preco_d - desconto_d),2)
            else:
                return preco_d
    else:
        return 'Algo deu errado'

def comprar_frutas(morango=0, uva=0):

    # Uma fruteira está vendendo frutas com a seguinte tabela de preços:
    #           Até 5 Kg                Acima de 5 Kg
    # Morango   R$ 2,50 por Kg          R$ 2,20 por Kg
    # Uva       R$ 1,80 por Kg          R$ 1,50 por Kg

    # Se o cliente comprar mais de 8 Kg em frutas ou o valor total da
    # compra ultrapassar R$ 25,00, receberá ainda um desconto de 10%
    # sobre este total.

    # Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
    # quantidade (em Kg) de uvas adquiridas e escreva o valor a ser
    # pago pelo cliente.

    # Argumentos:
        #morango (float): a quantidade de morangos, em Kg
        #uva (float): a quantidade de uvas, em Kg

    # Retorna:
        #float: o preço a pagar, com 2 casas decimais

    #valores estipulados no excercício  
    valor_mor = 2.50 
    valor_mor_5kg = 2.20
    valor_uva = 1.80
    valor_uva_5kg = 1.50

    #preço das frutas separadas
    preco_morango = (morango * valor_mor)
    preco_mor_5kg = (morango * valor_mor_5kg)
    preco_uva = (uva * valor_uva)
    preco_uva_5kg = (uva * valor_uva_5kg)

    #preço das frutas juntas
    preco_junto = (preco_morango + preco_uva)
    preco_junto_5kg = (preco_mor_5kg + preco_uva_5kg)

    #desconto para frutas > 25,00
    desconto_junto = round((preco_junto - ((preco_junto*10)/100)),2)
    desconto_junto_5kg = round((preco_junto_5kg - ((preco_junto_5kg*10)/100)),2)
    desconto_mor = (preco_mor_5kg - (preco_mor_5kg*10)/100)
    desconto_uva = (preco_uva_5kg - (preco_uva_5kg*10)/100)
    

    #resolução só com morango
    if morango != 0 and uva == 0:
        if morango <= 5:
            return round(preco_morango,2)
        elif 8 >= morango:
            return round(preco_mor_5kg,2)
        elif morango > 8 or preco_mor_5kg > 25:
            return round(desconto_mor,2)

    #resolução só com uva
    if morango == 0 and uva != 0:
        if uva <= 5:
            return round(preco_uva,2)
        elif 8 >= uva > 5:
            return round(preco_uva_5kg,2)
        elif uva > 8 and preco_junto_5kg < 25:
            return round(desconto_uva,2)
        elif uva > 8 or preco_mor_5kg > 25:
            return round(desconto_uva,2)

    #resolução com os dois juntos
    if (morango + uva) < 5:
        return round((preco_morango + preco_uva),2)
    if 5 < (morango+uva) <= 8:
        return round((preco_junto),2)
    if (morango+uva) > 8 and (preco_junto) < 25:
        return round((desconto_junto),2)
    if (morango+uva) >= 8 and (desconto_junto) > 25:
        return round((desconto_junto_5kg),2)

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
    print("Situacao aluno:")
    test(situacao_aluno(10, 10, 10, 18, 72), "AP")
    test(situacao_aluno(7, 7, 7, 18, 72), "AP")
    test(situacao_aluno(6, 7, 8, 18, 72), "AP")
    test(situacao_aluno(7, 7, 6, 18, 72), "EF")
    test(situacao_aluno(7, 7, 6.9, 18, 72), "EF")
    test(situacao_aluno(5, 7, 7, 18, 72), "EF")
    test(situacao_aluno(10, 10, 10, 19, 72), "RF")
    test(situacao_aluno(10, 10, 10, 20, 72), "RF")
    test(situacao_aluno(0, 0, 0, 30, 72), "RF")

    print("Aumento preço:")
    test(aumento_preco(100), (100, 20, 20.0, 120.0))
    test(aumento_preco(1500), (1500, 10, 150.0, 1650.0))
    test(aumento_preco(3000), (3000, 5, 150.0, 3150.0))

    print("Idade canina:")
    test(idade_canina(40, "pequeno"), 8)
    test(idade_canina(40, "medio"), 6)
    test(idade_canina(40, "grande"), 5)

    print("Aumento salarial:")
    # até 1 SM: 20%
    test(aumento_salario(500.00), 600.00)
    test(aumento_salario(724.00), 868.80)
    # 1-2 SM: 15%
    test(aumento_salario(725.00), 833.75)
    test(aumento_salario(1448.00), 1665.20)
    # 2-5 SM: 10%
    test(aumento_salario(1449.00), 1593.90)
    test(aumento_salario(3620.00), 3982.00)
    # >5 SM: 5%
    test(aumento_salario(3621.00), 3802.05)
    test(aumento_salario(4000.00), 4200.00)

    print("Nota para conceito:")
    test(nota_para_conceito(10.0), "A")
    test(nota_para_conceito(9.1), "A")
    test(nota_para_conceito(9.0), "A")
    test(nota_para_conceito(8.9), "B")
    test(nota_para_conceito(8.1), "B")
    test(nota_para_conceito(8.0), "B")
    test(nota_para_conceito(7.9), "C")
    test(nota_para_conceito(7.1), "C")
    test(nota_para_conceito(7.0), "C")
    test(nota_para_conceito(6.9), "D")
    test(nota_para_conceito(6.1), "D")
    test(nota_para_conceito(6.0), "D")
    test(nota_para_conceito(5.9), "E")
    test(nota_para_conceito(5.1), "E")
    test(nota_para_conceito(5.0), "E")
    test(nota_para_conceito(4.9), "E")
    test(nota_para_conceito(4.0), "E")

    print("IMC")
    test(imc(50, 1.80), "Subpeso")
    test(imc(80, 1.80), "Normal")
    test(imc(90, 1.80), "Sobrepeso")
    test(imc(110, 1.80), "Obeso")
    test(imc(50, 1.50), "Normal")

    print("Converte hora 24 para 12:")
    # 1- Adicione 12 à meia-noite e finalize com “am”.
    test(converte_hora_24_para_12("00:00"), "12:00 am")
    test(converte_hora_24_para_12("00:01"), "12:01 am")
    test(converte_hora_24_para_12("00:59"), "12:59 am")

    # 2- Coloque "am" nos horários entre “1:00” e “11:59”.
    # Retire o zero à esquerda.
    test(converte_hora_24_para_12("01:00"), "1:00 am")
    test(converte_hora_24_para_12("01:01"), "1:01 am")
    test(converte_hora_24_para_12("11:00"), "11:00 am")
    test(converte_hora_24_para_12("11:59"), "11:59 am")

    # Adicione “pm” ao intervalo entre “12:00” e “12:59”.
    test(converte_hora_24_para_12("12:00"), "12:00 pm")
    test(converte_hora_24_para_12("12:01"), "12:01 pm")
    test(converte_hora_24_para_12("12:59"), "12:59 pm")

    # Subtraia 12 dos horários entre “13:00” e “23:59” e finalize com “pm”.
    # Não acrescente zeros à esquerda.
    test(converte_hora_24_para_12("13:00"), "1:00 pm")
    test(converte_hora_24_para_12("13:01"), "1:01 pm")
    test(converte_hora_24_para_12("23:00"), "11:00 pm")
    test(converte_hora_24_para_12("23:59"), "11:59 pm")

    # print("Converte hora 12 para 24:")
    # # 1- Use “00:00” para representar a meia-noite.
    test(converte_hora_12_para_24("12:00 am"), "00:00")
    test(converte_hora_12_para_24("12:01 am"), "00:01")
    test(converte_hora_12_para_24("12:59 am"), "00:59")

    # 2- Apague o “am” das horas entre "1:00 am" e "11:59 am".
    # Acrescente um zero à esquerda se a hora for de um dígito apenas.
    test(converte_hora_12_para_24("1:00 am"), "01:00")
    test(converte_hora_12_para_24("1:01 am"), "01:01")
    test(converte_hora_12_para_24("9:01 am"), "09:01")
    test(converte_hora_12_para_24("11:00 am"), "11:00")
    test(converte_hora_12_para_24("11:59 am"), "11:59")

    # 3- Deixe o horário do meio-dia igual e simplesmente remova o “pm”.
    test(converte_hora_12_para_24("12:00 pm"), "12:00")
    test(converte_hora_12_para_24("12:01 pm"), "12:01")
    test(converte_hora_12_para_24("12:59 pm"), "12:59")

    # 4- Some 12 horas ao período entre "1:00 pm" e "11:59 pm" e apague o “pm”.
    test(converte_hora_12_para_24("1:00 pm"), "13:00")
    test(converte_hora_12_para_24("1:01 pm"), "13:01")
    test(converte_hora_12_para_24("11:00 pm"), "23:00")
    test(converte_hora_12_para_24("11:59 pm"), "23:59")

    print("Conta combustível:")
    test(conta_combustivel(1, "a", "c"), 3.16)
    test(conta_combustivel(10, "a", "c"), 31.59)
    test(conta_combustivel(1, "g", "c"), 3.74)
    test(conta_combustivel(10, "g", "c"), 37.39)
    test(conta_combustivel(1, "d", "c"), 3.09)
    test(conta_combustivel(10, "d", "c"), 30.90)
    test(conta_combustivel(1, "a", "d"), 2.84)
    test(conta_combustivel(10, "a", "d"), 28.43)
    test(conta_combustivel(1, "g", "d"), 3.37)
    test(conta_combustivel(10, "g", "d"), 33.65)
    test(conta_combustivel(1, "d", "d"), 2.78)
    test(conta_combustivel(10, "d", "d"), 27.81)
    test(conta_combustivel(10, "a", "v"), 28.43)
    test(conta_combustivel(10, "g", "v"), 33.65)
    test(conta_combustivel(10, "d", "v"), 27.81)

    print("Comprar frutas:")
    # Teste de zeros:
    test(comprar_frutas(), 0)
    test(comprar_frutas(morango=0), 0)
    test(comprar_frutas(uva=0), 0)
    test(comprar_frutas(morango=0, uva=0), 0)
    test(comprar_frutas(uva=0, morango=0), 0)
    test(comprar_frutas(morango=0), 0)

    # Testes só com morango:
    test(comprar_frutas(morango=1, uva=0), 2.50)
    test(comprar_frutas(morango=2, uva=0), 5.00)
    test(comprar_frutas(morango=4, uva=0), 10.00)
    test(comprar_frutas(morango=5, uva=0), 12.50)
    #Testes só com morangos, muda a faixa:
    test(comprar_frutas(morango=6, uva=0), 13.20)
    test(comprar_frutas(morango=5.1, uva=0), 11.22)
    test(comprar_frutas(morango=8, uva=0), 17.60)
    # Testes só com morangos, recebe desconto por peso:
    test(comprar_frutas(morango=9, uva=0), 17.82)
    test(comprar_frutas(morango=10, uva=0), 19.80)
    # Testes só com morangos, recebe desconto por preço:
    test(comprar_frutas(morango=20, uva=0), 39.60)

    # Testes só com uva:
    test(comprar_frutas(morango=0, uva=1), 1.80)
    test(comprar_frutas(morango=0, uva=2), 3.60)
    test(comprar_frutas(morango=0, uva=4), 7.20)
    test(comprar_frutas(morango=0, uva=5), 9.0)
    # Testes só com uvas, muda a faixa:
    test(comprar_frutas(morango=0, uva=6), 9.00)
    test(comprar_frutas(morango=0, uva=5.1), 7.65)
    test(comprar_frutas(morango=0, uva=8), 12.00)
    # Testes só com uvas, recebe desconto por peso:
    test(comprar_frutas(morango=0, uva=9), 12.15)
    test(comprar_frutas(morango=0, uva=10), 13.5)
    # Testes só com uvas, recebe desconto por preço:
    test(comprar_frutas(morango=0, uva=20), 27.00)

    # Testes com as duas frutas:
    test(comprar_frutas(morango=2, uva=2), 8.60)
    test(comprar_frutas(morango=4, uva=4), 17.20)
    test(comprar_frutas(morango=5, uva=5), 19.35)
    test(comprar_frutas(morango=10, uva=10), 33.30)


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
