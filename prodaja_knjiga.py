from import_books import *

def prodaja_knjiga():
    knjige = import_books()
    #print(knjige)
    knjige_akcija = knjige_i_cene()
    #print(knjige_akcija)

    print('da li zelite da otpocnete kupovinu knjiga')
    print('1. da')
    print('2. ne')

    izbor = input('unesite vas izbor: ')
    while izbor == '':
        print('unos nije validan \n')
        izbor = input('ponovo unesite zeljenu vrednost: ')

    shopping_knjige = []
    shopping_akcije = []
    daj_pare = 0
    while izbor == '1':
        print('1. kupovina knjiga')
        print('2. akcijska kupovina')
        print('3. izlaz')
        shopping_choice = input('unesite vas izbor: ')
        while shopping_choice == '':
            print('unos nije validan \n')
            shopping_choice = input('ponovo unesite zeljenu vrednost: ')

        if shopping_choice == '1':
            sifra_knjige = input('unesite sifru knjige: ')
            amount_input = int(input('unesite koliko kopija knjige zelite da kupite: '))
            while sifra_knjige == '':
                print('unos nije validan \n')
                sifra_knjige = input('ponovo unesite zeljenu vrednost: ')
            while amount_input == '':
                print('unos nije validan \n')
                amount_input = int(input('ponovo unesite zeljenu vrednost: '))
            amount = 0
            amount += amount_input

            shopping = []
            for k in knjige:
                if sifra_knjige.lower() == k['id'].lower() and k['status'] == '1':
                    k['kolicina'] = amount
                    shopping.append(k)

            if not shopping:
                print('trazena knjiga ne postoji / nema dovoljno na lageru')
            else:
                already_there = False
                for i in range(len(shopping_knjige)):
                    if shopping[0]['id'] == shopping_knjige[i]['id']:
                        shopping[0]['kolicina'] += amount_input
                        already_there = True
                        break
                if not already_there:
                    shopping_knjige.append(shopping[0])

            money_knjige = int(amount_input)*float(shopping[0]['price'])
            daj_pare += money_knjige

            naziv = shopping[0]['title']
            print(f'za sada ste kupili {amount} kopije knjige {naziv.upper()} u iznosu od {round(money_knjige,2)}')
            print(f'vas trenutni racun je {round(daj_pare,2)}')
            print('u vasoj korpi je')
            pretty_print(shopping_knjige)
            if shopping_akcije:
                pretty_print(shopping_akcije)

            print('da li zelite da nastavite kupovinu')
            print('1. da')
            print('2. ne')
            izbor = input('unesite vas izbor: ')
            while izbor == '':
                print('unos nije validan \n')
                izbor = input('ponovo unesite zeljenu vrednost: ')

        elif shopping_choice == '2':
            sifra_akcije = input('unesite sifru akcije: ')
            amounta_input = int(input('unesite koliko akcija zelite da kupite: '))
            while sifra_akcije == '':
                print('unos nije validan \n')
                sifra_akcije = input('ponovo unesite zeljenu vrednost: ')
            while amounta_input == '':
                print('unos nije validan \n')
                amounta_input = int(input('ponovo unesite zeljenu vrednost: '))
            amount = 0
            amount += amounta_input

            shopping = []
            for recnik in knjige_akcija:
                if recnik['valid_until'] < datetime.datetime.now():
                    knjige_akcija.remove(recnik)

            for k in knjige_akcija:
                if int(sifra_akcije) == k['ida']:
                    k['kolicina'] = amount
                    shopping.append(k)

            if not shopping:
                print(f'akcijska ponuda sa sifrom {sifra_akcije} je nazalost istekla')
            else:
                already_there = False
                for i in range(len(shopping_akcije)):
                    if int(shopping[0]['ida']) == int(shopping_akcije[i]['ida']):
                        shopping[0]['kolicina'] += amounta_input
                        already_there = True
                        break
                if not already_there:
                    shopping_akcije.append(shopping[0])

            cena_akcije = 0
            for item in shopping_akcije:
                for c in item['cene']:
                    cena_akcije += float(c)
                    money_akcije = int(amounta_input)*float(cena_akcije)
            daj_pare += money_akcije

            id_akc = shopping[0]['ida']
            print(f'za sada ste kupili {amount} akcije {id_akc} u iznosu od {round(money_akcije,2)}')
            print(f'vas trenutni racun je {round(daj_pare,2)}')
            print('u vasoj korpi je')
            if shopping_akcije:
                pretty_print(shopping_akcije)
            if shopping_knjige:
                pretty_print(shopping_knjige)
            print('da li zelite da nastavite kupovinu')
            print('1. da')
            print('2. ne')
            izbor = input('unesite vas izbor: ')
            while izbor == '':
                print('unos nije validan \n')
                izbor = input('ponovo unesite zeljenu vrednost: ')
        elif shopping_choice == '3':
            return

    if izbor == '2':
        print(f'vas racun iznosi {round(daj_pare,2)} dinara')
        print('da li zelite da nastavite sa uplatom')
        print('1. da')
        print('2. ne')
        pay_up  = input('unesite vas izbor: ')
        while pay_up == '':
            print('unos nije validan \n')
            pay_up = input('ponovo unesite zeljenu vrednost: ')

        if pay_up == '1':
            print(f'vas racun iznosi {round(daj_pare,2)} dinara')
            money_given = input('unesite kolicinu novca: ')
            while money_given == '' or float(money_given) < daj_pare:
                print('unos nije validan \n')
                money_given = input('ponovo unesite kolicinu novca: ')
            kusur = float(money_given) - daj_pare
            print(f'vas kusur je {round(kusur,2)}')

            kupljeno = []
            if shopping_knjige:
                kupljene_knjige = {'knjiga': '', 'cena_knjige': '', 'kolicina': '', 'ukupno': ''}
                for knjige in shopping_knjige:
                    for k, v in knjige.items():
                        if k == 'title':
                            kupljene_knjige['knjiga'] = v
                        elif k == 'price':
                            kupljene_knjige['cena_knjige'] = v
                        elif k == 'kolicina':
                            ck = kupljene_knjige['cena_knjige']
                            kupljene_knjige['kolicina'] = v
                            kupljene_knjige['ukupno'] = round(float(int(v)*float(ck)),2)
                            knjige_copy = kupljene_knjige.copy()
                            kupljeno.append(knjige_copy)
            if shopping_akcije:
                kupljene_akcije = {'akcija': '', 'knjige': '', 'cena_akcije': '', 'kolicina': '', 'ukupno': ''}
                for knjige in shopping_akcije:
                    for k, v in knjige.items():
                        if k == 'ida':
                            kupljene_akcije['akcija'] = v
                        elif k == 'knjige':
                            kupljene_akcije['knjige'] = v
                        elif k == 'cene':
                            cn = 0
                            for vv in v:
                                cn += float(vv)
                            kupljene_akcije['cena_akcije'] = cn
                        elif k == 'kolicina':
                            ca = kupljene_akcije['cena_akcije']
                            kupljene_akcije['kolicina'] = v
                            kupljene_akcije['ukupno'] = round(float(v*ca),2)
                            akcije_copy = kupljene_akcije.copy()
                            kupljeno.append(akcije_copy)
            datum = datetime.datetime.now()
            kupljeno_racun = ''
            for kupovina in kupljeno:
                i = 0
                for k,v in kupovina.items():
                    kupljeno_racun += str(v) + "|"
                    i += 1
                    if i == len(kupovina):
                        kupljeno_racun = kupljeno_racun[:-1]
                        kupljeno_racun += '\n'
            kupljeno_racun += str(round(daj_pare,2)) + "|" + str(round(kusur,2)) + '\n' + str(datum) + '\n'
            print(kupljeno_racun)
            racun = open('racun_final.txt','r+')
            racun.write(kupljeno_racun)
            racun.close()
        elif pay_up == '2':
            return



if __name__ == '__main__':
    prodaja_knjiga()