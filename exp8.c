#include<stdio.h>
#include<ctype.h>
#include<string.h>

int count, n = 0;
char calc_first[10][100];
char calc_follow[10][100];
char production[10][10];
char first[10], follow[10];
int m = 0;

void findFirst(char, int, int);
void findFollow(char);
void followFirst(char, int, int);

int main()
{
    int jm = 0, km = 0, i, choice;
    char c, ch;

    printf("Enter the number of productions: ");
    scanf("%d", &count);

    printf("Enter the productions (Example: S=AB):\n");
    for(i = 0; i < count; i++)
        scanf("%s", production[i]);

    do
    {
        m = 0;
        printf("\nEnter the Non-Terminal to find FOLLOW: ");
        scanf(" %c", &c);

        findFollow(c);

        printf("\nFOLLOW(%c) = { ", c);

        for(i = 0; i < m; i++)
            printf("%c ", follow[i]);

        printf("}\n");

        printf("\nDo you want to continue? (1/0): ");
        scanf("%d", &choice);

    } while(choice == 1);

    return 0;
}

void findFirst(char c, int q1, int q2)
{
    int j;

    if(!(isupper(c)))
    {
        first[n++] = c;
    }

    for(j = 0; j < count; j++)
    {
        if(production[j][0] == c)
        {
            if(production[j][2] == '#')
            {
                if(production[q1][q2] == '\0')
                    first[n++] = '#';
                else if(production[q1][q2] != '\0')
                    findFirst(production[q1][q2], q1, q2 + 1);
            }
            else if(!isupper(production[j][2]))
            {
                first[n++] = production[j][2];
            }
            else
            {
                findFirst(production[j][2], j, 3);
            }
        }
    }
}

void findFollow(char c)
{
    int i, j;

    if(production[0][0] == c)
        follow[m++] = '$';

    for(i = 0; i < count; i++)
    {
        for(j = 2; j < strlen(production[i]); j++)
        {
            if(production[i][j] == c)
            {
                if(production[i][j + 1] != '\0')
                {
                    followFirst(production[i][j + 1], i, j + 2);
                }

                if(production[i][j + 1] == '\0' && c != production[i][0])
                {
                    findFollow(production[i][0]);
                }
            }
        }
    }
}

void followFirst(char c, int c1, int c2)
{
    int k;

    if(!(isupper(c)))
    {
        follow[m++] = c;
    }
    else
    {
        n = 0;
        findFirst(c, c1, c2);

        for(k = 0; k < n; k++)
        {
            if(first[k] == '#')
            {
                if(production[c1][c2] == '\0')
                    findFollow(production[c1][0]);
                else
                    followFirst(production[c1][c2], c1, c2 + 1);
            }
            else
            {
                follow[m++] = first[k];
            }
        }
    }
}