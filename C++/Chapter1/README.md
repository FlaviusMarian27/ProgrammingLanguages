# Chapter 1: Anatomy of a Class in C++

## 📂 Structura Fișierelor

În C++, o clasă nu stă într-un singur fișier.

### 1. Header File (`NumeClasa.h`) - "Contractul"
* Conține doar **declarațiile** (variabile și prototipurile funcțiilor).
* Echivalentul unei interfețe din Java, dar pentru o clasă concretă.
* **Obligatoriu:** Începe cu `#pragma once` pentru a preveni erorile de includere multiplă.

### 2. Source File (`NumeClasa.cpp`) - "Implementarea"
* Conține codul efectiv al funcțiilor.
* Trebuie să includă header-ul: `#include "NumeClasa.h"`.
* Folosește operatorul `::` pentru a lega funcțiile de clasă.

---

## ⚠️ Diferențe Critice față de Java

| Concept | Java | C++ |
| :--- | :--- | :--- |
| **Definirea Clasei** | `class A { ... }` | `class A { ... };` (Semicoloana e obligatorie!) |
| **Acces (Public/Private)** | `private int x;` pe fiecare linie | Blocuri `private:` și `public:` |
| **Pointerul `this`** | `this.variabila` | `this->variabila` (este pointer) |
| **Legătura Metodă-Clasă** | Implicită (în interiorul clasei) | Explicită: `void Clasa::Metoda() { ... }` |
| **Instanțiere (Stack)** | Nu există (doar Heap) | `Clasa obj;` (Fără `new` - Recomandat) |
| **Instanțiere (Heap)** | `Clasa obj = new Clasa();` | `Clasa* obj = new Clasa();` (Pointer) |

---

## 📝 Exemplu de Sintaxă

### Fisier: `Carte.h`
```cpp
#pragma once
#include <string>

class Carte {
private:
    std::string titlu; // Membru privat
public:
    Carte(std::string t); // Constructor (doar declaratie)
    void afiseaza();      // Metoda (doar declaratie)
}; // <--- ATENTIE LA SEMICOLOANA!