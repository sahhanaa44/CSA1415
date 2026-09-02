%{
#include <stdio.h>
#include <string.h>

char oldword[50];
char newword[50];
%}

%%

[a-zA-Z]+ {
    if (strcmp(yytext, oldword) == 0)
        printf("%s", newword);
    else
        printf("%s", yytext);
}

. {
    printf("%s", yytext);
}

%%

int main()
{
    printf("Enter word to replace: ");
    scanf("%49s", oldword);

    printf("Enter new word: ");
    scanf("%49s", newword);

    printf("\nModified file contents:\n");

    yylex();

    return 0;
}

int yywrap()
{
    return 1;
}
