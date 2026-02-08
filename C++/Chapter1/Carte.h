#pragma once
// comanda speciala: Incarca o singura data fisierul - este obligatoriu

#include <string>
using namespace std;

class Carte{
    //zona de date (de obicei private, ca si in java)

    private:
        string titlu;
        int anPublicare;

    //zona de metode (de obicei publice, ca si in java)
    public:
        //Constructorul(Doar semnatura acestuia fara cod)
        Carte(string t, int an);

        //O metoda
        void afisareInfo();

        string getTitlu();
};