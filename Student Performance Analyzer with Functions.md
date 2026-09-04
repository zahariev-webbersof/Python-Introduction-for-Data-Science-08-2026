# 🧩 Student Performance Analyzer with Functions

Welcome to the **Student Performance Analyzer**! 🎓📊

This practical project is designed to help you practice one of the most important concepts in Python:

**Functions**

You will build a small application that analyzes a student's academic performance using multiple reusable functions.

Instead of writing the entire program as one large block of code, you will divide the problem into smaller functions.

Each function will have **one clear responsibility**.

---

# 🏗️ Project Architecture

Before writing any code, look at the general structure of the application:

```text
                 main()
                   |
        -------------------------
        |           |           |
        ↓           ↓           ↓
   calculate()  analyze()   report()
        |           |
        ↓           ↓
      return       return
```

The idea is simple:

```text
main()
   ↓
controls the program

calculate()
   ↓
performs calculations

analyze()
   ↓
makes decisions based on the data

report()
   ↓
displays the final results
```

The calculation and analysis functions should usually **return values**.

The report function is responsible for displaying information.

In our actual project, the architecture will look similar to this:

```text
                         main()
                           |
          -------------------------------------
          |                 |                 |
          ↓                 ↓                 ↓
     CALCULATE           ANALYZE            REPORT
          |                 |                 |
          ↓                 ↓                 ↓
 calculate_total()    get_category()    print_report()
 calculate_average()  has_passed()
 calculate_percent()
 find_highest()
 find_lowest()
          |                 |
          ↓                 ↓
        return            return
```

Think about the program as a pipeline:

```text
INPUT DATA
    ↓
CALCULATE
    ↓
ANALYZE
    ↓
REPORT
```

This is the main idea behind the project.

> **Break one large problem into multiple small functions.**

---

# 📝 Project Overview

Your task is to create a Python program that analyzes a student's academic performance.

The program should collect:

* Student name
* Student age
* Three test scores
* Number of completed exercises
* Total number of exercises
* Number of completed course hours
* Total course hours

The program should then use separate functions to calculate:

* Total test score
* Average test score
* Exercise completion percentage
* Course progress percentage
* Highest test score
* Lowest test score
* Difference between highest and lowest score
* Student performance category
* Whether the student has passed the course

Finally, the program should generate a complete student performance report.

---

# 🎯 Objectives

By completing this project, you will practice:

* Defining functions using `def`
* Calling functions
* Working with parameters
* Passing arguments
* Returning values using `return`
* Storing returned values in variables
* Writing functions that return numbers
* Writing functions that return strings
* Writing functions that return Boolean values
* Using conditional statements inside functions
* Using loops inside functions
* Working with lists
* Calling one function from another
* Reusing existing functions
* Separating calculations from presentation
* Organizing a program using `main()`

---

# 🧠 The Function Mindset

A function can be viewed as a small machine:

```text
        INPUT
          ↓
    ┌───────────┐
    │ FUNCTION  │
    └───────────┘
          ↓
        OUTPUT
```

For example:

```python
def calculate_total(a, b):
    return a + b
```

Calling:

```python
result = calculate_total(5, 3)
```

can be visualized as:

```text
5, 3
 ↓
calculate_total()
 ↓
5 + 3
 ↓
return 8
 ↓
result = 8
```

This pattern is extremely important:

```text
INPUT → PROCESS → RETURN
```

---

# 📥 Input Data

The program should ask the user to enter:

1. Student name
2. Student age
3. Test 1 score
4. Test 2 score
5. Test 3 score
6. Number of completed exercises
7. Total number of exercises
8. Number of completed course hours
9. Total course hours

Example:

```text
Enter student name: Maria
Enter student age: 22

Enter Test 1 score: 85
Enter Test 2 score: 90
Enter Test 3 score: 78

Enter completed exercises: 18
Enter total exercises: 20

Enter completed course hours: 32
Enter total course hours: 40
```

The three test scores should be stored inside a list:

```python
scores = [test_1, test_2, test_3]
```

Example:

```python
scores = [85.0, 90.0, 78.0]
```

This list will be passed to several different functions.

---

# 🔧 Function 1 — Calculate Total Score

Create the following function:

```python
def calculate_total_score(scores):
    ...
```

The function receives a list of test scores.

Example:

```python
scores = [85, 90, 78]
```

It should calculate:

```text
85 + 90 + 78 = 253
```

and return:

```text
253
```

Try solving the problem using a loop:

```python
total = 0

for score in scores:
    ...
```

The important part is that the function should **return** the result.

Do not simply print it.

---

# 🔧 Function 2 — Calculate Average Score

Create:

```python
def calculate_average_score(scores):
    ...
```

The function should calculate the average test score.

Formula:

```text
average = total score / number of scores
```

For:

```python
scores = [85, 90, 78]
```

the calculation is:

```text
253 / 3 = 84.33
```

Instead of calculating the total again, try calling:

```python
calculate_total_score(scores)
```

inside the function.

Conceptually:

```text
calculate_average_score()
          |
          ↓
calculate_total_score()
          |
          ↓
        return
```

This is your first example of **one function reusing another function**.

---

# 🔧 Function 3 — Calculate Percentage

Create:

```python
def calculate_percentage(completed, total):
    ...
```

The function should calculate:

```text
completed / total * 100
```

For example:

```python
calculate_percentage(18, 20)
```

should return:

```text
90.0
```

The important idea is that this function is **generic**.

It is not called:

```python
calculate_exercise_percentage()
```

because the same calculation can be reused for different types of data.

For exercises:

```python
exercise_completion = calculate_percentage(
    completed_exercises,
    total_exercises
)
```

For course hours:

```python
course_progress = calculate_percentage(
    completed_hours,
    total_hours
)
```

One function:

```text
calculate_percentage()
```

can solve multiple similar problems.

This is one of the main advantages of functions:

```text
WRITE ONCE → REUSE MANY TIMES
```

---

# 🔧 Function 4 — Find Highest Score

Create:

```python
def find_highest_score(scores):
    ...
```

The function should return the highest test score.

Example:

```python
scores = [85, 90, 78]
```

Result:

```text
90
```

For the first version, try solving this manually using a loop.

Example starting point:

```python
highest_score = float("-inf")

for score in scores:
    ...
```

Do not use `max()` in the first version.

---

# 🔧 Function 5 — Find Lowest Score

Create:

```python
def find_lowest_score(scores):
    ...
```

The function should return the lowest test score.

Example:

```python
scores = [85, 90, 78]
```

Result:

```text
78
```

Try solving this using a loop.

Possible starting value:

```python
lowest_score = float("inf")
```

Do not use `min()` in the first version.

---

# 🔧 Function 6 — Calculate Score Range

Create:

```python
def calculate_score_range(scores):
    ...
```

The score range represents the difference between the highest and lowest test score.

Formula:

```text
highest score - lowest score
```

Example:

```text
90 - 78 = 12
```

Do not write the highest and lowest search logic again.

Instead, reuse:

```python
find_highest_score(scores)
```

and:

```python
find_lowest_score(scores)
```

Conceptually:

```text
calculate_score_range()
          |
      -----------
      |         |
      ↓         ↓
find_highest() find_lowest()
      |         |
      ↓         ↓
   return     return
      |         |
      -----------
          ↓
     difference
          ↓
        return
```

---

# 🔧 Function 7 — Determine Performance Category

Create:

```python
def get_performance_category(average_score):
    ...
```

The function should analyze the average score and return a category.

Use the following rules:

```text
90 - 100    → Excellent
80 - 89.99  → Very Good
70 - 79.99  → Good
60 - 69.99  → Average
Below 60    → Needs Improvement
```

Example:

```python
category = get_performance_category(84.33)
```

Result:

```text
Very Good
```

This function introduces another important pattern:

```text
DATA
 ↓
ANALYSIS
 ↓
DECISION
 ↓
RETURN
```

The function receives a number but returns a string.

---

# 🔧 Function 8 — Check If Student Passed

Create:

```python
def has_passed(average_score, completion_rate):
    ...
```

A student passes only when **both conditions** are satisfied:

```text
Average score >= 60
```

AND:

```text
Exercise completion >= 70%
```

The function should return a Boolean value:

```python
True
```

or:

```python
False
```

For example:

```python
has_passed(84.33, 90)
```

should return:

```python
True
```

while:

```python
has_passed(84.33, 50)
```

should return:

```python
False
```

Try returning the Boolean expression directly.

---

# 🔧 Function 9 — Get Pass Status

Create:

```python
def get_pass_status(passed):
    ...
```

The function receives:

```python
True
```

or:

```python
False
```

If the value is `True`, return:

```text
PASSED
```

Otherwise return:

```text
NOT PASSED
```

Example:

```python
status = get_pass_status(True)
```

Result:

```text
PASSED
```

---

# 🔧 Function 10 — Print Student Report

Create:

```python
def print_student_report(
    name,
    age,
    scores,
    total_score,
    average_score,
    highest_score,
    lowest_score,
    score_range,
    completed_exercises,
    total_exercises,
    exercise_completion,
    completed_hours,
    total_hours,
    course_progress,
    performance_category,
    pass_status
):
    ...
```

This function is different from the calculation functions.

Its responsibility is:

```text
DISPLAY DATA
```

It should **not** contain the main calculations.

For example, avoid doing this inside the report function:

```python
average_score = sum(scores) / len(scores)
```

The average should already have been calculated before calling the report.

Think about the responsibilities:

```text
calculate_average_score()
        ↓
     CALCULATE


get_performance_category()
        ↓
      ANALYZE


print_student_report()
        ↓
      DISPLAY
```

---

# 🖥️ Expected Output

For the following data:

```text
Maria
22
85
90
78
18
20
32
40
```

the final report should look similar to:

```text
----------------------------------------
📊 STUDENT PERFORMANCE REPORT
----------------------------------------

Student: Maria
Age: 22

Test scores: [85.0, 90.0, 78.0]

Total score: 253.0
Average score: 84.33

Highest score: 90.0
Lowest score: 78.0
Score range: 12.0

Completed exercises: 18 / 20
Exercise completion: 90.0%

Completed course hours: 32 / 40
Course progress: 80.0%

Performance category: Very Good
Course status: PASSED

----------------------------------------
```

---

# 🛠️ Code Skeleton

Complete the missing parts marked with `TODO`.

```python
# 🧩 Student Performance Analyzer


# ----------------------------------------
# CALCULATION FUNCTIONS
# ----------------------------------------

def calculate_total_score(scores):
    # TODO: Calculate and return the total score
    pass


def calculate_average_score(scores):
    # TODO: Use calculate_total_score()
    # TODO: Calculate and return the average
    pass


def calculate_percentage(completed, total):
    # TODO: Calculate and return percentage
    pass


def find_highest_score(scores):
    # TODO: Find the highest score using a loop
    pass


def find_lowest_score(scores):
    # TODO: Find the lowest score using a loop
    pass


def calculate_score_range(scores):
    # TODO: Use find_highest_score()
    # TODO: Use find_lowest_score()
    # TODO: Return the difference
    pass


# ----------------------------------------
# ANALYSIS FUNCTIONS
# ----------------------------------------

def get_performance_category(average_score):
    # TODO: Return the correct category
    pass


def has_passed(average_score, completion_rate):
    # TODO: Return True or False
    pass


def get_pass_status(passed):
    # TODO: Return PASSED or NOT PASSED
    pass


# ----------------------------------------
# REPORT FUNCTION
# ----------------------------------------

def print_student_report(
    name,
    age,
    scores,
    total_score,
    average_score,
    highest_score,
    lowest_score,
    score_range,
    completed_exercises,
    total_exercises,
    exercise_completion,
    completed_hours,
    total_hours,
    course_progress,
    performance_category,
    pass_status
):
    print()
    print("----------------------------------------")
    print("📊 STUDENT PERFORMANCE REPORT")
    print("----------------------------------------")
    print()

    # TODO: Print student information
    # TODO: Print scores
    # TODO: Print calculated values
    # TODO: Print exercise completion
    # TODO: Print course progress
    # TODO: Print performance category
    # TODO: Print course status

    print()
    print("----------------------------------------")


# ----------------------------------------
# MAIN FUNCTION
# ----------------------------------------

def main():
    print("📊 Welcome to the Student Performance Analyzer!")
    print()

    # ----------------------------------------
    # INPUT
    # ----------------------------------------

    student_name = input("Enter student name: ")
    student_age = int(input("Enter student age: "))

    print()

    test_1 = float(input("Enter Test 1 score: "))
    test_2 = float(input("Enter Test 2 score: "))
    test_3 = float(input("Enter Test 3 score: "))

    scores = [test_1, test_2, test_3]

    print()

    completed_exercises = int(
        input("Enter completed exercises: ")
    )

    total_exercises = int(
        input("Enter total exercises: ")
    )

    print()

    completed_hours = int(
        input("Enter completed course hours: ")
    )

    total_hours = int(
        input("Enter total course hours: ")
    )

    # ----------------------------------------
    # CALCULATIONS
    # ----------------------------------------

    total_score = calculate_total_score(scores)

    average_score = calculate_average_score(scores)

    exercise_completion = calculate_percentage(
        completed_exercises,
        total_exercises
    )

    course_progress = calculate_percentage(
        completed_hours,
        total_hours
    )

    highest_score = find_highest_score(scores)

    lowest_score = find_lowest_score(scores)

    score_range = calculate_score_range(scores)

    # ----------------------------------------
    # ANALYSIS
    # ----------------------------------------

    performance_category = get_performance_category(
        average_score
    )

    passed = has_passed(
        average_score,
        exercise_completion
    )

    pass_status = get_pass_status(passed)

    # ----------------------------------------
    # REPORT
    # ----------------------------------------

    print_student_report(
        student_name,
        student_age,
        scores,
        total_score,
        average_score,
        highest_score,
        lowest_score,
        score_range,
        completed_exercises,
        total_exercises,
        exercise_completion,
        completed_hours,
        total_hours,
        course_progress,
        performance_category,
        pass_status
    )


main()
```

---

# 🧠 Understanding the Architecture

Now look again at the architecture from the beginning:

```text
                         main()
                           |
          -------------------------------------
          |                 |                 |
          ↓                 ↓                 ↓
     CALCULATE           ANALYZE            REPORT
          |                 |                 |
          ↓                 ↓                 ↓
 calculate_total()    get_category()    print_report()
 calculate_average()  has_passed()
 calculate_percent()
 find_highest()
 find_lowest()
          |                 |
          ↓                 ↓
        return            return
```

The `main()` function controls the program.

It does not need to know exactly **how** every calculation works.

It simply asks the appropriate function to perform the task.

For example:

```python
average_score = calculate_average_score(scores)
```

can be read as:

```text
"Calculate the average of these scores
and give me the result."
```

Similarly:

```python
performance_category = get_performance_category(
    average_score
)
```

means:

```text
"Analyze this average
and tell me the performance category."
```

This is an important programming concept:

> **The main program coordinates the work. Smaller functions perform specific tasks.**

---

# 🧠 Parameters vs Arguments

Consider:

```python
def calculate_percentage(completed, total):
    return completed / total * 100
```

Here:

```text
completed
total
```

are **parameters**.

They represent values that the function expects to receive.

When we call:

```python
calculate_percentage(18, 20)
```

the values:

```text
18
20
```

are **arguments**.

Conceptually:

```text
              ARGUMENTS
               18, 20
                 ↓
        calculate_percentage
                 ↓
          PARAMETERS
        completed = 18
        total = 20
                 ↓
             PROCESS
                 ↓
              RETURN
                 ↓
               90.0
```

---

# 🧠 `print()` vs `return`

This distinction is extremely important.

Consider:

```python
def calculate_total(a, b):
    print(a + b)
```

The function displays the result.

But:

```python
def calculate_total(a, b):
    return a + b
```

gives the result back to the program.

Now we can write:

```python
result = calculate_total(10, 20)
```

and:

```text
result = 30
```

The returned value can then be:

```python
print(result)
```

or used in another calculation:

```python
final_result = result * 2
```

or passed to another function:

```python
analyze_result(result)
```

Therefore:

```text
print()
   ↓
DISPLAY


return
   ↓
GIVE RESULT BACK
```

---

# ♻️ Reusing Functions

One of the most important objectives of this project is to avoid duplicated code.

Consider:

```python
exercise_completion = (
    completed_exercises / total_exercises * 100
)

course_progress = (
    completed_hours / total_hours * 100
)
```

The mathematical operation is identical.

Instead, create:

```python
def calculate_percentage(completed, total):
    return completed / total * 100
```

Now:

```python
exercise_completion = calculate_percentage(
    completed_exercises,
    total_exercises
)

course_progress = calculate_percentage(
    completed_hours,
    total_hours
)
```

The idea is:

```text
DO NOT REPEAT LOGIC

        ↓

CREATE A FUNCTION

        ↓

REUSE THE FUNCTION
```

---

# 🔗 Functions Calling Functions

Functions can also use other functions.

For example:

```python
def calculate_total_score(scores):
    total = 0

    for score in scores:
        total += score

    return total
```

Then:

```python
def calculate_average_score(scores):
    total = calculate_total_score(scores)

    return total / len(scores)
```

The relationship is:

```text
calculate_average_score()
          |
          ↓
calculate_total_score()
          |
          ↓
       return total
          |
          ↓
    calculate average
          |
          ↓
     return average
```

This allows us to build larger functionality from smaller pieces.

---

# 🌟 BONUS TASK 1 — Validate Test Score

Create:

```python
def is_valid_score(score):
    ...
```

A test score is valid when:

```text
0 <= score <= 100
```

The function should return:

```python
True
```

or:

```python
False
```

Examples:

```python
is_valid_score(85)
```

returns:

```text
True
```

while:

```python
is_valid_score(120)
```

returns:

```text
False
```

---

# 🌟 BONUS TASK 2 — Validate All Scores

Create:

```python
def are_scores_valid(scores):
    ...
```

The function should check every score in the list.

Instead of repeating the validation condition, call:

```python
is_valid_score(score)
```

for every score.

Example:

```python
scores = [85, 90, 78]
```

Result:

```text
True
```

But:

```python
scores = [85, 120, 78]
```

should return:

```text
False
```

Architecture:

```text
are_scores_valid()
        |
        ↓
     for score
        |
        ↓
is_valid_score()
        |
        ↓
   True / False
```

---

# 🌟 BONUS TASK 3 — Count Excellent Scores

Create:

```python
def count_excellent_scores(scores):
    ...
```

A score is considered excellent when:

```text
score >= 90
```

Example:

```python
scores = [95, 72, 91]
```

Result:

```text
2
```

Use:

```python
for
```

and a counter variable.

---

# 🌟 BONUS TASK 4 — Analyze Improvement

Create:

```python
def calculate_improvement(first_score, last_score):
    ...
```

The function should calculate:

```text
last_score - first_score
```

Example:

```text
Test 1: 70
Test 3: 85
```

Result:

```text
15
```

A positive value means improvement.

A negative value means performance decreased.

---

# 🌟 BONUS TASK 5 — Improvement Status

Create:

```python
def get_improvement_status(improvement):
    ...
```

Use the following rules:

```text
improvement > 0
        ↓
Improved


improvement == 0
        ↓
No Change


improvement < 0
        ↓
Declined
```

Example:

```python
get_improvement_status(15)
```

returns:

```text
Improved
```

---

# 🌟 BONUS TASK 6 — Weighted Performance Score

Create:

```python
def calculate_performance_score(
    average_score,
    exercise_completion,
    course_progress
):
    ...
```

The final score should be calculated using:

```text
Test performance       → 60%
Exercise completion    → 25%
Course progress        → 15%
```

Formula:

```text
performance_score =
    average_score * 0.60
    + exercise_completion * 0.25
    + course_progress * 0.15
```

Example:

```text
Average score: 84.33
Exercise completion: 90
Course progress: 80
```

Calculation:

```text
84.33 × 0.60 = 50.598
90 × 0.25 = 22.5
80 × 0.15 = 12
```

Final:

```text
50.598 + 22.5 + 12 = 85.098
```

Rounded to two decimal places:

```text
85.10
```

---

# 🌟 BONUS TASK 7 — Analyze One Student

Create:

```python
def analyze_student(name, scores):
    ...
```

The function should use your existing functions to determine:

* Total score
* Average score
* Highest score
* Lowest score
* Score range
* Performance category

Example:

```python
analyze_student(
    "Maria",
    [85, 90, 78]
)
```

The result could be:

```text
Student: Maria
Total: 253
Average: 84.33
Highest: 90
Lowest: 78
Range: 12
Category: Very Good
```

Do not write the calculations again.

Reuse:

```text
calculate_total_score()
calculate_average_score()
find_highest_score()
find_lowest_score()
calculate_score_range()
get_performance_category()
```

---

# 🚀 ADVANCED CHALLENGE — Multiple Students

Extend the application so that it can analyze multiple students.

Ask:

```text
How many students: 3
```

Then collect data for every student.

Example:

```text
Student 1
Name: Maria
Test 1: 85
Test 2: 90
Test 3: 78

Student 2
Name: Peter
Test 1: 65
Test 2: 72
Test 3: 68

Student 3
Name: John
Test 1: 95
Test 2: 91
Test 3: 98
```

Use the functions you have already created.

Do not rewrite the analysis logic.

---

# 🏆 FINAL CHALLENGE — Course Analytics

Extend the program one final time.

After analyzing all students, generate a course report.

Example:

```text
========================================
📊 COURSE ANALYTICS
========================================

Students analyzed: 3

Best average score: 94.67
Lowest average score: 68.33
Course average: 82.44

Passed students: 2
Failed students: 1

Pass rate: 66.67%

========================================
```

Think about which parts of this problem can become new functions.

Possible functions:

```python
def calculate_course_average(averages):
    ...


def count_passed_students(results):
    ...


def calculate_pass_rate(passed, total):
    ...


def find_best_average(averages):
    ...


def print_course_report(...):
    ...
```

Your architecture can now grow:

```text
                           main()
                             |
          -----------------------------------------
          |                   |                   |
          ↓                   ↓                   ↓
       INPUT              PROCESS              REPORT
                              |
                  -------------------------
                  |                       |
                  ↓                       ↓
             CALCULATE                 ANALYZE
                  |                       |
          -----------------         ----------------
          |       |       |         |              |
          ↓       ↓       ↓         ↓              ↓
       total   average  percent  category        passed
          |       |       |         |              |
          ↓       ↓       ↓         ↓              ↓
        return  return   return    return         return
```

---

# 📌 Requirements

Your main solution should use:

* ✅ Functions
* ✅ `def`
* ✅ Parameters
* ✅ Arguments
* ✅ `return`
* ✅ `main()`
* ✅ Variables
* ✅ Lists
* ✅ `for` loops
* ✅ Conditional statements
* ✅ Boolean values
* ✅ `input()`
* ✅ `print()`
* ✅ `int()`
* ✅ `float()`
* ✅ Arithmetic operators
* ✅ Functions calling other functions

Try to avoid:

* ❌ Duplicating calculation logic
* ❌ Writing everything inside `main()`
* ❌ Using global variables for calculations
* ❌ Mixing input, calculations, and output inside every function
* ❌ Creating one enormous function
* ❌ Repeating code that could be reused

---

# ⭐ Function Design Rule

For this project, follow one important rule:

> **One Function → One Clear Responsibility**

For example:

```python
def calculate_average_score(scores):
    ...
```

should calculate an average.

It should not:

```text
Ask for the student's name
Print the report
Calculate course progress
Determine whether the student passed
```

Similarly:

```python
def get_performance_category(average_score):
    ...
```

should analyze the score and return a category.

And:

```python
def print_student_report(...):
    ...
```

should display the report.

---

# 🧠 Think Like a Developer

When writing your solution, repeatedly ask yourself:

```text
Am I writing the same logic again?
        ↓
       YES
        ↓
Can I create or reuse a function?
```

Also ask:

```text
Does this function calculate something?
        ↓
Consider returning the result.


Does this function analyze something?
        ↓
Return the decision.


Does this function display something?
        ↓
print() may be appropriate.
```

The goal is not to create as many functions as possible.

The goal is to create **useful functions with clear responsibilities**.

---

# 🔬 Data Science Perspective

Functions are fundamental in Data Science because data processing usually happens through multiple stages.

A simplified real-world pipeline could look like:

```text
                 RAW DATA
                    |
                    ↓
              validate_data()
                    |
                    ↓
               clean_data()
                    |
                    ↓
            transform_data()
                    |
                    ↓
              analyze_data()
                    |
                    ↓
             create_report()
```

Your Student Performance Analyzer follows the same principle:

```text
              STUDENT DATA
                    |
                    ↓
          calculate_scores()
                    |
                    ↓
          calculate_average()
                    |
                    ↓
          analyze_performance()
                    |
                    ↓
             check_result()
                    |
                    ↓
              print_report()
```

The dataset in this exercise is small.

Later, the same idea can be applied to:

```text
3 values
30 values
30,000 values
3,000,000 values
```

The amount of data changes.

The architectural principle remains the same.

---

# 🏁 Conclusion

This project demonstrates one of the most important ideas in programming:

> **Do not try to solve one large problem at once. Break it into smaller problems.**

Instead of thinking:

```text
"How do I create the entire Student Performance Analyzer?"
```

think:

```text
How do I calculate the total?
        ↓
Create a function.

How do I calculate the average?
        ↓
Create a function.

How do I calculate a percentage?
        ↓
Create a reusable function.

How do I determine the category?
        ↓
Create a function.

How do I check whether the student passed?
        ↓
Create a function.

How do I display everything?
        ↓
Create a report function.
```

Then let:

```text
main()
```

connect everything together.

The final mental model should be:

```text
                         main()
                           |
          -------------------------------------
          |                 |                 |
          ↓                 ↓                 ↓
     CALCULATE           ANALYZE            REPORT
          |                 |                 |
          ↓                 ↓                 ↓
       functions          functions         function
          |                 |
          ↓                 ↓
        return            return
```

This is the transition from:

```text
"I can write Python statements."
```

to:

```text
"I can organize a Python program."
```

And that is the real purpose of learning functions.

> **Divide → Define → Call → Return → Reuse → Build 🐍🧩🚀**
