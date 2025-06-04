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

%token <number> NUMBER
%token <degree> DEGREE

%token NOUN PRONOUN
%token VERB
%token UNITS
%token COURTESY
%token VALID_DIRECTION INVALID_DIRECTION
%token AND THEN COMMA
%token ADVERBIAL
%token EOL
%token INVALID

%start sentence

%%

sentence:
    command_sequence EOL         { fprintf(output, "# Compilation successful.\n"); }
    ;

command_sequence:
    polite_command
    | command_sequence optional_comma AND polite_command
    | command_sequence optional_comma THEN polite_command
    | command_sequence optional_comma AND optional_comma THEN polite_command
    ;

optional_comma:
    /* vacío */
    | COMMA
    ;

polite_command:
    opener action
    ;

opener:
    NOUN courtesy_block
    | courtesy_block PRONOUN
    | courtesy_block
    | NOUN
    ;

courtesy_block:
    COURTESY
    | COURTESY COURTESY
    ;

action:
    move_command
    | turn_command
    ;

move_command:
    VERB NUMBER UNITS VALID_DIRECTION optional_adverb
        { fprintf(output, "MOV,%d\n", $2); }
    ;

turn_command:
    VERB DEGREE UNITS optional_adverb
        { fprintf(output, "TURN,%d\n", $2); }
    ;

optional_adverb:
    /* vacío */
    | ADVERBIAL
    ;

%%

int main(void) {
    output = fopen("instructions.asm", "w");
    if (!output) {
        perror("Could not open instructions.asm");
        exit(1);
    }

    printf("Enter a polite instruction to the robot:\n");
    yyparse();
    fclose(output);
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "❌ Syntax error: %s\n", s);
}
