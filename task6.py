
server = []
while True :
    print('''
1. Add server
2. Remove server
3. Show servers
4. Search server
5. Server statistics
6. serch by carecter 
0. Exit''')
    try:
        v1ue = int(input(':-'))
    except ValueError:
        print('enter the valide num')
        continue
    if v1ue == 0:
        print ("exiting the inventory")
        break 
    elif v1ue == 1 :
        v2ue = input('enter tehe name of serve you want to add \n:-')
        print(f'adding {v2ue} in server')
        server.append(v2ue)
    elif v1ue == 2 :
        if not server:
            print('server is empty')
            continue
        else:
            lis = 1 
            for m in server:
                print(f'{lis}. {m}')
                lis += 1 
            v3ue = int(input(f'entre the num of server for delete like for {server[0]} enter 1  ........\n:-')) - 1

            if v3ue < 0 or v3ue >= len(server) :
                print ("invalive input ser ver duas not exist")
                continue
            else :
                print(f'deleteing the', server[v3ue] )
                del server[v3ue]
    elif v1ue == 3:
        for i in server:
            print(i)
    elif v1ue == 4 :
        v4ue = input(f'enter the name of server for serch \n:-')
        if v4ue in server :
            print(f'{v4ue} found in the server inventory')
        else:
            print(f'{v4ue} not found in the server inventory' )
    elif v1ue == 5:
        print('the server lan is' , len(server))
        print(f'the servers is \n{server}')
    elif v1ue == 6 :
        lop = 0
        ape = []
        if not server:
            print('server is empty')
            continue
        else:
            op = input('entr the latter for search \n:- ')
            for mk in server :
                for km in mk :
                    if op == km :
                        lop += 1
                        lplo = (f"{lop}. {mk}")
                        ape.append(lplo)

                        break
            print(f'Servers containing {op}:{lop}')
            for a in ape :
                print(a)
        

