#!/bin/bash/python3
devices=[]
print ('''================================
      NETWORK DEVICE MANAGER
================================

1. Add device
2. Remove device
3. Show all devices
4. Search device or Find devices by type or name 
5. Count devices
6. Exit''')
while True :
    try: 
        mainin = int(input('entr the option \n:-'))
    except ValueError:
        print('enter the optione 1 to 7')
        continue
    if mainin == 6 :
        print('exiting')
        break 
    elif mainin == 1 :
        addevname = input('inter the name of device :- ')
        addevtype = input('inter the type of device :- ')
        devices.append({"name" : addevname , "type" : addevtype})
    elif mainin == 2 :
        if not devices :
            print('device empty')
            continue
        else:
            I = 0
            for i in devices:
                I += 1 
                print(f'{I}.{i}')
            try :
                rmv = int(input('enter the opion for del e.g, 1 \n:- ')) - 1
            except ValueError:
                print('inter the vlaid option for del')
                continue 
            if rmv > len(devices) or rmv < 0:
                print("Invalid option")
                continue
            else:
                print(f'deleting the {devices[rmv]}')
                del devices[rmv]
    elif mainin == 3 :
        A = 0
        for a in devices:
            A += 1
            print(f'{A}. {a}')
    elif mainin == 4 :

        srch = input('entr the name or type for search \n:- ')
        lp = 0
        for mm in devices:
            if srch in mm["type"]:
                print(f'{mm["name"]} - {mm["type"]}')
                lp += 1
            elif srch in mm["name"]:
                print(f'{mm["name"]} - {mm["type"]}')
                lp += 1
        if lp == 0:
            print(f'{srch} not found')
        else:
            print(f'Total found: {lp}')

        

    elif mainin == 5:
        L = 0
        for ll in devices:
            L += 1
        print(L)