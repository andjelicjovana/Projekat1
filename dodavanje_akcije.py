from import_books import *
from json_files import *
import numpy as np

def dodavanje_akcije():
    knjige = import_books()
    sve = akcije()
    data = import_akcije()
    while True:
        print('da li zelite da dodate novu akcijsku ponudu \n')
        print('1. da')
        print('2. ne (izlaz)')
        izbor = input('unesite zeljenu vrednost: ')
        while izbor == '':
            print('unos nije validan \n')
            izbor = input('ponovo unesite zeljenu vrednost: ')

        if izbor == '1':
            '''
            ODABIR SIFRI KNJIGA KOJE CE BITI NA AKCIJI
            I UNOSENJE AKCIJSKE CENE
            '''
            print('koju od knjiga iz prikazane tabele zelite da dodate u akcijsku ponudu: \n')
            pretty_print(knjige)
            print('vrednosti unosite u formatu id_prveknjige, id_drugeknjige (odvojene zarezom)')
            id = input('unesite id knjiga: ')
            while id == '':
                print('unos nije validan \n')
                id = input('ponovo unesite zeljenu vrednost: ')

            ubaci_u_akciju = []
            ids = np.unique(id.strip().split(','))
            if len(ids) == 1:
                print('u akciji mora biti bar dve knjige')
                id = input('unesite id knjiga: ')
                while id == '':
                    print('unos nije validan \n')
                    id = input('ponovo unesite zeljenu vrednost: ')
            else:
                for i in ids:
                    for k in knjige:
                        if i.lower() == str(k['id'].lower()) and k['status'] == '1':
                            tmp_price = k['price']
                            tmp_id = k['id']
                            print(f'trenutna cena knjige {tmp_id} je {tmp_price}')
                            new_price = input('unesite akcijsku cenu (float type) knjige: ')
                            while new_price == '' or float(new_price) > float(tmp_price):
                                print('unos nije validan \n')
                                new_price = input('ponovo unesite zeljenu vrednost: ')
                            k['price'] = new_price
                            ubaci_u_akciju.append(k)
                else:
                    print(f'knjiga sa siform {i} ne postoji / nema na lageru')
                #break

            '''
            ODABIR DATUMA DO KOJEG VAZI AKCIJA
            '''

            print('unesite datum do kad vazi akcija')
            print('vrednosti unosite u formatu godina (YYYY), mesec (MM), dan (DD) (odvojene zarezom)')
            datum_akcije = input('unesite datum: ')
            while datum_akcije == '':
                print('unos nije validan \n')
                datum_akcije = input('ponovo unesite zeljenu vrednost: ')
            dates = datum_akcije.strip().split(',')
            print(f'UNET DATUM {dates}')
            if len(dates) > 3 and len(dates[0]) > 4:
                print('unos nije validan')
                break
            if dates[1][0] == '0' or dates[2][0] == '0':
                print('unos nije validan')
                break

            datumi = []
            date_format = datetime.datetime(int(dates[0]), int(dates[1]), int(dates[2]))
            if date_format > datetime.datetime.now():
                for d in dates:
                    datumi.append(int(d))
            else:
                print('unos nije validan')
                break

            '''
            DODAVANJE AKCIJE U FAJL
            '''
            last_id = int(sve[-1]['ida'])
            next_id = last_id + 1
            keys = []
            d = {}
            for recnik in sve:
                for k,v in recnik.items():
                    if k not in keys:
                        keys.append(k)
            for k in keys:
                if k not in d:
                    d[k] = ''
                    if k == 'ida':
                        d[k] = next_id
                    elif k == 'knjige':
                        d[k] = ubaci_u_akciju
                    elif k == 'valid_until':
                        d[k] = datumi
                        data['akcije'].append(d)
                        add_akcije(data)

        elif izbor == '2':
            return


if __name__ == '__main__':
    dodavanje_akcije()