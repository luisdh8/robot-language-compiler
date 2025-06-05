%{
#include <stdio.h>
#include <stdlib.h>

FILE *output;
void yyerror(const char *s);
int yylex(void);
%}

%union {
    int number;
    int degree;
}

/* Tokens */
%token <number> NUMBER
%token <degree> DEGREE
%token NOUN PRONOUN COURTESY MOVE_VERB TURN_VERB 
%token BLOCKS DEGREES AHEAD INVALID_DIRECTION
%token AND THEN COMMA ADVERBIAL EOL INVALID

%start input

%%

input:
    /* empty */
    | input line
    ;

line:
    sentence EOL
    | EOL
    | error EOL { yyerrok; }
    ;

sentence:
    command
    {
        fprintf(output, "# Compilation successful.\n");
        printf("✅ Instruction parsed successfully!\n");
    }
    ;

command:
    polite_move
    | polite_turn
    | polite_move connector simple_turn
    | polite_turn connector simple_move
    ;

connector:
    COMMA AND
    | COMMA THEN  
    | AND
    | THEN
    ;

polite_move:
    courtesy_opener MOVE_VERB NUMBER BLOCKS AHEAD
    {
        fprintf(output, "MOV,%d\n", $3);
    }
    | courtesy_opener MOVE_VERB NUMBER BLOCKS AHEAD ADVERBIAL
    {
        fprintf(output, "MOV,%d\n", $3);
    }
    ;

polite_turn:
    courtesy_opener TURN_VERB DEGREE DEGREES
    {
        fprintf(output, "TURN,%d\n", $3);
    }
    | courtesy_opener TURN_VERB DEGREE DEGREES ADVERBIAL
    {
        fprintf(output, "TURN,%d\n", $3);
    }
    ;

simple_move:
    MOVE_VERB NUMBER BLOCKS AHEAD
    {
        fprintf(output, "MOV,%d\n", $2);
    }
    | MOVE_VERB NUMBER BLOCKS AHEAD ADVERBIAL
    {
        fprintf(output, "MOV,%d\n", $2);
    }
    ;

simple_turn:
    TURN_VERB DEGREE DEGREES
    {
        fprintf(output, "TURN,%d\n", $2);
    }
    | TURN_VERB DEGREE DEGREES ADVERBIAL
    {
        fprintf(output, "TURN,%d\n", $2);
    }
    ;

courtesy_opener:
    NOUN COURTESY
    | NOUN COURTESY PRONOUN
    | NOUN COURTESY COURTESY
    | NOUN COURTESY PRONOUN COURTESY
    | COURTESY
    | COURTESY PRONOUN
    | COURTESY COURTESY
    | COURTESY PRONOUN COURTESY
    ;

%%

int main(void) {
    output = fopen("instructions.asm", "w");
    if (!output) {
        perror("Could not open instructions.asm");
        exit(1);
    }

    printf("Robot Language Compiler\n");
    printf("Enter polite instructions (one per line, Ctrl+D to exit):\n");
    printf("Examples:\n");
    printf("  Robot please move 3 blocks ahead\n");
    printf("  Could you move 2 blocks ahead, then turn 90 degrees\n");
    printf("---\n");
    
    yyparse();
    fclose(output);
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "❌ Error: %s\n", s);
    fprintf(stderr, "💡 Try: 'Robot please move 3 blocks ahead'\n");
}