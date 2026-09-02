%{
#include <stdio.h>
%}

%%

[0-9]+[ ]*\+[ ]*[0-9]+ {
    int a, b;
    sscanf(yytext, "%d + %d", &a, &b);
    printf("Result = %d\n", a + b);
}

[0-9]+[ ]*-[ ]*[0-9]+ {
    int a, b;
    sscanf(yytext, "%d - %d", &a, &b);
    printf("Result = %d\n", a - b);
}

[0-9]+[ ]*\*[ ]*[0-9]+ {
    int a, b;
    sscanf(yytext, "%d * %d", &a, &b);
    printf("Result = %d\n", a * b);
}

[0-9]+[ ]*/[ ]*[0-9]+ {
    int a, b;
    sscanf(yytext, "%d / %d", &a, &b);

    if (b != 0)
        printf("Result = %.2f\n", (float)a / b);
    else
        printf("Division by zero is not allowed\n");
}

[ \t\n]+ ;

. {
    printf("Invalid expression\n");
}

%%

int main()
{
    printf("Enter expression: ");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
