#include <stdio.h>

int main()
{
    int n, i;
    char result, op1, op2, operator;

    printf("Enter number of instructions: ");
    scanf("%d", &n);

    printf("Enter TAC instructions:\n");

    for (i = 0; i < n; i++)
    {
        scanf(" %c=%c%c%c",
              &result, &op1, &operator, &op2);

        printf("\nLOAD R1, %c\n", op1);

        switch (operator)
        {
            case '+':
                printf("ADD R1, %c\n", op2);
                break;

            case '-':
                printf("SUB R1, %c\n", op2);
                break;

            case '*':
                printf("MUL R1, %c\n", op2);
                break;

            case '/':
                printf("DIV R1, %c\n", op2);
                break;

            default:
                printf("Invalid operator\n");
                continue;
        }

        printf("STORE %c, R1\n", result);
    }

    return 0;
}