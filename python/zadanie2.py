#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    
   
    n = m = 0 
    while n < 1:
            start = int(input("Podaj liczbę  1 : "))
    while m < 1 or m <= n:
            stop = int(input("Podaj liczbę 2 : "))
            
    for i in range(n ,m + 1): 
        print(i,  '', end = '')
   
       
        
        
    

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
