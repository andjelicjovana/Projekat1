from import_books import *
from json_files import *

def dodavanje_knjige():
    knjige = import_books()
    data = import_data()
    while True:
        print('da li zelite da dodate novu knjigu')
        print('1. da')
        print('2. ne(izlaz)')
        izbor = input('unesite zeljeni broj akcije: ')
        while izbor == '':
            print('unos nije validan \n')
            izbor = input('ponovo unesite zeljenu vrednost: ')

        if izbor == '1':
            sifra = input('unesite sifru knjige: ')
            while sifra == '':
                print('unos nije validan \n')
                sifra = input('ponovo unesite zeljenu vrednost: ')
            d = {}
            for k in knjige:
                if sifra.lower() == k['id'].lower():
                    print('ova sifra vec postoji, unesite novu')
                    break
            else:
                title = input('unesite naslov knjige: ')
                while title == '':
                    print('unos nije validan \n')
                    title = input('ponovo unesite zeljenu vrednost: ')
                isbn = input('unesite isbn knjige: ')
                while isbn == '':
                    print('unos nije validan \n')
                    isbn = input('ponovo unesite zeljenu vrednost: ')
                author = input('unesite autora knjige: ')
                while author == '':
                    print('unos nije validan \n')
                    author = input('ponovo unesite zeljenu vrednost: ')
                publisher = input('unesite izdavaca knjige: ')
                while publisher == '':
                    print('unos nije validan \n')
                    publisher = input('ponovo unesite zeljenu vrednost: ')
                number_of_pages = int(input('unesite broj strana knjige: '))
                while number_of_pages == '':
                    print('unos nije validan \n')
                    number_of_pages = int(input('ponovo unesite zeljenu vrednost: '))
                year = int(input('unesite godinu izdavanja knjige: '))
                while year == '':
                    print('unos nije validan \n')
                    year = int(input('ponovo unesite zeljenu vrednost: '))
                price = float(input('unesite cenu knjige (mora biti float): '))
                while price == '':
                    print('unos nije validan \n')
                    price = float(input('ponovo unesite zeljenu vrednost: '))
                category = input('unesite kategoriju : ')
                while category == '':
                    print('unos nije validan \n')
                    category = input('ponovo unesite zeljenu vrednost: ')
                keys = knjige[0].keys()
                vals = [sifra,title,isbn,author,publisher,number_of_pages,year,price,category,'1']
                for k,v in zip(keys,vals):
                    if k not in d:
                        d[k] = ''
                        d[k] = v
                data['books'].append(d)
                add_data(data)

        elif izbor == '2':
            return



if __name__ == '__main__':
    dodavanje_knjige()
