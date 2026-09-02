%{
#include <stdio.h>
%}

%%

[0-9] {
    printf("The given input is a digit\n");
}

. {
    printf("The given input is not a digit\n");
}

%%

int main()
{
    printf("Enter a character: ");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
