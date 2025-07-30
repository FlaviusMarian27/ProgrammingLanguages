
As applications grow more complex, it becomes necessary to divide tasks into smaller sub-tasks. The C language provides **functions** for this purpose.

---

## Function Syntax

```c
tip_returnat nume_functie(param1, param2, ..., paramN) {
    // instructiuni
}
```

- `tip_returnat` – The return type of the function (`int`, `float`, or `void` if nothing is returned)
- `nume_functie` – Name of the function
- `param1, ..., paramN` – Parameters (each declared with a type)

Even if there are no parameters, you must still write `()`.

---

## Example: Drawing the letter E (without functions)

```c
#include <stdio.h>
int main() {
    int n, i;
    scanf("%d", &n);

    for (i = 0; i < n; i++) printf("*");
    printf("\n");
    for (i = 0; i < (n - 3) / 2; i++) printf("*\n");
    for (i = 0; i < n; i++) printf("*");
    printf("\n");
    for (i = 0; i < (n - 3) / 2; i++) printf("*\n");
    for (i = 0; i < n; i++) printf("*");
    printf("\n");
    return 0;
}
```

---

## Same example (with functions)

```c
#include <stdio.h>

void linieOrizontala(int n) {
    for (int i = 0; i < n; i++) printf("*");
    printf("\n");
}

void linieVerticala(int n) {
    for (int i = 0; i < (n - 3) / 2; i++) printf("*\n");
}

int main() {
    int n;
    scanf("%d", &n);
    linieOrizontala(n);
    linieVerticala(n);
    linieOrizontala(n);
    linieVerticala(n);
    linieOrizontala(n);
    return 0;
}
```

---

## Notes

- Functions must be defined **outside** any other function
- `main()` is where execution begins
- Parameters and local variables are **private** to the function

---

## Local vs Global Variables

|Local Variables|Global Variables|
|---|---|
|Exist during function call|Exist for entire program|
|Not initialized by compiler|Auto-initialized to 0|
|Visible only in that function|Visible across all functions|

---

## `return` Statement

```c
return valoare; // for non-void functions
return;         // for void functions
```

- Exits the function immediately

---

## Parameter Passing

In C, parameters are passed **by value**.

### Example (incorrect swap):

```c
void swap1(int x, int y) {
    int tmp = x;
    x = y;
    y = tmp;
}

int main() {
    int a = 5, b = 7;
    swap1(a, b);
    printf("%d %d\n", a, b); // prints 5 7
}
```

Why doesn't it work?

- `a` and `b` are copied into `x` and `y`
- Swapping `x` and `y` does **not affect** the originals

---

## Benefits of Using Functions

- Avoid code duplication
- Simplifies debugging
- Easier to test
- Promotes code reuse
- Allows modular design
- Improves readability with descriptive names

---

## Standard Library Functions

C comes with a rich standard library:

- `stdio.h` — input/output
- `math.h` — math functions
- `string.h` — string manipulation
- `stdlib.h` — memory management, conversions

You can include these with `#include <header.h>`

---

Copy and paste this whole note into **Obsidian** to use it as your reference. Let me know if you want the Romanian version as well or more examples!