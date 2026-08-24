%{
#include <stdio.h>

int vowels = 0;
%}

%option noyywrap

%%

[AEIOUaeiou]    {
                    vowels++;
                }

.|\n            ;

%%

int main()
{
    printf("Enter a sentence:\n");

    yylex();

    printf("\nNumber of vowels = %d\n", vowels);

    return 0;
}