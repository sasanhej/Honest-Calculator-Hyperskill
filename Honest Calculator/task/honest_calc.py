msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msgdict={}
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msgdict[10]=msg_10
msgdict[11]=msg_11
msgdict[12]=msg_12


def is_one_digit(v):
    if -10<v<10 and v==int(v):
        return True
    return False


def check(v1,v2,v3):
    msg=""
    if is_one_digit(v1) and is_one_digit(v2):
        msg=msg+msg_6
    if (v1==1 or v2==1) and oper=='*':
        msg=msg+msg_7
    if (v1==0 or v2==0) and oper in ['*','+','-']:
        msg=msg+msg_8
    if msg!="":
        msg=msg_9+msg
        print(msg)


memory = float(0)
while True:
    x, oper, y = input(msg_0).split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    if not (str(x).replace(".","").isnumeric() and str(y).replace(".","").isnumeric()):
        print(msg_1)
    elif not oper in ['+','-','*','/']:
        print(msg_2)
    else:
        x, y = float(x), float(y)
        check(x,y,oper)
        if oper == '+':
            result=x+y
        elif oper == '-':
            result=x-y
        elif oper == '*':
            result=x*y
        elif oper == '/':
            if y == 0:
                print(msg_3)
                continue
            result=x/y
        print(result)
        q4 = input(msg_4)
        if q4 == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    q10=input(msgdict[msg_index])
                    if q10 == 'y':
                        if msg_index<12:
                            msg_index+=1
                            continue
                        else:
                            memory = result
                            break
                    elif q10!='n':
                        continue
                    else:
                        break
            else:
                memory = result
        elif not q4 == 'n':
            continue
        while True:
            q5 = input(msg_5)
            if q5 in ['y','n']:
                break
        if q5 == 'y':
            continue
        break      
            