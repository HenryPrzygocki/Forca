import sys


palavra = input("Qual a palavra? ").lower()
print(chr(27) + "[2J")
n = len(palavra)
d = []
for i in range(0,n):
    if(palavra[i].isalpha()):
        d.append("_")
    else:
        d.append(palavra[i])

w = []
print(' '.join(map(str, d)))
rep = 1
erros = 0
errrmax = 5
while(erros < errrmax):
    for i in range(0,errrmax):
        w.insert(i,input("Letra: ").lower()[0])
        if(w.count(w[i]) > 1):
            w.pop(i)
            rep = 1
            while(rep):
                print(chr(27) + "[2J")
                print("Essa letra ja foi, escolha outra ")
                print("Letras já escolhidas: ")
                w.sort()
                print(' '.join(map(str,w)))
                print(' '.join(map(str, d)))
                z = input("Letra: ")
                if(not(z  in w)):
                    w.insert(i, z)
                    rep = 0
        if(w[i] in palavra):
            pos = [j for j, x in enumerate(palavra) if x == w[i]]
            print(chr(27) + "[2J")
            for x, item in enumerate(pos):
                d[pos[x]]=w[i]
            if("".join(map(str, d))== palavra):
                print("Voce acertou! A palavra era: ")
                print(' '.join(map(str, d)))
                sys.exit()             
        else:
            erros += 1
            print(chr(27) + "[2J")
            print("Não possui letra " ,w[i]," | ","Vidas restantes: ", errrmax-erros)
            if(erros == errrmax):
                print("Perdeu! A palavra era: ")
                print(palavra)
                sys.exit()
        print("Letras já escolhidas: ")
        w.sort()
        print(' '.join(map(str,w)))
        print(' '.join(map(str, d)))



