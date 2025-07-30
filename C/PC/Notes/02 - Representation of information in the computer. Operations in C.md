
---

## 🔹 Variables in C

- Variables are named containers that store data.
- Must be declared with a **type** before use.
- Syntax:
  ```c
  int x = 5;
  float pi = 3.14;
  char letter = 'A';
  ```

- You can also declare multiple variables at once:
  ```c
  int a = 10, b = 20;
  ```

---

## 🔹 Reading Input from Keyboard

- C uses `scanf()` to read values from user input.
- Syntax:
  ```c
  int x;
  scanf("%d", &x);  // %d = format specifier for int
  ```

| Type     | Format Specifier |
|----------|------------------|
| `int`    | `%d`             |
| `float`  | `%f`             |
| `char`   | `%c`             |
| `double` | `%lf`            |

Example:
```c
int age;
printf("Enter your age: ");
scanf("%d", &age);
```

---

## 🔹 Number Systems

### 🔸 Binary (Base 2)
- Digits: `0` and `1`
- Computers work internally with binary.
- Example: `1010` = 10 in decimal

### 🔸 Octal (Base 8)
- Digits: `0` to `7`
- Prefix: `0`
- Example: `012` = 10 in decimal

### 🔸 Hexadecimal (Base 16)
- Digits: `0–9` and `A–F`
- Prefix: `0x`
- Example: `0xFF` = 255 in decimal

---

## 🔹 Integer Data Types in C

| Type            | Description                          | Size (typical) |
|------------------|--------------------------------------|----------------|
| `int`           | Standard integer                     | 4 bytes        |
| `short`         | Smaller range integer                | 2 bytes        |
| `long`          | Large range integer                  | 4/8 bytes      |
| `unsigned int`  | Only positive values                 | 4 bytes        |
| `char`          | Single character or small integer    | 1 byte         |

Example:
```c
unsigned int count = 100;
```

---

## 🔹 Logical Operators

Used to combine conditions:

| Operator | Name     | Example             |
|----------|----------|---------------------|
| `&&`     | AND      | `a > 0 && b < 10`   |
| `||`     | OR       | `x == 0 || y != 5`  |
| `!`      | NOT      | `!(a == b)`         |

Result:  
- `true` = non-zero  
- `false` = 0

---

## 🔹 Relational Operators

Used for comparison:

| Operator | Meaning         | Example         |
|----------|------------------|-----------------|
| `==`     | Equal            | `a == b`        |
| `!=`     | Not equal        | `x != 0`        |
| `>`      | Greater than     | `a > 5`         |
| `<`      | Less than        | `b < 100`       |
| `>=`     | Greater or equal | `score >= 50`   |
| `<=`     | Less or equal    | `temp <= 20`    |

Returns 1 (true) or 0 (false).

---

## 🔹 Conditional Statement: `if`

```c
if (condition) {
    // runs if condition is true
} else {
    // runs if condition is false
}
```

You can chain conditions with `else if`:
```c
if (grade >= 9)
    printf("Excellent");
else if (grade >= 7)
    printf("Good");
else if (grade >= 5)
    printf("Pass");
else
    printf("Fail");
```

---

## 🔹 Ternary Operator

A compact way to write simple `if` conditions.

Syntax:
```c
(condition) ? value_if_true : value_if_false;
```

Example:
```c
int max = (a > b) ? a : b;
```

---

## 🔹 Operator Precedence & Associativity

### 🔸 Precedence (order of execution):

From high to low:

1. `()` – parentheses  
2. `!` – logical NOT  
3. `*`, `/`, `%` – multiplication, division, modulo  
4. `+`, `-` – addition, subtraction  
5. `==`, `!=`, `<`, `>`, `<=`, `>=`  
6. `&&` – logical AND  
7. `||` – logical OR  
8. `=`, `+=`, `-=` – assignment  

### 🔸 Associativity:

| Operators       | Associativity   |
|-----------------|-----------------|
| `+`, `-`, `*`, `/`, `%` | Left to right |
| `=`, `+=`, `-=`         | Right to left |

---

### 🔍 Example:

```c
int result = 2 + 3 * 4;      // result = 14 (3 * 4 first)
int fixed = (2 + 3) * 4;     // fixed = 20 (2 + 3 first)
```

---

✅ Use this lab to understand how C handles values, types, and logical decisions at a low level — essential for writing structured programs.
