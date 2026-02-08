#include <iostream>
#include <string>

using namespace std;

// --- CLASA DE BAZA (Parinte) ---
class Animal{
    protected:
        string nume;
    
    public:
        // Constructor definit DIRECT in clasa
        Animal(string n) : nume(n){
            cout << "[Animal] S-a nascut: " << nume << endl;
        }

        // Metoda definita DIRECT in clasa
        // 'virtual' e necesar pentru ca o vom suprascrie
        virtual void scoateSunet(){
            cout << "Animalul " << nume << " scoate un sunet generic." << endl;
        }

        // Destructor (tot virtual)
        virtual ~Animal(){
            cout << "[Animal] A murit: " << nume << endl;
        }
};

// CLASA CAINE (Extends Animal)
class Caine: public Animal{
    public:
        // Constructorul
        // Aici ": Animal(n)" este echivalentul lui "super(n)"
        Caine(string n) : Animal(n){
            cout << "[Caine]  Constructor specific." << endl;
        }

        // Override (Suprascriem metoda)
        void scoateSunet() override {
            cout << "Cainele " << nume << " face: HAM HAM!" << endl;
        }

        ~Caine(){
            cout << "[Caine]  Destructor specific." << endl;
        }
};

// CLASA PISICA (Extends Animal)
class Pisica : public Animal{
    public:
        Pisica(string n) : Animal(n){
            cout << "[Pisica] Constructor specific." << endl;
        }

        void scoateSunet() override{
            cout << "Pisica " << nume << " face: MIAU MIAU!" << endl;
        }

        ~Pisica(){
            cout << "[Pisica] Destructor specific." << endl;
        }
};

int main(void){
    cout << "=== Testare Polimorfism (Stil Java) ===" << endl;
    
    // Pointer la Baza = New Copil
    Animal *a = new Caine("Rex");
    Animal *b = new Pisica("Kitty");

    cout << "\n--- Sunete ---" << endl;
    a->scoateSunet();
    b->scoateSunet();

    cout << "\n--- Curatenie (Delete) ---" << endl;

    delete a;
    delete b;

    cout << endl;

    Caine* c = new Caine("Bobi");
    c->scoateSunet();
    delete c;

    return 0;
}

/*
Dacă te uiți atent la linia Animal* a, variabila a este doar un pointer către un Animal. 
Teoretic, calculatorul ar trebui să zică: "Ok, a este un Animal, deci voi executa funcția 
scoateSunet() din clasa Animal".

DAR, datorită polimorfismului (activat de cuvântul virtual), calculatorul face ceva mai 
deștept la rulare:
    - Se uită la pointerul a.
    - Verifică: "Ce obiect se află de fapt la această adresă?"
    - Vede că e un Caine.
    - Execută scoateSunet() din Caine, nu din Animal.
*/