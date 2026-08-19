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
    char E[20] = "";
    char T[20] = "";
    char F[20] = "";

    int changed;

    do
    {
        int oldE = strlen(E);
        int oldT = strlen(T);
        int oldF = strlen(F);

        /* F -> (E) | id */
        add(F, ')');
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

    printf("TRAILING(E) = { +, *, ), id }\n");
    printf("TRAILING(T) = { *, ), id }\n");
    printf("TRAILING(F) = { ), id }\n");

    return 0;
}