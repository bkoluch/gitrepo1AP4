/*
 * cwltab.cpp
 * 
 * Copyright 2020  <>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>

using namespace std;

void pobierzLiczby(int  tablica1[] ,  int n) {
    for  (int i = 0; i < n; i++) {
        cout << "Podaj liczby: ";
        cin >> tablica1[i];
    }
}

void pobierzLiczby2(int tablica2[], int n) {
    
    for  (int i = 0; i < n; i++) {
        
        cout << "Podaj liczby: ";
        cin >> tablica2[i];
    }
    cout << endl;
}

float Sumuj (int tablica[], int n) {
    int suma = 0;
    for (int i = 0; i < n; i++) {
        suma = tablica2[i] + tablica1[i];
    }
    return (float)suma / (float)n;


int main(int argc, char **argv)
{
    
    int n = 5
    int tablica1[n]:
    int tablica2[n];
    pobierzLiczby1(tablica1 , n);
    pobierzLiczby2(tablica2, n);
    drukuj(tablica1, n);
    drukuj(tablica2, n);
    int s1 = sumujTab(tablica1 , n);
    int s2 = sumujTab(tablica2 , n);
	return 0;
    
}

