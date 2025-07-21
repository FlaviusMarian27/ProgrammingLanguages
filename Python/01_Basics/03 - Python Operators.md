## ➕ Arithmetic Operators

Used for basic mathematical operations.

| Operator | Description        | Example        |
|----------|--------------------|----------------|
| `+`      | Addition            | `a + b`        |
| `-`      | Subtraction         | `a - b`        |
| `*`      | Multiplication      | `a * b`        |
| `/`      | Division            | `a / b`        |
| `//`     | Floor division      | `a // b`       |
| `%`      | Modulus (remainder) | `a % b`        |
| `**`     | Exponentiation      | `a ** b`       |

### 🔹 Example:

```python
a = 10
b = 3
print(a + b)    # 13
print(a // b)   # 3
print(a ** b)   # 1000
```

---
## 🔁 Comparison Operators

- Used to compare values; return `True` or `False`.

| Operator | Description      | Example  |
| -------- | ---------------- | -------- |
| `==`     | Equal            | `a == b` |
| `!=`     | Not equal        | `a != b` |
| `>`      | Greater than     | `a > b`  |
| `<`      | Less than        | `a < b`  |
| `>=`     | Greater or equal | `a >= b` |
| `<=`     | Less or equal    | `a <= b` |

---
## 🔗 Logical Operators

- Used to combine conditions.

|Operator|Description|Example|
|---|---|---|
|`and`|True if both|`a > 0 and b > 0`|
|`or`|True if either|`a > 0 or b > 0`|
|`not`|Inverts boolean|`not(a > 0)`|

---
## 🧱 Assignment Operators

- Assign values to variables.

|Operator|Example|Equivalent to|
|---|---|---|
|`=`|`a = 5`|assign 5 to a|
|`+=`|`a += 2`|`a = a + 2`|
|`-=`|`a -= 3`|`a = a - 3`|
|`*=`|`a *= 2`|`a = a * 2`|
|`/=`|`a /= 4`|`a = a / 4`|
|`//=`|`a //= 2`|`a = a // 2`|
|`%=`|`a %= 3`|`a = a % 3`|
|`**=`|`a **= 2`|`a = a ** 2`|

---
## 🧮 Bitwise Operators (Advanced)

- Operate on bits directly.

|Operator|Description|Example|
|---|---|---|
|`&`|AND|`a & b`|
|`|`|OR|
|`^`|XOR|`a ^ b`|
|`~`|NOT|`~a`|
|`<<`|Left shift|`a << 2`|
|`>>`|Right shift|`a >> 2`|

---
## 🧪 Identity Operators

- Compare memory location.

|Operator|Description|Example|
|---|---|---|
|`is`|True if same object|`a is b`|
|`is not`|True if not same object|`a is not b`|

---
## 📦 Membership Operators

- Check if value exists in a container (like list, tuple, string, etc).

|Operator|Description|Example|
|---|---|---|
|`in`|True if present|`"x" in "text"`|
|`not in`|True if not present|`"y" not in "abc"`|
