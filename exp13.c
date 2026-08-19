#include <stdio.h>
#include <string.h>
#include <ctype.h>

char input[100];
int pos = 0;

void E();
void Eprime();
void T();
void Tprime();
void F();

void error()
{
    printf("INVALID STRING\n");
    printf("Syntax error at position %d\n", pos + 1);
    exit(0);
}

void E()
{
    T();
    Eprime();
}

void Eprime()
{
    if (input[pos] == '+')
    {
        pos++;
        T();
        Eprime();
    }
}

void T()
{
    F();
    Tprime();
}

void Tprime()
{
    if (input[pos] == '*')
    {
        pos++;
        F();
        Tprime();
    }
}

void F()
{
    if (input[pos] == 'i')
    {
        /* i represents id */
        pos++;
    }
    else if (input[pos] == '(')
    {
        pos++;
        E();

        if (input[pos] == ')')
            pos++;
        else
            error();
    }
    else
    {
        error();
    }
}

int main()
{
    printf("Grammar:\n");
    printf("E  -> T E'\n");
    printf("E' -> + T E' | epsilon\n");
    printf("T  -> F T'\n");
    printf("T' -> * F T' | epsilon\n");
    printf("F  -> (E) | id\n\n");

    printf("Enter expression (use i for id): ");
    scanf("%s", input);

    E();

    if (input[pos] == '\0')
        printf("VALID STRING\n");
    else
        printf("INVALID STRING\n");

    return 0;
}