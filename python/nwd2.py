#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nwd2.py


def main(args):
    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    licznik = 0
    while a > 0 :
        licznik += 1
        a %= b
        b -= a 
        
            
    print("Nwd =" , b )
    print("licznik:" , licznik)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
