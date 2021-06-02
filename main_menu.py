from dodavanje_knjige import *
from dodavanje_akcije import *
from import_books import *
from izmena_knjige import *
from izvestaj import *
from json_files import *
from logicko_brisanje import *
from login import *
from pretraga_knjiga import *
from pretraga_akcija import *
from prikaz_korisnika import *
from prikaz_knjiga import *
from prikaz_akcija import *
from prodaja_knjiga import *
from registracija import *

def print_login_meni():
    print('1. login')
    print('2. izlaz')

def print_together():
    print('1. prikaz knjiga')
    print('2. pretraga knjiga')
    print('3. prikaz akcija')
    print('4. pretraga akcija')
    print('5. izlaz')

def print_administrator():
    print('1. registracija')
    print('2. prikaz korisnika')
    print('3. prikaz knjiga')
    print('4. pretraga knjiga')
    print('5. prikaz akcija')
    print('6. pretraga akcija')
    print('7. dodavanje knjige')
    print('8. izmena knjige')
    print('9. logicko brisanje')
    print('10. izlaz')

def print_prodavac():
    print('1. prikaz knjiga')
    print('2. pretraga knjiga')
    print('3. prikaz akcija')
    print('4. pretraga akcija')
    print('5. prodaja knjiga')
    print('6. dodavanje knjige')
    print('7. izmena knjige')
    print('8. logicko brisanje')
    print('9. izlaz')

def print_menadzer():
    print('1. registracija')
    print('2. prikaz korisnika')
    print('3. prikaz knjiga')
    print('4. pretraga knjiga')
    print('5. prikaz akcija')
    print('6. pretraga akcija')
    print('7. dodavanje akcije')
    print('8. izvestaj')
    print('9. izlaz')


def loginmeni():
    while True:
        print_login_meni()
        izbor = input('unesite zeljenu akciju: ')
        while izbor == '':
            print('unos nije validan \n')
            izbor = input('ponovo unesite zeljenu vrednost: ')
        if izbor == '1':
            uspeh, uloga, u_name = login()
            if uloga == 'administrator':
                administrator()
            elif uloga == 'menadzer':
                menadzer()
            else:
                prodavac()
        elif izbor == '2':
            quit()
        else:
            print("vas izbor nije ispravan, morate uneti broj 1-3")

def administrator():
    while True:
        print_administrator()
        izbor = input('unesite zeljenu akciju: ')
        while izbor == '':
            print('unos nije validan \n')
            izbor = input('ponovo unesite zeljenu vrednost: ')
        if izbor == '1':
            registracija()
        elif izbor == '2':
            prikaz_korisnika()
        elif izbor == '3':
            prikaz_knjiga()
        elif izbor == '4':
            pretraga_knjiga()
        elif izbor == '5':
            prikaz_akcija()
        elif izbor == '6':
            pretraga_akcija()
        elif izbor == '7':
            dodavanje_knjige()
        elif izbor == '8':
            izmena_knjiga()
        elif izbor == '9':
            logicko_brisanje()
        elif izbor == '10':
            return
        else:
            print('vas izbor nije ispravan, morate uneti broj 1-10')


def prodavac():
    while True:
        print_prodavac()
        izbor = input('unesite zeljenu akciju: ')
        while izbor == '':
            print('unos nije validan \n')
            izbor = input('ponovo unesite zeljenu vrednost: ')
        if izbor == '1':
            prikaz_knjiga()
        elif izbor == '2':
            pretraga_knjiga()
        elif izbor == '3':
            prikaz_akcija()
        elif izbor == '4':
            pretraga_akcija()
        elif izbor == '5':
            prodaja_knjiga()
        elif izbor == '6':
            dodavanje_knjige()
        elif izbor == '7':
            izmena_knjiga()
        elif izbor == '8':
            logicko_brisanje()
        elif izbor == '9':
            return
        else:
            print('vas izbor nije ispravan, morate uneti broj 1-9')


def menadzer():
    while True:
        print_menadzer()
        izbor = input('unesite zeljenu akciju: ')
        while izbor == '':
            print('unos nije validan \n')
            izbor = input('ponovo unesite zeljenu vrednost: ')
        if izbor == '1':
            registracija()
        elif izbor == '2':
            prikaz_korisnika()
        elif izbor == '3':
            prikaz_knjiga()
        elif izbor == '4':
            pretraga_knjiga()
        elif izbor == '5':
            prikaz_akcija()
        elif izbor == '6':
            pretraga_akcija()
        elif izbor == '7':
            dodavanje_akcije()
        elif izbor == '8':
            izvestaj()
        elif izbor == '9':
            return
        else:
            print('vas izbor nije ispravan, morate uneti broj 1-9')


if __name__ == '__main__':
  loginmeni()