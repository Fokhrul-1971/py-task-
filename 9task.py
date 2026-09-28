
lpo = []
while True:
    lam=input('inter the option \n{for add prees:-(1)}\n{for remove prees:-(2)}\n{for show servers prees:-(3)}\n{for Search server prees :-(4)}\n{for Server statistics prees :-(5)}\n{for exit :-(0)}\n:-')
    if lam == '0':
        print('exiting')
        break
    elif lam == '1':
        klo = input('add the serves name:-')
        lpo.append(klo)
        print(f'{klo} is added')
    elif lam == '2' :
        mnp = int(input(f'{lpo}\nfor delete schose like {lop[0]} press (1)\n:')) - 1
        print(f'{lpo[mnp]} is deleted')
        del lpo[mnp]
    elif lam == '3':
        for i in lpo:
            print(i)
    elif lam == '4' :
        homp = input('inter the server name for serch \n:-')
        if homp in lpo :
            print(f'{homp} in the server list')
        elif homp not in lpo:
            print (f'{homp} not in the server list')
    elif lam == '5':
        print('i am not learnd yat to do comlite this section so you will ger soon')


