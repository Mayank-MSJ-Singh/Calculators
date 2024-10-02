z = 10
y = 1
a = input()
while y<=z:
    if a == "exit":
        break
    try:
        try:
            a = float(a)
        except:
            a = input('You can only write number or type "exit": ')
            continue
        b = input()
        if b == "exit":
            break
        elif b == "+":
            pass
        elif b == "-":
            pass
        elif b == "/":
            pass
        elif b == "*":
            pass
        else:
            u = 10
            for v in range(1, u):
                try:
                    if b == "exit":
                        print("Process finished with exit code -1")
                        break
                    elif b == "+":
                        pass
                    elif b == "-":
                        pass
                    elif b == "/":
                        pass
                    elif b == "*":
                        pass
                    else:
                        b = float(b)
                        a = b
                    if v == u - 1:
                        if a == b:
                            pass
                        elif b == "+":
                            pass
                        elif b == "-":
                            pass
                        elif b == "/":
                            pass
                        elif b == "*":
                            pass
                        else:
                            u += 1
                except:
                    print("Invalid Input, Try Again")
                    b = input()
            if a == b:
                continue
        c = input()
        if c == "exit":
            break
        c = float(c)
        if b == "+":
            print(a + c)
            a = a + c
        elif b == "-":
            print(a - c)
            a = a - c
        elif b == "/":
            print(a / c)
            a = a / c
        elif b == "*":
            print(a * c)
            a = a * c
        else:
            print("Invalid Input, Try Again")
    except:
        print("Try Again!")
        continue