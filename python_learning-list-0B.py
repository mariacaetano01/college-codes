# Lista de exercícios com testes


def media_notas(nota1, nota2):
    
    media = (nota1 + nota2) / 2
    return round (media,1)


def aprovado(media):
    
    if media >= 7:
        media = True
    else:
        media = False
    
    return media 
    
# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % 'Falhou'
    else:
        prefixo = '\033[32m%s' % 'Passou'
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():

    print(' Média de notas:')
    test(media_notas(nota1=10.0, nota2=10.0, ), 10.0)
    test(media_notas(nota1=0, nota2=0), 0.0)
    test(media_notas(nota1=10, nota2=0), 5.0)
    test(media_notas(nota1=0, nota2=10), 5.0)
    test(media_notas(nota1=7.0, nota2=8.0), 7.5)
    test(media_notas(nota1=7.5, nota2=8.2), 7.8)

    print(' Situação do aluno:')
    test(aprovado(media=0.0), False)
    test(aprovado(media=1.0), False)
    test(aprovado(media=6.9), False)
    test(aprovado(media=7.0), True)
    test(aprovado(media=7.1), True)
    test(aprovado(media=9.9), True)
    test(aprovado(media=10.0), True)

if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (
        total, acertos, total - acertos, float(acertos * 10) / total)
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
