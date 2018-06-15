from Lexer import tokenizer

def test (cadenaPrueba, resultadoEsperado):
    result = tokenizer(cadenaPrueba)
    print 'Cadena de prueba: "'+cadenaPrueba+'"'
    print 'Resultado lexer:', result
    print 'Resultado esper:', resultadoEsperado
    if (result == resultadoEsperado):
        print "\033[92mOK"
    else:
        print "\033[91mFALLO"
    print '\033[0m'


test("if", [('Cond', 'if')])
test(" if  ", [('Cond', 'if')])
test("if(", [('Cond', 'if'), ('ParOp', '(')])
test("while ==(", [('Loop', 'while'), ('OpRel', '=='), ('ParOp', '(')])
test("whileif", [('id', 'whileif')])
test("if(while", [('Cond', 'if'), ('ParOp', '('), ('Loop', 'while')])
test("1234", [('number', '1234')])
test("123asd", "Error")
test("if [ *", "Error")
test(" (  ]", "Error")
test("===", "")
test("<= == <", [('OpRel', '<='), ('OpRel', '=='), ('OpRel', '<')])