
server = []
while True :
    print('''
1. Add server
2. Remove server
3. Show servers
4. Search server
5. Server statistics
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
            v3ue = int(input(f'entre the num of server for delete like for {server[0]} enter 1 {server[1]} enter 2 ........\n:-')) - 1
            print(f'deleteing the {v3ue} ')
            del server[v3ue]
    elif v1ue == 3:
        for i in server:
            print(i)
    elif v1ue == 4 :
        v4ue = input(f'enter the name of server for serch \n:-')
        if v4ue in server :
            print(f'{v4ue} in {server}')
        else:
            print(f'{v4ue} not in {server}')
    elif v1ue == 5:
        print('the server lan is' , len(server))
        print(f'the servers is \n{server}')

