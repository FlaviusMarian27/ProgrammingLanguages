#include <iostream>
#include "Carte.h"

using namespace std;

int main(void){
    cout << "=== 1. Inceput de program ===" << endl;

    Carte c1("Ion (Stack)",1920);
    
    cout << "\n=== 2. Intram intr-un bloc de cod temporar { ... } ===" << endl;
    {
        // B. Obiect TEMPORAR (tot pe Stack)
        // Traieste doar intre acoladele acestea.
        Carte c2("Baltagul (Temporar)", 1930);
        c2.afisareInfo();
        
        cout << "    ...suntem inca in bloc..." << endl;
    }

    // <--- AICI se apeleaza automat destructorul pentru c2!
    cout << "=== 3. Am iesit din bloc (c2 a murit deja) ===" << endl;

    cout << "\n=== 4. Alocare Dinamica pe HEAP (Stil Java) ===" << endl;
    // C. Obiect pe HEAP
    // Folosim 'new'. Returneaza pointer (*).
    Carte* c3 = new Carte("Morometii (Heap)", 1955);
    c3->afisareInfo();

    cout << "    ...c3 traieste pana il stergem noi..." << endl;

    delete c3;
    cout << "\n=== 5. Final de program ===" << endl;

    return 0;
}