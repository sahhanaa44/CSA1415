#include <stdio.h>

int main()
{
    char ch;
    int spaces = 0, newlines = 0;

    printf("Enter text (Press Ctrl+Z then Enter to stop):\n");

    while ((ch = getchar()) != EOF)
    {
        if (ch == ' ')
            spaces++;

        if (ch == '\n')
            newlines++;
    }

    printf("\nNumber of Whitespaces = %d\n", spaces);
    printf("Number of Newline Characters = %d\n", newlines);

    return 0;
}