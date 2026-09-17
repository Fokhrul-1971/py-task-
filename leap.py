lis = []
op=0
while True:
    opto = int(input('enter the type for convaeter \nfor bi to b - 1 \nfor b to bi - 2 \n 0 to exit \n:- '))
    if opto == 0:
        print(f'the vlue is {lis}')
        break
    elif opto == 1:
        try:
            value1 = int(input('enter the vlue for enter for converting ti bi to b\n :- '))
        except ValueError:
            print('you ediate inter int not str')
        typee1 = int(input('enter the type vlue eg for kib - 1 , mib - 2 , gib - 3 , tib - 4 , pib - 5  \n:- '))
        clu1 = value1*(1000/1024)**typee1
        lis.append(f"{value1} -> {clu1:.4f}")
    elif opto == 2:
        try :
            value2 = int(input('enter the vlue for enter for converting to b to bi\n :- '))
        except ValueError :
            print('you ediate inter int not str')           
        typee2 = int(input('enter the type vlue eg for kb - 1 , mb - 2 , gb - 3 , tb - 4 , pb - 5 \n:- '))
        clu2 = value2*(1024/1000)**typee2
        lis.append(f"{value2} -> {clu2:.4f}")
    else:
        print("invalide input ")