from import_books import *
from json_files import *

def izmena_knjiga():
    knjige = import_books()
    data = {}
    data['books'] = []
    while True:
        print('zelite li da izmenite odredjenu knjigu?')
        print('1. da')
        print('2. ne (izlaz)')
        izbor = input('unesite zeljenju vrednost: ')
        while izbor == '':
            print('unos nije validan \n')
            izbor = input('ponovo unesite zeljenu vrednost: ')

        if izbor == '1':
            sifra = input('unesite sifru knjige: ')
            while sifra == '':
                print('unos nije validan \n')
                sifra = input('ponovo unesite zeljenu vrednost: ')
            d = {}
            k_br = -1
            for k in knjige:
                k_br += 1
                if sifra.lower() == k['id'] and k['status'] == '1':
                    title = input('unesite naslov knjige: ')
                    if title == '':
                        val_title = k['title']
                    else:
                        val_title = title
                    isbn = input('unesite isbn knjige: ')
                    if isbn == '':
                        val_isbn = k['isbn']
                    else:
                        val_isbn = isbn
                    author = input('unesite autora knjige: ')
                    if author == '':
                        val_author = k['author']
                    else:
                        val_author = author
                    publisher = input('unesite izdavaca knjige: ')
                    if publisher == '':
                        val_publisher = k['publisher']
                    else:
                        val_publisher = publisher
                    number_of_pages = input('unesite broj strana knjige: ')
                    if number_of_pages == '':
                        val_number_of_pages = k['number of pages']
                    else:
                        val_number_of_pages = number_of_pages
                    year = input('unesite godinu izdavanja knjige: ')
                    if year == '':
                        val_year = k['pub year']
                    else:
                        val_year = year
                    price = input('unesite cenu knjige (mora biti float): ')
                    if price == '':
                        val_price = k['price']
                    else:
                        val_price = price
                    category = input('unesite kategoriju : ')
                    if category == '':
                        val_category = k['category']
                    else:
                        val_category = category
                    knjige.pop(k_br)
                    keys = knjige[0].keys()
                    vals = [sifra, val_title, val_isbn, val_author, val_publisher, val_number_of_pages, val_year, val_price, val_category, '1']
                    for k, v in zip(keys, vals):
                        if k not in d:
                            d[k] = ''
                            d[k] = v
                    knjige.insert(k_br,d)
                    for kk in knjige:
                        data['books'].append(kk)
                    change_data(data)
                    break

            else:
                print('trazena knjiga ne postoji')
        elif izbor == '2':
            return




if __name__ == '__main__':
    izmena_knjiga()