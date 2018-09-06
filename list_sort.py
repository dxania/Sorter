def inputs():
    listb = [str(n) for n in raw_input("Enter the list elements:").split(",")]
    print(list_sort(listb))

def list_sort(lista):
    evens = []
    odds = []
    chars = []
    for n in lista:
        if int(n)%2 == 0:
            evens.append(n)
            evens.sort()
        elif int(n)%2 == 1:
            odds.append(n)
            odds.sort()
        else:
            chars.append(n)
            chars.sort()
    return evens, odds, chars
    
inputs()
