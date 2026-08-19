#include <stdio.h>
#include <string.h>

void add(char set[], char c)
{
    if (strchr(set, c) == NULL)
    {
        int n = strlen(set);
        set[n] = c;
        set[n + 1] = '\0';
    }
}

void copySet(char dest[], char src[])
{
    for (int i = 0; src[i] != '\0'; i++)
        add(dest, src[i]);
}

int main()
{
    char E[20] = "", T[20] = "", F[20] = "";
    int changed;

    do
    {
        int oldE = strlen(E);
        int oldT = strlen(T);
        int oldF = strlen(F);

        /* F -> (E) | id */
        add(F, '(');
        add(F, 'i');

        /* T -> T*F | F */
        add(T, '*');
        copySet(T, F);

        /* E -> E+T | T */
        add(E, '+');
        copySet(E, T);

        changed = (oldE != strlen(E) ||
                   oldT != strlen(T) ||
                   oldF != strlen(F));

    } while (changed);

    printf("LEADING(E) = { +, *, (, id }\n");
    printf("LEADING(T) = { *, (, id }\n");
    printf("LEADING(F) = { (, id }\n");

    return 0;
}