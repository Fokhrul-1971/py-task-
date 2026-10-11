
op = ['lpy','plinux','bp']
op.append('lgit')
op[1]=('plinuxcmd')
print(op)
print(len(op))
servers=['a009' , 'b1111' , 'c2222' , 'e33333']
for server in servers:
    print("server:-",server)

laern = ['linux' , 'read' , 'devops' , 'op']
for ans in laern:
    if ans == 'devops':
        print('we find the :',ans)


users = ["ali", "ahmed", "ali", "john", "ali"]
count = 0
for user in users:
    if user == 'ali':
        print(user)
        count+=1
print(count)


servers=['a009' , 'b1111' , 'c2222' , 'e33333']
if 'b1111' in servers:
    print ('Database server found')
else:
    exit()


servers=['a009' , 'b1111' , 'c2222' , 'e33333']
if "mail01" not in servers:
    print("Mail server is missing")

numbers = [30, 5, 100, 20, 1]

numbers.sort()

print(numbers)

ser = []
while True:
    ie = input("entr the server names \nfor add press '1' \nfor remove press '2'\n'0' for exit  \n:- ")
    if int(ie) == 0:
        print(f'exiting')
        break
    elif int(ie) == 2:
        print(ser,' chose option 0 to ',len(ser) - 1,' for deleteing the option  ')
        swe = int(input(':-'))
        del ser[swe]
    elif int(ie) == 1:
        server = input("Enter server name: ")
        ser.append(server)
    else:
        break


