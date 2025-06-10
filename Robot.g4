grammar Robot;

// Regla principal
program: (polite_command (connector polite_command)* EOL?)* EOF;

polite_command: polite_move | polite_turn;

polite_move:
	courtesy_opener? MOVE_VERB NUMBER (BLOCKS | BLOCK)? AHEAD? adverbial?;

polite_turn:
	courtesy_opener? TURN_VERB DEGREE (DEGREES | DEGREEWORD)? adverbial?;

courtesy_opener: (NOUN | PRONOUN | COURTESY)+;

adverbial: ADVERBIAL;

connector:
	COMMA? AND THEN	# AndThenConnector
	| COMMA? AND	# AndConnector
	| COMMA? THEN	# ThenConnector
	| COMMA			# CommaConnector;

// Tokens
NOUN:
	[Rr][Oo][Bb][Oo][Tt]
	| [Aa][Ii]
	| [Tt][Hh][Ii][Nn][Gg];
PRONOUN: [Yy][Oo][Uu];
COURTESY:
	[Cc][Oo][Uu][Ll][Dd]
	| [Ww][Oo][Uu][Ll][Dd]
	| [Ss][Hh][Oo][Uu][Ll][Dd]
	| [Pp][Ll][Ee][Aa][Ss][Ee]
	| [Kk][Ii][Nn][Dd][Ll][Yy];
MOVE_VERB: [Mm][Oo][Vv][Ee];
TURN_VERB: [Tt][Uu][Rr][Nn];
BLOCKS: [Bb][Ll][Oo][Cc][Kk][Ss];
BLOCK: [Bb][Ll][Oo][Cc][Kk];
DEGREES: [Dd][Ee][Gg][Rr][Ee][Ee][Ss];
DEGREEWORD: [Dd][Ee][Gg][Rr][Ee][Ee];
AHEAD: [Aa][Hh][Ee][Aa][Dd];
AND: [Aa][Nn][Dd];
THEN: [Tt][Hh][Ee][Nn];
COMMA: ',';
ADVERBIAL:
	[Rr][Ii][Gg][Hh][Tt] WS+ [Nn][Oo][Ww]
	| [Nn][Oo][Ww]
	| [Qq][Uu][Ii][Cc][Kk][Ll][Yy]
	| [Ii][Mm][Mm][Ee][Dd][Ii][Aa][Tt][Ee][Ll][Yy];
DEGREE: '90' | '180' | '270' | '360';
NUMBER: [0-9]+;
WS: [ \t]+ -> skip;
EOL: '\r'? '\n';
ERROR_CHAR: . -> channel(HIDDEN);