# Capitolul 4: Clase Abstracte și Funcții Virtuale Pure

Acest capitol abordează echivalentul conceptelor de `interface` și `abstract class` din Java.
În C++, nu avem cuvinte cheie separate pentru acestea. Totul se face prin **Funcții Virtuale Pure**.

## 1. Ce este o Funcție Virtuală Pură?

Este o funcție care **NU are implementare** (corp) în clasa de bază. Este doar o definiție, o "promisiune" că această funcție va exista în clasele copil.

* **Sintaxă:** Se adaugă `= 0` la finalul declarației.
    ```cpp
    virtual void makeMove() = 0; // <--- Aceasta este o functie pura
    ```
* **Semnificație:** "Eu (clasa părinte) nu știu să fac asta, dar te oblig pe tine (clasa copil) să scrii codul pentru ea."

---

## 2. Ce este o Clasă Abstractă?

În C++, o clasă devine **automat** abstractă dacă conține **cel puțin o funcție virtuală pură**.

### Regulile de Aur:
1.  **Interzisă Instanțierea:** Nu poți crea obiecte din această clasă.
    * `Animal a;` ❌ (Eroare de compilare)
    * `Animal* a;` ✅ (Pointerii sunt permiși și necesari pentru polimorfism)
2.  **Obligativitatea Implementării:** Orice clasă care moștenește o clasă abstractă **TREBUIE** să implementeze toate funcțiile pure.
    * Dacă nu o face, devine și ea abstractă (nu o poți instanția).

---

## 3. Java vs. C++ (Dicționar de Traducere)

Deoarece C++ nu are cuvântul `interface`, folosim clase abstracte pentru a simula acest comportament.

| Concept Java | Implementare C++ | Descriere |
| :--- | :--- | :--- |
| **`abstract class`** | Clasă cu **unele** funcții virtuale pure (`= 0`) și altele normale. | Poate avea și variabile membre (`int x`), constructor și logică comună. |
| **`interface`** | Clasă cu **TOATE** funcțiile virtuale pure (`= 0`). | Nu are variabile membre (decât statice), doar metode publice pure. |
| **`implements`** | `: public Interfata` | Se folosește tot sintaxa de moștenire. |

---

## 4. De ce avem nevoie de Destructor Virtual?

Chiar dacă o clasă este abstractă pură (Interfață), ea **trebuie** să aibă un destructor virtual (chiar și gol).

```cpp
virtual ~Interfata() {}
```

**Motivul:** Când ștergem un obiect prin pointerul interfeței (delete player;), compilatorul trebuie să știe să apeleze destructorul clasei concrete (~HumanPlayer). Fără virtual, se produce un Memory Leak.

## 📝 Exemplu de Sintaxă (Blueprint)

### Interfața (Fisier .h)

```cpp
class Player {
public:
    // 1. Functie Pura (Interface method)
    // Toti jucatorii TREBUIE sa aiba o metoda de mutare.
    virtual void makeMove() = 0; 

    // 2. Destructor Virtual (Obligatoriu)
    virtual ~Player() {}
};
```

### Implementarea (Clasa Concretă)

```cpp
class HumanPlayer : public Player {
public:
    // Suntem OBLIGATI sa scriem codul pentru makeMove,
    // altfel HumanPlayer nu poate fi creat.
    void makeMove() override {
        std::cout << "Omul a mutat." << std::endl;
    }
};
```

# Interfața este echivalentul unei clase abstracte pure, clasă care poate conține spre exemplu:
```cpp
// Interface equivalent pure abstract class
class I {
  public:
    virtual string getName() = 0;
};

// Class B which inherits I
class B : public I {
  public:
    string getName() {
        return "GFG";
    }
};

// Class C which inherits I
class C : public I {
  public:
    string getName() {
        return "GeeksforGeeks";
    }
};

int main() {
    B obj1;
    C obj2;
    I *ptr;

    // Assigning the address of obj1 to ptr
    ptr = &obj1;
    cout << ptr->getName() << endl;

    // Assigning the address of obj2 to ptr
    ptr = &obj2;
    cout << ptr->getName();
  
    return 0;
}
```

---

# 📦 std::vector (Echivalentul ArrayList)

În C++, nu folosim `ArrayList`, ci `std::vector`. Este un array dinamic care își redimensionează automat memoria.
Pentru a-l folosi, trebuie inclus header-ul: `#include <vector>`.

## ⚔️ Java vs. C++ (Tabel Rapid)

| Operație | Java (`ArrayList<Integer>`) | C++ (`std::vector<int>`) |
| :--- | :--- | :--- |
| **Creare** | `var list = new ArrayList<>();` | `std::vector<int> list;` |
| **Adăugare** | `list.add(10);` | `list.push_back(10);` |
| **Accesare** | `list.get(0);` | `list[0]` sau `list.at(0)` |
| **Modificare** | `list.set(0, 50);` | `list[0] = 50;` |
| **Dimensiune** | `list.size();` | `list.size();` |
| **Ștergere (Ultimul)**| `list.remove(list.size()-1);` | `list.pop_back();` |
| **Verificare gol** | `list.isEmpty();` | `list.empty();` |
| **Ștergere Tot** | `list.clear();` | `list.clear();` |

---

## 🛠️ Cele mai folosite funcții

### 1. Adăugarea elementelor
În C++ se adaugă mereu la final (coadă).
```cpp
vector<string> nume;
nume.push_back("Ana");
nume.push_back("Ion");
```

## 2. Accesarea Elementelor
Există două moduri principale:

* **Rapid (Nesigur):** `nume[0]`
    * Nu verifică limitele memoriei.
    * **Riscuri:** Dacă accesezi `nume[100]` și lista are doar 2 elemente, programul crapă (*Segmentation Fault*) sau, mai rău, returnează date "gunoi" de la acea adresă.
* **Sigur (Lent):** `nume.at(0)`
    * Verifică limitele înainte de accesare.
    * **Siguranță:** Dacă greșești indexul, aruncă o excepție controlată (`std::out_of_range`).

---

## 3. Iterarea (Parcurgerea)

### Varianta Modernă (Recomandată)
Cunoscută ca *Range-based for loop*. Este exact ca "Enhanced For" din Java.
```cpp
for (string s : nume) {
    cout << s << endl;
}
```

### Varianta Clasică (cu index)
*   ⚠️**Atenție**: Funcția **.size()** returnează **unsigned int** (sau **size_t**), nu **int**.

```cpp
// Folosim 'size_t' pentru a evita warning-urile de comparatie (int vs unsigned)
for (size_t i = 0; i < nume.size(); i++) {
    cout << nume[i] << endl;
}
```

Sigur, iată textul formatat, gata de adăugat în continuarea secțiunii despre std::vector din README-ul tău.

Markdown
## 2. Accesarea Elementelor
Există două moduri principale:

* **Rapid (Nesigur):** `nume[0]`
    * Nu verifică limitele memoriei.
    * **Riscuri:** Dacă accesezi `nume[100]` și lista are doar 2 elemente, programul crapă (*Segmentation Fault*) sau, mai rău, returnează date "gunoi" de la acea adresă.
* **Sigur (Lent):** `nume.at(0)`
    * Verifică limitele înainte de accesare.
    * **Siguranță:** Dacă greșești indexul, aruncă o excepție controlată (`std::out_of_range`).

---

## 3. Iterarea (Parcurgerea)

### Varianta Modernă (Recomandată)
Cunoscută ca *Range-based for loop*. Este exact ca "Enhanced For" din Java.
```cpp
for (string s : nume) {
    cout << s << endl;
}
Varianta Clasică (cu index)
⚠️ Atenție: Funcția .size() returnează unsigned int (sau size_t), nu int.

C++
// Folosim 'size_t' pentru a evita warning-urile de comparatie (int vs unsigned)
for (size_t i = 0; i < nume.size(); i++) {
    cout << nume[i] << endl;
}
```

### 4. Ștergerea unui element specific

*   În C++, ștergerea de la un index arbitrar se face folosind iteratori, nu direct indexul numeric ca în Java (**remove(2)**).

### ⚠️ Diferență Critică: Vector de Obiecte vs. Pointeri

**Cazul 1: Vector de Obiecte (Valori)**
Stochează copiile obiectelor direct în vector. 

```cpp
vector<Robot> roboti;
roboti.push_back(Robot("R2D2")); 
// ATENTIE: Aici se face o COPIE a obiectului in vector.
// Memoria este eliberata AUTOMAT cand vectorul este distrus.
```

**Cazul 2: Vector de Pointeri (Polimorfism)**
*   Dacă vrei polimorfism (ex: Animal* care ține și Pisica și Caine la un loc), ești obligat să folosești vector de pointeri.

```cpp
vector<Animal*> zoo;
zoo.push_back(new Pisica("Tom")); // Heap Allocation
zoo.push_back(new Caine("Rex"));  // Heap Allocation

// CRITIC: Cand nu mai ai nevoie de vector, trebuie sa dai DELETE manual!
// Altfel ai Memory Leak (Java are Garbage Collector, C++ NU).
for(size_t i = 0; i < zoo.size(); i++) {
    delete zoo[i]; // Sterge obiectul din memorie (Heap)
}
zoo.clear(); // Goleste vectorul de adrese (Stack)
```