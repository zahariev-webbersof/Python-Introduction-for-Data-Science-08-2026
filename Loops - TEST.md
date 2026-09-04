# 🔁 For and While Loops - TEST

This quiz will test your understanding of **For Loops, While Loops, range(), break, continue, else, and Loop Control** in Python.

Each question includes multiple-choice options. The correct answer is hidden below each question so you can check your knowledge after answering.

---

### 🔄 1. What is the main purpose of a loop in Python?

* A: To store multiple variables
* B: To repeat a block of code
* C: To create a function
* D: To convert data types

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: To repeat a block of code

Loops allow us to execute the same block of code multiple times.

Python provides two main types of loops:

```python
for
while
```

</p>
</details>

---

### 🔢 2. What will the following code output?

```python
for number in range(5):
    print(number)
```

* A: `1 2 3 4 5`
* B: `0 1 2 3 4`
* C: `0 1 2 3 4 5`
* D: `1 2 3 4`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `0 1 2 3 4`

`range(5)` starts from `0` and stops before `5`.

The generated values are:

```text
0
1
2
3
4
```

</p>
</details>

---

### 🎯 3. What will the following code output?

```python
for number in range(1, 6):
    print(number)
```

* A: `0 1 2 3 4 5`
* B: `1 2 3 4 5`
* C: `1 2 3 4 5 6`
* D: `0 1 2 3 4`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `1 2 3 4 5`

The `range()` function can receive a start and stop value:

```python
range(start, stop)
```

The `start` value is included, but the `stop` value is excluded.

Therefore:

```python
range(1, 6)
```

generates:

```text
1 2 3 4 5
```

</p>
</details>

---

### 👣 4. What will the following code output?

```python
for number in range(0, 10, 2):
    print(number)
```

* A: `0 1 2 3 4 5 6 7 8 9`
* B: `0 2 4 6 8`
* C: `2 4 6 8 10`
* D: `0 2 4 6 8 10`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `0 2 4 6 8`

The third argument of `range()` represents the **step**:

```python
range(start, stop, step)
```

Here the loop starts from `0` and increases the value by `2` on every iteration.

</p>
</details>

---

### ⏪ 5. What will the following code output?

```python
for number in range(5, 0, -1):
    print(number)
```

* A: `1 2 3 4 5`
* B: `5 4 3 2 1 0`
* C: `5 4 3 2 1`
* D: The loop will not execute

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `5 4 3 2 1`

A negative step allows us to iterate backwards.

```python
range(5, 0, -1)
```

starts at `5`, decreases by `1`, and stops before `0`.

</p>
</details>

---

### 🧮 6. How many times will this loop execute?

```python
for number in range(1, 10, 2):
    print(number)
```

* A: 4 times
* B: 5 times
* C: 9 times
* D: 10 times

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: 5 times

The generated values are:

```text
1
3
5
7
9
```

Therefore, the loop executes `5` times.

</p>
</details>

---

### 📦 7. What will the following code output?

```python
total = 0

for number in range(1, 5):
    total += number

print(total)
```

* A: `4`
* B: `5`
* C: `10`
* D: `15`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `10`

The loop calculates:

```text
0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
```

The final value of `total` is `10`.

</p>
</details>

---

### 🔍 8. What does `break` do inside a loop?

* A: Skips the current iteration
* B: Restarts the loop
* C: Immediately terminates the loop
* D: Pauses the loop

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: Immediately terminates the loop

The `break` statement stops the entire loop immediately.

Execution continues with the first statement after the loop.

</p>
</details>

---

### 🛑 9. What will the following code output?

```python
for number in range(1, 6):
    if number == 3:
        break

    print(number)
```

* A: `1 2`
* B: `1 2 3`
* C: `1 2 4 5`
* D: `1 2 3 4 5`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `1 2`

When `number` becomes `3`, Python executes:

```python
break
```

The entire loop terminates before `3` is printed.

</p>
</details>

---

### ⏭️ 10. What does `continue` do inside a loop?

* A: Stops the entire program
* B: Stops the entire loop
* C: Skips the rest of the current iteration
* D: Repeats the current iteration forever

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: Skips the rest of the current iteration

`continue` skips the remaining statements in the current iteration and moves to the next iteration of the loop.

Unlike `break`, it does **not** terminate the entire loop.

</p>
</details>

---

### 🚦 11. What will the following code output?

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

* A: `1 2`
* B: `1 2 3 4 5`
* C: `1 2 4 5`
* D: `3`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `1 2 4 5`

When `number == 3`, `continue` skips:

```python
print(number)
```

The loop then continues with the next value.

</p>
</details>

---

### 🔁 12. When does a `while` loop continue executing?

* A: Until the program ends
* B: While its condition is `True`
* C: While its condition is `False`
* D: Exactly 10 times

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: While its condition is `True`

A `while` loop repeatedly executes its body while its condition evaluates to `True`.

Example:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

</p>
</details>

---

### 🧠 13. What will the following code output?

```python
number = 1

while number <= 3:
    print(number)
    number += 1
```

* A: `0 1 2`
* B: `1 2 3`
* C: `1 2 3 4`
* D: Infinite loop

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `1 2 3`

Initially:

```python
number = 1
```

After every iteration, the value increases by `1`.

When `number` becomes `4`, the condition:

```python
number <= 3
```

becomes `False` and the loop terminates.

</p>
</details>

---

### ⚠️ 14. What is wrong with the following code?

```python
number = 1

while number <= 5:
    print(number)
```

* A: Nothing is wrong
* B: `while` cannot work with numbers
* C: It creates an infinite loop
* D: `print()` cannot be used inside `while`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: It creates an infinite loop

The value of `number` never changes.

Therefore:

```python
number <= 5
```

remains `True` forever.

A possible solution is:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

</p>
</details>

---

### 🔄 15. What will the following code output?

```python
number = 5

while number > 0:
    print(number)
    number -= 1
```

* A: `1 2 3 4 5`
* B: `5 4 3 2 1`
* C: `5 4 3 2 1 0`
* D: Infinite loop

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `5 4 3 2 1`

The value decreases by `1` after every iteration.

When `number` becomes `0`, the condition:

```python
number > 0
```

becomes `False`.

</p>
</details>

---

### 🛑 16. What will the following code output?

```python
number = 1

while number <= 10:
    if number == 4:
        break

    print(number)
    number += 1
```

* A: `1 2 3`
* B: `1 2 3 4`
* C: `1 2 3 5 6 7 8 9 10`
* D: Infinite loop

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `1 2 3`

When `number` reaches `4`, `break` immediately terminates the loop.

Because `break` is executed before `print(number)`, the value `4` is not printed.

</p>
</details>

---

### 🔓 17. What is a common reason to use `while True`?

* A: To create a loop that can be stopped manually with `break`
* B: To execute the loop exactly once
* C: To create a `for` loop
* D: To prevent loops from executing

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: To create a loop that can be stopped manually with `break`

For example:

```python
while True:
    command = input()

    if command == "Stop":
        break

    print(command)
```

The loop can continue indefinitely until a specific condition causes `break` to execute.

</p>
</details>

---

### 🎮 18. What will happen when the user enters `"Stop"`?

```python
while True:
    command = input()

    if command == "Stop":
        break

    print(command)
```

* A: `"Stop"` will be printed
* B: The loop will terminate
* C: The program will produce an error
* D: The loop will restart

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: The loop will terminate

When:

```python
command == "Stop"
```

is `True`, Python executes `break`.

Because `break` appears before `print(command)`, `"Stop"` will not be printed.

</p>
</details>

---

### 🧩 19. What will the following code output?

```python
number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)
```

* A: `1 2 3 4 5`
* B: `1 2`
* C: `1 2 4 5`
* D: Infinite loop

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `1 2 4 5`

When `number` becomes `3`, `continue` skips:

```python
print(number)
```

The loop then continues with the next iteration.

</p>
</details>

---

### ⚠️ 20. What happens in the following code?

```python
number = 1

while number <= 5:
    if number == 3:
        continue

    print(number)
    number += 1
```

* A: It prints `1 2 4 5`
* B: It prints `1 2 3 4 5`
* C: It enters an infinite loop when `number` becomes `3`
* D: It produces a syntax error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: It enters an infinite loop when `number` becomes `3`

When `number` becomes `3`, Python executes:

```python
continue
```

This skips:

```python
number += 1
```

Therefore, `number` remains `3`, and the condition:

```python
number <= 5
```

continues to be `True`.

This is an important potential problem when using `continue` inside a `while` loop.

</p>
</details>

---

### 🧠 21. When is the `else` block of a loop executed?

* A: Only when `break` is executed
* B: When the loop finishes normally without `break`
* C: Before the loop starts
* D: After every iteration

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: When the loop finishes normally without `break`

Python allows both `for` and `while` loops to have an `else` block.

The `else` block executes when the loop completes normally.

If the loop is terminated with `break`, the `else` block is skipped.

</p>
</details>

---

### 🔍 22. What will the following code output?

```python
for number in range(3):
    print(number)
else:
    print("Done")
```

* A: `0 1 2`
* B: `0 1 2 Done`
* C: `1 2 3 Done`
* D: `Done`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `0 1 2 Done`

The `for` loop completes normally without encountering `break`.

Therefore, the `else` block is executed.

</p>
</details>

---

### 🚫 23. What will the following code output?

```python
for number in range(5):
    if number == 2:
        break

    print(number)
else:
    print("Done")
```

* A: `0 1 Done`
* B: `0 1`
* C: `0 1 2`
* D: `0 1 2 Done`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `0 1`

When `number` becomes `2`, `break` terminates the loop.

Because the loop was terminated using `break`, the `else` block is **not** executed.

</p>
</details>

---

### 🔄 24. What will the following code output?

```python
number = 1

while number <= 3:
    print(number)
    number += 1
else:
    print("Finished")
```

* A: `1 2 3`
* B: `1 2 3 Finished`
* C: `1 2 Finished`
* D: Infinite loop

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `1 2 3 Finished`

The `while` condition eventually becomes `False`.

Because the loop finishes normally without `break`, Python executes the `else` block.

</p>
</details>

---

### ⚖️ 25. What is the main difference between `for` and `while` loops?

* A: `for` loops can print values, but `while` loops cannot
* B: `while` loops cannot use `break`
* C: `for` is commonly used for iteration over a sequence or known range, while `while` repeats based on a condition
* D: There is no difference

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C

A `for` loop is commonly used when iterating through a sequence or a known range of values:

```python
for number in range(5):
    print(number)
```

A `while` loop is useful when repetition depends on a condition:

```python
while condition:
    # code
```

</p>
</details>

---

## 🌟 BONUS 1: Data Processing

You have the following dataset:

```python
values = [10, 20, 30, 40, 50]

total = 0

for value in values:
    total += value

print(total)
```

What will the program output?

* A: `50`
* B: `100`
* C: `150`
* D: `200`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `150`

The loop visits every value and adds it to `total`:

```text
10 + 20 + 30 + 40 + 50 = 150
```

Loops are fundamental when processing collections of data.

</p>
</details>

---

## 🌟 BONUS 2: Filtering Data

What will the following program output?

```python
for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number)
```

* A: `2 4 6 8 10`
* B: `1 3 5 7 9`
* C: `1 2 3 4 5 6 7 8 9 10`
* D: `2 3 5 7`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `1 3 5 7 9`

The condition:

```python
number % 2 == 0
```

detects even numbers.

When an even number is found, `continue` skips the `print()` statement.

Therefore, only odd numbers are printed.

This is a simple example of **filtering data using loops and conditions**.

</p>
</details>

---

## 🌟 BONUS 3: Find the Biggest Number

What will the following program output?

```python
numbers = [-10, -3, -25, -2, -15]

biggest_number = float("-inf")

for number in numbers:
    if number > biggest_number:
        biggest_number = number

print(biggest_number)
```

* A: `-25`
* B: `-15`
* C: `-2`
* D: `0`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `-2`

The variable:

```python
biggest_number = float("-inf")
```

starts with negative infinity.

Every normal finite number is greater than negative infinity.

The loop compares each value and keeps the largest value found so far.

The largest number in the dataset is:

```text
-2
```

This pattern is commonly used when searching for minimum or maximum values.

</p>
</details>

---

## 🌟 BONUS 4: User-Controlled Loop

What will happen when the user enters:

```text
5
8
3
0
```

into the following program?

```python
total = 0

while True:
    number = int(input())

    if number == 0:
        break

    total += number

print(total)
```

* A: `8`
* B: `16`
* C: `0`
* D: Infinite loop

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `16`

The program adds:

```text
5 + 8 + 3 = 16
```

When the user enters `0`, the condition:

```python
if number == 0:
    break
```

terminates the loop.

The value `0` is not added to the total.

</p>
</details>

---

## 🌟 BONUS 5: Think Like a Data Scientist

You have a dataset containing temperature measurements:

```python
temperatures = [18, 22, -5, 25, -10, 30]

for temperature in temperatures:
    if temperature < 0:
        continue

    print(temperature)
```

What will the program output?

* A: `-5 -10`
* B: `18 22 25 30`
* C: `18 22 -5 25 -10 30`
* D: Nothing

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `18 22 25 30`

The condition:

```python
temperature < 0
```

detects negative temperatures.

When a negative value is found, `continue` skips the `print()` statement.

As a result, only non-negative values are processed.

This demonstrates a simple data-cleaning pattern:

```text
Read data → Check condition → Skip unwanted values → Process valid values
```

</p>
</details>

---

# 🎯 Quiz Summary

This test covers the fundamental concepts of **For and While Loops**:

* `for` loops
* `while` loops
* The `range()` function
* `range(start, stop, step)`
* Positive and negative steps
* Loop counters
* Accumulating values
* Infinite loops
* `while True`
* The `break` statement
* The `continue` statement
* `else` with `for`
* `else` with `while`
* The difference between `break` and `continue`
* Common `while` loop mistakes
* Iterating through collections
* Basic data filtering
* Finding minimum and maximum values
* Processing user input with loops

Loops are one of the most important programming concepts because they allow us to **automate repetitive operations and process large amounts of data efficiently**.

> **Repeat → Check → Process → Control the flow. 🐍🔁📊**
