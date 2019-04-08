
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ARR CTEF CTEI CTES EQ GE ID LE NEQ PR_AND PR_BOOL PR_ELSE PR_FALSE PR_FLOAT PR_FUNCTION PR_IF PR_INT PR_MAIN PR_NOT PR_OR PR_PRINT PR_PROGRAM PR_READ PR_REPEAT PR_RETURN PR_STRING PR_TRUE PR_VAR PR_VOID PR_calculaBinomial PR_calculaMedia PR_calculaMediana PR_calculaModa PR_calculaNormal PR_calculaPoisson PR_calculaRegresion PR_prediceResultadoprograma : PR_PROGRAM '{' more_vars more_funcs main '}' vars : PR_VAR ids ids : type ID indexindex : '[' CTEI ']'\n             | '[' CTEI ']' '[' CTEI ']'\n             | empty type : PR_INT\n            | PR_FLOAT\n            | PR_BOOL\n            | PR_STRING func : func1 func2func1 : func1_1 func1_2func1_1 : PR_FUNCTION func_type ID '(' func1_2 : more_ids ')' '{' func2 : more_vars more_bloques '}' more_ids : ids \n                | ids more_ids\n                | empty func_type : type\n                 | PR_VOID bloque : assignation\n              | loop\n              | cond\n              | return\n              | lecture\n              | writing\n              | call  more_vars : vars \n                 | vars more_vars\n                 | empty more_funcs : func\n                  | func more_funcs\n                  | empty more_bloques : bloque\n                    | bloque more_bloques \n                    | empty assignation : assignTo '=' mega_expassignTo : ID other_indexother_index : '[' exp ']'\n                   | '[' exp ']' '[' exp ']'\n                   | empty loop : PR_REPEAT '(' mega_exp ')' '{' more_bloques '}' cond : cond1 cond2cond1 : PR_IF '(' mega_exp ')' '{' cond2 : more_bloques '}' maybe_elsemaybe_else : check_else do_else \n                | emptycheck_else : PR_ELSE '{' do_else : more_bloques '}' return : PR_RETURN mega_exp lecture : PR_READ ARR ID index writing : PR_PRINT '(' mega_exp ')' func_pred : PR_calculaRegresion '(' exp ')'\n                 | PR_prediceResultado '(' exp ')'\n                 | PR_calculaModa '(' exp ')'\n                 | PR_calculaMediana '(' exp ')'\n                 | PR_calculaMedia '(' exp ')' \n                 | PR_calculaPoisson '(' exp ')'\n                 | PR_calculaBinomial '(' exp ')'\n                 | PR_calculaNormal '(' exp ')' call : call_1 call_2 \n            | func_pred call_1 : ID '(' call_2 : exp ')' mega_exp : opt_not super_exp\n                | opt_not super_exp log_op mega_exp log_op : PR_AND\n              | PR_OR\n              | PR_NOT opt_not : PR_NOT\n               | empty super_exp : exp \n                 | exp rel_op super_exp rel_op : '<'\n              | '>'\n              | LE\n              | GE\n              | EQ\n              | NEQ exp : termino\n           | termino '+' exp\n           | termino '-' exp termino : factor\n               | factor '*' termino\n               | factor '/' termino factor : '(' super_exp ')'\n              | '+' var_cte\n              | '-' var_cte\n              | var_cte var_cte : other\n               | CTEI\n               | CTEF\n               | CTES\n               | PR_TRUE\n               | PR_FALSE other : ID other_index\n             | call\n             | empty main : PR_MAIN '{' more_vars more_bloques '}' empty : "
    
_lr_action_items = {'PR_PROGRAM':([0,],[2,]),'$end':([1,34,],[0,-1,]),'{':([2,22,64,145,149,169,],[3,35,113,179,182,186,]),'PR_VAR':([3,5,11,15,26,33,35,67,69,113,143,191,],[7,7,7,-2,-12,-100,7,-3,-6,-14,-4,-5,]),'PR_FUNCTION':([3,4,5,6,9,14,15,24,33,67,69,71,143,191,],[-100,13,-28,-30,13,-29,-2,-11,-100,-3,-6,-15,-4,-5,]),'PR_MAIN':([3,4,5,6,8,9,10,14,15,23,24,33,67,69,71,143,191,],[-100,-100,-28,-30,22,-31,-33,-29,-2,-32,-11,-100,-3,-6,-15,-4,-5,]),'PR_REPEAT':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,54,67,69,70,73,75,77,78,79,80,85,87,89,90,91,92,94,95,96,97,98,99,100,101,102,103,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,186,189,191,192,193,],[-28,-30,-100,-29,-2,47,-12,-100,-100,47,-21,-22,-23,-24,-25,-26,-27,47,-100,-62,-3,-6,47,-100,-43,-50,-100,-70,-71,-41,-61,-80,-100,-100,-83,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-14,-37,-100,-65,-72,-100,-64,-100,-100,-87,-88,-100,-100,-96,-4,-45,47,-47,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,47,-46,-48,-66,-73,-44,-49,-5,-42,-40,]),'PR_RETURN':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,54,67,69,70,73,75,77,78,79,80,85,87,89,90,91,92,94,95,96,97,98,99,100,101,102,103,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,186,189,191,192,193,],[-28,-30,-100,-29,-2,49,-12,-100,-100,49,-21,-22,-23,-24,-25,-26,-27,49,-100,-62,-3,-6,49,-100,-43,-50,-100,-70,-71,-41,-61,-80,-100,-100,-83,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-14,-37,-100,-65,-72,-100,-64,-100,-100,-87,-88,-100,-100,-96,-4,-45,49,-47,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,49,-46,-48,-66,-73,-44,-49,-5,-42,-40,]),'PR_READ':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,54,67,69,70,73,75,77,78,79,80,85,87,89,90,91,92,94,95,96,97,98,99,100,101,102,103,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,186,189,191,192,193,],[-28,-30,-100,-29,-2,50,-12,-100,-100,50,-21,-22,-23,-24,-25,-26,-27,50,-100,-62,-3,-6,50,-100,-43,-50,-100,-70,-71,-41,-61,-80,-100,-100,-83,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-14,-37,-100,-65,-72,-100,-64,-100,-100,-87,-88,-100,-100,-96,-4,-45,50,-47,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,50,-46,-48,-66,-73,-44,-49,-5,-42,-40,]),'PR_PRINT':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,54,67,69,70,73,75,77,78,79,80,85,87,89,90,91,92,94,95,96,97,98,99,100,101,102,103,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,186,189,191,192,193,],[-28,-30,-100,-29,-2,52,-12,-100,-100,52,-21,-22,-23,-24,-25,-26,-27,52,-100,-62,-3,-6,52,-100,-43,-50,-100,-70,-71,-41,-61,-80,-100,-100,-83,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-14,-37,-100,-65,-72,-100,-64,-100,-100,-87,-88,-100,-100,-96,-4,-45,52,-47,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,52,-46,-48,-66,-73,-44,-49,-5,-42,-40,]),'ID':([5,6,11,14,15,16,17,18,19,20,25,26,30,31,32,33,35,37,39,40,41,42,43,44,45,48,49,53,54,67,69,70,73,74,75,77,78,79,80,81,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,185,186,189,191,192,193,],[-28,-30,-100,-29,-2,33,-7,-8,-9,-10,51,-12,66,-19,-20,-100,-100,51,-21,-22,-23,-24,-25,-26,-27,51,-100,101,-62,-3,-6,51,-100,-100,-43,-50,101,-70,-71,122,-63,101,-41,-100,-61,-80,101,101,-83,101,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,101,101,101,101,101,101,101,101,-14,-37,-100,-65,-72,-100,-64,101,101,-87,-88,101,101,-96,-4,-45,51,-47,-100,-67,-68,-69,101,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,51,-46,-48,-66,-73,101,-44,-49,-5,-42,-40,]),'PR_IF':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,54,67,69,70,73,75,77,78,79,80,85,87,89,90,91,92,94,95,96,97,98,99,100,101,102,103,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,186,189,191,192,193,],[-28,-30,-100,-29,-2,55,-12,-100,-100,55,-21,-22,-23,-24,-25,-26,-27,55,-100,-62,-3,-6,55,-100,-43,-50,-100,-70,-71,-41,-61,-80,-100,-100,-83,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-14,-37,-100,-65,-72,-100,-64,-100,-100,-87,-88,-100,-100,-96,-4,-45,55,-47,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,55,-46,-48,-66,-73,-44,-49,-5,-42,-40,]),'PR_calculaRegresion':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,53,54,67,69,70,73,74,75,77,78,79,80,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,185,186,189,191,192,193,],[-28,-30,-100,-29,-2,56,-12,-100,-100,56,-21,-22,-23,-24,-25,-26,-27,56,-100,56,-62,-3,-6,56,-100,-100,-43,-50,56,-70,-71,-63,56,-41,-100,-61,-80,56,56,-83,56,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,56,56,56,56,56,56,56,56,-14,-37,-100,-65,-72,-100,-64,56,56,-87,-88,56,56,-96,-4,-45,56,-47,-100,-67,-68,-69,56,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,56,-46,-48,-66,-73,56,-44,-49,-5,-42,-40,]),'PR_prediceResultado':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,53,54,67,69,70,73,74,75,77,78,79,80,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,185,186,189,191,192,193,],[-28,-30,-100,-29,-2,57,-12,-100,-100,57,-21,-22,-23,-24,-25,-26,-27,57,-100,57,-62,-3,-6,57,-100,-100,-43,-50,57,-70,-71,-63,57,-41,-100,-61,-80,57,57,-83,57,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,57,57,57,57,57,57,57,57,-14,-37,-100,-65,-72,-100,-64,57,57,-87,-88,57,57,-96,-4,-45,57,-47,-100,-67,-68,-69,57,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,57,-46,-48,-66,-73,57,-44,-49,-5,-42,-40,]),'PR_calculaModa':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,53,54,67,69,70,73,74,75,77,78,79,80,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,185,186,189,191,192,193,],[-28,-30,-100,-29,-2,58,-12,-100,-100,58,-21,-22,-23,-24,-25,-26,-27,58,-100,58,-62,-3,-6,58,-100,-100,-43,-50,58,-70,-71,-63,58,-41,-100,-61,-80,58,58,-83,58,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,58,58,58,58,58,58,58,58,-14,-37,-100,-65,-72,-100,-64,58,58,-87,-88,58,58,-96,-4,-45,58,-47,-100,-67,-68,-69,58,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,58,-46,-48,-66,-73,58,-44,-49,-5,-42,-40,]),'PR_calculaMediana':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,53,54,67,69,70,73,74,75,77,78,79,80,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,185,186,189,191,192,193,],[-28,-30,-100,-29,-2,59,-12,-100,-100,59,-21,-22,-23,-24,-25,-26,-27,59,-100,59,-62,-3,-6,59,-100,-100,-43,-50,59,-70,-71,-63,59,-41,-100,-61,-80,59,59,-83,59,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,59,59,59,59,59,59,59,59,-14,-37,-100,-65,-72,-100,-64,59,59,-87,-88,59,59,-96,-4,-45,59,-47,-100,-67,-68,-69,59,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,59,-46,-48,-66,-73,59,-44,-49,-5,-42,-40,]),'PR_calculaMedia':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,53,54,67,69,70,73,74,75,77,78,79,80,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,185,186,189,191,192,193,],[-28,-30,-100,-29,-2,60,-12,-100,-100,60,-21,-22,-23,-24,-25,-26,-27,60,-100,60,-62,-3,-6,60,-100,-100,-43,-50,60,-70,-71,-63,60,-41,-100,-61,-80,60,60,-83,60,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,60,60,60,60,60,60,60,60,-14,-37,-100,-65,-72,-100,-64,60,60,-87,-88,60,60,-96,-4,-45,60,-47,-100,-67,-68,-69,60,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,60,-46,-48,-66,-73,60,-44,-49,-5,-42,-40,]),'PR_calculaPoisson':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,53,54,67,69,70,73,74,75,77,78,79,80,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,185,186,189,191,192,193,],[-28,-30,-100,-29,-2,61,-12,-100,-100,61,-21,-22,-23,-24,-25,-26,-27,61,-100,61,-62,-3,-6,61,-100,-100,-43,-50,61,-70,-71,-63,61,-41,-100,-61,-80,61,61,-83,61,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,61,61,61,61,61,61,61,61,-14,-37,-100,-65,-72,-100,-64,61,61,-87,-88,61,61,-96,-4,-45,61,-47,-100,-67,-68,-69,61,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,61,-46,-48,-66,-73,61,-44,-49,-5,-42,-40,]),'PR_calculaBinomial':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,53,54,67,69,70,73,74,75,77,78,79,80,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,185,186,189,191,192,193,],[-28,-30,-100,-29,-2,62,-12,-100,-100,62,-21,-22,-23,-24,-25,-26,-27,62,-100,62,-62,-3,-6,62,-100,-100,-43,-50,62,-70,-71,-63,62,-41,-100,-61,-80,62,62,-83,62,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,62,62,62,62,62,62,62,62,-14,-37,-100,-65,-72,-100,-64,62,62,-87,-88,62,62,-96,-4,-45,62,-47,-100,-67,-68,-69,62,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,62,-46,-48,-66,-73,62,-44,-49,-5,-42,-40,]),'PR_calculaNormal':([5,6,11,14,15,25,26,33,35,37,39,40,41,42,43,44,45,48,49,53,54,67,69,70,73,74,75,77,78,79,80,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,117,119,120,121,122,125,126,127,128,129,130,131,133,143,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,182,183,184,185,186,189,191,192,193,],[-28,-30,-100,-29,-2,63,-12,-100,-100,63,-21,-22,-23,-24,-25,-26,-27,63,-100,63,-62,-3,-6,63,-100,-100,-43,-50,63,-70,-71,-63,63,-41,-100,-61,-80,63,63,-83,63,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,63,63,63,63,63,63,63,63,-14,-37,-100,-65,-72,-100,-64,63,63,-87,-88,63,63,-96,-4,-45,63,-47,-100,-67,-68,-69,63,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,63,-46,-48,-66,-73,63,-44,-49,-5,-42,-40,]),'}':([5,6,11,14,15,21,25,26,33,35,36,37,38,39,40,41,42,43,44,45,48,49,54,67,69,70,72,73,75,76,77,78,79,80,85,87,89,90,91,92,94,95,96,97,98,99,100,101,102,103,113,116,117,119,120,121,122,125,126,127,128,129,130,131,133,143,144,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,172,173,174,175,176,177,179,180,181,182,183,184,186,188,189,191,192,193,],[-28,-30,-100,-29,-2,34,-100,-12,-100,-100,71,-34,-36,-21,-22,-23,-24,-25,-26,-27,-100,-100,-62,-3,-6,-100,-35,-100,-43,119,-50,-100,-70,-71,-41,-61,-80,-100,-100,-83,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-14,144,-37,-100,-65,-72,-100,-64,-100,-100,-87,-88,-100,-100,-96,-4,-99,-45,-100,-47,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-51,-39,-52,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,-100,-46,189,-48,-66,-73,-44,192,-49,-5,-42,-40,]),'PR_INT':([7,12,13,28,33,67,69,114,143,191,],[17,17,17,17,-100,-3,-6,-13,-4,-5,]),'PR_FLOAT':([7,12,13,28,33,67,69,114,143,191,],[18,18,18,18,-100,-3,-6,-13,-4,-5,]),'PR_BOOL':([7,12,13,28,33,67,69,114,143,191,],[19,19,19,19,-100,-3,-6,-13,-4,-5,]),'PR_STRING':([7,12,13,28,33,67,69,114,143,191,],[20,20,20,20,-100,-3,-6,-13,-4,-5,]),')':([12,27,28,29,33,53,54,65,67,69,74,78,79,80,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,118,120,121,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,150,151,152,153,154,155,156,157,158,159,160,162,164,165,166,167,168,170,171,172,173,174,175,176,177,183,184,191,193,],[-100,64,-16,-18,-100,-100,-62,-17,-3,-6,-100,-100,-70,-71,-63,-41,-100,-61,125,-80,-100,-100,-83,-100,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,-100,-100,-100,-100,-100,-100,-100,-100,-13,145,-65,-72,163,-64,-100,-100,-87,-88,-100,-100,168,-96,169,170,171,172,173,174,175,176,177,-4,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-39,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,-66,-73,-5,-40,]),'PR_VOID':([13,],[32,]),'[':([33,51,101,122,143,162,],[68,84,84,68,178,185,]),'=':([46,51,82,85,162,193,],[73,-100,-38,-41,-39,-40,]),'(':([47,49,51,52,53,55,56,57,58,59,60,61,62,63,66,73,74,78,79,80,83,84,86,93,101,104,105,106,107,108,109,110,111,112,126,127,130,131,150,151,152,153,154,155,156,157,158,159,160,185,],[74,-100,83,86,93,104,105,106,107,108,109,110,111,112,114,-100,-100,93,-70,-71,-63,93,-100,93,83,-100,93,93,93,93,93,93,93,93,93,93,93,93,-100,-67,-68,-69,93,-74,-75,-76,-77,-78,-79,93,]),'PR_NOT':([49,54,73,74,78,79,80,85,86,87,89,90,91,92,94,95,96,97,98,99,100,101,102,103,104,120,121,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,164,165,166,167,168,170,171,172,173,174,175,176,177,184,193,],[79,-62,79,79,-100,-70,-71,-41,79,-61,-80,-100,-100,-83,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,79,153,-72,-64,-100,-100,-87,-88,-100,-100,-96,79,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-39,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,-73,-40,]),'+':([49,53,54,73,74,78,79,80,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,166,167,168,170,171,172,173,174,175,176,177,185,193,],[-100,90,-62,-100,-100,90,-70,-71,-63,90,-41,-100,-61,126,-100,-100,-83,90,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,90,90,90,90,90,90,90,90,-64,90,90,-87,-88,90,90,-96,-100,-67,-68,-69,90,-74,-75,-76,-77,-78,-79,-39,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,90,-40,]),'-':([49,53,54,73,74,78,79,80,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,166,167,168,170,171,172,173,174,175,176,177,185,193,],[-100,91,-62,-100,-100,91,-70,-71,-63,91,-41,-100,-61,127,-100,-100,-83,91,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,91,91,91,91,91,91,91,91,-64,91,91,-87,-88,91,91,-96,-100,-67,-68,-69,91,-74,-75,-76,-77,-78,-79,-39,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,91,-40,]),'CTEI':([49,53,68,73,74,78,79,80,83,84,86,90,91,93,104,105,106,107,108,109,110,111,112,126,127,130,131,150,151,152,153,154,155,156,157,158,159,160,178,185,],[-100,96,115,-100,-100,96,-70,-71,-63,96,-100,96,96,96,-100,96,96,96,96,96,96,96,96,96,96,96,96,-100,-67,-68,-69,96,-74,-75,-76,-77,-78,-79,187,96,]),'CTEF':([49,53,73,74,78,79,80,83,84,86,90,91,93,104,105,106,107,108,109,110,111,112,126,127,130,131,150,151,152,153,154,155,156,157,158,159,160,185,],[-100,97,-100,-100,97,-70,-71,-63,97,-100,97,97,97,-100,97,97,97,97,97,97,97,97,97,97,97,97,-100,-67,-68,-69,97,-74,-75,-76,-77,-78,-79,97,]),'CTES':([49,53,73,74,78,79,80,83,84,86,90,91,93,104,105,106,107,108,109,110,111,112,126,127,130,131,150,151,152,153,154,155,156,157,158,159,160,185,],[-100,98,-100,-100,98,-70,-71,-63,98,-100,98,98,98,-100,98,98,98,98,98,98,98,98,98,98,98,98,-100,-67,-68,-69,98,-74,-75,-76,-77,-78,-79,98,]),'PR_TRUE':([49,53,73,74,78,79,80,83,84,86,90,91,93,104,105,106,107,108,109,110,111,112,126,127,130,131,150,151,152,153,154,155,156,157,158,159,160,185,],[-100,99,-100,-100,99,-70,-71,-63,99,-100,99,99,99,-100,99,99,99,99,99,99,99,99,99,99,99,99,-100,-67,-68,-69,99,-74,-75,-76,-77,-78,-79,99,]),'PR_FALSE':([49,53,73,74,78,79,80,83,84,86,90,91,93,104,105,106,107,108,109,110,111,112,126,127,130,131,150,151,152,153,154,155,156,157,158,159,160,185,],[-100,100,-100,-100,100,-70,-71,-63,100,-100,100,100,100,-100,100,100,100,100,100,100,100,100,100,100,100,100,-100,-67,-68,-69,100,-74,-75,-76,-77,-78,-79,100,]),'PR_AND':([49,54,73,74,78,79,80,85,86,87,89,90,91,92,94,95,96,97,98,99,100,101,102,103,104,120,121,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,164,165,166,167,168,170,171,172,173,174,175,176,177,184,193,],[-100,-62,-100,-100,-100,-70,-71,-41,-100,-61,-80,-100,-100,-83,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,151,-72,-64,-100,-100,-87,-88,-100,-100,-96,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-39,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,-73,-40,]),'PR_OR':([49,54,73,74,78,79,80,85,86,87,89,90,91,92,94,95,96,97,98,99,100,101,102,103,104,120,121,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,164,165,166,167,168,170,171,172,173,174,175,176,177,184,193,],[-100,-62,-100,-100,-100,-70,-71,-41,-100,-61,-80,-100,-100,-83,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,152,-72,-64,-100,-100,-87,-88,-100,-100,-96,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-39,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,-73,-40,]),'<':([49,54,73,74,78,79,80,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,121,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,164,165,166,167,168,170,171,172,173,174,175,176,177,193,],[-100,-62,-100,-100,-100,-70,-71,-41,-100,-61,-80,-100,-100,-83,-100,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,155,-64,-100,-100,-87,-88,-100,-100,-96,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-39,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,-40,]),'>':([49,54,73,74,78,79,80,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,121,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,164,165,166,167,168,170,171,172,173,174,175,176,177,193,],[-100,-62,-100,-100,-100,-70,-71,-41,-100,-61,-80,-100,-100,-83,-100,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,156,-64,-100,-100,-87,-88,-100,-100,-96,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-39,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,-40,]),'LE':([49,54,73,74,78,79,80,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,121,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,164,165,166,167,168,170,171,172,173,174,175,176,177,193,],[-100,-62,-100,-100,-100,-70,-71,-41,-100,-61,-80,-100,-100,-83,-100,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,157,-64,-100,-100,-87,-88,-100,-100,-96,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-39,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,-40,]),'GE':([49,54,73,74,78,79,80,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,121,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,164,165,166,167,168,170,171,172,173,174,175,176,177,193,],[-100,-62,-100,-100,-100,-70,-71,-41,-100,-61,-80,-100,-100,-83,-100,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,158,-64,-100,-100,-87,-88,-100,-100,-96,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-39,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,-40,]),'EQ':([49,54,73,74,78,79,80,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,121,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,164,165,166,167,168,170,171,172,173,174,175,176,177,193,],[-100,-62,-100,-100,-100,-70,-71,-41,-100,-61,-80,-100,-100,-83,-100,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,159,-64,-100,-100,-87,-88,-100,-100,-96,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-39,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,-40,]),'NEQ':([49,54,73,74,78,79,80,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,121,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,164,165,166,167,168,170,171,172,173,174,175,176,177,193,],[-100,-62,-100,-100,-100,-70,-71,-41,-100,-61,-80,-100,-100,-83,-100,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,160,-64,-100,-100,-87,-88,-100,-100,-96,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-39,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,-40,]),'*':([49,53,54,73,74,78,79,80,83,84,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,168,170,171,172,173,174,175,176,177,185,193,],[-100,-100,-62,-100,-100,-100,-70,-71,-63,-100,-41,-100,-61,-100,-100,130,-100,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,-100,-100,-100,-100,-100,-100,-100,-100,-64,-100,-100,-87,-88,-100,-100,-96,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-39,-86,-53,-54,-55,-56,-57,-58,-59,-60,-100,-40,]),'/':([49,53,54,73,74,78,79,80,83,84,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,125,126,127,128,129,130,131,133,150,151,152,153,154,155,156,157,158,159,160,162,168,170,171,172,173,174,175,176,177,185,193,],[-100,-100,-62,-100,-100,-100,-70,-71,-63,-100,-41,-100,-61,-100,-100,131,-100,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,-100,-100,-100,-100,-100,-100,-100,-100,-100,-64,-100,-100,-87,-88,-100,-100,-96,-100,-67,-68,-69,-100,-74,-75,-76,-77,-78,-79,-39,-86,-53,-54,-55,-56,-57,-58,-59,-60,-100,-40,]),'ARR':([50,],[81,]),']':([54,84,85,87,89,90,91,92,94,95,96,97,98,99,100,101,102,103,115,123,125,126,127,128,129,130,131,133,162,164,165,166,167,168,170,171,172,173,174,175,176,177,185,187,190,193,],[-62,-100,-41,-61,-80,-100,-100,-83,-89,-90,-91,-92,-93,-94,-95,-100,-97,-98,143,162,-64,-100,-100,-87,-88,-100,-100,-96,-39,-81,-82,-84,-85,-86,-53,-54,-55,-56,-57,-58,-59,-60,-100,191,193,-40,]),'PR_ELSE':([119,],[149,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'more_vars':([3,5,11,35,],[4,14,25,70,]),'vars':([3,5,11,35,],[5,5,5,5,]),'empty':([3,4,5,9,11,12,25,28,33,35,37,48,49,51,53,70,73,74,78,84,86,90,91,93,101,104,105,106,107,108,109,110,111,112,119,122,126,127,130,131,147,150,154,179,185,],[6,10,6,10,6,29,38,29,69,6,38,38,80,85,103,38,80,80,103,103,80,103,103,103,85,80,103,103,103,103,103,103,103,103,148,69,103,103,103,103,38,80,103,38,103,]),'more_funcs':([4,9,],[8,23,]),'func':([4,9,],[9,9,]),'func1':([4,9,],[11,11,]),'func1_1':([4,9,],[12,12,]),'ids':([7,12,28,],[15,28,28,]),'type':([7,12,13,28,],[16,16,31,16,]),'main':([8,],[21,]),'func2':([11,],[24,]),'func1_2':([12,],[26,]),'more_ids':([12,28,],[27,65,]),'func_type':([13,],[30,]),'more_bloques':([25,37,48,70,147,179,],[36,72,76,116,181,188,]),'bloque':([25,37,48,70,147,179,],[37,37,37,37,37,37,]),'assignation':([25,37,48,70,147,179,],[39,39,39,39,39,39,]),'loop':([25,37,48,70,147,179,],[40,40,40,40,40,40,]),'cond':([25,37,48,70,147,179,],[41,41,41,41,41,41,]),'return':([25,37,48,70,147,179,],[42,42,42,42,42,42,]),'lecture':([25,37,48,70,147,179,],[43,43,43,43,43,43,]),'writing':([25,37,48,70,147,179,],[44,44,44,44,44,44,]),'call':([25,37,48,53,70,78,84,90,91,93,105,106,107,108,109,110,111,112,126,127,130,131,147,154,179,185,],[45,45,45,102,45,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,45,102,45,102,]),'assignTo':([25,37,48,70,147,179,],[46,46,46,46,46,46,]),'cond1':([25,37,48,70,147,179,],[48,48,48,48,48,48,]),'call_1':([25,37,48,53,70,78,84,90,91,93,105,106,107,108,109,110,111,112,126,127,130,131,147,154,179,185,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'func_pred':([25,37,48,53,70,78,84,90,91,93,105,106,107,108,109,110,111,112,126,127,130,131,147,154,179,185,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'index':([33,122,],[67,161,]),'cond2':([48,],[75,]),'mega_exp':([49,73,74,86,104,150,],[77,117,118,124,134,183,]),'opt_not':([49,73,74,86,104,150,],[78,78,78,78,78,78,]),'other_index':([51,101,],[82,133,]),'call_2':([53,],[87,]),'exp':([53,78,84,93,105,106,107,108,109,110,111,112,126,127,154,185,],[88,121,123,121,135,136,137,138,139,140,141,142,164,165,121,190,]),'termino':([53,78,84,93,105,106,107,108,109,110,111,112,126,127,130,131,154,185,],[89,89,89,89,89,89,89,89,89,89,89,89,89,89,166,167,89,89,]),'factor':([53,78,84,93,105,106,107,108,109,110,111,112,126,127,130,131,154,185,],[92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,]),'var_cte':([53,78,84,90,91,93,105,106,107,108,109,110,111,112,126,127,130,131,154,185,],[94,94,94,128,129,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,]),'other':([53,78,84,90,91,93,105,106,107,108,109,110,111,112,126,127,130,131,154,185,],[95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,]),'super_exp':([78,93,154,],[120,132,184,]),'maybe_else':([119,],[146,]),'check_else':([119,],[147,]),'log_op':([120,],[150,]),'rel_op':([121,],[154,]),'do_else':([147,],[180,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PR_PROGRAM { more_vars more_funcs main }','programa',6,'p_programa','scan_par.py',377),
  ('vars -> PR_VAR ids','vars',2,'p_vars','scan_par.py',381),
  ('ids -> type ID index','ids',3,'p_ids','scan_par.py',384),
  ('index -> [ CTEI ]','index',3,'p_index','scan_par.py',387),
  ('index -> [ CTEI ] [ CTEI ]','index',6,'p_index','scan_par.py',388),
  ('index -> empty','index',1,'p_index','scan_par.py',389),
  ('type -> PR_INT','type',1,'p_type','scan_par.py',392),
  ('type -> PR_FLOAT','type',1,'p_type','scan_par.py',393),
  ('type -> PR_BOOL','type',1,'p_type','scan_par.py',394),
  ('type -> PR_STRING','type',1,'p_type','scan_par.py',395),
  ('func -> func1 func2','func',2,'p_func','scan_par.py',400),
  ('func1 -> func1_1 func1_2','func1',2,'p_func1','scan_par.py',403),
  ('func1_1 -> PR_FUNCTION func_type ID (','func1_1',4,'p_func1_1','scan_par.py',407),
  ('func1_2 -> more_ids ) {','func1_2',3,'p_func1_2','scan_par.py',411),
  ('func2 -> more_vars more_bloques }','func2',3,'p_func2','scan_par.py',414),
  ('more_ids -> ids','more_ids',1,'p_more_ids','scan_par.py',419),
  ('more_ids -> ids more_ids','more_ids',2,'p_more_ids','scan_par.py',420),
  ('more_ids -> empty','more_ids',1,'p_more_ids','scan_par.py',421),
  ('func_type -> type','func_type',1,'p_func_type','scan_par.py',424),
  ('func_type -> PR_VOID','func_type',1,'p_func_type','scan_par.py',425),
  ('bloque -> assignation','bloque',1,'p_bloque','scan_par.py',428),
  ('bloque -> loop','bloque',1,'p_bloque','scan_par.py',429),
  ('bloque -> cond','bloque',1,'p_bloque','scan_par.py',430),
  ('bloque -> return','bloque',1,'p_bloque','scan_par.py',431),
  ('bloque -> lecture','bloque',1,'p_bloque','scan_par.py',432),
  ('bloque -> writing','bloque',1,'p_bloque','scan_par.py',433),
  ('bloque -> call','bloque',1,'p_bloque','scan_par.py',434),
  ('more_vars -> vars','more_vars',1,'p_more_vars','scan_par.py',437),
  ('more_vars -> vars more_vars','more_vars',2,'p_more_vars','scan_par.py',438),
  ('more_vars -> empty','more_vars',1,'p_more_vars','scan_par.py',439),
  ('more_funcs -> func','more_funcs',1,'p_more_funcs','scan_par.py',442),
  ('more_funcs -> func more_funcs','more_funcs',2,'p_more_funcs','scan_par.py',443),
  ('more_funcs -> empty','more_funcs',1,'p_more_funcs','scan_par.py',444),
  ('more_bloques -> bloque','more_bloques',1,'p_more_bloques','scan_par.py',447),
  ('more_bloques -> bloque more_bloques','more_bloques',2,'p_more_bloques','scan_par.py',448),
  ('more_bloques -> empty','more_bloques',1,'p_more_bloques','scan_par.py',449),
  ('assignation -> assignTo = mega_exp','assignation',3,'p_assignation','scan_par.py',452),
  ('assignTo -> ID other_index','assignTo',2,'p_assignTo','scan_par.py',455),
  ('other_index -> [ exp ]','other_index',3,'p_other_index','scan_par.py',458),
  ('other_index -> [ exp ] [ exp ]','other_index',6,'p_other_index','scan_par.py',459),
  ('other_index -> empty','other_index',1,'p_other_index','scan_par.py',460),
  ('loop -> PR_REPEAT ( mega_exp ) { more_bloques }','loop',7,'p_loop','scan_par.py',463),
  ('cond -> cond1 cond2','cond',2,'p_cond','scan_par.py',467),
  ('cond1 -> PR_IF ( mega_exp ) {','cond1',5,'p_cond1','scan_par.py',470),
  ('cond2 -> more_bloques } maybe_else','cond2',3,'p_cond2','scan_par.py',473),
  ('maybe_else -> check_else do_else','maybe_else',2,'p_maybe_else','scan_par.py',476),
  ('maybe_else -> empty','maybe_else',1,'p_maybe_else','scan_par.py',477),
  ('check_else -> PR_ELSE {','check_else',2,'p_checkElse','scan_par.py',480),
  ('do_else -> more_bloques }','do_else',2,'p_do_else','scan_par.py',483),
  ('return -> PR_RETURN mega_exp','return',2,'p_return','scan_par.py',486),
  ('lecture -> PR_READ ARR ID index','lecture',4,'p_lecture','scan_par.py',489),
  ('writing -> PR_PRINT ( mega_exp )','writing',4,'p_writing','scan_par.py',492),
  ('func_pred -> PR_calculaRegresion ( exp )','func_pred',4,'p_func_pred','scan_par.py',495),
  ('func_pred -> PR_prediceResultado ( exp )','func_pred',4,'p_func_pred','scan_par.py',496),
  ('func_pred -> PR_calculaModa ( exp )','func_pred',4,'p_func_pred','scan_par.py',497),
  ('func_pred -> PR_calculaMediana ( exp )','func_pred',4,'p_func_pred','scan_par.py',498),
  ('func_pred -> PR_calculaMedia ( exp )','func_pred',4,'p_func_pred','scan_par.py',499),
  ('func_pred -> PR_calculaPoisson ( exp )','func_pred',4,'p_func_pred','scan_par.py',500),
  ('func_pred -> PR_calculaBinomial ( exp )','func_pred',4,'p_func_pred','scan_par.py',501),
  ('func_pred -> PR_calculaNormal ( exp )','func_pred',4,'p_func_pred','scan_par.py',502),
  ('call -> call_1 call_2','call',2,'p_call','scan_par.py',505),
  ('call -> func_pred','call',1,'p_call','scan_par.py',506),
  ('call_1 -> ID (','call_1',2,'p_call_1','scan_par.py',510),
  ('call_2 -> exp )','call_2',2,'p_call_2','scan_par.py',513),
  ('mega_exp -> opt_not super_exp','mega_exp',2,'p_mega_exp','scan_par.py',516),
  ('mega_exp -> opt_not super_exp log_op mega_exp','mega_exp',4,'p_mega_exp','scan_par.py',517),
  ('log_op -> PR_AND','log_op',1,'p_log_op','scan_par.py',520),
  ('log_op -> PR_OR','log_op',1,'p_log_op','scan_par.py',521),
  ('log_op -> PR_NOT','log_op',1,'p_log_op','scan_par.py',522),
  ('opt_not -> PR_NOT','opt_not',1,'p_opt_not','scan_par.py',525),
  ('opt_not -> empty','opt_not',1,'p_opt_not','scan_par.py',526),
  ('super_exp -> exp','super_exp',1,'p_super_exp','scan_par.py',530),
  ('super_exp -> exp rel_op super_exp','super_exp',3,'p_super_exp','scan_par.py',531),
  ('rel_op -> <','rel_op',1,'p_rel_op','scan_par.py',534),
  ('rel_op -> >','rel_op',1,'p_rel_op','scan_par.py',535),
  ('rel_op -> LE','rel_op',1,'p_rel_op','scan_par.py',536),
  ('rel_op -> GE','rel_op',1,'p_rel_op','scan_par.py',537),
  ('rel_op -> EQ','rel_op',1,'p_rel_op','scan_par.py',538),
  ('rel_op -> NEQ','rel_op',1,'p_rel_op','scan_par.py',539),
  ('exp -> termino','exp',1,'p_exp','scan_par.py',542),
  ('exp -> termino + exp','exp',3,'p_exp','scan_par.py',543),
  ('exp -> termino - exp','exp',3,'p_exp','scan_par.py',544),
  ('termino -> factor','termino',1,'p_termino','scan_par.py',547),
  ('termino -> factor * termino','termino',3,'p_termino','scan_par.py',548),
  ('termino -> factor / termino','termino',3,'p_termino','scan_par.py',549),
  ('factor -> ( super_exp )','factor',3,'p_factor','scan_par.py',552),
  ('factor -> + var_cte','factor',2,'p_factor','scan_par.py',553),
  ('factor -> - var_cte','factor',2,'p_factor','scan_par.py',554),
  ('factor -> var_cte','factor',1,'p_factor','scan_par.py',555),
  ('var_cte -> other','var_cte',1,'p_var_cte','scan_par.py',558),
  ('var_cte -> CTEI','var_cte',1,'p_var_cte','scan_par.py',559),
  ('var_cte -> CTEF','var_cte',1,'p_var_cte','scan_par.py',560),
  ('var_cte -> CTES','var_cte',1,'p_var_cte','scan_par.py',561),
  ('var_cte -> PR_TRUE','var_cte',1,'p_var_cte','scan_par.py',562),
  ('var_cte -> PR_FALSE','var_cte',1,'p_var_cte','scan_par.py',563),
  ('other -> ID other_index','other',2,'p_other','scan_par.py',566),
  ('other -> call','other',1,'p_other','scan_par.py',567),
  ('other -> empty','other',1,'p_other','scan_par.py',568),
  ('main -> PR_MAIN { more_vars more_bloques }','main',5,'p_main','scan_par.py',571),
  ('empty -> <empty>','empty',0,'p_empty','scan_par.py',574),
]
