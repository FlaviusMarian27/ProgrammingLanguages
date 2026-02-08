# Capitolul 3: Moștenirea și Polimorfismul.

## 1. Moștenirea (Inheritance)

**Definiție:** Capacitatea unei clase (Copil/Derivată) de a prelua atributele și metodele altei clase (Părinte/Bază). Este relația de tip **"IS-A"** (ex: Pisica ESTE un Animal).

* **În Java:** Foloseai `extends`.
    ```java
    class Pisica extends Animal { ... }
    ```
* **În C++:** Folosești două puncte `:` urmate de tipul de acces (de obicei `public`).
    ```cpp
    class Pisica : public Animal { ... };
    ```

> **⚠️ Marea Diferență:** C++ suportă **Moștenire Multiplă**. O clasă poate avea 2 părinți simultan.
> *Exemplu C++:* `class Strutocamila : public Strut, public Camila { ... };`
> (În Java acest lucru era interzis, se puteau folosi doar interfețe multiple).

---

## 2. Polimorfismul (Polymorphism)

**Definiție:** Capacitatea de a trata un obiect dintr-o clasă derivată (`Pisica`) ca și cum ar fi din clasa de bază (`Animal`), dar programul să fie suficient de inteligent încât să execute metoda specifică derivatei.

### Tipuri:
1.  **Static (Compile-time):** Overloading (supraîncărcarea funcțiilor - același nume, parametri diferiți). Există și în Java.
2.  **Dinamic (Run-time):** Aici este diferența majoră. Se întâmplă când ai un pointer de tip `Animal*` care arată spre o `Pisica` și apelezi `scoateSunet()`.

> **⚠️ Marea Diferență:**
> * **Java:** Toate metodele (care nu sunt statice/finale) sunt polimorfice **implicit**. Java știe automat să apeleze metoda din `Pisica`.
> * **C++:** Polimorfismul este **OPȚIONAL**. Dacă nu pui cuvântul cheie `virtual` în clasa părinte, C++ va apela metoda din `Animal` (ignoranța totală față de copil).
> * Aceasta este diferența dintre **"Early Binding"** (C++ default) și **"Late Binding"** (Java default / C++ virtual).

---

## 3. Override (Suprascriere)

**Definiție:** Momentul în care clasa copil decide să schimbe comportamentul unei metode moștenite de la părinte.

* **În Java:** Scriai (opțional) `@Override` deasupra metodei.
* **În C++:** Scrii cuvântul cheie `override` **după** numele funcției (la finalul liniei).
    ```cpp
    void scoateSunet() override;
    ```

**De ce e vital `override` în C++?**
Este o măsură de siguranță. Dacă greșești puțin numele funcției sau tipul parametrilor în clasa copil, C++ va crede că ai creat o funcție *nouă*, nu că o suprascrii pe cea veche. Cuvântul `override` obligă compilatorul să verifice: *"Există funcția asta în părinte?"*. Dacă nu, primești eroare la compilare.

---

## 4. Conceptul Extra: `virtual` (Specific C++)

Acest concept nu exista explicit în Java (fiind comportamentul default).

În C++, `virtual` pus în fața unei funcții spune compilatorului:
> *"Nu decide acum (la compilare) ce funcție să apelezi. Așteaptă până rulează programul, vezi ce tip de obiect se află de fapt la acea adresă de memorie, și apelează funcția corectă."*

---

## 📊 Tabel Recapitulativ: Java vs. C++

| Concept | Java (Ce știi) | C++ (Ce scriem acum) |
| :--- | :--- | :--- |
| **Moștenire** | `extends` | `: public` |
| **Super-clasa** | `super` | `NumeClasaParinte::` |
| **Polimorfism** | Implicit (automat) | **Explicit** (trebuie `virtual`) |
| **Suprascriere** | `@Override` (înainte) | `override` (după funcție) |
| **Interfețe** | `interface` | Clase Abstracte Pure (metode `= 0`) |