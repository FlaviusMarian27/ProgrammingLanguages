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