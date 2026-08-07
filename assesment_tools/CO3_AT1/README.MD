# Compiler Design Experiments

This repository contains implementations and simulations of five Compiler Design experiments covering syntax-directed definitions, expression evaluation, attribute grammars, type equivalence, and semantic type checking.

## Experiments

### Experiment 1 — Syntax-Directed Definition for Expression Evaluation

**Objective:**
Implement a Syntax-Directed Definition (SDD) for evaluating arithmetic expressions using synthesized attributes.

**Features:**

* Supports `+`, `-`, `*`, `/`, and parentheses
* Constructs an expression/syntax tree
* Demonstrates synthesized attributes
* Performs bottom-up evaluation
* Demonstrates operator precedence and associativity
* Displays annotated evaluation steps

**Implementation:**

* HTML5
* CSS3
* JavaScript

**Files:**

```text
Q1/
├── index.html
├── style.css
└── script.js
```

---

### Experiment 2 — Postfix Expression Evaluation Using Stack

**Objective:**
Evaluate postfix expressions using a stack and demonstrate bottom-up computation related to S-attributed definitions.

**Features:**

* Stack-based evaluation
* Supports `+`, `-`, `*`, and `/`
* Displays intermediate calculations
* Produces the final result
* Demonstrates bottom-up computation

**Implementation:**

* C
* Visual Studio Code
* GCC Compiler

**File:**

```text
Q2/
└── q2_postfix.c
```

---

### Experiment 3 — L-Attributed Definition for Expression Evaluation

**Objective:**
Simulate an L-attributed definition using inherited attributes and demonstrate top-down, left-to-right evaluation.

**Features:**

* Uses inherited attributes
* Demonstrates attribute propagation
* Maintains operator precedence
* Displays grammar rules
* Shows step-by-step evaluation
* Provides a visual representation of attribute flow

**Implementation:**

* Python
* Tkinter
* Visual Studio Code

**Files:**

```text
Q3/
└── q3_l_attributed.py
```

---

### Experiment 4 — Type Equivalence Checking

**Objective:**
Check whether two type expressions are equivalent during semantic analysis.

**Features:**

* Supports basic types such as `int`, `float`, and `char`
* Supports pointer types
* Compares base types
* Compares pointer levels
* Reports whether types are equivalent

**Implementation:**

* C
* Visual Studio Code / Code::Blocks
* GCC Compiler

**File:**

```text
Q4/
└── q4_type_equivalence.c
```

---

### Experiment 5 — Type Checking of Arithmetic Expressions

**Objective:**
Perform semantic type checking on arithmetic expressions and detect invalid operand combinations.

**Features:**

* Accepts operand types and operators
* Checks type compatibility
* Detects type errors
* Supports arithmetic operators
* Displays the resulting type for valid expressions

**Implementation:**

* C
* Visual Studio Code / Dev-C++
* GCC Compiler

**File:**

```text
Q5/
└── q5_type_checking.c
```

---

## Repository Structure

```text
Compiler-Design-Experiments/
│
├── README.md
│
├── Q1_SDD_Expression_Evaluation/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── Q2_Postfix_Stack_Evaluation/
│   └── q2_postfix.c
│
├── Q3_L_Attributed_Evaluation/
│   └── q3_l_attributed.py
│
├── Q4_Type_Equivalence/
│   └── q4_type_equivalence.c
│
└── Q5_Type_Checking/
    └── q5_type_checking.c
```

## Technologies Used

| Experiment | Technology            |
| ---------- | --------------------- |
| Q1         | HTML, CSS, JavaScript |
| Q2         | C, GCC                |
| Q3         | Python, Tkinter       |
| Q4         | C, GCC                |
| Q5         | C, GCC                |

## Concepts Covered

* Syntax-Directed Definitions
* Synthesized Attributes
* Inherited Attributes
* S-Attributed Definitions
* L-Attributed Definitions
* Syntax Trees
* Abstract Syntax Trees
* Bottom-Up Evaluation
* Top-Down Evaluation
* Postfix Expression Evaluation
* Stack-Based Evaluation
* Operator Precedence
* Type Equivalence
* Pointer Types
* Semantic Analysis
* Type Checking
* Type Errors

## How to Run

### Q1 — HTML

Open `index.html` in a web browser such as Google Chrome or Microsoft Edge.

### Q2 — C

Compile using GCC:

```bash
gcc q2_postfix.c -o q2_postfix
```

Run:

```bash
q2_postfix
```

### Q3 — Python

Run:

```bash
python q3_l_attributed.py
```

The Tkinter graphical interface will open automatically.

### Q4 — C

Compile:

```bash
gcc q4_type_equivalence.c -o q4_type_equivalence
```

Run:

```bash
q4_type_equivalence
```

### Q5 — C

Compile:

```bash
gcc q5_type_checking.c -o q5_type_checking
```

Run:

```bash
q5_type_checking
```

## Sample Inputs

### Q1

```text
(2+3)*4
```

### Q2

```text
23*54*+9-
```

### Q3

```text
Expression: a + b * c
a = 2
b = 3
c = 4
```

Expected result:

```text
14
```

### Q4

```text
Type 1: int*
Type 2: int*
```

Expected:

```text
Types are Equivalent
```

### Q5

```text
Type 1: int
Operator: +
Type 2: char
```

Expected:

```text
Type Error
```

## Author

**Compiler Design Laboratory Project**

This repository is intended for academic demonstration and learning of compiler design concepts.
