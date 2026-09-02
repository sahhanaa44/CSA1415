%{
#include <stdio.h>
#include <string.h>

int max_length = 0;
char longest[100];
%}

%%

[a-zA-Z]+ {
    if (strlen(yytext) > max_length)
    {
        max_length = strlen(yytext);
        strcpy(longest, yytext);
    }
}

[ \t\n]+ ;

. ;

%%

int main()
{
    printf("Enter a sentence:\n");
    yylex();

    printf("Longest word = %s\n", longest);
    printf("Length = %d\n", max_length);

    return 0;
}

int yywrap()
{
    return 1;
}
