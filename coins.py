coins = [1,2,5,10,20,50,100,200]
goal = 200
pos =  0
for a in range (0 ,201):
    r1 = goal - (a * 1)
    for b in range (0, 101):
        r2 = r1 - (b * 2)
        for c in range (0, 51):
            r3 = r2 - (c * 5)
            for d in range (0, 21):
                r4 = r3 - (d * 10)
                for e in range (0, 11):
                    r5 = r4 - (e * 20)
                    for f in range (0 , 5):
                        r6 = r5 - (f* 50)
                        for g in range (0, 3):
                            r7 = r6 - (g * 100)
                            for h in range (0, 2):
                                r8 = r7 - (h * 200)
                                if ( r8 == 0):
                                    pos += 1
                                    print(pos)
