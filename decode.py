def conv_bi(num):
    re = []
    while num != 0:
        re.append(num % 2)
        num = num // 2
    re = re[::-1]
    string = ""
    for i in re:
        string = string + str(i)
    return string

def digits(i):
    a = 0
    lst = []
    string = str(i)
    while a < len(string):
        n = int(string[a])
        lst.append(n)
        a += 1
    return lst

def conv_dec(bi):
    dig = digits(bi)
    i = len(dig) - 1
    j = 0
    dec = 0
    while i >= 0 and j < len(dig):
        dec += dig[j] * 2**i
        i -= 1
        j += 1
    return dec

is_int = False
is_dec = False
inp = None

while True:
    inp = input("Input 0 to convert binary to decimal, 1 to convert decimal to binary: ")
    if inp == "1":
        is_dec = True
    elif inp == "0":
        is_dec = False
    elif inp == "quit":
        break
    else:
        print("Don't do that. Start again.\n")

    while is_int == False:
        num = input("Type in an integer: ")
        try:
            num = int(num)
            is_int = True
        except ValueError:
            print("Oh no, that's not a integer... Please try again.\n")
        if is_int == True:
            if is_dec == False:
                abc = 0
                for c in str(num):
                    if int(c) == 1:
                        abc += 0
                    elif int(c) == 0:
                        abc += 0
                    else:
                        abc += 1
                if abc != 0:
                    print("This is not a binary number... Try again.\n")
                    abc = 0
                    is_int = False
            
    if is_dec == True:
        print("Your decimal integer converted to binary is {}\n".format(conv_bi(num)))
        is_int = False
    elif is_dec == False:
        print("Your binary integer converted to decimal is {}\n".format(conv_dec(num)))
        is_int = False
print("Bye~\n")
