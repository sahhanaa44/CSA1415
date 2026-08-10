#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Global variables for string tracking
char input[100];
int cursor = 0;

// Function prototypes
void E();
void E_prime();
void T();
void T_prime();
void F();

void E() {
    T();
    E_prime();
}

void E_prime() {
    if (input[cursor] == '+') {
        cursor++; // Match '+'
        T();
        E_prime();
    }
    // Epsilon case: do nothing and return
}

void T() {
    F();
    T_prime();
}

void T_prime() {
    if (input[cursor] == '*') {
        cursor++; // Match '*'
        F();
        T_prime();
    }
    // Epsilon case: do nothing and return
}

void F() {
    if (input[cursor] == '(') {
        cursor++; // Match '('
        E();
        if (input[cursor] == ')') {
            cursor++; // Match ')'
        } else {
            printf("Error: Missing closing parenthesis ')'\n");
            exit(1);
        }
    } else if (isalnum(input[cursor])) {
        // Match identifier (alphanumeric characters like 'id' or numbers)
        while (isalnum(input[cursor])) {
            cursor++;
        }
    } else {
        printf("Error: Invalid character '%c'\n", input[cursor]);
        exit(1);
    }
}

int main() {
    printf("Enter an expression to parse (e.g., id+id*id): ");
    scanf("%s", input);

    // Start parsing from the start symbol E
    E();

    // Check if the parser consumed the entire input string
    if (input[cursor] == '\0') {
        printf("String parsed successfully! Input matches the grammar.\n");
    } else {
        printf("Error: Compilation failed at character '%c'\n", input[cursor]);
    }

    return 0;
}
