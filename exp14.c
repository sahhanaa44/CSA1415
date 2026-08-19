#include <stdio.h>
#include <string.h>
#include <ctype.h>

char stack[100];
int top = -1;

void push(char c)
{
    stack[++top] = c;
}

char pop()
{
    return stack[top--];
}

int precedence(char c)
{
    if (c == '+' || c == '-')
        return 1;

    if (c == '*' || c == '/')
        return 2;

    return 0;
}

void infixToPostfix(char infix[], char postfix[])
{
    int i, j = 0;
    char c;

    for (i = 0; infix[i] != '\0'; i++)
    {
        c = infix[i];

        if (isalnum(c))
        {
            postfix[j++] = c;
        }
        else if (c == '(')
        {
            push(c);
        }
        else if (c == ')')
        {
            while (top != -1 && stack[top] != '(')
                postfix[j++] = pop();

            if (top != -1)
                pop();
        }
        else
        {
            while (top != -1 &&
                   precedence(stack[top]) >= precedence(c))
            {
                postfix[j++] = pop();
            }

            push(c);
        }
    }

    while (top != -1)
        postfix[j++] = pop();

    postfix[j] = '\0';
}

int main()
{
    char infix[100], postfix[100];
    char operands[100][20];
    int operandTop = -1;
    int temp = 1;

    printf("Enter expression: ");
    scanf("%s", infix);

    infixToPostfix(infix, postfix);

    printf("\nPostfix Expression: %s\n", postfix);
    printf("\nThree Address Code:\n");

    for (int i = 0; postfix[i] != '\0'; i++)
    {
        char c = postfix[i];

        if (isalnum(c))
        {
            operands[++operandTop][0] = c;
            operands[operandTop][1] = '\0';
        }
        else
        {
            char op1[20], op2[20], result[20];

            strcpy(op2, operands[operandTop--]);
            strcpy(op1, operands[operandTop--]);

            sprintf(result, "t%d", temp++);

            printf("%s = %s %c %s\n",
                   result, op1, c, op2);

            strcpy(operands[++operandTop], result);
        }
    }

    return 0;
}