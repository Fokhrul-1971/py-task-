#!/usr/bin/env python3
def pritban():
    print('''================================
      NETWORK DEVICE MANAGER
    ================================
    1. Add device
    2. Remove device
    3. Show all devices
    4. Search device  
    5. Count devices
    6. Exit''')

def opt1(moi):
    print(f'adding {moi} in device')
    return device.append(moi)

def opt2():
  while True:
    if not device:
      print('devise is empty')
      break
    p = 0
    for i in device:
      p += 1 
      print(f"{p}. {i}")
    try:
      oo = int(input('entr the option num of devise you want to delete \nfor exit deleting press (0) \n:- ')) 
    except ValueError:
      print('enter the vlide number')
      continue
    if oo == 0:
      print('exiting del option ')
      break
    elif (oo < 1 or oo > len(device) ):
      print(f"{oo} is not vlide num ")
      continue
    else:
      print(f"deleting {device[oo-1]}")
      del device[oo-1]
def opt3 ():
  if not device:
    print('devise empty')
    return
  vv = 0 
  for ii in  device:
    vv += 1 
    print(f" {vv}. {ii}")
def opt4 ():
  if not device:
    print('devise empty')
    return
  while True:
    sl = input('enter the name of devise for serch 0 for exit \n:- ')
    if sl == '0':
      print("exiting the serch option")
      break
    for ooo in device:
      if sl in ooo:
        print (f"{ooo} devise find in network ")
def opt5 ():
  if not device:
    print('devise empty')
    return
  pl = len(device)
  print(f" {pl} devise found in natwork")

device = []
while True :
  pritban()
  try:
    lmd = int(input('inter the num bitwin 1 to 6 \n:- '))
  except ValueError:
    print('enter the vlide num 1 to 6 ')
    continue
  if lmd == 6 :
    break
  elif lmd == 1 :
    mmk = input('enter the nam eof devise you want ot add \n:- ') 
    opt1(mmk)
  elif lmd == 2 :
    opt2()
  elif lmd == 3:
    opt3()
  elif lmd == 4:
    opt4()
  elif lmd == 5:
    opt5()
  else :
    print('you are idieat ')
    break
