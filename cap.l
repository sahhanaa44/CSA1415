%{
#include <stdio.h>
%}

%%
[A-Z]+      { printf("%s", yytext); }
.           ;
%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter string:\n");
    yylex();
    return 0;
}