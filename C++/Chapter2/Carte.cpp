#include "Carte.h"

//implementare constructor(folosim metoda cu Lista de initializare)
Carte::Carte(string title, int year) : titlu(title), anPublicare(year) {
    cout << " [+] CONSTRUCTOR: S-a nascut cartea '" << titlu << "'" << endl;
}

//implementare destructor
Carte::~Carte(){
    cout << " [-] DESTRUCTOR:  A murit cartea  '" << titlu << "' (Memorie eliberata)" << endl;
}

void Carte::afisareInfo(){
    cout << "     Info: " << titlu << " din anul " << anPublicare << endl;
}