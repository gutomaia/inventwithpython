# Este é o jogo adivinhe o número.
import random
tentativas = 0
print('Olá! Qual é o seu nome?')
meuNome = input()
numero = random.randint(1, 20)
print('Bem, ' + meuNome + ', eu estou pensando em um número entre 1 e 20.')
while tentativas < 6:
    print('Tente adivinhar.') # Há quatro espaços na frente do print.
    palpite = input()
    palpite = int(palpite)
    tentativas = tentativas + 1
    if palpite < numero:
        print('Seu palpite é muito baixo.') # Há oito espaços na frente do print.
    if palpite > numero:
        print('Seu palpite é muito alto.')
    if palpite == numero:
        break
if palpite == numero:
    tentativas = str(tentativas)
    print('Bom trabalho, ' + meuNome + '! Você acertou o meu número em ' + tentativas + ' tentativas!')
if palpite != numero:
    numero = str(numero)
    print('Não. O número que eu estava pensando era ' + numero)
