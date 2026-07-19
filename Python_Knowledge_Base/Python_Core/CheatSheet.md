# print()

```python
print(*objects, sep=" ", end="\n")
```

---

# input()

```python
name = input("Введите имя: ")
```

---

# Преобразование типов

```python
int()
float()
str()
bool()
```

---

# Escape-последовательности

```text
\n   Новая строка
\t   Табуляция
\\   Символ \
\"   Двойная кавычка
```

[//]: # (=================================================================================)

[//]: # (L   E   S   S   O   N   -   2   V  A  R  I  A  B  L  E  S)  

[//]: # (=================================================================================)


# Lesson 2 Cheat Sheet

## Variables

```python
age = 25
name = "Alex"
price = 19.99
is_admin = True
```

## Input

```python
name = input("Name: ")
```

```python
age = int(input("Age: "))
```

```python
price = float(input("Price: "))
```

## Type

```python
print(type(age))
```

## Conversion

```python
int("10")
float("2.5")
str(100)
```

## Operators

```python
+
-
*
/
//
%
**
```

## Assignment

```python
x += 1
x -= 1
x *= 2
x /= 2
x //= 2
x %= 2
x **= 2
```

## divmod

```python
divmod(17, 5)
```

↓

```python
(3, 2)
```

или

```python
q, r = divmod(17, 5)
```

## Examples

```python
print(10 / 2)
# 5.0
```

```python
print(10 // 3)
# 3
```

```python
print(10 % 3)
# 1
```

```python
print(2 ** 5)
# 32
```

```python
print("10" + "5")
# 105
```

```python
print(int("10") + int("5"))
# 15
```

