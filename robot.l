%{
#include "robot.tab.h"
#include <stdlib.h>
%}

%%

[Rr]obot|[Aa][Ii]|[Tt]hing                  { return NOUN; }
[Yy]ou                                      { return PRONOUN; }
[Cc]ould|[Ww]ould|[Ss]hould|[Pp]lease|[Kk]indly   { return COURTESY; }
[Mm]ove                                     { return MOVE_VERB; }
[Tt]urn                                     { return TURN_VERB; }
[Bb]locks                                   { return BLOCKS; }
[Dd]egrees                                  { return DEGREES; }
[Aa]head                                    { return AHEAD; }
[Rr]ight|[Ll]eft|[Bb]ehind                  { return INVALID_DIRECTION; }
[Aa]nd                                      { return AND; }
[Tt]hen                                     { return THEN; }
","                                         { return COMMA; }
[Rr]ight[ \t]+[Nn]ow|[Nn]ow|[Qq]uickly|[Ii]mmediately { return ADVERBIAL; }
90|180|270|360                              { yylval.degree = atoi(yytext); return DEGREE; }
[0-9]+                                      { yylval.number = atoi(yytext); return NUMBER; }
[ \t]+                                      ;
\n                                          { return EOL; }
.                                           { return INVALID; }

%%

int yywrap(void) { return 1; }