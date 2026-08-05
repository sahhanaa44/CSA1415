%{
#include <stdio.h>
%}

%%

[ \t\n]+        ;          /* Ignore spaces, tabs, and newlines */

.               { printf("%s", yytext); }

%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter the code (Press Ctrl+Z then Enter to stop):\n\n");
    yylex();
    return 0;
}