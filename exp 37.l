%{
#include <stdio.h>
#include <string.h>

char target[50];
int count = 0;
%}

%%

[a-zA-Z]+ {
    if (strcmp(yytext, target) == 0)
        count++;
}

[ \t\n]+ ;

. ;

%%

int main()
{
    printf("Enter the word to search: ");
    scanf("%49s", target);

    printf("Enter the sentence:\n");

    yylex();

    printf("Frequency of '%s' = %d\n", target, count);

    return 0;
}

int yywrap()
{
    return 1;
}
