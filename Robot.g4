grammar Robot;

// Regla principal
program: (instruction EOL?)* EOF;

instruction: 
    polite_command
    | compound_command
    ;

compound_command:
    polite_move connector polite_turn
    | polite_turn connector polite_move
    ;

connector:
    COMMA? (AND | THEN)
    ;

polite_command:
    polite_move
    | polite_turn
    ;

polite_move:
    courtesy_opener? MOVE_VERB NUMBER BLOCKS AHEAD adverbial?
    ;

polite_turn:
    courtesy_opener? TURN_VERB DEGREE DEGREES adverbial?
    ;

courtesy_opener:
    (NOUN | PRONOUN | COURTESY)+
    ;

adverbial:
    ADVERBIAL
    ;

// Tokens
NOUN: [Rr][Oo][Bb][Oo][Tt] | [Aa][Ii] | [Tt][Hh][Ii][Nn][Gg];
PRONOUN: [Yy][Oo][Uu];
COURTESY: [Cc][Oo][Uu][Ll][Dd] | [Ww][Oo][Uu][Ll][Dd] | [Ss][Hh][Oo][Uu][Ll][Dd] | [Pp][Ll][Ee][Aa][Ss][Ee] | [Kk][Ii][Nn][Dd][Ll][Yy];
MOVE_VERB: [Mm][Oo][Vv][Ee];
TURN_VERB: [Tt][Uu][Rr][Nn];
BLOCKS: [Bb][Ll][Oo][Cc][Kk][Ss]?;
DEGREES: [Dd][Ee][Gg][Rr][Ee][Ee][Ss]?;
AHEAD: [Aa][Hh][Ee][Aa][Dd];
AND: [Aa][Nn][Dd];
THEN: [Tt][Hh][Ee][Nn];
COMMA: ',';
ADVERBIAL: [Rr][Ii][Gg][Hh][Tt] WS+ [Nn][Oo][Ww] | [Nn][Oo][Ww] | [Qq][Uu][Ii][Cc][Kk][Ll][Yy] | [Ii][Mm][Mm][Ee][Dd][Ii][Aa][Tt][Ee][Ll][Yy];
DEGREE: '90' | '180' | '270' | '360';
NUMBER: [0-9]+;
WS: [ \t]+ -> skip;
EOL: '\r'? '\n';
INVALID: .;