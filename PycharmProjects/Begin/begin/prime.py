i = 2
while i < 10:
    j = 2
    print(i / j)
    while j <= i / j:
        print('true')
        if not (i % j): break
        j = j + 1
    if j > i / j:
        print(i, " la so nguyen to")
    i = i + 1
#continue: bo qua phan code con lai cua vong lap, chuyen den lan lap tiep theo