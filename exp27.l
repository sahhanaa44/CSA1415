%{
#include <stdio.h>
%}

%option noyywrap

%%

abc         {
                printf("ABC");
            }

.|\n        {
                printf("%s", yytext);
            }

%%

int main()
{
    printf("Enter a string:\n");
    yylex();

    return 0;
}