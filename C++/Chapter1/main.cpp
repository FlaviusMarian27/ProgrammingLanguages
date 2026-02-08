#include <iostream>
#include "Carte.h"

using namespace std;

int main(void){
    Carte c1("Ion", 1920);
    c1.afisareInfo();
    // in cazul acesta c1 este sters automat la final/distrus
    // practic in C++ aceasta ii varianta statica, varinta in care c1 este creat pe STACK
    // obiectul c1 este creat static

    Carte *c2 = new Carte("Morometii",1955);
    c2->afisareInfo();
    delete c2;
    //varianta cu "new" este varianta alocata dinamic practic pe HEAP
    //practic avem un pointer aici.
    //Atentie mare!!! in C++, nu exista Garbage Collector standard
    //Totul trebuie sters manual!!!


    return 0;
}