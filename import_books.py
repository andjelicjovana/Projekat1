from json_files import *
from tabulate import tabulate
import datetime

def pretty_print(lista):
    headers = lista[0].keys()
    rows = [k.values() for k in lista]
    print(tabulate(rows, headers, tablefmt="fancy_grid"))

def import_books():
    data = import_data()
    #print(data)
    lista = []
    for k, v in data.items():
        for item in v:
            lista.append(item)
    #print(lista)
    return lista

def import_people():
    data = import_users()
    #print(data)
    lista = []
    for k, v in data.items():
        for item in v:
            lista.append(item)
    #print(lista)
    return lista

def akcije():
    data = import_akcije()
    #print(data)
    lista = []
    for k, v in data.items():
        for item in v:
            lista.append(item)
    #print(lista)
    return lista

def knjige_i_cene():
    sve = akcije()
    datum = []
    books = []
    prices = []
    lens = []
    for recnik in sve:
        for knjige in recnik['knjige']:
            knjige.pop('id')
            knjige.pop('isbn')
            knjige.pop('author')
            knjige.pop('publisher')
            knjige.pop('number of pages')
            knjige.pop('pub year')
            knjige.pop('category')
            knjige.pop('status')
            books.append(knjige['title'])
            prices.append(knjige['price'])
        lens.append(len(recnik['knjige']))
        for dat in recnik['valid_until']:
            datum.append(dat)

    datumi = []
    for d in range(0,len(datum)-2,3):
        date_format = datetime.datetime(int(datum[d]),int(datum[d+1]),int(datum[d+2]))
        datumi.append(date_format)
    dt = []
    for recnik in sve:
        recnik['knjige'] = []
        recnik.pop('valid_until')
        recnik['cene'] = []
        recnik['valid_until'] = []

    for l, br_l,date in zip(lens, range(len(lens)),datumi):
        sve[br_l]['knjige'].insert(br_l,books[:l])
        sve[br_l]['cene'].insert(br_l,prices[:l])
        sve[br_l]['valid_until'].insert(br_l, date)
        books = books[l:]
        prices = prices[l:]

    for recnik in sve:
        tmp_k = recnik['knjige']
        tmp_p = recnik['cene']
        tmp_d = recnik['valid_until']
        tmp_k = tmp_k[0]
        tmp_p = tmp_p[0]
        tmp_d = tmp_d[0]
        recnik['knjige'] = tmp_k
        recnik['cene'] = tmp_p
        recnik['valid_until'] = tmp_d
    #print(sve)
    final = sve
    return final




knjige_i_cene()


