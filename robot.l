%{
#include "robot.tab.h"
#include <stdlib.h>
%}

%%
/* --- Sujeto / nombres del robot --- */
[Rr]obot|[Aa][Ii]|[Tt]hing           { return NOUN; }

/* --- Pronombres personales --- */
[Yy]ou                               { return PRONOUN; }

/* --- Palabras de cortesía / apertura --- */
[Pp]lease |
[Cc]ould[ \t]+[Yy]ou |
[Ww]ould[ \t]+[Yy]ou |
[Kk]indly                             { return COURTESY; }

/* --- Verbos principales --- */
[Mm]ove|[Tt]urn                       { return VERB; }

/* --- Unidades de movimiento / giro --- */
[Bb]locks|[Dd]egrees                  { return UNITS; }

/* --- Direcciones --- */
[Aa]head                              { return VALID_DIRECTION; }
[Rr]ight|[Ll]eft|[Bb]ehind            { return INVALID_DIRECTION; }

/* --- Conectores gramaticales --- */
[Aa]nd                                { return AND; }
[Tt]hen                               { return THEN; }
","                                   { return COMMA; }

/* --- Adverbios opcionales --- */
[Rr]ight[ \t]+[Nn]ow |
[Nn]ow |
[Qq]uickly |
[Ii]mmediately                         { return ADVERBIAL; }

/* --- Números y grados --- */
90|180|270|360                        { yylval.degree = atoi(yytext); return DEGREE; }
[0-9]+                                { yylval.number = atoi(yytext); return NUMBER; }

/* --- Espacios y saltos de línea --- */
[ \t]+                                ;
\n                                    { return EOL; }

/* --- Todo lo no reconocido --- */
.                                     { return INVALID; }

%%

int yywrap(void) { return 1; }