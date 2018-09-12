def printPinic(itemsDict, leftWidth, rightWidth):
    print("PICNIC ITEMS".center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth,'*'))
picnicItems = {'sanwiches' : 4, 'apple' : 12, 'cup' : 4 , 'cookies' : 8000}
printPinic(picnicItems, 12, 5)
printPinic(picnicItems, 20, 6)

