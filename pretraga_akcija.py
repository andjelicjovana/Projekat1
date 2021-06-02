from import_books import *
def pretraga_specs():
    print('odaberite zeljenu akciju')
    print('1. pretraga po sifri')
    print('2. pretraga po naslovu')
    print('3. pretraga po autoru')
    print('4. pretraga po kategoriji')
    print('5. izlaz')

    izbor = input("unesite vas izbor: ")
    while izbor == '':
        print('unos nije validan \n')
        izbor = input('ponovo unesite zeljenu vrednost: ')

    if izbor == '1':
        key = 'ida'
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
        return
    else:
        print("morate uneti vrednosti izmedju 1 i 5")


def pretraga_akcija():
    sve = akcije()
    key = pretraga_specs()
    if key != 'ida':
        search_word = input('unesite vrednost pretrage: ')
        while search_word == '':
            print('unos nije validan \n')
            search_word = input('ponovo unesite zeljenu vrednost: ')
        list_spec = []
        tmp = {}
        for recnik in sve:
            for knjige in recnik['knjige']:
                for k,v in knjige.items():
                    if search_word in v:
                            tmp = knjige
                if tmp in recnik['knjige']:
                    list_spec.append(knjige)

        if len(list_spec) != 0:
            pretty_print(list_spec)
        else:
            print(f'za vrednost {search_word.upper()} nema trazene knjige')

    else:
        search_word = input('unesite vrednost pretrage: ')
        while search_word == '':
            print('unos nije validan \n')
            search_word = input('ponovo unesite zeljenu vrednost: ')
        list_spec = []
        for recnik in sve:
            for k,v in recnik.items():
                if int(search_word) == v:
                    for d in recnik['knjige']:
                        list_spec.append(d)

        if len(list_spec) != 0:
            pretty_print(list_spec)
        else:
            print(f'za vrednost {search_word.upper()} nema trazene knjige')





if __name__ == '__main__':
    pretraga_akcija()