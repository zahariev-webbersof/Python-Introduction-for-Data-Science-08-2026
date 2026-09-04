# 🧩 Python Functions - TEST

This quiz will test your understanding of **Python Functions, def, Parameters, Arguments, return, Scope, Default Parameters, and Function Calls**.

Each question includes multiple-choice options. The correct answer is hidden below each question so you can check your knowledge after answering.

---

### 🧠 1. What is a function in Python?

* A: A variable that stores multiple values
* B: A reusable block of code that performs a specific task
* C: A loop that executes forever
* D: A special type of string

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: A reusable block of code that performs a specific task

A function is a block of code designed to perform a particular task.

Functions allow us to organize our programs and reuse code instead of writing the same logic multiple times.

Example:

```python
def greet():
    print("Hello!")
```

</p>
</details>

---

### 🔨 2. Which keyword is used to define a function in Python?

* A: `function`
* B: `func`
* C: `def`
* D: `define`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `def`

Python uses the `def` keyword to define a function.

Example:

```python
def greet():
    print("Hello!")
```

The general syntax is:

```python
def function_name():
    # function body
```

</p>
</details>

---

### 📞 3. How do we call the following function?

```python
def greet():
    print("Hello!")
```

* A: `greet`
* B: `greet()`
* C: `call greet`
* D: `def greet()`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `greet()`

Writing:

```python
greet()
```

calls the function and executes the code inside it.

Defining a function does not automatically execute it.

We first define:

```python
def greet():
    print("Hello!")
```

and then call:

```python
greet()
```

</p>
</details>

---

### 🖥️ 4. What will the following code output?

```python
def greet():
    print("Hello!")

greet()
```

* A: `greet`
* B: `Hello!`
* C: Nothing
* D: An error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Hello!`

The function is first defined:

```python
def greet():
    print("Hello!")
```

Then it is called:

```python
greet()
```

Therefore, the statement inside the function is executed:

```text
Hello!
```

</p>
</details>

---

### ⚠️ 5. What will the following code output?

```python
def greet():
    print("Hello!")
```

* A: `Hello!`
* B: `greet`
* C: Nothing
* D: SyntaxError

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: Nothing

The function has only been **defined**.

It has not been called.

Python remembers the function, but the code inside it will not execute until we write:

```python
greet()
```

This is an important distinction:

```text
Define a function → Create it

Call a function → Execute it
```

</p>
</details>

---

### 📦 6. What is a parameter?

Consider:

```python
def greet(name):
    print(f"Hello, {name}!")
```

What is `name`?

* A: An argument
* B: A parameter
* C: A return value
* D: A function call

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: A parameter

A **parameter** is a variable written in the function definition.

Here:

```python
def greet(name):
```

`name` is the parameter.

It receives a value when the function is called.

</p>
</details>

---

### 🎁 7. What is an argument?

Consider:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Peter")
```

What is `"Peter"`?

* A: A parameter
* B: An argument
* C: A function name
* D: A variable declaration

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: An argument

An **argument** is the actual value passed to a function when the function is called.

Here:

```python
greet("Peter")
```

`"Peter"` is the argument.

Inside the function, the parameter:

```python
name
```

receives the value:

```text
Peter
```

</p>
</details>

---

### 🔄 8. What will the following code output?

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Maria")
```

* A: `Hello`
* B: `Maria`
* C: `Hello, Maria!`
* D: `Hello, name!`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `Hello, Maria!`

The argument:

```python
"Maria"
```

is passed to the parameter:

```python
name
```

Therefore:

```python
print(f"Hello, {name}!")
```

produces:

```text
Hello, Maria!
```

</p>
</details>

---

### ➕ 9. What will the following code output?

```python
def add_numbers(a, b):
    print(a + b)

add_numbers(5, 3)
```

* A: `5`
* B: `3`
* C: `8`
* D: `53`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `8`

The function receives:

```text
a = 5
b = 3
```

Then Python calculates:

```text
5 + 3 = 8
```

Therefore:

```python
print(a + b)
```

prints:

```text
8
```

</p>
</details>

---

### 🔢 10. How many parameters does this function have?

```python
def calculate_price(price, quantity, discount):
    pass
```

* A: 1
* B: 2
* C: 3
* D: 4

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: 3

The parameters are:

```text
price
quantity
discount
```

Therefore, the function has three parameters.

Parameters are separated by commas inside the parentheses.

</p>
</details>

---

### 📤 11. What is the purpose of `return`?

* A: To repeat the function
* B: To stop the entire Python program
* C: To send a value back from a function
* D: To print a value on the screen

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: To send a value back from a function

The `return` statement sends a result back to the place where the function was called.

Example:

```python
def add(a, b):
    return a + b
```

Now we can store the result:

```python
result = add(5, 3)
```

The value of `result` becomes:

```text
8
```

</p>
</details>

---

### 🧮 12. What will the following code output?

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)

print(result)
```

* A: `4`
* B: `5`
* C: `9`
* D: `20`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: `20`

The function calculates:

```text
4 * 5 = 20
```

Then:

```python
return a * b
```

returns the value `20`.

The returned value is stored in:

```python
result
```

and then printed.

</p>
</details>

---

### 🖨️ 13. What is the main difference between `print()` and `return` inside a function?

* A: There is no difference
* B: `print()` displays a value, while `return` sends a value back
* C: `return` always prints a value
* D: `print()` can only be used outside functions

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `print()` displays a value, while `return` sends a value back

`print()` displays information on the screen:

```python
def add(a, b):
    print(a + b)
```

`return` sends the result back:

```python
def add(a, b):
    return a + b
```

This means a returned value can be stored:

```python
result = add(5, 3)
```

and reused later.

</p>
</details>

---

### 🔍 14. What will be stored in `result`?

```python
def subtract(a, b):
    return a - b

result = subtract(10, 4)
```

* A: `4`
* B: `6`
* C: `10`
* D: Nothing

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `6`

The function calculates:

```text
10 - 4 = 6
```

The value `6` is returned:

```python
return a - b
```

and stored inside:

```python
result
```

Therefore:

```text
result = 6
```

</p>
</details>

---

### 🛑 15. What happens when Python executes `return`?

```python
def example():
    print("A")
    return
    print("B")

example()
```

* A: It prints `A` and `B`
* B: It prints only `A`
* C: It prints only `B`
* D: It produces an error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: It prints only `A`

Python first executes:

```python
print("A")
```

Then it reaches:

```python
return
```

`return` immediately ends the execution of the function.

Therefore:

```python
print("B")
```

is never reached.

The output is:

```text
A
```

</p>
</details>

---

### 🚦 16. What will the following function return?

```python
def check_number(number):
    if number > 0:
        return "Positive"

    return "Not positive"


result = check_number(5)

print(result)
```

* A: `Positive`
* B: `Not positive`
* C: `5`
* D: `True`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `Positive`

The function receives:

```text
number = 5
```

The condition:

```python
number > 0
```

is `True`.

Therefore:

```python
return "Positive"
```

is executed.

The function ends immediately after this `return`.

</p>
</details>

---

### 🎯 17. What will the following code output?

```python
def is_even(number):
    return number % 2 == 0

print(is_even(8))
```

* A: `8`
* B: `0`
* C: `True`
* D: `False`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `True`

The expression:

```python
number % 2 == 0
```

checks whether the number is divisible by `2`.

For:

```text
8 % 2 = 0
```

Therefore:

```python
8 % 2 == 0
```

evaluates to:

```text
True
```

The function returns that Boolean value.

</p>
</details>

---

### 🧩 18. What will the following code output?

```python
def square(number):
    return number ** 2

print(square(6))
```

* A: `12`
* B: `36`
* C: `6`
* D: `216`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `36`

The exponent operator:

```python
**
```

raises a number to a power.

Therefore:

```text
6 ** 2 = 36
```

The function returns `36`.

</p>
</details>

---

### 🏷️ 19. What is a default parameter?

Consider:

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")
```

What does `"Guest"` represent?

* A: A required argument
* B: A default value for the parameter
* C: The function name
* D: A return value

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: A default value for the parameter

The parameter:

```python
name
```

has a default value:

```python
"Guest"
```

If no argument is passed:

```python
greet()
```

Python uses the default value.

Therefore, the output will be:

```text
Hello, Guest!
```

</p>
</details>

---

### 👤 20. What will the following code output?

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
```

* A: `Hello, name!`
* B: `Hello, Guest!`
* C: Nothing
* D: An error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Hello, Guest!`

No argument is provided when the function is called:

```python
greet()
```

Therefore, Python uses the default value:

```python
name = "Guest"
```

The output is:

```text
Hello, Guest!
```

</p>
</details>

---

### 🔄 21. What will the following code output?

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("John")
```

* A: `Hello, Guest!`
* B: `Hello, John!`
* C: `Guest John`
* D: An error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Hello, John!`

The default value is used only when no argument is provided.

Here:

```python
greet("John")
```

passes `"John"` as the argument.

Therefore:

```text
name = "John"
```

and the output is:

```text
Hello, John!
```

</p>
</details>

---

### 🔐 22. What is a local variable?

Consider:

```python
def calculate():
    result = 10 + 5
    return result
```

What is `result`?

* A: A local variable
* B: A global variable
* C: A function parameter
* D: A built-in function

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: A local variable

The variable:

```python
result
```

is created inside the function.

Therefore, it is a **local variable**.

Local variables normally exist only inside the function where they are created.

</p>
</details>

---

### ⚠️ 23. What happens in the following code?

```python
def calculate():
    result = 10
    print(result)

calculate()

print(result)
```

* A: It prints `10` twice
* B: It prints `10`, then produces a `NameError`
* C: It prints nothing
* D: It produces a `SyntaxError`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: It prints `10`, then produces a `NameError`

Inside the function:

```python
result = 10
```

creates a local variable.

Therefore:

```python
print(result)
```

inside the function works.

But after the function finishes, this statement:

```python
print(result)
```

tries to access the local variable outside its scope.

Python cannot find it there and raises:

```text
NameError
```

</p>
</details>

---

### 🌍 24. What will the following code output?

```python
message = "Hello"

def show_message():
    print(message)

show_message()
```

* A: `message`
* B: `Hello`
* C: Nothing
* D: `NameError`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Hello`

The variable:

```python
message
```

is created outside the function.

It is therefore available in the global scope.

The function can read its value:

```python
print(message)
```

and outputs:

```text
Hello
```

</p>
</details>

---

### 🔗 25. What will the following code output?

```python
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


result = multiply(add(2, 3), 4)

print(result)
```

* A: `9`
* B: `10`
* C: `20`
* D: `24`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `20`

Python first evaluates the inner function:

```python
add(2, 3)
```

which returns:

```text
5
```

The expression then becomes:

```python
multiply(5, 4)
```

which returns:

```text
20
```

This demonstrates that the result of one function can be passed to another function.

</p>
</details>

---

# 🌟 BONUS QUESTIONS

---

## 🌟 BONUS 1: Function With User Input

What will happen if the user enters:

```text
5
```

into the following program?

```python
def square(number):
    return number ** 2


number = int(input())

result = square(number)

print(result)
```

* A: `5`
* B: `10`
* C: `25`
* D: `52`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `25`

The user enters:

```text
5
```

After conversion:

```python
number = 5
```

The function call:

```python
square(5)
```

calculates:

```text
5 ** 2 = 25
```

Therefore, the program prints:

```text
25
```

</p>
</details>

---

## 🌟 BONUS 2: Function and Conditional Statement

What will the following code output?

```python
def get_grade(score):
    if score >= 90:
        return "Excellent"

    if score >= 60:
        return "Passed"

    return "Failed"


print(get_grade(75))
```

* A: `Excellent`
* B: `Passed`
* C: `Failed`
* D: `75`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Passed`

First:

```python
75 >= 90
```

is `False`.

Then:

```python
75 >= 60
```

is `True`.

Therefore:

```python
return "Passed"
```

is executed.

The output is:

```text
Passed
```

</p>
</details>

---

## 🌟 BONUS 3: Function and Loop

What will the following program output?

```python
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


values = [10, 20, 30, 40]

print(calculate_sum(values))
```

* A: `40`
* B: `60`
* C: `100`
* D: `120`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `100`

The function receives:

```python
[10, 20, 30, 40]
```

The loop calculates:

```text
0 + 10 = 10
10 + 20 = 30
30 + 30 = 60
60 + 40 = 100
```

Then:

```python
return total
```

returns:

```text
100
```

</p>
</details>

---

## 🌟 BONUS 4: Find the Maximum Value

What will the following program output?

```python
def find_biggest(numbers):
    biggest = float("-inf")

    for number in numbers:
        if number > biggest:
            biggest = number

    return biggest


values = [-5, 12, 7, 25, 3]

print(find_biggest(values))
```

* A: `-5`
* B: `12`
* C: `25`
* D: `3`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `25`

The function checks every number and remembers the largest value found so far.

The values are:

```text
-5
12
7
25
3
```

The largest value is:

```text
25
```

Therefore, the function returns `25`.

</p>
</details>

---

## 🌟 BONUS 5: Think Like a Data Scientist

You have a dataset containing temperature measurements:

```python
temperatures = [18, 22, 25, 30, 35]
```

What will the following program output?

```python
def calculate_average(values):
    total = 0

    for value in values:
        total += value

    return total / len(values)


temperatures = [18, 22, 25, 30, 35]

average = calculate_average(temperatures)

print(average)
```

* A: `25`
* B: `26`
* C: `30`
* D: `130`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `26`

The function first calculates the total:

```text
18 + 22 + 25 + 30 + 35 = 130
```

There are:

```text
5
```

values in the list.

Therefore:

```text
130 / 5 = 26
```

The function returns:

```text
26.0
```

Python's `/` operator performs floating-point division, so the exact printed result is:

```text
26.0
```

</p>
</details>

---

# 🎯 Quiz Summary

This test covers the fundamental concepts of **Python Functions**:

* What a function is
* Why functions are useful
* The `def` keyword
* Defining functions
* Calling functions
* Function names
* Parameters
* Arguments
* Multiple parameters
* Passing values to functions
* The `return` statement
* Returning values
* Storing returned values
* The difference between `print()` and `return`
* Returning Boolean values
* Using conditional statements inside functions
* Using loops inside functions
* Default parameters
* Passing arguments instead of default values
* Local variables
* Global variables
* Variable scope
* Calling one function from another
* Passing the result of one function to another function
* Processing collections with functions
* Reusing function results

Functions are one of the most important concepts in programming because they allow us to **divide larger problems into smaller reusable pieces of logic**.

Instead of writing the same code again and again, we can define the logic once:

```python
def calculate(a, b):
    return a + b
```

and reuse it whenever we need it:

```python
result_1 = calculate(5, 3)
result_2 = calculate(10, 20)
result_3 = calculate(100, 50)
```

This makes our programs:

* easier to read
* easier to test
* easier to maintain
* easier to reuse
* easier to understand

A good way to think about a function is:

```text
INPUT → FUNCTION → OUTPUT
```

For example:

```text
5, 3 → add() → 8
```

or:

```text
"Peter" → greet() → "Hello, Peter!"
```

> **Define → Call → Process → Return → Reuse. 🐍🧩🚀**
