%{
#include <stdio.h>

int pos = 0, neg = 0;
%}

%%

-[0-9]+      { neg++; }

[0-9]+       { pos++; }

[ \t\n]+     ;      /* Ignore spaces, tabs, and newlines */

.            ;      /* Ignore other characters */

%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter numbers (Ctrl+Z then Enter to stop):\n");
    yylex();

    printf("\nNumber of positive numbers = %d", pos);
    printf("\nNumber of negative numbers = %d\n", neg);

    return 0;
}