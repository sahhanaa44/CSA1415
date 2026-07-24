#include <stdio.h>
#include <ctype.h>

int main()
{
    char id[100];
    int i = 1, valid = 1;

    printf("Enter an identifier: ");
    scanf("%s", id);

    if (!(isalpha(id[0]) || id[0] == '_'))
        valid = 0;

    while (id[i] != '\0')
    {
        if (!(isalnum(id[i]) || id[i] == '_'))
        {
            valid = 0;
            break;
        }
        i++;
    }

    if (valid)
        printf("%s is a Valid Identifier.\n", id);
    else
        printf("%s is an Invalid Identifier.\n", id);

    return 0;
}