%{
#include <stdio.h>
%}

%option noyywrap

%%

"#include"                   { printf("PREPROCESSOR : %s\n", yytext); }

"int"|"float"|"char"|"double"|
"void"|"if"|"else"|"for"|
"while"|"do"|"return"|
"break"|"continue"           {
                                printf("KEYWORD      : %s\n", yytext);
                             }

[0-9]+                       {
                                printf("NUMBER       : %s\n", yytext);
                             }

[A-Za-z_][A-Za-z0-9_]*       {
                                printf("IDENTIFIER   : %s\n", yytext);
                             }

\"([^\\\"]|\\.)*\"            {
                                printf("STRING       : %s\n", yytext);
                             }

"=="|"!="|"<="|">="|
"++"|"--"|"&&"|"||"|
"+"|"-"|"*"|"/"|"="|
"<"|">"                      {
                                printf("OPERATOR     : %s\n", yytext);
                             }

[{}();,\[\]]                  {
                                printf("SPECIAL SYMBOL: %s\n", yytext);
                             }

[ \t\n]+                     ;

.                            {
                                printf("UNKNOWN      : %s\n", yytext);
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
    yylex();

    fclose(fp);

    return 0;
}