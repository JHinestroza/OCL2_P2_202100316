
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDleftMENORMAYORleftMENORIGMAYORIGleftMASMENOSrightUMENOSleftPORDIVIDIDOAND BOOL BREAK CADENA CASE COMA CONSOLE CONTINUE CORDER CORIZQ DECIMAL DEFAULT DIF DIVIDIDO DOSPTS ELSE ENTERO FLOAT FUNC ID IF IGUAL IGUALDAD INDEXOF INTERFACE JOIN LCASE LENGHT LLAVEDER LLAVEIZQ LOG MAS MAYOR MAYORIG MENOR MENORIG MENOS MOD NOT NUMBER OR PARDER PARIZQ PARSEFLOAT PARSEINT POP POR PUNTO PUNTOCOMA PUSH RETURN STRING SWITCH TERN TOSTRING TYPEOF UPCASE VAR WHILEs : blockblock : block instruccion\n            | instruccion instruccion : print\n                | ifinstruction \n                | whileinstruction \n                | declaration\n                | arraydeclaration\n                | assignment\n                | breakstmt\n                | continuestmt\n                | functionstmt\n                | call\n                | returnstmt\n                | interfacecreation\n                | interdeclarationprint : CONSOLE PUNTO LOG PARIZQ expressionList PARDER PUNTOCOMAifinstruction : IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER ELSE LLAVEIZQ block LLAVEDER\n                     | IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER ELSE ifinstruction\n                     | IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDERwhileinstruction : WHILE PARIZQ expression PARDER LLAVEIZQ block LLAVEDERdeclaration : VAR ID DOSPTS type IGUAL expression PUNTOCOMAarraydeclaration : VAR ID DOSPTS type CORIZQ CORDER IGUAL expression PUNTOCOMAinterdeclaration : VAR ID DOSPTS ID IGUAL LLAVEIZQ interfaceContent LLAVEDER PUNTOCOMAinterfaceContent : interfaceContent COMA ID DOSPTS expression\n                | ID DOSPTS expressionassignment : ID IGUAL expression PUNTOCOMAreturnstmt : RETURN expression PUNTOCOMA\n                | RETURN PUNTOCOMAcall : ID PARIZQ expressionList PARDER PUNTOCOMA\n            | ID PARIZQ PARDER PUNTOCOMAfunctionstmt : FUNC ID funcparams functype LLAVEIZQ block LLAVEDERfuncparams : PARIZQ paramsList PARDER\n                |  PARIZQ PARDERinterfacecreation : INTERFACE ID LLAVEIZQ attributeList LLAVEDER PUNTOCOMAattributeList : attributeList ID DOSPTS type PUNTOCOMA\n                | ID DOSPTS type PUNTOCOMAparamsList : paramsList COMA ID DOSPTS type\n                | ID DOSPTS typefunctype : DOSPTS type\n                | breakstmt : BREAK PUNTOCOMAcontinuestmt : CONTINUE PUNTOCOMAtype : NUMBER\n            | FLOAT\n            | STRING\n            | BOOLexpressionList : expressionList COMA expression\n                    | expression expression : expression MAS expression\n                  | expression MENOS expression\n                  | expression POR expression\n                  | expression DIVIDIDO expression\n                  | expression MOD expression     expression : MENOS expression %prec UMENOSexpression : expression MENOR expression\n                  | expression MAYOR expression\n                  | expression MENORIG expression\n                  | expression MAYORIG expressionexpression : expression IGUALDAD expressionexpression : expression DIF expressionexpression : expression AND expressionexpression : expression OR expressionexpression : NOT expressionexpression : PARIZQ expression PARDERexpression :    PARSEINT PARIZQ expression PARDER \n                    | PARSEFLOAT PARIZQ expression PARDER expression : expression TERN expression DOSPTS expressionexpression    : ENTERO\n                    | CADENA\n                    | DECIMAL\n                    | listArrayexpression : CORIZQ expressionList CORDERexpression : ID PARIZQ expressionList PARDER\n            | ID PARIZQ PARDERlistArray : ID CORIZQ expression CORDER\n                | ID'
    
_lr_action_items = {'CONSOLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,61,94,97,127,128,132,134,148,149,153,159,160,161,162,165,167,178,179,181,183,184,186,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-42,-43,-29,-28,-27,-31,17,17,-30,17,17,17,17,-35,-17,-20,-21,-22,-32,17,-19,-24,-23,17,-18,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,61,94,97,127,128,132,134,148,149,153,159,160,161,162,165,167,171,178,179,181,183,184,186,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-42,-43,-29,-28,-27,-31,18,18,-30,18,18,18,18,-35,-17,-20,-21,-22,-32,18,18,-19,-24,-23,18,-18,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,61,94,97,127,128,132,134,148,149,153,159,160,161,162,165,167,178,179,181,183,184,186,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-42,-43,-29,-28,-27,-31,19,19,-30,19,19,19,19,-35,-17,-20,-21,-22,-32,19,-19,-24,-23,19,-18,]),'VAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,61,94,97,127,128,132,134,148,149,153,159,160,161,162,165,167,178,179,181,183,184,186,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-42,-43,-29,-28,-27,-31,20,20,-30,20,20,20,20,-35,-17,-20,-21,-22,-32,20,-19,-24,-23,20,-18,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,24,25,26,27,29,30,32,33,34,35,38,39,40,41,48,54,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,82,83,84,85,94,96,97,125,127,128,130,132,134,137,139,148,149,150,153,159,160,161,162,165,166,167,169,172,174,177,178,179,181,183,184,185,186,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,31,36,49,50,-2,49,49,49,49,-42,-43,-29,49,49,49,49,88,102,-28,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,124,49,-27,49,-31,145,21,21,49,-30,21,154,49,21,21,163,21,-35,-17,-20,-21,-22,49,-32,-37,49,182,-36,21,-19,-24,-23,21,49,-18,]),'BREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,61,94,97,127,128,132,134,148,149,153,159,160,161,162,165,167,178,179,181,183,184,186,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-42,-43,-29,-28,-27,-31,22,22,-30,22,22,22,22,-35,-17,-20,-21,-22,-32,22,-19,-24,-23,22,-18,]),'CONTINUE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,61,94,97,127,128,132,134,148,149,153,159,160,161,162,165,167,178,179,181,183,184,186,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-42,-43,-29,-28,-27,-31,23,23,-30,23,23,23,23,-35,-17,-20,-21,-22,-32,23,-19,-24,-23,23,-18,]),'FUNC':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,61,94,97,127,128,132,134,148,149,153,159,160,161,162,165,167,178,179,181,183,184,186,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-42,-43,-29,-28,-27,-31,24,24,-30,24,24,24,24,-35,-17,-20,-21,-22,-32,24,-19,-24,-23,24,-18,]),'RETURN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,61,94,97,127,128,132,134,148,149,153,159,160,161,162,165,167,178,179,181,183,184,186,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-42,-43,-29,-28,-27,-31,25,25,-30,25,25,25,25,-35,-17,-20,-21,-22,-32,25,-19,-24,-23,25,-18,]),'INTERFACE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,61,94,97,127,128,132,134,148,149,153,159,160,161,162,165,167,178,179,181,183,184,186,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-42,-43,-29,-28,-27,-31,26,26,-30,26,26,26,26,-35,-17,-20,-21,-22,-32,26,-19,-24,-23,26,-18,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,61,94,97,132,159,160,161,162,165,167,179,181,183,186,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-42,-43,-29,-28,-27,-31,-30,-35,-17,-20,-21,-22,-32,-19,-24,-23,-18,]),'LLAVEDER':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,44,45,46,47,49,61,76,77,94,97,103,104,105,106,107,108,109,110,111,112,113,114,115,117,120,122,125,132,140,141,142,143,148,149,153,156,159,160,161,162,164,165,167,169,177,179,180,181,183,184,186,187,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-42,-43,-29,-69,-70,-71,-72,-77,-28,-55,-64,-27,-31,-50,-51,-52,-53,-54,-56,-57,-58,-59,-60,-61,-62,-63,-65,-73,-75,146,-30,-66,-67,-74,-76,161,162,167,-68,-35,-17,-20,-21,173,-22,-32,-37,-36,-19,-26,-24,-23,186,-18,-25,]),'PUNTO':([17,],[28,]),'PARIZQ':([18,19,21,25,29,30,32,33,36,39,40,41,42,43,48,49,51,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,82,83,85,96,130,139,166,172,185,],[29,30,33,41,41,41,41,41,60,41,41,41,79,80,41,82,85,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'IGUAL':([21,88,89,90,91,92,93,152,],[32,129,130,-44,-45,-46,-47,166,]),'PUNTOCOMA':([22,23,25,37,44,45,46,47,49,55,57,76,77,90,91,92,93,95,103,104,105,106,107,108,109,110,111,112,113,114,115,117,120,122,140,141,142,143,146,147,151,156,157,170,173,175,],[34,35,38,61,-69,-70,-71,-72,-77,94,97,-55,-64,-44,-45,-46,-47,132,-50,-51,-52,-53,-54,-56,-57,-58,-59,-60,-61,-62,-63,-65,-73,-75,-66,-67,-74,-76,159,160,165,-68,169,177,181,183,]),'MENOS':([25,29,30,32,33,37,39,40,41,44,45,46,47,48,49,52,53,55,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,85,96,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,130,133,139,140,141,142,143,151,156,166,172,175,180,185,187,],[39,39,39,39,39,63,39,39,39,-69,-70,-71,-72,39,-77,63,63,63,63,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-55,63,63,39,39,39,39,39,39,-50,-51,-52,-53,63,63,63,63,63,63,63,63,63,63,-65,63,63,-73,-75,63,39,63,39,-66,-67,-74,-76,63,63,39,39,63,63,39,63,]),'NOT':([25,29,30,32,33,39,40,41,48,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,82,83,85,96,130,139,166,172,185,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'PARSEINT':([25,29,30,32,33,39,40,41,48,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,82,83,85,96,130,139,166,172,185,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'PARSEFLOAT':([25,29,30,32,33,39,40,41,48,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,82,83,85,96,130,139,166,172,185,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'ENTERO':([25,29,30,32,33,39,40,41,48,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,82,83,85,96,130,139,166,172,185,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'CADENA':([25,29,30,32,33,39,40,41,48,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,82,83,85,96,130,139,166,172,185,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'DECIMAL':([25,29,30,32,33,39,40,41,48,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,82,83,85,96,130,139,166,172,185,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'CORIZQ':([25,29,30,32,33,39,40,41,48,49,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,82,83,85,89,90,91,92,93,96,130,139,166,172,185,],[48,48,48,48,48,48,48,48,48,83,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,131,-44,-45,-46,-47,48,48,48,48,48,48,]),'LOG':([28,],[51,]),'DOSPTS':([31,44,45,46,47,49,59,76,77,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,120,122,124,136,140,141,142,143,145,154,156,163,182,],[54,-69,-70,-71,-72,-77,99,-55,-64,-34,138,-50,-51,-52,-53,-54,-56,-57,-58,-59,-60,-61,-62,-63,139,-65,-73,-75,144,-33,-66,-67,-74,-76,158,168,-68,172,185,]),'PARDER':([33,44,45,46,47,49,52,53,56,58,60,76,77,78,82,90,91,92,93,100,103,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,120,121,122,126,133,140,141,142,143,155,156,176,],[57,-69,-70,-71,-72,-77,86,87,95,-49,101,-55,-64,117,122,-44,-45,-46,-47,136,-50,-51,-52,-53,-54,-56,-57,-58,-59,-60,-61,-62,-63,-65,140,141,-73,142,-75,147,-48,-66,-67,-74,-76,-39,-68,-38,]),'MAS':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[62,-69,-70,-71,-72,-77,62,62,62,62,-55,62,62,-50,-51,-52,-53,62,62,62,62,62,62,62,62,62,62,-65,62,62,-73,-75,62,62,-66,-67,-74,-76,62,62,62,62,62,]),'POR':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[64,-69,-70,-71,-72,-77,64,64,64,64,64,64,64,64,64,-52,-53,64,64,64,64,64,64,64,64,64,64,-65,64,64,-73,-75,64,64,-66,-67,-74,-76,64,64,64,64,64,]),'DIVIDIDO':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[65,-69,-70,-71,-72,-77,65,65,65,65,65,65,65,65,65,-52,-53,65,65,65,65,65,65,65,65,65,65,-65,65,65,-73,-75,65,65,-66,-67,-74,-76,65,65,65,65,65,]),'MOD':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[66,-69,-70,-71,-72,-77,66,66,66,66,-55,66,66,-50,-51,-52,-53,66,-56,-57,-58,-59,66,66,-62,66,66,-65,66,66,-73,-75,66,66,-66,-67,-74,-76,66,66,66,66,66,]),'MENOR':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[67,-69,-70,-71,-72,-77,67,67,67,67,-55,67,67,-50,-51,-52,-53,67,-56,-57,-58,-59,67,67,67,67,67,-65,67,67,-73,-75,67,67,-66,-67,-74,-76,67,67,67,67,67,]),'MAYOR':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[68,-69,-70,-71,-72,-77,68,68,68,68,-55,68,68,-50,-51,-52,-53,68,-56,-57,-58,-59,68,68,68,68,68,-65,68,68,-73,-75,68,68,-66,-67,-74,-76,68,68,68,68,68,]),'MENORIG':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[69,-69,-70,-71,-72,-77,69,69,69,69,-55,69,69,-50,-51,-52,-53,69,69,69,-58,-59,69,69,69,69,69,-65,69,69,-73,-75,69,69,-66,-67,-74,-76,69,69,69,69,69,]),'MAYORIG':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[70,-69,-70,-71,-72,-77,70,70,70,70,-55,70,70,-50,-51,-52,-53,70,70,70,-58,-59,70,70,70,70,70,-65,70,70,-73,-75,70,70,-66,-67,-74,-76,70,70,70,70,70,]),'IGUALDAD':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[71,-69,-70,-71,-72,-77,71,71,71,71,-55,71,71,-50,-51,-52,-53,71,-56,-57,-58,-59,71,71,-62,71,71,-65,71,71,-73,-75,71,71,-66,-67,-74,-76,71,71,71,71,71,]),'DIF':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[72,-69,-70,-71,-72,-77,72,72,72,72,-55,72,72,-50,-51,-52,-53,72,-56,-57,-58,-59,72,72,-62,72,72,-65,72,72,-73,-75,72,72,-66,-67,-74,-76,72,72,72,72,72,]),'AND':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[73,-69,-70,-71,-72,-77,73,73,73,73,-55,73,73,-50,-51,-52,-53,73,-56,-57,-58,-59,73,73,-62,73,73,-65,73,73,-73,-75,73,73,-66,-67,-74,-76,73,73,73,73,73,]),'OR':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[74,-69,-70,-71,-72,-77,74,74,74,74,-55,74,74,-50,-51,-52,-53,74,-56,-57,-58,-59,74,74,-62,74,74,-65,74,74,-73,-75,74,74,-66,-67,-74,-76,74,74,74,74,74,]),'TERN':([37,44,45,46,47,49,52,53,55,58,76,77,78,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,133,140,141,142,143,151,156,175,180,187,],[75,-69,-70,-71,-72,-77,75,75,75,75,-55,75,75,-50,-51,-52,-53,75,-56,-57,-58,-59,75,75,-62,75,75,-65,75,75,-73,-75,75,75,-66,-67,-74,-76,75,75,75,75,75,]),'COMA':([44,45,46,47,49,56,58,76,77,81,90,91,92,93,100,103,104,105,106,107,108,109,110,111,112,113,114,115,117,120,121,122,126,133,140,141,142,143,155,156,164,176,180,187,],[-69,-70,-71,-72,-77,96,-49,-55,-64,96,-44,-45,-46,-47,137,-50,-51,-52,-53,-54,-56,-57,-58,-59,-60,-61,-62,-63,-65,-73,96,-75,96,-48,-66,-67,-74,-76,-39,-68,174,-38,-26,-25,]),'CORDER':([44,45,46,47,49,58,76,77,81,103,104,105,106,107,108,109,110,111,112,113,114,115,117,120,122,123,131,133,140,141,142,143,156,],[-69,-70,-71,-72,-77,-49,-55,-64,120,-50,-51,-52,-53,-54,-56,-57,-58,-59,-60,-61,-62,-63,-65,-73,-75,143,152,-48,-66,-67,-74,-76,-68,]),'LLAVEIZQ':([50,59,86,87,90,91,92,93,98,101,129,135,136,171,],[84,-41,127,128,-44,-45,-46,-47,134,-34,150,-40,-33,178,]),'NUMBER':([54,99,138,144,158,168,],[90,90,90,90,90,90,]),'FLOAT':([54,99,138,144,158,168,],[91,91,91,91,91,91,]),'STRING':([54,99,138,144,158,168,],[92,92,92,92,92,92,]),'BOOL':([54,99,138,144,158,168,],[93,93,93,93,93,93,]),'ELSE':([161,],[171,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'s':([0,],[1,]),'block':([0,127,128,134,178,],[2,148,149,153,184,]),'instruccion':([0,2,127,128,134,148,149,153,178,184,],[3,27,3,3,3,27,27,27,3,27,]),'print':([0,2,127,128,134,148,149,153,178,184,],[4,4,4,4,4,4,4,4,4,4,]),'ifinstruction':([0,2,127,128,134,148,149,153,171,178,184,],[5,5,5,5,5,5,5,5,179,5,5,]),'whileinstruction':([0,2,127,128,134,148,149,153,178,184,],[6,6,6,6,6,6,6,6,6,6,]),'declaration':([0,2,127,128,134,148,149,153,178,184,],[7,7,7,7,7,7,7,7,7,7,]),'arraydeclaration':([0,2,127,128,134,148,149,153,178,184,],[8,8,8,8,8,8,8,8,8,8,]),'assignment':([0,2,127,128,134,148,149,153,178,184,],[9,9,9,9,9,9,9,9,9,9,]),'breakstmt':([0,2,127,128,134,148,149,153,178,184,],[10,10,10,10,10,10,10,10,10,10,]),'continuestmt':([0,2,127,128,134,148,149,153,178,184,],[11,11,11,11,11,11,11,11,11,11,]),'functionstmt':([0,2,127,128,134,148,149,153,178,184,],[12,12,12,12,12,12,12,12,12,12,]),'call':([0,2,127,128,134,148,149,153,178,184,],[13,13,13,13,13,13,13,13,13,13,]),'returnstmt':([0,2,127,128,134,148,149,153,178,184,],[14,14,14,14,14,14,14,14,14,14,]),'interfacecreation':([0,2,127,128,134,148,149,153,178,184,],[15,15,15,15,15,15,15,15,15,15,]),'interdeclaration':([0,2,127,128,134,148,149,153,178,184,],[16,16,16,16,16,16,16,16,16,16,]),'expression':([25,29,30,32,33,39,40,41,48,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,82,83,85,96,130,139,166,172,185,],[37,52,53,55,58,76,77,78,58,103,104,105,106,107,108,109,110,111,112,113,114,115,116,118,119,58,123,58,133,151,156,175,180,187,]),'listArray':([25,29,30,32,33,39,40,41,48,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,82,83,85,96,130,139,166,172,185,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'expressionList':([33,48,82,85,],[56,81,121,126,]),'funcparams':([36,],[59,]),'type':([54,99,138,144,158,168,],[89,135,155,157,170,176,]),'functype':([59,],[98,]),'paramsList':([60,],[100,]),'attributeList':([84,],[125,]),'interfaceContent':([150,],[164,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> s","S'",1,None,None,None),
  ('s -> block','s',1,'p_start','parser.py',226),
  ('block -> block instruccion','block',2,'p_instruction_block','parser.py',230),
  ('block -> instruccion','block',1,'p_instruction_block','parser.py',231),
  ('instruccion -> print','instruccion',1,'p_instruction_list','parser.py',240),
  ('instruccion -> ifinstruction','instruccion',1,'p_instruction_list','parser.py',241),
  ('instruccion -> whileinstruction','instruccion',1,'p_instruction_list','parser.py',242),
  ('instruccion -> declaration','instruccion',1,'p_instruction_list','parser.py',243),
  ('instruccion -> arraydeclaration','instruccion',1,'p_instruction_list','parser.py',244),
  ('instruccion -> assignment','instruccion',1,'p_instruction_list','parser.py',245),
  ('instruccion -> breakstmt','instruccion',1,'p_instruction_list','parser.py',246),
  ('instruccion -> continuestmt','instruccion',1,'p_instruction_list','parser.py',247),
  ('instruccion -> functionstmt','instruccion',1,'p_instruction_list','parser.py',248),
  ('instruccion -> call','instruccion',1,'p_instruction_list','parser.py',249),
  ('instruccion -> returnstmt','instruccion',1,'p_instruction_list','parser.py',250),
  ('instruccion -> interfacecreation','instruccion',1,'p_instruction_list','parser.py',251),
  ('instruccion -> interdeclaration','instruccion',1,'p_instruction_list','parser.py',252),
  ('print -> CONSOLE PUNTO LOG PARIZQ expressionList PARDER PUNTOCOMA','print',7,'p_instruction_console','parser.py',256),
  ('ifinstruction -> IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER ELSE LLAVEIZQ block LLAVEDER','ifinstruction',11,'p_instruction_if_else','parser.py',261),
  ('ifinstruction -> IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER ELSE ifinstruction','ifinstruction',9,'p_instruction_if_else','parser.py',262),
  ('ifinstruction -> IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER','ifinstruction',7,'p_instruction_if_else','parser.py',263),
  ('whileinstruction -> WHILE PARIZQ expression PARDER LLAVEIZQ block LLAVEDER','whileinstruction',7,'p_instruction_while','parser.py',274),
  ('declaration -> VAR ID DOSPTS type IGUAL expression PUNTOCOMA','declaration',7,'p_instruction_declaration','parser.py',279),
  ('arraydeclaration -> VAR ID DOSPTS type CORIZQ CORDER IGUAL expression PUNTOCOMA','arraydeclaration',9,'p_instruction_array_declaration','parser.py',284),
  ('interdeclaration -> VAR ID DOSPTS ID IGUAL LLAVEIZQ interfaceContent LLAVEDER PUNTOCOMA','interdeclaration',9,'p_instruction_interface_declaration','parser.py',289),
  ('interfaceContent -> interfaceContent COMA ID DOSPTS expression','interfaceContent',5,'p_instruction_interface_content','parser.py',294),
  ('interfaceContent -> ID DOSPTS expression','interfaceContent',3,'p_instruction_interface_content','parser.py',295),
  ('assignment -> ID IGUAL expression PUNTOCOMA','assignment',4,'p_instruction_assignment','parser.py',306),
  ('returnstmt -> RETURN expression PUNTOCOMA','returnstmt',3,'p_instruction_return','parser.py',311),
  ('returnstmt -> RETURN PUNTOCOMA','returnstmt',2,'p_instruction_return','parser.py',312),
  ('call -> ID PARIZQ expressionList PARDER PUNTOCOMA','call',5,'p_instruction_call_function','parser.py',320),
  ('call -> ID PARIZQ PARDER PUNTOCOMA','call',4,'p_instruction_call_function','parser.py',321),
  ('functionstmt -> FUNC ID funcparams functype LLAVEIZQ block LLAVEDER','functionstmt',7,'p_instruction_function','parser.py',329),
  ('funcparams -> PARIZQ paramsList PARDER','funcparams',3,'p_instruction_function_params_list','parser.py',334),
  ('funcparams -> PARIZQ PARDER','funcparams',2,'p_instruction_function_params_list','parser.py',335),
  ('interfacecreation -> INTERFACE ID LLAVEIZQ attributeList LLAVEDER PUNTOCOMA','interfacecreation',6,'p_instruction_interface_creation','parser.py',342),
  ('attributeList -> attributeList ID DOSPTS type PUNTOCOMA','attributeList',5,'p_instruction_interface_attribute','parser.py',347),
  ('attributeList -> ID DOSPTS type PUNTOCOMA','attributeList',4,'p_instruction_interface_attribute','parser.py',348),
  ('paramsList -> paramsList COMA ID DOSPTS type','paramsList',5,'p_expression_param_list','parser.py',359),
  ('paramsList -> ID DOSPTS type','paramsList',3,'p_expression_param_list','parser.py',360),
  ('functype -> DOSPTS type','functype',2,'p_instruction_function_type','parser.py',371),
  ('functype -> <empty>','functype',0,'p_instruction_function_type','parser.py',372),
  ('breakstmt -> BREAK PUNTOCOMA','breakstmt',2,'p_instruction_break','parser.py',379),
  ('continuestmt -> CONTINUE PUNTOCOMA','continuestmt',2,'p_instruction_continue','parser.py',384),
  ('type -> NUMBER','type',1,'p_type_prod','parser.py',389),
  ('type -> FLOAT','type',1,'p_type_prod','parser.py',390),
  ('type -> STRING','type',1,'p_type_prod','parser.py',391),
  ('type -> BOOL','type',1,'p_type_prod','parser.py',392),
  ('expressionList -> expressionList COMA expression','expressionList',3,'p_expression_list','parser.py',403),
  ('expressionList -> expression','expressionList',1,'p_expression_list','parser.py',404),
  ('expression -> expression MAS expression','expression',3,'p_expression_binaria','parser.py',414),
  ('expression -> expression MENOS expression','expression',3,'p_expression_binaria','parser.py',415),
  ('expression -> expression POR expression','expression',3,'p_expression_binaria','parser.py',416),
  ('expression -> expression DIVIDIDO expression','expression',3,'p_expression_binaria','parser.py',417),
  ('expression -> expression MOD expression','expression',3,'p_expression_binaria','parser.py',418),
  ('expression -> MENOS expression','expression',2,'p_expresion_unaria','parser.py',427),
  ('expression -> expression MENOR expression','expression',3,'p_expression_Relacionales','parser.py',433),
  ('expression -> expression MAYOR expression','expression',3,'p_expression_Relacionales','parser.py',434),
  ('expression -> expression MENORIG expression','expression',3,'p_expression_Relacionales','parser.py',435),
  ('expression -> expression MAYORIG expression','expression',3,'p_expression_Relacionales','parser.py',436),
  ('expression -> expression IGUALDAD expression','expression',3,'p_expression_igual','parser.py',444),
  ('expression -> expression DIF expression','expression',3,'p_expression_diferente','parser.py',449),
  ('expression -> expression AND expression','expression',3,'p_expression_and','parser.py',454),
  ('expression -> expression OR expression','expression',3,'p_expression_or','parser.py',459),
  ('expression -> NOT expression','expression',2,'p_expression_not','parser.py',465),
  ('expression -> PARIZQ expression PARDER','expression',3,'p_expression_agrupacion','parser.py',470),
  ('expression -> PARSEINT PARIZQ expression PARDER','expression',4,'p_instruction_embebidas','parser.py',475),
  ('expression -> PARSEFLOAT PARIZQ expression PARDER','expression',4,'p_instruction_embebidas','parser.py',476),
  ('expression -> expression TERN expression DOSPTS expression','expression',5,'p_expression_ternario','parser.py',485),
  ('expression -> ENTERO','expression',1,'p_expression_primitiva','parser.py',490),
  ('expression -> CADENA','expression',1,'p_expression_primitiva','parser.py',491),
  ('expression -> DECIMAL','expression',1,'p_expression_primitiva','parser.py',492),
  ('expression -> listArray','expression',1,'p_expression_primitiva','parser.py',493),
  ('expression -> CORIZQ expressionList CORDER','expression',3,'p_expression_array_primitiva','parser.py',497),
  ('expression -> ID PARIZQ expressionList PARDER','expression',4,'p_expression_call_function','parser.py',502),
  ('expression -> ID PARIZQ PARDER','expression',3,'p_expression_call_function','parser.py',503),
  ('listArray -> ID CORIZQ expression CORDER','listArray',4,'p_expression_list_array','parser.py',511),
  ('listArray -> ID','listArray',1,'p_expression_list_array','parser.py',512),
]
