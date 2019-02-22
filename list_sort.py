def list_sort(lista):
    
    even = []
    odd = []
    characters = []
    mydict = dict()
    if not isinstance(lista, list):
        return 'Invalid Input'

    if not lista:
        mydict['evens'] = even
        mydict['odds'] = odd
        mydict['chars'] = characters
        return mydict

    for b in lista:

        if isinstance(b, int):
            if b % 2 == 0:
                even.append(b)

            else:
                odd.append(b)

        elif isinstance(b, str):
            characters.append(b)

    mydict['evens'] = sorted(even)
    mydict['odds'] = sorted(odd)
    mydict['chars'] = sorted(characters)
    return mydict


print(list_sort([4, 5, 8, 7, 9, 1, 'q', 's']))


