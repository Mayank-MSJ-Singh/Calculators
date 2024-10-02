import time
while 1<2:
    try:
        a = list(input())
        ti = time.time()
    except:
        print("Error, Try Again")
    b = a.copy()
    r = len(a)
    wh = 0
    while wh<r:
        if wh<1:
            wh+=1
        elif wh>=1:
            tj = time.time() - ti
            print(tj)
            a = list(input())
            ti = time.time()
            b = a.copy()
            r = len(a)
        for z in range(0, r):
            b[z] = '0'
        l=1
        while l<r:
            if a[l] == "+":
                s=l-1
                l = r
            elif a[l] == "-":
               s=l-1
               l = r
            elif a[l] == "*":
                s=l-1
                l = r
            elif a[l] == "/":
               s=l-1
               l = r
            else:
                s = len(a)-1
            l+=1
        n=0
        while n<=s:
                b[0]=str(b[0])
                b[0] = b[0] + a[n]
                n+=1
        b[0] = float(b[0])
        try:
         for o in range(n+1, r):
              b[1] = str(b[1])
              b[1] = b[1] + a[o]
         b[1] = float(b[1])
         for l in range(0,r):
            if a[l] == "+":
                print(b[0]+b[1])
            elif a[l] == "-":
                print(b[0]-b[1])
            elif a[l] == "*":
                print(b[0]*b[1])
            elif a[l] == "/":
                if b[1] == 0:
                    print("Error! Try Again")
                else:
                    print(b[0]/b[1])
        except:
            #print(b[0])??????????????????????????????????????????????????????
            print("Need 2 terms.")
            continue