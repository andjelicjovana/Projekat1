from import_books import *
from tabulate import tabulate

def prikaz_knjiga():
    knjige = import_books()
    while True:
        print('odaberite zeljenu akciju')
        print('1. soritranje po naslovu')
        print('2. soritranje po kategoriji')
        print('3. soritranje po autoru')
        print('4. sortiranje po izdavacu')
        print('5. soritranje po ceni')
        print('6. izlaz')

        izbor = input('unesite vas izbor: ')
        while izbor == '':
            print('unos nije validan \n')
            izbor = input('ponovo unesite zeljenu vrednost: ')

            for k in knjige:
                if k['status'] == 'o':
                    knjige.remove(k)

        if izbor == '1':
                for i in range(len(knjige)):
                    for j in range(len(knjige)):
                        if knjige[i]['title'].lower() < knjige[j]['title'].lower():
                            knjige[i],knjige[j] = knjige[j],knjige[i]
                break
        elif izbor == '2':
            for i in range(len(knjige)):
                for j in range(len(knjige)):
                    if knjige[i]['category'].lower() < knjige[j]['category'].lower():
                        knjige[i], knjige[j] = knjige[j], knjige[i]
            break
        elif izbor == '3':
            for i in range(len(knjige)):
                for j in range(len(knjige)):
                    if knjige[i]['author'].lower() < knjige[j]['author'].lower():
                        knjige[i], knjige[j] = knjige[j], knjige[i]
            break
        elif izbor== '4':
            for i in range(len(knjige)):
                for j in range(len(knjige)):
                    if knjige[i]['publisher'].lower() < knjige[j]['publisher'].lower():
                        knjige[i],knjige[j] = knjige[j],knjige[i]
            break
        elif izbor== '5':
            for i in range(len(knjige)):
                for j in range(len(knjige)):
                    if knjige[i]['price'] < knjige[j]['price']:
                        knjige[i],knjige[j] = knjige[j],knjige[i]
            break

        elif izbor == '6':
            return
        else:
            print('uneli ste nepostojecu akciju')

    pretty_print(knjige)





if __name__ == '__main__':
    prikaz_knjiga()
