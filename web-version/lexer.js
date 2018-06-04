function Automata (
    token,
    estados = [],
    alfabeto = [],
    estadoInicial = '',
    funcionTransicion = () => {},
    estadosAceptados = []
) {
    this.token = token;
    this.estados = estados;
    this.alfabeto = alfabeto; //Esta variable esta aca nomas por la definicion de automata pero actualmente no se usa
    this.estadoInicial = estadoInicial;
    this.funcionTransicion = funcionTransicion;
    this.estadosAceptados = estadosAceptados;
    this.estadoActual = estadoInicial;

    this.input = function (input) {
        this.estadoActual = this.funcionTransicion(input);
    }

    this.isActualAceptado = function () {
        return this.estadosAceptados.includes(this.estadoActual);
    }

    this.reset = function () {
        this.estadoActual = this.estadoInicial;
    }

    this.isTrampa = function () {
        return this.estadoActual === null;
    }
}

var Helpers = Helpers || {

    isAlphaNumeric (str) {
      for (let i = 0; i < str.length; ++i) {
        let code = str.charCodeAt(i);
        if (!(code > 47 && code < 58) // numeric (0-9)
            && !(code > 64 && code < 91) // upper alpha (A-Z)
            && !(code > 96 && code < 123) // lower alpha (a-z)
        ) {
          return false;
        }
      }
      return true;
    },

    isSpace (str) {
        return str.trim() === '';
    },
};

var Lexer = Lexer || (function () {
    let self;
    let automatas = [];
    let buffer = '';
    let tokens = [];

    return {

        init (definiciones) {
            self = this;
            self.createAutomatas(definiciones);
        },

        main (src) {
            try {
                src += ' ';
                let allTrampas;
                let line = 1;
                let position = -1;
                let aceptados = [];
                tokens = [];
                self.resetAutomatas();
                for (x in src) {
                    if (src[x] === '\n') {
                        ++line;
                        position = -1;
                    }
                    if (buffer === '' && Helpers.isSpace(src[x])) continue;
                    allTrampas = true;
                    let nuevosAceptados = []
                    automatas.forEach(
                        (automata) => { 
                            automata.input(src[x]);
                            allTrampas = allTrampas && automata.isTrampa();
                            if (automata.isActualAceptado()) {
                                nuevosAceptados.push(automata);
                            }
                        }
                    );
 
                    if (allTrampas && buffer !== '') {
                        if (aceptados.length > 0) {
                            self.addToken(aceptados[0].token);
                            if (!Helpers.isSpace(src[x])) {
                                automatas.forEach(
                                    (automata) => {
                                        automata.input(src[x]);
                                        allTrampas = allTrampas && automata.isTrampa();
                                        if (automata.isActualAceptado()) {
                                            nuevosAceptados.push(automata);
                                        }
                                    }
                                );
                            }
                        } else {
                            throw `Syntax Error: Line ${line}, position: ${position}`;
                        }
                    }

                    buffer += src[x].trim();
                    aceptados = nuevosAceptados;

                    ++position;
                }
                return tokens;
            } catch (e) {
                return e;
            }
        },

        addToken (token) {
            tokens.push([token, buffer]);
            self.resetAutomatas();
        },

        createAutomatas (expresiones = []) {
            for (let x in expresiones) {
                automatas.push(self.defineAutomata(expresiones[x]));
            }
        },

        defineAutomata (expresion) {

            function addInicial (expresion) {
                return ' '+expresion;
            }

            return new Automata(
                expresion[0],
                addInicial(expresion[1]).split(''),
                [],
                0,
                expresion[2],
                [(expresion[1].length)]
            );
        },

        resetAutomatas () {
            automatas.forEach((aut) => {aut.reset();});
            buffer = '';
        },
    };
})();

Lexer.init(definiciones);
