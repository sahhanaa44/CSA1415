#include <stdio.h>
#include <ctype.h>
#include <string.h>

int n;
char production[10][10];
char first[10];

void findFirst(char c)
{
    int i, j;

    if (!isupper(c))
    {
        printf("%c ", c);
        return;
    }

    for (i = 0; i < n; i++)
    {
        if (production[i][0] == c)
        {
            if (production[i][2] == '#')
            {
                printf("# ");
            }
            else if (!isupper(production[i][2]))
            {
                printf("%c ", production[i][2]);
            }
            else
            {
                findFirst(production[i][2]);
            }
        }
    }
}

int main()
{
    int i;
    char ch;

    printf("Enter number of productions: ");
    scanf("%d", &n);

    printf("Use # for epsilon\n");
    printf("Enter productions (Example: S=Aa):\n");

    for(i=0;i<n;i++)
        scanf("%s", production[i]);

    printf("\nEnter Non-Terminal to find FIRST: ");
    scanf(" %c",&ch);

    printf("\nFIRST(%c) = { ", ch);
    findFirst(ch);
    printf("}\n");

    return 0;
}