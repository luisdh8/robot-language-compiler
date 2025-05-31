%{
#include "robot.tab.h"
#include <stdlib.h>
%}

%%
[Rr]obot                    { return ROBOT; }
[Pp]lease                   { return PLEASE; }

[Mm]ove                     { return MOVE; }
[Tt]urn                     { return TURN; }

[Bb]locks                  { return BLOCKS; }
[Dd]egrees                 { return DEGREES; }

[Aa]head                   { return AHEAD; }

/* Rechazar direcciones no válidas */
[Rr]ight|[Ll]eft|[Bb]ehind { return INVALID_DIRECTION; }

[Aa]nd                     { return AND; }
[Tt]hen                    { return THEN; }
","                        { return COMMA; }

90|180|270|360             { yylval.degree = atoi(yytext); return DEGREE; }
[0-9]+                     { yylval.number = atoi(yytext); return NUMBER; }

[ \t]+                     ; // Espacios ignorados
\n                         { return EOL; }
.                          { return INVALID; }

%%

int yywrap(void) { return 1; }
