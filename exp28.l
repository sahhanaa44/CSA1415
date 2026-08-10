%{
#include <stdio.h>
%}

%%
[6-9][0-9]{9}    { printf("mobile number valid\n"); }
[0-9]+           { printf("mobile number invalid\n"); }
\n               { return 0; }
.                ;
%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("enter the mobile number:");
    yylex();
    return 0;
}