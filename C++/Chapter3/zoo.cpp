#include <iostream>
#include <string>

using namespace std;

class Animal{
    protected:
        string nume;
    
    public:
        Animal(string n) : nume(n){}

    virtual void scoateSunet(){
        cout << "Animalul " << nume << " scoate un sunet ciudat." << endl;
    }

    virtual ~Animal(){
        cout << "[System] A fost sters animalul: " << nume << endl;
    }
};

class Leu : public Animal{
    public:
        Leu(string n) : Animal(n){}

        void scoateSunet() override{
            cout << "Leul " << nume << " rage: Rooooaahrrr!" << endl;
        }
};

class Maimuta : public Animal{
    public:
        Maimuta(string n) : Animal(n){}

        void scoateSunet() override{
            cout << "Maimuta " << nume << " face: Uh ah ah!" << endl;
        }
};

class Elefant : public Animal{
    public:
        Elefant(string n) : Animal(n){}

        void scoateSunet() override{
            cout << "Elefantul " << nume << " face: Taa-daaam!" << endl;
        }
};

int main(void){
    Animal *gradinaZoo[3];

    cout << "=== 1. Deschidem portile Zoo (Creare Obiecte) ===" << endl;
    gradinaZoo[0] = new Leu("Simba");
    gradinaZoo[1] = new Maimuta("George");
    gradinaZoo[2] = new Elefant("Dumbo");

    cout << "\n=== 2. Incepe Concertul (Polimorfism) ===" << endl;

    for(int i = 0; i < 3; i = i + 1){
        cout << "Animalul #" << i << ": ";
        gradinaZoo[i]->scoateSunet();
    }

    cout << "\n=== 3. Inchidem Zoo (Curatenie) ===" << endl;

    for(int i = 0; i < 3; i = i + 1){
        delete gradinaZoo[i];
    }

    return 0;
}