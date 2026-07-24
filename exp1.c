#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isKeyword(char str[])
{
    char keywords[][10] = {
        "int", "float", "char", "double", "if",
        "else", "while", "for", "return", "void"
    };

    int n = 10;

    for (int i = 0; i < n; i++)
    {
        if (strcmp(str, keywords[i]) == 0)
            return 1;
    }
    return 0;
}

int isOperator(char ch)
{
    return (ch == '+' || ch == '-' || ch == '*' ||
            ch == '/' || ch == '=' || ch == '%' ||
            ch == '<' || ch == '>');
}

int isSpecialSymbol(char ch)
{
    return (ch == ';' || ch == ',' || ch == '(' ||
            ch == ')' || ch == '{' || ch == '}');
}

int main()
{
    char input[200];
    char token[50];
    int i = 0, j;

    printf("Enter a C statement:\n");
    fgets(input, sizeof(input), stdin);

    while (input[i] != '\0')
    {
        if (isspace(input[i]))
        {
            i++;
            continue;
        }

        if (isalpha(input[i]) || input[i] == '_')
        {
            j = 0;
            while (isalnum(input[i]) || input[i] == '_')
            {
                token[j++] = input[i++];
            }
            token[j] = '\0';

            if (isKeyword(token))
                printf("%s --> Keyword\n", token);
            else
                printf("%s --> Identifier\n", token);
        }
        else if (isdigit(input[i]))
        {
            j = 0;
            while (isdigit(input[i]) || input[i] == '.')
            {
                token[j++] = input[i++];
            }
            token[j] = '\0';

            printf("%s --> Constant\n", token);
        }
        else if (isOperator(input[i]))
        {
            printf("%c --> Operator\n", input[i]);
            i++;
        }
        else if (isSpecialSymbol(input[i]))
        {
            printf("%c --> Special Symbol\n", input[i]);
            i++;
        }
        else
        {
            i++;
        }
    }

    return 0;
}