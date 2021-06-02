from import_books import *
from json_files import *


def logicko_brisanje():
    data = {}
    data['books'] = []
    knjige = import_books()
    sifra = input('unesite sifru knjige: ')
    while sifra == '':
        print('unos nije validan \n')
        sifra = input('ponovo unesite zeljenu vrednost: ')
    for k in knjige:
        if k['status'] == '1' and k['id'] == sifra:
            k['status'] = '0'
            break
    else:
        print('trazena knjiga ne postoji')

    for k in knjige:
        data['books'].append(k)
    change_data(data)







if __name__ == '__main__':
    logicko_brisanje()