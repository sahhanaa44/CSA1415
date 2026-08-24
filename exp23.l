%{
#include <stdio.h>

int line = 1;
%}

%option noyywrap

%%

\n              {
                    printf("\n%4d  ", ++line);
                }

.               {
                    printf("%s", yytext);
                }

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

    printf("%4d  ", line);
    yylex();

    fclose(fp);

    return 0;
}