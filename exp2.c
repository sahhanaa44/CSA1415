#include <stdio.h>
#include <string.h>

int main()
{
    char line[500];

    printf("Enter a line:\n");
    fgets(line, sizeof(line), stdin);

    if (strncmp(line, "//", 2) == 0)
    {
        printf("Single-line Comment\n");
    }
    else if (strncmp(line, "/*", 2) == 0)
    {
        if (strstr(line, "*/") != NULL)
        {
            printf("Multi-line Comment\n");
        }
        else
        {
            printf("Beginning of Multi-line Comment\n");
        }
    }
    else
    {
        printf("Not a Comment\n");
    }

    return 0;
}