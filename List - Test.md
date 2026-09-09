# 📋 Python Lists - TEST

This quiz will test your understanding of **Python Lists, Indexing, Slicing, List Methods, Built-in Functions, and List Operations**.

Each question includes multiple-choice options. The correct answer is hidden below each question so you can check your knowledge after answering.

---

### 📦 1. What is a list in Python?

* A: A collection that can store multiple values
* B: A loop that repeats code
* C: A function for reading input
* D: A special type of integer

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: A collection that can store multiple values

A list allows us to store multiple elements inside a single variable.

```python
cars = ["BMW", "Audi", "Toyota"]
```

A list can contain many values and we can access them using their indexes.

</p>
</details>

---

### 🔢 2. What is the index of the first element in a Python list?

* A: `-1`
* B: `0`
* C: `1`
* D: It depends on the list

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `0`

Python uses **zero-based indexing**.

```python
numbers = [10, 20, 30]
```

The indexes are:

```text
Value:    10    20    30
Index:     0     1     2
```

Therefore:

```python
print(numbers[0])
```

outputs:

```text
10
```

</p>
</details>

---

### 🎯 3. What will the following code output?

```python
cars = ["BMW", "Audi", "Toyota"]

print(cars[1])
```

* A: `BMW`
* B: `Audi`
* C: `Toyota`
* D: `1`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Audi`

The indexes are:

```text
BMW     Audi     Toyota
 0       1         2
```

Index `1` contains `"Audi"`.

</p>
</details>

---

### ⏪ 4. What does index `-1` represent?

```python
numbers = [10, 20, 30, 40]
```

* A: The first element
* B: The second element
* C: The last element
* D: An invalid index

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: The last element

Negative indexes allow us to count from the end of the list.

```python
print(numbers[-1])
```

Output:

```text
40
```

We can also use:

```python
numbers[-2]
```

to access the second-to-last element.

</p>
</details>

---

### ✏️ 5. What will the following code output?

```python
cars = ["BMW", "Audi", "Toyota"]

cars[1] = "Mercedes"

print(cars)
```

* A: `['BMW', 'Audi', 'Toyota']`
* B: `['BMW', 'Mercedes', 'Toyota']`
* C: `['Mercedes', 'Audi', 'Toyota']`
* D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `['BMW', 'Mercedes', 'Toyota']`

Lists are **mutable**, which means their elements can be changed.

```python
cars[1] = "Mercedes"
```

replaces the element at index `1`.

</p>
</details>

---

### ➕ 6. What does `append()` do?

* A: Adds an element at the beginning
* B: Adds an element at the end
* C: Removes the last element
* D: Sorts the list

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Adds an element at the end

Example:

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

`append()` is one of the most commonly used list methods.

</p>
</details>

---

### 📍 7. What will the following code output?

```python
cars = ["BMW", "Toyota"]

cars.insert(1, "Audi")

print(cars)
```

* A: `['Audi', 'BMW', 'Toyota']`
* B: `['BMW', 'Toyota', 'Audi']`
* C: `['BMW', 'Audi', 'Toyota']`
* D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `['BMW', 'Audi', 'Toyota']`

The syntax is:

```python
list.insert(index, value)
```

Therefore:

```python
cars.insert(1, "Audi")
```

inserts `"Audi"` at index `1`.

</p>
</details>

---

### 🗑️ 8. What does `remove()` use to remove an element?

* A: The element's value
* B: The element's index
* C: The length of the list
* D: The last element only

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: The element's value

Example:

```python
cars = ["BMW", "Audi", "Toyota"]

cars.remove("Audi")

print(cars)
```

Output:

```text
['BMW', 'Toyota']
```

`remove()` searches for a **value**, not an index.

</p>
</details>

---

### 🧹 9. What will the following code output?

```python
numbers = [10, 20, 30, 40]

numbers.pop()

print(numbers)
```

* A: `[10, 20, 30]`
* B: `[20, 30, 40]`
* C: `[10, 20, 30, 40]`
* D: `[]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `[10, 20, 30]`

When `pop()` is called without an index, it removes the **last element**.

The value `40` is removed.

</p>
</details>

---

### 🔍 10. What will the following code output?

```python
numbers = [10, 20, 30, 40]

removed_number = numbers.pop(1)

print(removed_number)
```

* A: `10`
* B: `20`
* C: `30`
* D: `40`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `20`

`pop(1)` removes the element at index `1`.

It also **returns the removed value**, so we can save it inside a variable.

</p>
</details>

---

### 🧽 11. What does `clear()` do?

* A: Removes the first element
* B: Removes duplicate elements
* C: Removes all elements
* D: Deletes the variable itself

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: Removes all elements

Example:

```python
numbers = [1, 2, 3]

numbers.clear()

print(numbers)
```

Output:

```text
[]
```

The list still exists, but it is now empty.

</p>
</details>

---

### 🔎 12. What will the following code output?

```python
cars = ["BMW", "Audi", "Toyota", "Mercedes"]

print(cars.index("Toyota"))
```

* A: `1`
* B: `2`
* C: `3`
* D: `Toyota`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `2`

`index()` returns the index of the first matching element.

```text
BMW      Audi      Toyota      Mercedes
 0        1          2            3
```

</p>
</details>

---

### 🔢 13. What will the following code output?

```python
numbers = [5, 2, 5, 8, 5, 10]

print(numbers.count(5))
```

* A: `1`
* B: `2`
* C: `3`
* D: `5`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `3`

`count()` returns how many times a value appears inside the list.

The number `5` appears three times.

</p>
</details>

---

### 📏 14. What will the following code output?

```python
numbers = [10, 20, 30, 40, 50]

print(len(numbers))
```

* A: `4`
* B: `5`
* C: `50`
* D: `150`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `5`

`len()` returns the number of elements inside the list.

</p>
</details>

---

### 🧮 15. What will the following code output?

```python
numbers = [10, 20, 30, 40]

print(sum(numbers))
```

* A: `40`
* B: `70`
* C: `100`
* D: `4`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `100`

`sum()` calculates the sum of all numeric elements.

```text
10 + 20 + 30 + 40 = 100
```

</p>
</details>

---

### 📊 16. What will the following code output?

```python
numbers = [17, 4, 25, 8, 11]

print(min(numbers))
print(max(numbers))
```

* A: `4` and `25`
* B: `17` and `11`
* C: `25` and `4`
* D: `5` and `65`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `4` and `25`

`min()` returns the smallest element.

`max()` returns the largest element.

</p>
</details>

---

### 🔃 17. What will the following code output?

```python
numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)
```

* A: `[5, 2, 8, 1, 3]`
* B: `[8, 5, 3, 2, 1]`
* C: `[1, 2, 3, 5, 8]`
* D: `[1, 3, 8, 2, 5]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `[1, 2, 3, 5, 8]`

`sort()` sorts the list in ascending order by default.

</p>
</details>

---

### ⬇️ 18. How can we sort a list in descending order?

* A: `numbers.sort(down=True)`
* B: `numbers.sort(reverse=True)`
* C: `numbers.reverse(sort=True)`
* D: `numbers.sort(False)`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `numbers.sort(reverse=True)`

Example:

```python
numbers = [3, 1, 5, 2]

numbers.sort(reverse=True)

print(numbers)
```

Output:

```text
[5, 3, 2, 1]
```

</p>
</details>

---

### 🔄 19. What does `reverse()` do?

* A: Sorts the list from largest to smallest
* B: Reverses the current order of the elements
* C: Removes elements in reverse order
* D: Creates an empty list

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Reverses the current order of the elements

For example:

```python
numbers = [5, 1, 10, 2]

numbers.reverse()

print(numbers)
```

Output:

```text
[2, 10, 1, 5]
```

Important:

`reverse()` does **not** sort the list.

It simply reverses its current order.

</p>
</details>

---

### 🔗 20. What will the following code output?

```python
first = [1, 2]
second = [3, 4]

first.extend(second)

print(first)
```

* A: `[1, 2, [3, 4]]`
* B: `[1, 2, 3, 4]`
* C: `[3, 4, 1, 2]`
* D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `[1, 2, 3, 4]`

`extend()` adds the individual elements from another iterable to the list.

</p>
</details>

---

### ⚖️ 21. What is the difference between `append()` and `extend()`?

Consider:

```python
numbers = [1, 2, 3]
```

* A: There is no difference
* B: `append()` adds one object, while `extend()` adds the individual elements
* C: `append()` removes elements
* D: `extend()` can only work with strings

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B

Using `append()`:

```python
numbers = [1, 2, 3]

numbers.append([4, 5])

print(numbers)
```

Output:

```text
[1, 2, 3, [4, 5]]
```

Using `extend()`:

```python
numbers = [1, 2, 3]

numbers.extend([4, 5])

print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

</p>
</details>

---

### ✂️ 22. What will the following slicing operation return?

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

* A: `[10, 20, 30, 40]`
* B: `[20, 30, 40]`
* C: `[20, 30, 40, 50]`
* D: `[10, 20, 30]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `[20, 30, 40]`

Slicing follows:

```python
list[start:stop]
```

The `start` index is included.

The `stop` index is excluded.

Therefore:

```python
numbers[1:4]
```

takes indexes:

```text
1, 2, 3
```

</p>
</details>

---

### ✂️ 23. What will the following code output?

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
```

* A: `[10, 20, 30]`
* B: `[20, 30, 40]`
* C: `[10, 20, 30, 40]`
* D: `[30, 40, 50]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `[10, 20, 30]`

When the starting index is omitted, slicing starts from the beginning of the list.

```python
numbers[:3]
```

means:

```text
Start → index 3
```

Index `3` itself is not included.

</p>
</details>

---

### ✂️ 24. What will the following code output?

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[2:])
```

* A: `[10, 20]`
* B: `[20, 30]`
* C: `[30, 40, 50]`
* D: `[20, 30, 40]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `[30, 40, 50]`

When the stop index is omitted, slicing continues until the end of the list.

</p>
</details>

---

### 🔍 25. What will the following code output?

```python
cars = ["BMW", "Audi", "Toyota"]

if "Audi" in cars:
    print("Found")
else:
    print("Missing")
```

* A: `Audi`
* B: `Found`
* C: `Missing`
* D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `Found`

The `in` operator checks whether a value exists inside a collection.

Because `"Audi"` exists in the list, the condition is `True`.

</p>
</details>

---

## 🌟 BONUS 1: Reverse a List

What will the following program output?

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[::-1])
```

* A: `[1, 2, 3, 4, 5]`
* B: `[5, 4, 3, 2, 1]`
* C: `[2, 3, 4, 5]`
* D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `[5, 4, 3, 2, 1]`

Slicing can contain a third value:

```python
list[start:stop:step]
```

A step of `-1` moves backwards through the list.

Therefore:

```python
numbers[::-1]
```

is a common Python technique for reversing a list.

</p>
</details>

---

## 🌟 BONUS 2: Every Second Element

What will the following program output?

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(numbers[::2])
```

* A: `[1, 2, 3, 4]`
* B: `[2, 4, 6, 8]`
* C: `[1, 3, 5, 7]`
* D: `[1, 4, 7]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `[1, 3, 5, 7]`

The third slicing value represents the step.

```python
numbers[::2]
```

means:

```text
Start from the beginning
↓
Take an element
↓
Move 2 positions
↓
Take another element
```

</p>
</details>

---

## 🌟 BONUS 3: Create Multiple Zeros

What will the following program output?

```python
results = [0] * 5

print(results)
```

* A: `[0]`
* B: `[5]`
* C: `[0, 0, 0, 0, 0]`
* D: `0`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `[0, 0, 0, 0, 0]`

Python allows us to repeat the elements of a list using `*`.

This technique is useful when creating counters or initial result lists.

For example:

```python
beggars_count = 3

beggars = [0] * beggars_count
```

creates:

```text
[0, 0, 0]
```

</p>
</details>

---

## 🌟 BONUS 4: Swap Elements

What will the following program output?

```python
numbers = [10, 20, 30]

numbers[0], numbers[2] = numbers[2], numbers[0]

print(numbers)
```

* A: `[10, 20, 30]`
* B: `[30, 20, 10]`
* C: `[20, 10, 30]`
* D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `[30, 20, 10]`

Python allows two values to be swapped without creating a temporary variable.

Instead of:

```python
temp = numbers[0]
numbers[0] = numbers[2]
numbers[2] = temp
```

we can write:

```python
numbers[0], numbers[2] = numbers[2], numbers[0]
```

</p>
</details>

---

## 🌟 BONUS 5: Think Like a Data Scientist

You have the following dataset:

```python
temperatures = [18, 22, -5, 25, -10, 30]

valid_temperatures = []

for temperature in temperatures:
    if temperature >= 0:
        valid_temperatures.append(temperature)

print(valid_temperatures)
```

What will the program output?

* A: `[-5, -10]`
* B: `[18, 22, 25, 30]`
* C: `[18, 22, -5, 25, -10, 30]`
* D: `[]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `[18, 22, 25, 30]`

The loop checks every temperature.

Only values greater than or equal to `0` are added to the new list:

```python
valid_temperatures.append(temperature)
```

This demonstrates a common data-processing pattern:

```text
Read data
    ↓
Check condition
    ↓
Select valid data
    ↓
Append to a new list
```

</p>
</details>

---

# 🎯 Quiz Summary

This test covers the fundamental concepts of **Python Lists**:

* Creating lists
* Zero-based indexing
* Positive indexes
* Negative indexes
* Accessing elements
* Changing elements
* `append()`
* `insert()`
* `remove()`
* `pop()`
* `clear()`
* `index()`
* `count()`
* `sort()`
* `reverse()`
* `extend()`
* Difference between `append()` and `extend()`
* `len()`
* `sum()`
* `min()`
* `max()`
* The `in` operator
* List slicing
* `list[start:stop]`
* `list[start:stop:step]`
* Reversing with `[::-1]`
* Taking every second element with `[::2]`
* Creating repeated values with `[0] * n`
* Swapping list elements
* Iterating through lists
* Basic list filtering

Lists are one of the most important data structures in Python because they allow us to **store, modify, organize, and process collections of data efficiently**.

> **Store → Access → Modify → Process. 🐍📋📊**
