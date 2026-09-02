%{
#include <stdio.h>
%}

%%

https?:\/\/(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+([\/a-zA-Z0-9._?=&%-]*)?
{
    printf("Valid URL\n");
}

.*  {
    printf("Invalid URL\n");
}

%%

int main()
{
    printf("Enter URL: ");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
