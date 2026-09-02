# PMRL Compiler Front-End

## Patient Monitoring Rule Language

A lightweight compiler front-end developed for **Patient Monitoring Rule Language (PMRL)** as part of the Compiler Design course (CSA1415).

## Project Overview

PMRL is a small domain-specific language designed to represent simple patient-monitoring rules. The compiler front-end processes PMRL source code through lexical analysis and syntax analysis, constructs a parse tree for valid programs, and reports lexical and syntax errors for invalid inputs.

The project is implemented using **Python** and **Flask** and provides a browser-based interface for entering rules and viewing compilation results.

## Features

* Lexical analysis and token generation
* Keyword, identifier and integer recognition
* Arithmetic expressions
* Relational expressions
* Assignment statements
* `if-then-else` conditional statements
* Parenthesized expressions
* Recursive descent parsing
* Operator precedence handling
* Parse-tree construction
* Lexical and syntax error reporting
* Source-position-based diagnostics
* Predefined test cases
* Browser-based compiler interface
* Downloadable compilation reports

## PMRL Syntax Examples

### Assignment

```text
heartRate = 125;
```

### Conditional Rule

```text
if heartRate > 120 then
alert = 1;
else
alert = 0;
```

### Arithmetic Expression

```text
oxygenLevel = heartRate + 5 * 2;
```

### Parenthesized Expression

```text
temperature = (38 + 2) * 2;
```

## System Architecture

```text
Browser Interface
       ↓
Flask Backend
       ↓
Lexical Analyzer
       ↓
Recursive Descent Parser
       ↓
Parse Tree / Diagnostics
       ↓
JSON Result
       ↓
Browser Display
```

## Project Structure

```text
Assignment/
│
├── app.py
│
├── compiler/
│   ├── __init__.py
│   ├── lexer.py
│   ├── parser.py
│   └── tree.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── reports/
```

## Technologies Used

* **Python** – Compiler implementation
* **Flask** – Backend web framework
* **HTML** – Interface structure
* **CSS** – Interface styling
* **JavaScript** – Client-side interaction
* **Git/GitHub** – Version control
* **VS Code** – Development environment

## Compiler Components

### Lexer

The lexer scans the PMRL source code and converts the input into tokens such as:

* Keywords
* Identifiers
* Integer constants
* Arithmetic operators
* Relational operators
* Assignment operator
* Parentheses
* Semicolons

Unsupported symbols are reported as lexical errors.

### Parser

The parser uses a **Recursive Descent Parsing** approach. The parser follows the defined PMRL grammar and contains functions for statements, assignments, conditionals, conditions and expressions.

Expression parsing is divided into:

```text
expression()
    ↓
term()
    ↓
factor()
```

This structure allows multiplication and division to have higher precedence than addition and subtraction.

### Parse Tree

For valid PMRL input, the parser constructs a hierarchical parse tree representing the syntactic structure of the program.

### Error Handling

The compiler distinguishes between:

* **Lexical errors** – unsupported or invalid symbols
* **Syntax errors** – incorrect grammatical structures such as missing expressions or semicolons

## Test Cases

The project includes tests for both valid and invalid inputs.

| Test Case | Description              | Expected Result |
| --------- | ------------------------ | --------------- |
| TC1       | Simple assignment        | Accepted        |
| TC2       | Conditional rule         | Accepted        |
| TC3       | Missing expression       | Syntax Error    |
| TC4       | Invalid symbol `@`       | Lexical Error   |
| TC5       | Incomplete condition     | Syntax Error    |
| TC6       | Missing semicolon        | Syntax Error    |
| TC7       | Arithmetic expression    | Accepted        |
| TC8       | Parenthesized expression | Accepted        |

## Running the Project

### 1. Install Python

Make sure Python is installed on your system.

### 2. Install Flask

```bash
pip install flask
```

### 3. Run the Application

From the project directory:

```bash
python app.py
```

### 4. Open the Browser

Open the local Flask address shown in the terminal.

The PMRL Compiler Studio interface can then be used to enter and compile PMRL rules.

## Compilation Output

For a valid rule, the application provides:

* Compilation status
* Generated tokens
* Parse tree
* Diagnostics
* Token count
* Compilation report

For invalid input, the application reports the corresponding lexical or syntax error.

## Limitations

The current implementation is intentionally limited to the compiler front-end. It does not include:

* Semantic analysis
* Symbol tables
* Type checking
* Intermediate representation
* Code generation
* Optimization
* Runtime execution
* Database integration
* Medical-device integration

The system is a compiler-design prototype and is **not intended for clinical deployment or medical decision-making**.

## Future Improvements

Possible future extensions include:

* Semantic analysis
* Symbol-table implementation
* Type checking
* Additional data types
* Intermediate representation
* Rule interpretation
* More complex logical conditions
* Improved error recovery
* Integration with validated monitoring data

## Learning Outcomes

This project provided practical experience with:

* Token specification
* Lexical analysis
* Context-Free Grammar
* Recursive descent parsing
* Operator precedence
* Parse-tree construction
* Error detection
* Compiler module integration
* Web-based compiler interfaces
* Testing and validation

## Authors

**Swetha S** – 192521076
**Sahhanaa Shree T** – 192511283

### Course

**Compiler Design – CSA1415**

### Guide

**Dr. C. Anitha**
