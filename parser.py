import Lexer.py


#Comienza el parser
def Parser(tokens):
    self = {
        'backtrack_id' :0,
        'tokens': tokens,
        'token_index': 0,
    }

def get_token_index():
    return self['token_index']

def set_token_index(newValue):
    self ['token_index'] = newValue
    return newValue

def get_word():
    tokens = self ['tokens']
    token_index = self['token_index']
    return tokens[token_index]

def next_word():
    self ['token_index'] += 1
    return get_word()

#Todo

def eat_word(expected_word):
    if get_word() == expected_word:
            next_word()
            return True
    return False

def get_backtrack_id():
    id = self['backtrack_id']
    self ['backtrack_id'] += 1
    return id

def parse():
    result = S()
    if get_word() != 'eof' or result == None:
        print('Unexpected input termination')
        return definiciones
    return result

def S():
    result = None

    backtrack_id = get_token_index()
    backtrack_id = get_backtrack_id()

    if eat_word('a'):
        s=S()
        if s != None:
            if eat_word('a'):
                return {'type': 'S', 'children' : ['a']}
listaNoTerminales = [
    ()
]
