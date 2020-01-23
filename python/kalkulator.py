#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kalkulator.py

wynik = 0

def PobierzLiczbe():
    liczba = int(input('Podaj liczbe:'))
    return liczba
    

def Wynik():
    
    
def Dodaj(liczba1 , liczba2)
    global wynik
    wynik = liczba1 + liczba2
    
    return wynik
    
    
def Odejmij(liczba1 , liczba2)
    global wynik
    wynik = liczba1 - liczba2
    
    return wynik
    
def Podziel(liczba1 , liczba2)
    global wynik
    wynik = liczba1 / liczba2
    
    return  wynik

    
def Pomnoz(liczba1 , liczba2)
    global wynik
    wynik = liczba1 * liczba2
    
    return wynik
    
def WydrukujWynik():
    

def main(args):
    
operacja = input("Jaka operacje chcesz wykonac (+ , - , / , * )")
    
    liczba1 = PobierzLiczbe()
    liczba2 = PobierzLiczbe()
    wynik1 = Dodaj()
    wynik2 = Odejmij()
    wynik3 = Podziel()
    wynik4 = Pomnoz()
    
    

   
   if operacja == '+':
       Dodaj(liczba ,liczba2)
    elif operacja == '-':
        Odejmij(liczba1 ,liczba2)
    elif operacja == '/':
        Podziel(liczba1 ,liczba2)
    elif operacja == '*':
        Pomnoz(liczba ,iczba2)
        
   

    
    return 0




if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
