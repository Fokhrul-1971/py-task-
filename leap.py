print('this is a coverter for iB to B and B to iB ')
k = 'stander unit (B)'
b = ' binary (iB)'
while True :
    q = int(input("inter the unit\nlike standard unit eg., KB, MB etc. \nBinary unit eg., KiB, MiB, GiB etc.\nfor standard unit to Binary unit press [ 0 ] \n3for Binary unit to standard unit press [ 1 ]\nFor exit enter [ 9 ]\n :- "))
    if q == 9:
        break
    elif q == 1:
        m=int(input(f'enter the amount of {b}'))
        w = int(input('Enter the valu for coaculate the binary to standard unit\n* 1 = Kilo (KiB / KB)\n* 2 = Mega (MiB / MB)\n* 3 = Giga (GiB / GB)\n* 4 = Tera (TiB / TB)\n* 5 = Peta (PiB / PB)1\n:- '))
        M = (1024 / 1000)** w
        e = (m * M )
        print(f'{m} {b}  To  {e} {k}')
        print(f'{k}\n\n')
    elif q == 0 :
        v=int(input(f'enter the amount of {k}'))
        h = int(input('Enter the valu for coaculate the  standard unit to binary \n* 1 = Kilo (KB / KiB)\n* 2 = Mega (MB / MiB)\n* 3 = Giga (GB / GiB)\n* 4 = Tera (TB / TiB)\n* 5 = Peta (PB / PiB)\n'))
        V = (1000 / 1024)** h
        f = (v * V)
        print(f'{v} {k}  To  {f} {b}')
        print(f'{f}\n\n')
    else :
        print ('enter the valide option ')
