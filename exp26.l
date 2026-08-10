%{
#include <stdio.h>
%}

%%
[a-zA-Z0-9._]+@[a-zA-Z]+\.(com|in)    { printf("It is valid\n"); }
.+                                    { printf("It is not valid\n"); }
%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter the mail: ");
    yylex();
    return 0;
}