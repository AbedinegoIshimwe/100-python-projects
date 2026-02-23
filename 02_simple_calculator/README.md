# 🧮 Simple Python Calculator

This project is a simple command-line calculator built with Python.  
It allows the user to choose an operation (addition, subtraction, multiplication, or division) and then enter two numbers to get the result.

---

## 🎯 Goal

To practice:
- Using `input()` and `print()`
- Conditional statements (`if`, `elif`, `else`)
- Converting user input into numbers
- Debugging common beginner mistakes

---

## ❌ Mistakes I Made

### 1. Comparing strings with integers

At first, I compared the value returned by `input()` directly with numbers.  
This caused the condition that checks the selected operation to always fail because user input is read as text (a string) by default.

---

### 2. Syntax error in a conditional statement

I accidentally added an extra character at the end of one of the `elif` lines.  
This resulted in a syntax error and prevented the program from running.

---

### 3. Using a variable before it was defined

When an invalid operation was entered, the program still attempted to display the result even though no calculation had been performed.  
This caused an error because the variable holding the result had not yet been created.

---

### 4. Using integer division instead of normal division

The program originally used integer division, which only returned whole numbers.  
This was not suitable for a calculator that should return accurate decimal results.

---

## 🛠 How I Fixed the Errors

- Converted user input into an integer before comparing it with numeric values
- Removed the extra character that caused the syntax error
- Displayed the result only when a valid operation was selected
- Used normal division to produce accurate results

---

## 📚 What I Learned

From building this project, I learned that:

- User input in Python is always treated as a string unless converted
- Data types are important when performing comparisons
- Small syntax mistakes can prevent a program from running
- Variables must be created before they are used
- Debugging is an essential part of the programming process
- Writing clear logic makes programs easier to fix and improve

---

## 🚀 Future Improvements

- Allow the user to perform multiple calculations without restarting the program
- Add checks to prevent division by zero
- Support decimal numbers for more precise calculations
- Organize the logic into reusable functions


