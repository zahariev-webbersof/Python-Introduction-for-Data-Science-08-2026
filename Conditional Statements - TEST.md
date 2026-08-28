# 📝 Conditional Statements - TEST

This quiz will test your understanding of **Comparison Operators, Control-Flow Logic, and Logical Operators (`and`, `or`, `not`)** in Python.

Each question includes multiple-choice options. The correct answer is hidden below each question so you can check your knowledge after answering.

---

### 🔍 1. Which operator checks if two values are equal?

* A: `=`
* B: `==`
* C: `!=`
* D: `>=`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `==`

The `==` operator compares two values and returns `True` if they are equal.

</p>
</details>

---

### ⚖️ 2. What will the following code output?

```python
age = 20

print(age >= 18)
```

* A: `True`
* B: `False`
* C: `20`
* D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `True`

`20` is greater than or equal to `18`, so the comparison returns `True`.

</p>
</details>

---

### 🔍 3. Which operator means "not equal to" in Python?

* A: `<>`
* B: `=!`
* C: `!=`
* D: `not=`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `!=`

The `!=` operator checks whether two values are different.

</p>
</details>

---

### 🧠 4. What will the following code output?

```python
temperature = 25

if temperature > 20:
    print("Warm")
```

* A: `Cold`
* B: `Warm`
* C: `True`
* D: Nothing

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Warm`

The condition `temperature > 20` is `True`, so the code inside the `if` block is executed.

</p>
</details>

---

### 🚦 5. What is the purpose of an `if` statement?

* A: To repeat code
* B: To store data
* C: To execute code when a condition is true
* D: To create a variable

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: To execute code when a condition is true

An `if` statement allows a program to make decisions based on conditions.

</p>
</details>

---

### 🎯 6. What will the following code output?

```python
score = 45

if score >= 50:
    print("Passed")
else:
    print("Failed")
```

* A: `Passed`
* B: `Failed`
* C: `True`
* D: Nothing

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Failed`

`45 >= 50` is `False`, so the `else` block is executed.

</p>
</details>

---

### 🔀 7. When is `elif` used?

* A: To stop the program
* B: To check another condition
* C: To repeat an `if` statement
* D: To create a Boolean variable

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: To check another condition

`elif` allows us to check additional conditions when previous conditions are `False`.

</p>
</details>

---

### 📊 8. What will the following code output?

```python
score = 75

if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Passed")
else:
    print("Failed")
```

* A: `Excellent`
* B: `Passed`
* C: `Failed`
* D: `75`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Passed`

The first condition is `False`, but `75 >= 60` is `True`.

</p>
</details>

---

### 🔗 9. When does the `and` operator return `True`?

* A: When at least one condition is true
* B: When both conditions are true
* C: When both conditions are false
* D: Always

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: When both conditions are true

The `and` operator requires all connected conditions to be `True`.

</p>
</details>

---

### 👤 10. What will the following code output?

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Access granted")
else:
    print("Access denied")
```

* A: `Access granted`
* B: `Access denied`
* C: `True`
* D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `Access granted`

Both conditions are `True`, so access is granted.

</p>
</details>

---

### 🔗 11. When does the `or` operator return `True`?

* A: Only when both conditions are true
* B: When at least one condition is true
* C: Only when both conditions are false
* D: Never

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: When at least one condition is true

With `or`, only one of the conditions needs to be `True`.

</p>
</details>

---

### 🌤️ 12. What will the following code output?

```python
temperature = 5
is_snowing = True

if temperature < 0 or is_snowing:
    print("Winter conditions")
else:
    print("Normal conditions")
```

* A: `Winter conditions`
* B: `Normal conditions`
* C: `False`
* D: Nothing

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `Winter conditions`

Although `temperature < 0` is `False`, `is_snowing` is `True`.

With `or`, one true condition is enough.

</p>
</details>

---

### 🚫 13. What does the `not` operator do?

* A: Compares two numbers
* B: Reverses a Boolean value
* C: Checks if two values are equal
* D: Stops an `if` statement

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Reverses a Boolean value

`not True` becomes `False`, while `not False` becomes `True`.

</p>
</details>

---

### 🔐 14. What will the following code output?

```python
is_blocked = False

if not is_blocked:
    print("Login allowed")
else:
    print("Login blocked")
```

* A: `Login allowed`
* B: `Login blocked`
* C: `False`
* D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `Login allowed`

`is_blocked` is `False`.

The expression `not is_blocked` therefore becomes `True`.

</p>
</details>

---

### 📏 15. Which condition checks whether `x` is between 10 and 20?

* A: `x > 10 or x < 20`
* B: `x >= 10 and x <= 20`
* C: `x >= 10 or x <= 20`
* D: `x == 10 and x == 20`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `x >= 10 and x <= 20`

Both conditions must be satisfied for the value to be inside the interval.

</p>
</details>

---

### 🧪 16. What will the following code output?

```python
x = 10
y = 20

print(x < y and y < 30)
```

* A: `True`
* B: `False`
* C: `30`
* D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `True`

Both comparisons are true:

`10 < 20` → `True`

`20 < 30` → `True`

Therefore:

`True and True` → `True`

</p>
</details>

---

### 💰 17. What will the following code output?

```python
balance = 1000
withdraw = 1200

if withdraw > balance:
    print("Insufficient funds")
else:
    print("Transaction approved")
```

* A: `Transaction approved`
* B: `Insufficient funds`
* C: `1200`
* D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Insufficient funds`

The requested amount is greater than the available balance.

</p>
</details>

---

### 🎓 18. What will the following code output?

```python
score = 85
attendance = 90

if score >= 80 and attendance >= 80:
    print("Certificate")
else:
    print("No certificate")
```

* A: `Certificate`
* B: `No certificate`
* C: `True`
* D: `85`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `Certificate`

Both requirements are satisfied:

`85 >= 80` → `True`

`90 >= 80` → `True`

</p>
</details>

---

### 🧩 19. What will the following code output?

```python
value = 15

if value > 10:
    if value < 20:
        print("Valid")
```

* A: `Invalid`
* B: `Valid`
* C: `True`
* D: Nothing

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Valid`

Both the outer and inner conditions are `True`.

This is an example of a nested conditional statement.

</p>
</details>

---

### ⚡ 20. What will the following code output?

```python
age = 16
has_permission = True

if age >= 18 or has_permission:
    print("Allowed")
else:
    print("Not allowed")
```

* A: `Allowed`
* B: `Not allowed`
* C: `False`
* D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `Allowed`

`age >= 18` is `False`, but `has_permission` is `True`.

Because the conditions use `or`, one `True` value is enough.

</p>
</details>

---

## 🌟 BONUS 1: Data Filtering

A dataset contains information about customers.

```python
age = 32
country = "Germany"

if age >= 18 and country == "Germany":
    print("Selected")
else:
    print("Not selected")
```

What will the program output?

* A: `Selected`
* B: `Not selected`
* C: `True`
* D: `Germany`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `Selected`

Both filtering conditions are satisfied.

This is a simple example of using conditional logic to filter data.

</p>
</details>

---

## 🌟 BONUS 2: Transaction Analysis

Consider the following transaction data:

```python
amount = 2500
country = "Unknown"

if amount > 2000 or country == "Unknown":
    print("Review transaction")
else:
    print("Approved")
```

What will the program output?

* A: `Approved`
* B: `Review transaction`
* C: `2500`
* D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Review transaction`

The amount is greater than `2000`, and the country is also marked as `"Unknown"`.

Because the conditions use `or`, even one matching condition would be enough.

</p>
</details>

---

## 🌟 BONUS 3: Think Like a Data Scientist

You receive the following customer record:

```python
age = 29
income = 4500
active_customer = True
```

You want to select customers who:

- are at least 25 years old
- have an income greater than 3000
- are active customers

Which condition is correct?

* A: `age >= 25 or income > 3000 or active_customer`
* B: `age >= 25 and income > 3000 and active_customer`
* C: `age == 25 and income == 3000`
* D: `not active_customer`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `age >= 25 and income > 3000 and active_customer`

All three requirements must be satisfied, so the conditions should be connected using `and`.

This type of Boolean filtering is fundamental when working with datasets.

</p>
</details>

---

# 🎯 Quiz Summary

This test covers the fundamental concepts from **Conditional Statements**:

* Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
* Boolean values: `True` and `False`
* `if` statements
* `if-else` statements
* `if-elif-else` statements
* Nested conditional statements
* Logical operator `and`
* Logical operator `or`
* Logical operator `not`
* Combining multiple conditions
* Basic data filtering and decision-making

These concepts are essential for working with data because they allow us to **filter, classify, validate, and make decisions based on values in a dataset**.

> **Compare the data → Apply conditions → Make decisions. 🐍📊**
