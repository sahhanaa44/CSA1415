%{
#include <stdio.h>

int whitespace = 0;
int newline = 0;
%}

%%

[ \t]      { whitespace++; }   /* Count spaces and tabs */

\n         { newline++; }      /* Count newlines */

.          ;                   /* Ignore other characters */

%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter the input (Ctrl+Z then Enter to stop):\n");
    yylex();

    printf("\nNumber of whitespaces = %d", whitespace);
    printf("\nNumber of newlines = %d\n", newline);

    return 0;
}