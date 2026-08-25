# 📊 Student Data Analyzer

Welcome to the **Student Data Analyzer**! 🧠📈

This practical task is designed to help you practice the fundamental Python concepts covered in:

**Data Types, Variables and Simple Operations**

You will create a small program that collects information about a student, performs several calculations, and displays a simple summary of the data.

---

## 📝 Project Overview

Your task is to create a Python program that collects the following information:

* Student name
* Age
* Score from Test 1
* Score from Test 2
* Score from Test 3
* Number of completed exercises

The program should then calculate several useful values and display them in a readable format.

This is a simple example of how Python can be used to **collect, store, transform, and summarize data**.

---

## 🎯 Objectives

By completing this task, you will practice:

* Creating and using **variables**
* Working with `str`, `int`, and `float`
* Reading data using `input()`
* Converting input using `int()` and `float()`
* Performing arithmetic operations
* Calculating an average
* Working with percentages
* Formatting output using `print()`
* Understanding how basic Python operations can be used for simple data analysis

---

# 📥 Input Data

The program should ask the user to enter:

1️⃣ Student name
2️⃣ Student age
3️⃣ Test 1 score
4️⃣ Test 2 score
5️⃣ Test 3 score
6️⃣ Number of completed exercises
7️⃣ Total number of exercises in the course

Example:

```text
Enter student name: Maria
Enter student age: 22
Enter Test 1 score: 85
Enter Test 2 score: 90
Enter Test 3 score: 78
Enter completed exercises: 18
Enter total exercises: 20
```

---

# 🧮 Calculations

Your program should calculate the following values.

### 1️⃣ Total Test Score

Calculate the sum of the three test scores.

Example:

```text
85 + 90 + 78 = 253
```

---

### 2️⃣ Average Test Score

Calculate the average score.

Formula:

```text
average = total_score / 3
```

Example:

```text
253 / 3 = 84.33
```

---

### 3️⃣ Exercise Completion Percentage

Calculate what percentage of the exercises the student has completed.

Formula:

```text
completion_percentage = completed_exercises / total_exercises * 100
```

Example:

```text
18 / 20 * 100 = 90%
```

---

### 4️⃣ Age Next Year

Calculate how old the student will be next year.

Formula:

```text
age_next_year = age + 1
```

---

# 🖥️ Expected Output

The final result should look similar to this:

```text
------------------------------
📊 STUDENT DATA REPORT
------------------------------

Student: Maria
Current age: 22
Age next year: 23

Test 1: 85.0
Test 2: 90.0
Test 3: 78.0

Total score: 253.0
Average score: 84.33

Completed exercises: 18 / 20
Completion rate: 90.0%

------------------------------
```

---

# 🛠️ Code Skeleton

```python
# 📊 Student Data Analyzer

print("📊 Welcome to the Student Data Analyzer!")

# Step 1: Read student information

student_name = input("Enter student name: ")

age = int(input("Enter student age: "))

test_1 = float(input("Enter Test 1 score: "))
test_2 = float(input("Enter Test 2 score: "))
test_3 = float(input("Enter Test 3 score: "))

completed_exercises = int(input("Enter completed exercises: "))
total_exercises = int(input("Enter total exercises: "))


# Step 2: Calculate total test score

# TODO:
total_score = ...


# Step 3: Calculate average score

# TODO:
average_score = ...


# Step 4: Calculate exercise completion percentage

# TODO:
completion_percentage = ...


# Step 5: Calculate student's age next year

# TODO:
age_next_year = ...


# Step 6: Display the report

print()
print("------------------------------")
print("📊 STUDENT DATA REPORT")
print("------------------------------")

print()

print("Student:", student_name)

# TODO: Print current age
# TODO: Print age next year

print()

# TODO: Print Test 1
# TODO: Print Test 2
# TODO: Print Test 3

print()

# TODO: Print total score
# TODO: Print average score

print()

# TODO: Print completed exercises
# TODO: Print completion percentage

print()
print("------------------------------")
```

---

# 🧠 Questions to Think About

Before running the program, try to answer these questions:

### Why do we use `int()` for the student's age?

Because age is represented as a whole number.

```python
age = int(input("Enter student age: "))
```

---

### Why do we use `float()` for test scores?

Because test scores may contain decimal values.

Example:

```text
87.5
```

---

### Why can't we calculate directly with values returned by `input()`?

Because `input()` returns a value of type:

```python
str
```

For example:

```python
number = input()
```

If the user enters:

```text
25
```

Python initially stores it as:

```python
"25"
```

To perform numerical operations, we need to convert it:

```python
number = int(input())
```

or:

```python
number = float(input())
```

---

# 🔬 Data Science Perspective

Even though this is a simple program, it follows an important pattern that appears constantly in Data Science:

```text
Raw Data
   ↓
Read Data
   ↓
Convert Data Types
   ↓
Perform Calculations
   ↓
Create New Values
   ↓
Display Results
```

In this exercise:

```text
Student scores
      ↓
Python variables
      ↓
Arithmetic operations
      ↓
Average score
      ↓
Completion percentage
      ↓
Student report
```

This is a simplified version of the same process used when analyzing larger datasets.

---

# 🌟 BONUS TASK 1 — Course Progress

Add another variable:

```python
course_hours = 40
```

Ask the student how many hours they have completed:

```python
completed_hours = int(input("Enter completed course hours: "))
```

Calculate the percentage of the course completed.

Formula:

```python
course_progress = completed_hours / course_hours * 100
```

Display:

```text
Course progress: 75.0%
```

---

# 🌟 BONUS TASK 2 — Dataset Size

Imagine that every student produces `3` test results.

Ask the user how many students are in the course:

```python
students_count = int(input("Enter number of students: "))
```

Calculate how many test results will exist in the dataset.

Example:

```text
Students: 25
Tests per student: 3

Total data points: 75
```

Think about what the following operation represents:

```python
students_count * 3
```

---

# 🌟 BONUS TASK 3 — Score Difference

Calculate the difference between Test 1 and Test 3.

Example:

```text
Test 1: 85
Test 3: 78

Difference: 7
```

Use:

```python
difference = test_1 - test_3
```

Try changing the scores and observe what happens when the result becomes negative.

---

# 🌟 BONUS TASK 4 — Rounded Average

Try displaying the average score rounded to two decimal places.

You can use:

```python
round(average_score, 2)
```

Example:

```text
84.33333333333333
```

becomes:

```text
84.33
```

---

# 📌 Requirements

Your solution should use:

* ✅ Variables
* ✅ `input()`
* ✅ `print()`
* ✅ `int()`
* ✅ `float()`
* ✅ Arithmetic operators
* ✅ Correct data types

Do **not** use:

* ❌ `if` statements
* ❌ loops
* ❌ lists
* ❌ dictionaries
* ❌ functions

These concepts will be introduced later in the course.

---

# 🏁 Conclusion

This project demonstrates an important idea:

> Data Science starts with understanding how to represent and manipulate data.

Before working with libraries such as **NumPy**, **Pandas**, or **Matplotlib**, it is essential to understand how Python handles:

* values
* variables
* data types
* numerical operations
* input and output

The same principles used in this small program will later be applied to thousands or even millions of data records.

> **Collect → Store → Calculate → Analyze → Understand 📊🐍**
