from import_books import *
from tabulate import tabulate

def pretraga_specs():
    print("odaberite zeljenu akciju")
    print("1. pretraga po sifri")
    print("2. pretraga po naslovu")
    print("3. pretraga po autoru")
    print("4. pretraga po kategoriji")
    print("5. pretraga po izdavacu")
    print("6. pretraga po opsegu cene")
    print("7. izlaz")

    izbor = input("unesite vas izbor: ")
    while izbor == '':
        print('unos nije validan \n')
        izbor = input('ponovo unesite zeljenu vrednost: ')

    if izbor == '1':
        key = 'id'
        return key
    elif izbor == '2':
        key = 'title'
        return key
    elif izbor == '3':
        key = 'author'
        return key
    elif izbor == '4':
        key = 'category'
        return key
    elif izbor == '5':
        key = 'publisher'
        return key
    elif izbor == '6':
        key = 'price'
        return key
    elif izbor == '7':
        return
    else:
        print("morate uneti vrednosti izmedju 1 i 5")


def pretraga_knjiga():
    knjige = import_books()
    key = pretraga_specs()
    if key != 'price':
        search_word = input('unesite vrednost pretrage: ')
        while search_word == '':
            print('unos nije validan \n')
            search_word = input('ponovo unesite zeljenu vrednost: ')
        list_spec = []
        for k in knjige:
            if search_word.lower() in (k[key]).lower() and k['status'] == '1':
                list_spec.append(k)

        if len(list_spec) != 0:
            pretty_print(list_spec)
        else:
            print(f'za vrednost {search_word.upper()} nema trazene knjige')
    else:
        range1 = int(input('unesite minimalnu vrednost cene: '))
        range2 = int(input('unesite maksimalnu vrednost cene: '))
        while (range1 == '' and range2 == '') or (range1 > range2):
            print('unesite validnu vrednost cene \n')
            range1 = int(input('ponovo unesite minimalnu vrednost cene: '))
            range2 = int(input('ponovo unesite maksimalnu vrednost cene: '))
        list_spec = []
        for k in knjige:
            if float(range1) <= float((k[key])) <= float(range2) and k['status'] == '1':
                list_spec.append(k)

        if len(list_spec) != 0:
            pretty_print(list_spec)
        else:
            print(f'za opseg vrednosti {range1,range2} nema trazene knjige')


if __name__ == '__main__':
    pretraga_knjiga()
