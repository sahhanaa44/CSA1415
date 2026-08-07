#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_TYPE_LENGTH 50

/* ---------------------------------------------------------
   Structure used to store the internal representation
   of a type expression.
   --------------------------------------------------------- */
typedef struct
{
    char original[MAX_TYPE_LENGTH];
    char baseType[20];
    int pointerLevel;
    int valid;
} TypeDescriptor;


/* ---------------------------------------------------------
   Remove spaces from the input type.
   Example:
       "int * *"  ->  "int**"
   --------------------------------------------------------- */
void removeSpaces(char input[])
{
    int i, j = 0;

    for (i = 0; input[i] != '\0'; i++)
    {
        if (!isspace((unsigned char)input[i]))
        {
            input[j++] = input[i];
        }
    }

    input[j] = '\0';
}


/* ---------------------------------------------------------
   Identify the base type.
   --------------------------------------------------------- */
int identifyBaseType(char type[], char baseType[])
{
    if (strncmp(type, "int", 3) == 0)
    {
        strcpy(baseType, "int");
        return 3;
    }

    if (strncmp(type, "float", 5) == 0)
    {
        strcpy(baseType, "float");
        return 5;
    }

    if (strncmp(type, "char", 4) == 0)
    {
        strcpy(baseType, "char");
        return 4;
    }

    if (strncmp(type, "double", 6) == 0)
    {
        strcpy(baseType, "double");
        return 6;
    }

    return -1;
}


/* ---------------------------------------------------------
   Parse the complete type expression.

   Example:
       int**  -> base = int, pointerLevel = 2
       float* -> base = float, pointerLevel = 1
   --------------------------------------------------------- */
TypeDescriptor parseType(char input[])
{
    TypeDescriptor descriptor;

    int position;
    int baseLength;

    strcpy(descriptor.original, input);

    descriptor.pointerLevel = 0;
    descriptor.valid = 0;
    strcpy(descriptor.baseType, "invalid");

    /* Remove spaces */
    removeSpaces(input);

    /* Identify base type */
    baseLength = identifyBaseType(input, descriptor.baseType);

    if (baseLength == -1)
    {
        return descriptor;
    }

    position = baseLength;

    /* Count pointer symbols */
    while (input[position] != '\0')
    {
        if (input[position] == '*')
        {
            descriptor.pointerLevel++;
        }
        else
        {
            /* Any character other than * is invalid */
            descriptor.valid = 0;
            return descriptor;
        }

        position++;
    }

    descriptor.valid = 1;

    return descriptor;
}


/* ---------------------------------------------------------
   Display a separator.
   --------------------------------------------------------- */
void printLine()
{
    printf("====================================================\n");
}


/* ---------------------------------------------------------
   Display the internal representation of a type.
   --------------------------------------------------------- */
void displayDescriptor(TypeDescriptor type, char name[])
{
    printf("\n%s TYPE DESCRIPTOR\n", name);
    printf("---------------------------------------------\n");

    printf("Original Type       : %s\n", type.original);
    printf("Base Type           : %s\n", type.baseType);
    printf("Pointer Depth       : %d\n", type.pointerLevel);

    if (type.pointerLevel == 0)
    {
        printf("Type Category       : Basic Type\n");
    }
    else
    {
        printf("Type Category       : Pointer Type\n");
    }
}


/* ---------------------------------------------------------
   Compare base types.
   --------------------------------------------------------- */
int compareBaseTypes(TypeDescriptor type1,
                     TypeDescriptor type2)
{
    printf("\n[CHECK 1] Comparing Base Types...\n");

    printf("Type A Base : %s\n", type1.baseType);
    printf("Type B Base : %s\n", type2.baseType);

    if (strcmp(type1.baseType, type2.baseType) == 0)
    {
        printf("Base Type Result : MATCH\n");
        return 1;
    }

    printf("Base Type Result : MISMATCH\n");

    return 0;
}


/* ---------------------------------------------------------
   Compare pointer levels.
   --------------------------------------------------------- */
int comparePointerLevels(TypeDescriptor type1,
                         TypeDescriptor type2)
{
    printf("\n[CHECK 2] Comparing Pointer Levels...\n");

    printf("Type A Pointer Depth : %d\n",
           type1.pointerLevel);

    printf("Type B Pointer Depth : %d\n",
           type2.pointerLevel);

    if (type1.pointerLevel == type2.pointerLevel)
    {
        printf("Pointer Level Result : MATCH\n");
        return 1;
    }

    printf("Pointer Level Result : MISMATCH\n");

    return 0;
}


/* ---------------------------------------------------------
   Perform complete structural equivalence checking.
   --------------------------------------------------------- */
int checkEquivalence(TypeDescriptor type1,
                     TypeDescriptor type2)
{
    int baseMatch;
    int pointerMatch;

    printf("\n");
    printLine();
    printf("        STRUCTURAL EQUIVALENCE ANALYSIS\n");
    printLine();

    baseMatch = compareBaseTypes(type1, type2);

    pointerMatch = comparePointerLevels(type1, type2);

    printf("\n[FINAL ANALYSIS]\n");

    if (baseMatch && pointerMatch)
    {
        printf("Base Types       : MATCH\n");
        printf("Pointer Depth    : MATCH\n");

        return 1;
    }

    printf("Base Types       : %s\n",
           baseMatch ? "MATCH" : "MISMATCH");

    printf("Pointer Depth    : %s\n",
           pointerMatch ? "MATCH" : "MISMATCH");

    return 0;
}


/* ---------------------------------------------------------
   Explain the result in compiler terminology.
   --------------------------------------------------------- */
void displayResult(TypeDescriptor type1,
                   TypeDescriptor type2,
                   int equivalent)
{
    printf("\n");
    printLine();
    printf("                 SEMANTIC RESULT\n");
    printLine();

    printf("\nType A : %s\n", type1.original);
    printf("Type B : %s\n", type2.original);

    printf("\n");

    if (equivalent)
    {
        printf("RESULT: TYPES ARE EQUIVALENT\n");

        printf("\nReason:\n");
        printf("1. Both types have the same base type.\n");
        printf("2. Both types have the same pointer depth.\n");
        printf("3. Therefore, their type structures match.\n");

        printf("\nSemantic Analysis:\n");
        printf("\"%s\" and \"%s\" represent the same\n",
               type1.original, type2.original);

        printf("type structure under this equivalence rule.\n");
    }
    else
    {
        printf("RESULT: TYPES ARE NOT EQUIVALENT\n");

        printf("\nReason:\n");

        if (strcmp(type1.baseType, type2.baseType) != 0)
        {
            printf("- Base types are different.\n");
        }

        if (type1.pointerLevel != type2.pointerLevel)
        {
            printf("- Pointer depths are different.\n");
        }

        printf("\nSemantic Analysis:\n");
        printf("The internal type structures do not match.\n");
    }

    printLine();
}


/* ---------------------------------------------------------
   MAIN PROGRAM
   --------------------------------------------------------- */
int main()
{
    char input1[MAX_TYPE_LENGTH];
    char input2[MAX_TYPE_LENGTH];

    TypeDescriptor typeA;
    TypeDescriptor typeB;

    int equivalent;

    printf("\n");
    printLine();
    printf("          TYPE EQUIVALENCE CHECKER\n");
    printf("             SEMANTIC ANALYSIS\n");
    printLine();

    printf("\nSupported base types:\n");
    printf("int, float, char, double\n");

    printf("\nExamples:\n");
    printf("int       -> Basic type\n");
    printf("int*      -> Pointer depth 1\n");
    printf("int**     -> Pointer depth 2\n");
    printf("float***  -> Pointer depth 3\n");

    printLine();

    /* -----------------------------------------------------
       INPUT PHASE
       ----------------------------------------------------- */

    printf("\nINPUT PHASE\n");
    printf("---------------------------------------------\n");

    printf("Enter Type A: ");
    fgets(input1, MAX_TYPE_LENGTH, stdin);

    printf("Enter Type B: ");
    fgets(input2, MAX_TYPE_LENGTH, stdin);

    /* Remove newline */
    input1[strcspn(input1, "\n")] = '\0';
    input2[strcspn(input2, "\n")] = '\0';

    /* -----------------------------------------------------
       PARSING PHASE
       ----------------------------------------------------- */

    printf("\n");
    printLine();
    printf("                PARSING PHASE\n");
    printLine();

    typeA = parseType(input1);
    typeB = parseType(input2);

    if (!typeA.valid || !typeB.valid)
    {
        printf("\nError: Invalid type expression.\n");

        if (!typeA.valid)
            printf("Type A is invalid.\n");

        if (!typeB.valid)
            printf("Type B is invalid.\n");

        return 0;
    }

    printf("\nType A successfully parsed.\n");
    printf("Type B successfully parsed.\n");

    /* -----------------------------------------------------
       INTERNAL REPRESENTATION
       ----------------------------------------------------- */

    displayDescriptor(typeA, "TYPE A");
    displayDescriptor(typeB, "TYPE B");

    /* -----------------------------------------------------
       EQUIVALENCE CHECK
       ----------------------------------------------------- */

    equivalent = checkEquivalence(typeA, typeB);

    /* -----------------------------------------------------
       FINAL RESULT
       ----------------------------------------------------- */

    displayResult(typeA, typeB, equivalent);

    return 0;
}