from import_books import *

def prikaz_akcija():
    akcije = knjige_i_cene()
    #print(akcije)
    while True:
        print('odaberite zeljenu akciju')
        print('1. soritranje po sifri')
        print('2. soritranje po datumu')
        print('3. izlaz')

        izbor = input('unesite vas izbor: ')
        while izbor == '':
            print('unos nije validan \n')
            izbor = input('ponovo unesite zeljenu vrednost: ')

        if izbor == '1':
            for recnik in akcije:
                if recnik['valid_until'] < datetime.datetime.now():
                    akcije.remove(recnik)
            for i in range(len(akcije)):
                for j in range(len(akcije)):
                    if akcije[i]['ida'] < akcije[j]['ida']:
                        akcije[i], akcije[j] = akcije[j], akcije[i]
            break
        elif izbor == '2':
            for recnik in akcije:
                if recnik['valid_until'] < datetime.datetime.now():
                    akcije.remove(recnik)
            for i in range(len(akcije)):
                for j in range(len(akcije)):
                    if akcije[i]['valid_until'] < akcije[j]['valid_until']:
                        akcije[i], akcije[j] = akcije[j], akcije[i]
            break
        elif izbor == '3':
            return
        else:
            print('uneli ste nepostojecu akciju')
    pretty_print(akcije)

if __name__ == '__main__':
    prikaz_akcija()