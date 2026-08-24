%{
#include <stdio.h>
%}

%option noyywrap

%%

[0-9]+(\.[0-9]+)?    {
                        printf("%s\n", yytext);
                     }

\"([^\\\"]|\\.)*\"    {
                        printf("%s\n", yytext);
                     }

\'([^\\\']|\\.)*\'    {
                        printf("%s\n", yytext);
                     }

.|\n                 ;

%%

int main()
{
    FILE *fp;

    fp = fopen("exp18.c", "r");

    if (fp == NULL)
    {
        printf("Cannot open sample.c\n");
        return 1;
    }

    yyin = fp;

    printf("Constants in the C program:\n");
    printf("----------------------------\n");

    yylex();

    fclose(fp);

    return 0;
}