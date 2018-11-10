from parsing import parsing

assert parsing('int a ( float a ) { int b }')
assert parsing('int a ( float a ) { int b }')
assert parsing('int')
assert parsing('int a ( float b ) { int c }')
assert parsing('1')
assert parsing('int a (float hola){ab}')
assert parsing('int hola ( float beta ) { 34 }')
assert parsing('int chau ( float beta ) { if (beta) int alfa else (float tita) }')
assert parsing('int trabajoPractico {int nota} { if (francisoBueno) nota == 10 else (nota == 1)}')
assert parsing('int Franciso == bueno')
assert parsing('int nota := 10')
assert parsing('promocionDirecta == True')
