import random
while True:

    n = int (input ('quantos jogos?:'))
    if n == 0:
        quit()
    for n in range (1,n+1):
        print ('jogo',n,':')
        num = ' '
        for m in range (1,16):
            r = random.randint(1,26)
            num = num + " " +str (r)
        print(num)