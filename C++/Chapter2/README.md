# Capitolul 2: Managementul Memoriei

Acest capitol acoperă cea mai mare diferență conceptuală față de Java: **gestionarea manuală a memoriei**.
În C++, programatorul este responsabil pentru "curățenie", nu există un Garbage Collector care să ruleze automat în fundal (decât în situații specifice cu smart pointers, pe care îi vom discuta mai târziu).

## 🗑️ Destructorul

În Java, eliberarea memoriei se face automat. În C++, avem o funcție specială numită **Destructor** care se apelează atunci când un obiect este distrus.

* **Scop:** Eliberarea resurselor (memorie, fișiere deschise, conexiuni).
* **Sintaxă:** `~NumeClasa()`.
* **Regulă:** Nu are parametri și nu returnează nimic.

```cpp
// Fisier: Carte.h
class Carte {
public:
    Carte();  // Constructor
    ~Carte(); // Destructor (NOU)
};

// Fisier: Carte.cpp
Carte::~Carte() {
    // Aici scriem codul de curatenie (ex: delete[] pointeri)
    std::cout << "Obiect distrus, memorie eliberata." << std::endl;
}
```

## ⚔️ Stack (Stivă) vs. Heap (Grămadă)

În Java, aproape toate obiectele sunt pe Heap (new). În C++, ai două opțiuni.

1. Stack (Memorie Statică/Automată) - RECOMANDAT
*   Viteza: Foarte mare.
*   Viața: Obiectul trăiește doar în interiorul blocului `{ ... }` în care a fost creat.
*   **Distrugere:** Automată. Când se termină funcția/blocul, se apelează destructorul singur.

```cpp
void functie() {
    Carte c1; // Obiect creat pe Stack
    c1.afiseaza();
} // <--- Aici c1 este distrus AUTOMAT.
```

2. Heap (Memorie Dinamică) - Stil Java
*   **Viteza:** Mai lentă (alocare manuală).
*   **Viața:** Obiectul trăiește până când decizi tu să îl ștergi.
*   **Distrugere:** Manuală. Trebuie să folosești delete.

```cpp
void functie() {
    Carte* c2 = new Carte(); // Obiect creat pe Heap (pointer)
    c2->afiseaza();          // Accesam cu sageata ->
    
    delete c2; // <--- OBLIGATORIU: Daca uitam asta, avem MEMORY LEAK.
}
```

## ⚠️ Tabel Comparativ: Java vs. C++

| Concept | Java (Ce știi) | C++ (Cum e corect) |
| :--- | :--- | :--- |
| **Creare Obiect** | `Carte c = new Carte();` | **Stack:** `Carte c;` (Preferat)<br>**Heap:** `Carte* c = new Carte();` |
| **Acces Membri** | `c.metoda()` | **Stack:** `c.metoda()`<br>**Heap:** `c->metoda()` |
| **Distrugere** | Garbage Collector (Automat) | **Stack:** Automat (la `}`)<br>**Heap:** Manual (`delete c;`) |
| **Destructor** | Nu există (doar `finalize`) | `~Carte() { ... }` |