%{
#include <stdio.h>

int keyword_count = 0;
int identifier_count = 0;
%}

%%

"auto"|"break"|"case"|"char"|"const"|"continue"|"default"|"do"|
"double"|"else"|"enum"|"extern"|"float"|"for"|"goto"|"if"|
"int"|"long"|"register"|"return"|"short"|"signed"|"sizeof"|
"static"|"struct"|"switch"|"typedef"|"union"|"unsigned"|
"void"|"volatile"|"while"
{
    printf("Keyword    : %s\n", yytext);
    keyword_count++;
}

[a-zA-Z_][a-zA-Z0-9_]*
{
    printf("Identifier : %s\n", yytext);
    identifier_count++;
}

[ \t\n]+      ;

.             ;

%%

int main()
{
    printf("Enter the C program/code:\n");
    yylex();

    printf("\nTotal Keywords    : %d\n", keyword_count);
    printf("Total Identifiers  : %d\n", identifier_count);

    return 0;
}

int yywrap()
{
    return 1;
}
