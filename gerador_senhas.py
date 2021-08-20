import random
import string

tamanho = int(input("Digite tamanho de senha: "))

letras = str(input("Deseja letra minuscula? (M)aiuscula, (m)inuscula ou (A)mbos: "))

while True:
    while letras not in 'MmA':
        letras = str(input('Digite (M)aiuscula, (m)inuscula ou (A)mbos: ')).split()[0]
    if letras == 'M' or letras == 'm' or letras == 'A':
        break

caracteres = input("Digite caracteres desejados: ")

if letras == 'M':
    chars = string.ascii_uppercase + string.digits + caracteres
    rnd = random.SystemRandom()
elif letras == 'm':
    chars = string.ascii_lowercase + string.digits + caracteres
    rnd = random.SystemRandom()
else:
    chars = string.ascii_letters + string.digits + caracteres
    rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
