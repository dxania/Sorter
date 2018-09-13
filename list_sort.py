chara = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def inputs():
    listb = [n for n in input("Enter the list elements:").split(",")]
    print(list_sort(listb))

def list_sort(lista):
    evens = []
    odds = []
    chars = []
    for n in lista:
        if n in chara:
            chars.append(n)
            chars.sort()
        elif int(n)%2 == 0:
            evens.append(n)
            evens.sort()
        elif int(n)%2 == 1:
            odds.append(n)
            odds.sort()
        else:
            print("Input was not an interger or letter")
    return evens, odds, chars
    
inputs()
