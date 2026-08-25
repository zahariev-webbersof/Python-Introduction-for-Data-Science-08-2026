# 📝 Data Types, Variables and Simple Operations - TEST

This quiz will test your understanding of **Data Types, Variables, Type Conversion, Input/Output, and Simple Operations** in Python.

Each question includes multiple-choice options. The correct answer is hidden below each question so you can check your knowledge after answering.

---

### 🔢 1. What is the correct way to create a variable in Python?

* A: `age = 25`
* B: `int age = 25`
* C: `var age = 25`
* D: `age := 25`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `age = 25`

In Python, variables are created by assigning a value using the `=` operator. You do not need to explicitly declare the variable's type.

</p>
</details>

---

### 🔍 2. What is the data type of the following variable?

```python
price = 19.99
```

* A: `int`
* B: `float`
* C: `str`
* D: `bool`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `float`

Numbers containing a decimal point are represented using the `float` data type.

</p>
</details>

---

### 📚 3. Which Python data type is used to store text?

* A: `int`
* B: `float`
* C: `str`
* D: `bool`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `str`

The `str` data type is used to store sequences of characters such as names, sentences, and other textual information.

</p>
</details>

---

### 🧠 4. What will the following code output?

```python
x = 10
y = 5
print(x + y)
```

* A: `105`
* B: `15`
* C: `10 + 5`
* D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `15`

Both variables contain integers, so Python performs numerical addition.

</p>
</details>

---

### ➕ 5. What will the following code output?

```python
first_name = "Data"
last_name = "Science"

print(first_name + " " + last_name)
```

* A: `DataScience`
* B: `Data Science`
* C: `Data + Science`
* D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Data Science`

The `+` operator can be used to concatenate strings.

</p>
</details>

---

### 🔄 6. What does the `type()` function do?

* A: Converts a variable to another data type
* B: Returns the data type of an object
* C: Prints a variable
* D: Creates a new variable

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Returns the data type of an object

For example:

```python
age = 25
print(type(age))
```

The result will show that `age` is an integer.

</p>
</details>

---

### 🧮 7. What will the following code output?

```python
x = 10
y = 3

print(x // y)
```

* A: `3.333`
* B: `3`
* C: `1`
* D: `30`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `3`

The `//` operator performs **floor division** and returns the whole-number result of the division.

</p>
</details>

---

### ➗ 8. What will the following code output?

```python
x = 10
y = 4

print(x / y)
```

* A: `2`
* B: `2.0`
* C: `2.5`
* D: `3`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `2.5`

The `/` operator performs standard division and returns a floating-point result.

</p>
</details>

---

### 🧩 9. What does the `%` operator return?

* A: The result of division
* B: The remainder after division
* C: The power of a number
* D: The percentage of a number

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: The remainder after division

For example:

```python
print(10 % 3)
```

The result is:

```text
1
```

because `10 / 3` leaves a remainder of `1`.

</p>
</details>

---

### ⚡ 10. What will the following code output?

```python
print(2 ** 3)
```

* A: `6`
* B: `8`
* C: `9`
* D: `5`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `8`

The `**` operator is used for exponentiation.

`2 ** 3` means:

```text
2 × 2 × 2 = 8
```

</p>
</details>

---

### 🎯 11. What is the value of `result`?

```python
result = 5 + 2 * 3
```

* A: `21`
* B: `11`
* C: `15`
* D: `9`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `11`

Python follows the standard order of mathematical operations.

Multiplication is performed before addition:

```text
2 * 3 = 6
5 + 6 = 11
```

</p>
</details>

---

### 🧮 12. What will the following code output?

```python
result = (5 + 2) * 3
print(result)
```

* A: `11`
* B: `15`
* C: `21`
* D: `10`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `21`

Parentheses have higher priority, so Python calculates:

```text
5 + 2 = 7
7 * 3 = 21
```

</p>
</details>

---

### ⌨️ 13. What data type does `input()` return by default?

```python
age = input("Enter your age: ")
```

* A: `int`
* B: `float`
* C: `str`
* D: Depends on what the user enters

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `str`

The `input()` function always returns the entered value as a string unless we explicitly convert it to another data type.

</p>
</details>

---

### 🔄 14. How can we correctly read an integer from the console?

* A: `age = input(int)`
* B: `age = int(input())`
* C: `age = input().int()`
* D: `int age = input()`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `age = int(input())`

First, `input()` reads the value as a string. Then `int()` converts it to an integer.

</p>
</details>

---

### 💰 15. How can we correctly read a decimal number from the console?

* A: `price = decimal(input())`
* B: `price = int(input())`
* C: `price = float(input())`
* D: `price = input(float)`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `price = float(input())`

The `float()` function converts the input value to a floating-point number.

</p>
</details>

---

### 🧪 16. What will the following code output?

```python
value = "25"
number = int(value)

print(number + 5)
```

* A: `255`
* B: `30`
* C: `"30"`
* D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `30`

`int(value)` converts the string `"25"` into the integer `25`.

Python then calculates:

```text
25 + 5 = 30
```

</p>
</details>

---

### 🧬 17. Which of the following values has the `bool` data type?

* A: `"True"`
* B: `1`
* C: `True`
* D: `"False"`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `True`

`True` and `False` are Python's Boolean values.

Notice that `"True"` is different because the quotation marks make it a string.

</p>
</details>

---

### 🏷️ 18. Which of the following is a valid Python variable name?

* A: `student-name`
* B: `2students`
* C: `student_name`
* D: `student name`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `student_name`

Python variable names can contain letters, numbers, and underscores, but they cannot start with a number or contain spaces or hyphens.

</p>
</details>

---

### 📊 19. What will the following code output?

```python
students = 20
new_students = 5

students = students + new_students

print(students)
```

* A: `20`
* B: `5`
* C: `25`
* D: `205`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `25`

The current value of `students` is `20`.

After:

```python
students = students + new_students
```

the variable receives the new value:

```text
20 + 5 = 25
```

</p>
</details>

---

### 🔬 20. What will the following code output?

```python
temperature = 23.5

print(type(temperature))
```

* A: `<class 'int'>`
* B: `<class 'str'>`
* C: `<class 'float'>`
* D: `<class 'number'>`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `<class 'float'>`

Because `23.5` contains a decimal point, Python stores it as a `float`.

</p>
</details>

---

## 🌟 BONUS 1: Data Processing

A dataset contains `120` records. Another `35` records are added.

What will the following code output?

```python
records = 120
new_records = 35

total_records = records + new_records

print(total_records)
```

* A: `12035`
* B: `155`
* C: `85`
* D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `155`

Both variables contain integers, so Python performs numerical addition:

```text
120 + 35 = 155
```

This is a simple example of how variables and arithmetic operations can be used when working with data.

</p>
</details>

---

## 🌟 BONUS 2: Average Value

What will the following code output?

```python
value_1 = 10
value_2 = 20
value_3 = 30

average = (value_1 + value_2 + value_3) / 3

print(average)
```

* A: `20`
* B: `20.0`
* C: `60`
* D: `10.0`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `20.0`

First, Python calculates:

```text
10 + 20 + 30 = 60
```

Then:

```text
60 / 3 = 20.0
```

The `/` operator returns a floating-point number.

Calculating averages is one of the simplest examples of numerical data processing.

</p>
</details>

---

## 🌟 BONUS 3: Think Like a Data Scientist

You receive the following value from a dataset:

```python
price = "125.50"
```

You want to increase the price by `10`. Which solution is correct?

* A: `price + 10`
* B: `int(price) + 10`
* C: `float(price) + 10`
* D: `str(price + 10)`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `float(price) + 10`

The value `"125.50"` is initially stored as a string.

Because it contains a decimal value, we can convert it using:

```python
float(price)
```

The calculation becomes:

```text
125.50 + 10 = 135.50
```

Understanding and converting data types correctly is an essential skill when working with real-world datasets.

</p>
</details>

---

# 🎯 Quiz Summary

This test covers the fundamental concepts from **Data Types, Variables and Simple Operations**:

* Variables and assignment
* `int`, `float`, `str`, and `bool`
* The `type()` function
* Basic arithmetic operators
* `/`, `//`, `%`, and `**`
* Operator precedence
* Working with `input()` and `print()`
* Type conversion with `int()` and `float()`
* Valid variable names
* Basic numerical data processing

These concepts provide an important programming foundation for the next topics in the **Python Introduction for Data Science** course.

> **Understand the data → Store it → Transform it → Use it. 🐍📊**
