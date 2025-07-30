
## Increment and Decrement Operators

- `++x` / `--x` (prefix): increment/decrement first, then return value
- `x++` / `x--` (postfix): return value first, then increment/decrement

### Example

```c
int a=3,b=7,c;
c=a++ + ++b;   // a=4, b=8, c=11
c=--a + --b;   // a=3, b=7, c=10
c=--a - b--;   // a=2, b=6, c=-5
c=a-- - --b;   // a=1, b=5, c=-3
```

## `switch` Statement

- Useful for checking a variable against multiple values
    

```c
switch(expression) {
  case value1:
    // statements
    break;
  case value2:
    // statements
    break;
  default:
    // fallback
}
```

- Use `break` to exit case
- `default` is optional
- Group multiple `case` labels for same logic

## `while` Loop

- Executes a block while the condition is true

```c
int v = 1;
while (v < n) {
  printf("%d\n", v);
  v *= 2;
}
```

## Formatting Tips

- Indent nested statements
- Use either tabs or spaces (not both)
- Place `{}` on separate lines
- Match opening/closing braces visually
- Align `else if`, `switch`, and `case` blocks clearly

## `for` Loop

- Compact loop for known iteration counts

```c
for (i = 0; i < n; i++) {
  // logic
}
```

- Equivalent to `while (i < n)` with init and update
- Can include multiple expressions using `,`

## `do...while` Loop

- Executes block at least once, condition checked afterward

```c
do {
  // logic
} while (condition);
```

## Nested Loops

```c
for (i = 0; i < n; i++) {
  for (j = 0; j < i; j++) {
    printf("*");
  }
  printf("\n");
}
```

## `break` and `continue`

- `break`: exits the loop
- `continue`: skips to next iteration

```c
for (;;) {
  scanf("%g", &r);
  if (r == expected) break;
  if (r == 0) continue;
  // logic
}
```

## Comma Operator `,`

- Evaluates expressions left to right, returns last

```c
int a = (i++, j + 1); // i is incremented, a = j + 1
```

## Fibonacci Example

```c
if (n == 0) f = 0;
else if (n == 1) f = 1;
else {
  for (fm2 = 0, fm1 = 1, i = 2; i <= n; f = fm1 + fm2, fm2 = fm1, fm1 = f, i++) {}
}
```

Use `{}` as empty block if no loop body is needed.

---

## **Summary:**
- Increment/Decrement
- `switch` selection
- `while`, `do...while`, `for` loops
- Nested loops
- `break`, `continue`
- `,` operator for sequencing
- Formatting practices for clean code