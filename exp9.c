#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char production[100];
    char non_terminal;
    char alpha[50] = "", beta[50] = "";
    int i = 0, j = 0, has_recursion = 0;

    printf("Enter production (e.g., L->L,S|S): ");
    scanf("%s", production);

    // Get the LHS non-terminal
    non_terminal = production[0];

    // Verify it uses the '->' format
    if (production[1] != '-' || production[2] != '>') {
        printf("Invalid production format!\n");
        return 1;
    }

    // Step to the start of the RHS options
    i = 3; 

    // Check if the first production option is left-recursive
    if (production[i] == non_terminal) {
        has_recursion = 1;
        i++; // Skip the recursive non-terminal character
        
        // Extract alpha (everything up to the pipe character '|')
        while (production[i] != '|' && production[i] != '\0') {
            alpha[j++] = production[i++];
        }
        alpha[j] = '\0';

        // Check if a alternative beta option exists after '|'
        if (production[i] == '|') {
            i++;
            j = 0;
            while (production[i] != '\0') {
                beta[j++] = production[i++];
            }
            beta[j] = '\0';
        } else {
            strcpy(beta, "e"); // Default to epsilon if no beta is given
        }
    }

    // Display the computed results
    printf("\n--- Original Grammar ---\n");
    printf("%s\n", production);

    printf("\n--- After Eliminating Left Recursion ---\n");
    if (has_recursion) {
        printf("%c -> %s%c'\n", non_terminal, beta, non_terminal);
        printf("%c' -> %s%c' | e\n", non_terminal, alpha, non_terminal);
    } else {
        printf("The production rule is not left-recursive.\n");
    }

    return 0;
}
