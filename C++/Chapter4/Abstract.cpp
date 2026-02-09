#include <iostream>
#include <string>
#include <vector>

using namespace std;

// 1. CLASA ABSTRACTA (Parintele)
class Forma{
    protected:
        string nume;

    public:
        Forma(string n) : nume(n){}

        // --- FUNCTIE NORMALA (Implementata) ---
        // O clasa abstracta poate avea logica comuna!
        void afiseazaNume(){
            cout << "Eu sunt o forma de tip: " << nume << endl;
        }

        // --- FUNCTIE VIRTUALA PURA (= 0) ---
        // Aici e cheia!
        // Spunem: "Orice forma are arie, dar NU stiu formula generica."
        // Cine ma mosteneste ESTE OBLIGAT sa scrie formula.
        // Echivalentul cu Abstractizarea din Java
        virtual double calculeazaAria() = 0;

        // Destructor Virtual (OBLIGATORIU)
        virtual ~Forma(){
            cout << "[System] Stergem forma: " << nume << endl;
        }
};

// 2. CLASA CONCRETA (Cerc)
class Cerc : public Forma{
    private:
        double raza;

    public:
        Cerc(double r) : Forma("Cerc"), raza(r){}

        // Daca stergem functia asta, primim eroare de compilare!
        // Suntem obligati sa implementam contractul (= 0) din parinte.
        double calculeazaAria() override{
            return 3.14 * raza * raza;
        }
};

// 3. CLASA CONCRETA (Dreptunghi)
class Dreptunghi : public Forma{
    private:
        double lungime;
        double latime;

    public:
        Dreptunghi(double lg, double lt) : 
            Forma("Dreptunghi"), lungime(lg),latime(lt) {}
        
        double calculeazaAria() override{
            return lungime * latime;
        }
};

class Patrat : public Forma{
    private:
        double lungime;

    public:
        Patrat(double l) : Forma("Patrat"), lungime(l) {}

        double calculeazaAria() override{
            return lungime * lungime;
        }
};

int main(void){
    // 1. TEST INSTANTIERE (GRESIT)
    // Forma f("Test"); // <--- EROARE: "Cannot instantiate abstract class"
    // Nu poti crea un concept abstract!

    // 2. POLIMORFISM
    // Dar poti face un vector de pointeri la acel concept.
    
    // Folosim vector din STL (ca ArrayList in Java)
    vector<Forma*> forme;
    forme.push_back(new Cerc(5.0));
    forme.push_back(new Dreptunghi(4.0,5.0));
    forme.push_back(new Patrat(7.0));

    cout << "=== Calculam Ariile ===" << endl;

    for(unsigned int i = 0; i < forme.size(); i = i + 1){
        cout << "Forma de la indexul " << i << " este: ";

        forme[i]->afiseazaNume();
        cout << "Aria: " << forme[i]->calculeazaAria() << endl; 
        cout << "-----------------" << endl;
    }

    for(unsigned int i = 0; i < forme.size(); i = i + 1){
        delete forme[i];
    }

    forme.clear();

    return 0;
}