#include <stdio.h>
#include <string.h>

int main() {
    char production[100];
    char non_terminal;
    char part1[30] = "", part2[30] = "", remaining[30] = "";
    char prefix[30] = "";
    int i = 0, j = 0, k = 0;

    printf("Enter production (e.g., S->iEtS|iEtSeS|a): ");
    scanf("%s", production);

    non_terminal = production[0];
    i = 3; // Advance past the LHS 'A->' syntax

    // Extract the first alternative up to '|'
    while (production[i] != '|' && production[i] != '\0') {
        part1[j++] = production[i++];
    }
    part1[j] = '\0';

    // Extract the second alternative up to the next '|'
    if (production[i] == '|') {
        i++;
        j = 0;
        while (production[i] != '|' && production[i] != '\0') {
            part2[j++] = production[i++];
        }
        part2[j] = '\0';
    }

    // Extract any remaining terms without the prefix (e.g., '|a')
    if (production[i] == '|') {
        i++;
        j = 0;
        while (production[i] != '\0') {
            remaining[j++] = production[i++];
        }
        remaining[j] = '\0';
    }

    // Calculate the length of the common prefix between part1 and part2
    int len = 0;
    while (part1[len] != '\0' && part2[len] != '\0' && part1[len] == part2[len]) {
        prefix[len] = part1[len];
        len++;
    }
    prefix[len] = '\0';

    printf("\n--- Original Grammar ---\n");
    printf("%s\n", production);

    printf("\n--- After Eliminating Left Factoring ---\n");
    if (len > 0) {
        // Safe string offsets for tracking the suffixes after the common prefix
        char *suffix1 = part1 + len;
        char *suffix2 = part2 + len;

        // If suffix is empty, represent it using epsilon 'e'
        if (strlen(suffix1) == 0) suffix1 = "e";
        if (strlen(suffix2) == 0) suffix2 = "e";

        if (strlen(remaining) > 0) {
            printf("%c -> %s%c' | %s\n", non_terminal, prefix, non_terminal, remaining);
        } else {
            printf("%c -> %s%c'\n", non_terminal, prefix, non_terminal);
        }
        printf("%c' -> %s | %s\n", non_terminal, suffix1, suffix2);
    } else {
        printf("The production rule does not require left factoring.\n");
    }

    return 0;
}
