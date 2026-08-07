#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX 100

int stack[MAX];
int top = -1;

/* Push an element onto the stack */
void push(int value)
{
    if (top == MAX - 1)
    {
        printf("Stack Overflow\n");
        exit(1);
    }

    stack[++top] = value;
}

/* Pop an element from the stack */
int pop()
{
    if (top == -1)
    {
        printf("Invalid postfix expression\n");
        exit(1);
    }

    return stack[top--];
}

/* Check whether character is an operator */
int isOperator(char ch)
{
    return ch == '+' || ch == '-' || ch == '*' || ch == '/';
}

/* Perform arithmetic operation */
int calculate(int a, int b, char operator)
{
    switch (operator)
    {
        case '+':
            return a + b;

        case '-':
            return a - b;

        case '*':
            return a * b;

        case '/':
            if (b == 0)
            {
                printf("Error: Division by zero\n");
                exit(1);
            }
            return a / b;

        default:
            printf("Invalid operator\n");
            exit(1);
    }
}

int main()
{
    char expression[MAX];
    int i;
    int a, b, result;

    printf("============================================\n");
    printf(" POSTFIX EXPRESSION EVALUATION USING STACK\n");
    printf("============================================\n");

    printf("\nEnter postfix expression: ");
    scanf("%s", expression);

    printf("\n--------------------------------------------\n");
    printf("BOTTOM-UP COMPUTATION\n");
    printf("--------------------------------------------\n");

    for (i = 0; expression[i] != '\0'; i++)
    {
        char symbol = expression[i];

        /* If operand, push onto stack */
        if (isdigit(symbol))
        {
            int value = symbol - '0';

            push(value);

            printf("Read operand %d -> Push onto stack\n", value);
        }

        /* If operator, pop operands and calculate */
        else if (isOperator(symbol))
        {
            b = pop();
            a = pop();

            result = calculate(a, b, symbol);

            printf("%d %c %d = %d\n",
                   a, symbol, b, result);

            push(result);

            printf("Result %d -> Push onto stack\n", result);
        }

        else
        {
            printf("Invalid symbol: %c\n", symbol);
            return 1;
        }
    }

    /* Final result */
    if (top != 0)
    {
        printf("\nInvalid postfix expression\n");
        return 1;
    }

    result = pop();

    printf("\n--------------------------------------------\n");
    printf("FINAL RESULT\n");
    printf("--------------------------------------------\n");

    printf("Postfix Expression = %s\n", expression);
    printf("Final Evaluated Result = %d\n", result);

    printf("\n--------------------------------------------\n");
    printf("S-ATTRIBUTED DEFINITION CONNECTION\n");
    printf("--------------------------------------------\n");

    printf("Each intermediate result is synthesized from\n");
    printf("the operands below it and passed upward.\n");

    printf("\nEvaluation completed successfully.\n");

    return 0;
}