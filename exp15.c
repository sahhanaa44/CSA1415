#include <stdio.h>
#include <ctype.h>

int main()
{
    FILE *fp;
    char filename[100];
    char ch, previous = ' ';

    int characters = 0;
    int words = 0;
    int lines = 0;

    printf("Enter file name: ");
    scanf("%s", filename);

    fp = fopen(filename, "r");

    if (fp == NULL)
    {
        printf("Invalid: File cannot be opened.\n");
        return 1;
    }

    while ((ch = fgetc(fp)) != EOF)
    {
        characters++;

        if (ch == '\n')
            lines++;

        if (!isspace(ch) && isspace(previous))
            words++;

        previous = ch;
    }

    fclose(fp);

    printf("\nCharacters = %d\n", characters);
    printf("Words      = %d\n", words);
    printf("Lines      = %d\n", lines);

    return 0;
}