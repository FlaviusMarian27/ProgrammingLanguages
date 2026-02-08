#include <iostream>
#include "Carte.h"

using namespace std;

// Sintaxa: TipReturnat NumeClasa::NumeFunctie(parametri) { ... }

// Implementarea Constructorului
Carte::Carte(string title, int year){
    this->titlu = title; // this reprezinta un pointer in C++, deci trebuie folosit C++
    this->anPublicare  = year;
}

//Implementarea metoda
void Carte::afisareInfo(){
    cout << "Cartea: " << titlu << " (" << anPublicare << ")" << endl; 
}

//Implementare getter
string Carte::getTitlu(){
    return this->titlu;
}