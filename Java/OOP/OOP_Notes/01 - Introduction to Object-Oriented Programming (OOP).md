## What is Object-Oriented?

- Object-oriented is a **programming style**.
- Software systems can be decomposed into smaller entities.

---

## Algorithmic Decomposition

- Each entity represents an execution step in a task.

### Structure

```
Main Routine
├── Routine 1
│   ├── Routine 1.1
│   └── Routine 1.2
├── Routine 2
└── Routine 3
```

- Data is external and passed among routines.

---

## Object-Oriented Decomposition

- The system is decomposed into **collaborating objects** (and their classes).

### Structure

```
Object
├── Data
└── Operations

Objects collaborate via method invocations.
```

---

## Partial Definition of OOP (Grady Booch)

> "Object-oriented programming is a method of program implementation in which programs are organized as cooperative collections of objects."

---

## First Steps in Java

### First Java Program

```java
class PrimulProgram {
   public static void main(String argv[]) {
        System.out.println("Hello world!");
   }
}
```

### Compile and Run

```bash
javac Prog.java  # generates PrimulProgram.class (bytecode)
java PrimulProgram  # executes main method
```

---

## Primitive Data Types

|Type|Bits|Example / Range|
|---|---|---|
|byte|8|-128 to 127|
|short|16|-32768 to 32767|
|int|32|-2147483648 to 2147483647|
|long|64|-9223372036854775808 to 9223372036854775807|
|float|32|±1.4E−45 to ±3.4028235E+38|
|double|64|±4.9E−324 to ±1.7976931348623157E+308|
|char|16|'a', '\u03C0' (Unicode encoding)|
|boolean|-|true, false (keywords)|

---

## Identifiers

- Naming of program entities (variables, parameters).
- Can start with letters, `_`, `$`. Contains letters, digits, `_`, `$`.
- Java is case-sensitive (e.g., `a` ≠ `A`).

---

## Local Variables

- Allocated on the execution stack.
- Must be explicitly initialized.

```java
class Example {
  public static void main(String[] args) {
    int a = 10;
    String b = "Mama";
    double c;

    System.out.println(a);
    System.out.println(b);
    System.out.println(c); // compilation error (uninitialized)
  }
}
```

---

## Operators

### Arithmetic Operators
- Unary: `+`, `-`
- Multiplicative: `*`, `/`, `%`
- Additive: `+`, `-`

### Logical Operators
- Negation: `!`
- Conjunction: `&&`, `&`
- Disjunction: `||`, `|`
- Exclusive OR: `^`

### Relational & Equality Operators
- Equality: `==`, `!=`
- Relational: `<`, `<=`, `>`, `>=`
    

### Assignment Operators
- `=`, `+=`, `*=`, etc.

### Conditional Operator
- Ternary: `exp_boolean ? exp1 : exp2`

---

## Control Statements

### if-else Statement

```java
if (boolean_expression) {
  // code
} else {
  // optional else code
}
```

### switch Statement

```java
switch(expression) {
  case constant1:
    // code
    break;
  case constant2:
    // code
    break;
  default:
    // code
}
```

### Loops

- **while loop**:

```java
while(boolean_expression) {
  // code
}
```

- **do-while loop**:

```java
do {
  // code
} while(boolean_expression);
```

- **for loop**:

```java
for(initialization; boolean_expression; update) {
  // code
}
```

### Break & Continue

- **break** exits the loop.
- **continue** skips the current iteration.

```java
for(int j = 0; j < 10; j++) {
  if(j == 5) continue;
  System.out.println(j);
}
```

OUTPUT: 0, 1, 2, 3, 4, 6, 7, 8, 9