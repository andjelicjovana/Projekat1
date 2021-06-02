from import_books import *

def akcijske_cene():
    akcije = knjige_i_cene()
    d = []
    for a in akcije:
        d.append(list(a.items()))
    for i in range(len(d)):
        d[i] = d[i][1:3]
    #print(d)
    return d

def izvestaj():
    d = akcijske_cene()
    racun = open('racun_final.txt','r')
    racun = racun.readlines()

    total = []
    for line in racun:
        line = line.strip().split('|')
        total.append(line)
    total = total[:-1]
    print(total)
    new = []
    for item in total:
        if len(item) > 4:
            for i, j in zip(item, range(len(item))):
                if j == 1:
                    i = i.rstrip(']')
                    i = i.lstrip('[')
                    if ',' in i:
                        i = i.split(',')
                        for ii in range(len(i)):
                            i[ii] = i[ii][1:-1]
                            i[ii+1] = i[ii+1].strip(' ')[1:-1]
                            break
                        for it in i:
                            new.append(it)
                    item[j] = new
    #print(total)

    print('odaberite tip izvestaja')
    print('1. ukupna prodaja svih knjiga (ukljucujuci i knjige prodate kroz akcijsku ponudu)')
    print('2. ukupna prodaja svih akcija')
    print('3. ukupna prodaja knjiga odabranog autora (ukljucujuci i knjige prodate kroz akcijsku ponudu)')
    print('4. ukupna prodaja knjiga odabranog izdavaca (ukljucujuci i knjige prodate kroz akcijsku ponudu)')
    print('5. ukupna prodaja knjiga odabrane kategorije (ukljucujuci i knjige prodate kroz akcijsku ponudu)')
    print('6. izlaz')

    izbor = input('unesite vas izbor: ')
    while izbor == '':
        print('unos nije validan \n')
        izbor = input('ponovo unesite zeljenu vrednost: ')

    if izbor == '1':
        sold_books = []
        amount_sold = []
        prices = []
        for books in total:
            if len(books) > 4:
                '''
                KNJIGE PRODATE KROZ AKCIJSKU PONUDU I NJIHOVA KOLICINA
                '''
                for b,bb in zip(books,range(len(books))):
                    if bb == 1:
                        for book in b:
                            sold_books.append(book)
                    elif bb == 3:
                        k = len(books[1])
                        for kk in range(k):
                            amount_sold.append(b)
                '''
                AKCIJSKA CENA KNJIGA
                '''
                for a_knjiga in sold_books:
                    for sve_akcije in d:
                        br_k = 0
                        br_v = 1
                        for s in sve_akcije:
                            for ss in s:
                                if a_knjiga in ss:
                                    get_index = ss.index(a_knjiga)
                                    br_k += 1
                                    br_v += 1
                                    prices.append(sve_akcije[br_k][br_k][get_index])

            elif len(books) == 4:
                sold_books.append(books[0])
                prices.append(books[1])
                amount_sold.append(books[2])
        ukupna_zarada = []
        for i,j in zip(prices,amount_sold):
            ukupna_zarada.append(float(i)*float(j))
        headers = ['knjiga','cena','kolicina','ukupna zarada']
        rows = zip(sold_books,prices,amount_sold,ukupna_zarada)
        print(tabulate(rows, headers, tablefmt="fancy_grid"))

    elif izbor == '2':
        # a_id = []
        sold_books = []
        # amount_sold = []
        # prices = []
        # ukupna_zarada = []
        d = {'akcija': '','knjige':'','cena':'','kolicina':'','ukupna zarada': ''}
        keys = d.keys()
        for books in total:
            if len(books) > 4:
                for a, aa, k in zip(books, range(len(books)),keys):
                    if aa == 0:
                        d[k] = a
                    elif aa == 1:
                        for book in a:
                            sold_books.append(book)
                        d[k] = sold_books
                    elif aa == 2:
                        d[k] = a
                    elif aa == 3:
                        d[k] = a
                    elif aa == 4:
                        d[k] = a
        rows = []
        rows.append(d)
        pretty_print(rows)

    elif izbor == '3':
        p = 'report unavailabe'
        print(f'{p.upper()} \n')
    elif izbor == '4':
        p = 'report unavailabe'
        print(f'{p.upper()} \n')
    elif izbor == '5':
        p = 'report unavailabe'
        print(f'{p.upper()} \n')
    elif izbor == '5':
        return
    else:
        print('uneli ste nepostojecu akciju')


if __name__ == '__main__':
    izvestaj()
    akcijske_cene()