#pragma once
#include <string>
#include <iostream>

using namespace std;

class Carte{
    private:
        string titlu;
        int anPublicare;

    public:
        Carte(string title, int year);

        ~Carte(); //Destructor (Nou - piesa de rezistenta)

        void afisareInfo();
};

