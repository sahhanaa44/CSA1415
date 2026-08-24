%{
#include <stdio.h>

int characters = 0;
int lines = 0;
int words = 0;
%}

%option noyywrap

%x COMMENT

%%

"//".*                  ;       /* Ignore single-line comments */

"/*"                    BEGIN(COMMENT);

<COMMENT>"*/"           BEGIN(INITIAL);

<COMMENT>\n             lines++;

<COMMENT>.              ;

\n                      lines++;

[ \t]+                  ;       /* Ignore spaces and tabs */

\"([^\\\"]|\\.)*\"      {
                            characters += yyleng;
                            words++;
                        }

[A-Za-z_][A-Za-z0-9_]*  {
                            characters += yyleng;
                            words++;
                        }

[0-9]+                  {
                            characters += yyleng;
                            words++;
                        }

.                       {
                            characters++;
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

    printf("\nNumber of Characters : %d", characters);
    printf("\nNumber of Lines      : %d", lines);
    printf("\nNumber of Words      : %d\n", words);

    fclose(fp);

    return 0;
}