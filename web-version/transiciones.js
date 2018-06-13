const transicionDefault = function (input) {
    return  this.estadoActual === null 
            || this.estados[this.estadoActual+1] !== input.toUpperCase()
            ? null //Null es el estado trampa
            : ++this.estadoActual;
};

const transicionAlfaNumerica = function (input) {
    return  this.estadoActual === null 
            || !Helpers.isAlphaNumeric(input) 
            ? null //Null es el estado trampa
            : this.estadoActual === 0 
                ? ++this.estadoActual
                : this.estadoActual;
};

const transicionAlfabetica = function (input) {
    return  this.estadoActual === null 
            || !Helpers.isAlphabetic(input) 
            ? null //Null es el estado trampa
            : this.estadoActual === 0 
                ? ++this.estadoActual
                : this.estadoActual;
};

const transicionNumerica = function (input) {
    return  this.estadoActual === null 
            || !Helpers.isNumeric(input) 
            ? null //Null es el estado trampa
            : this.estadoActual === 0 
                ? ++this.estadoActual
                : this.estadoActual;
};
