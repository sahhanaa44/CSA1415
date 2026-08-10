%{
#include <stdio.h>

FILE *yyin, *yyout;
%}

%%

"<"[^>]*">"      { fprintf(yyout, "%s\n", yytext); }

.|\n             ;

%%

int yywrap()
{
    return 1;
}

int main()
{
    yyin = fopen("sample.html", "r");
    if (yyin == NULL)
    {
        printf("Error: Cannot open sample.html\n");
        return 1;
    }

    yyout = fopen("output.txt", "w");
    if (yyout == NULL)
    {
        printf("Error: Cannot create output.txt\n");
        fclose(yyin);
        return 1;
    }

    yylex();

    fclose(yyin);
    fclose(yyout);

    printf("HTML tags extracted successfully.\n");

    return 0;
}