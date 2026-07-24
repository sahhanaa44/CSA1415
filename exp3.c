#include <stdio.h>

int main()
{
    char ch, next;

    printf("Enter the program (Press Ctrl+Z then Enter to stop):\n");

    while ((ch = getchar()) != EOF)
    {
        if (ch == ' ' || ch == '\t' || ch == '\n')
            continue;

        if (ch == '/')
        {
            next = getchar();

            if (next == '/')
            {
                while ((ch = getchar()) != '\n' && ch != EOF);
            }
            else if (next == '*')
            {
                char prev = 0;

                while ((ch = getchar()) != EOF)
                {
                    if (prev == '*' && ch == '/')
                        break;

                    prev = ch;
                }
            }
            else
            {
                printf("%c%c", ch, next);
            }
        }
        else
        {
            printf("%c", ch);
        }
    }

    return 0;
}