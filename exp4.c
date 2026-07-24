#include <stdio.h>

int main()
{
    char op;

    printf("Enter an operator: ");
    scanf("%c", &op);

    if (op == '+' || op == '-' || op == '*' || op == '/')
    {
        printf("%c is a Valid Arithmetic Operator.\n", op);
    }
    else
    {
        printf("%c is NOT a Valid Arithmetic Operator.\n", op);
    }

    return 0;
}