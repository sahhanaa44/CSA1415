#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 20

struct Symbol {
    char name[10];
    char type[10];
    int address;
    struct Symbol* next;
};

struct Symbol* hashTable[SIZE];

int hash(char* name) {
    int sum = 0;
    for (int i = 0; name[i] != '\0'; i++) {
        sum += name[i];
    }
    return sum % SIZE;
}

void insert() {
    struct Symbol* sym = (struct Symbol*)malloc(sizeof(struct Symbol));
    printf("Enter variable name: ");
    scanf("%s", sym->name);
    printf("Enter data type: ");
    scanf("%s", sym->type);
    printf("Enter memory address: ");
    scanf("%d", &sym->address);
    sym->next = NULL;

    int index = hash(sym->name);
    if (hashTable[index] == NULL) {
        hashTable[index] = sym;
    } else {
        struct Symbol* temp = hashTable[index];
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = sym;
    }
    printf("Symbol inserted successfully!\n");
}

void search() {
    char name[10];
    printf("Enter variable name to search: ");
    scanf("%s", name);
    
    int index = hash(name);
    struct Symbol* temp = hashTable[index];
    while (temp != NULL) {
        if (strcmp(temp->name, name) == 0) {
            printf("Found! Type: %s, Address: %d\n", temp->type, temp->address);
            return;
        }
        temp = temp->next;
    }
    printf("Symbol not found.\n");
}

void display() {
    printf("\n--- Symbol Table ---\n");
    printf("%-10s %-10s %-10s\n", "Name", "Type", "Address");
    for (int i = 0; i < SIZE; i++) {
        struct Symbol* temp = hashTable[i];
        while (temp != NULL) {
            printf("%-10s %-10s %-10d\n", temp->name, temp->type, temp->address);
            temp = temp->next;
        }
    }
}

int main() {
    int choice;
    for (int i = 0; i < SIZE; i++) hashTable[i] = NULL;

    while (1) {
        printf("\n1. Insert  2. Search  3. Display  4. Exit\nEnter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1: insert(); break;
            case 2: search(); break;
            case 3: display(); break;
            case 4: exit(0);
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}
