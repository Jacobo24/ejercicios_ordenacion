# ejercicios_ordenacion

Link al repositorio: https://github.com/Jacobo24/ejercicios_ordenacion.git

## A. Pasando lista
Problema
Eres profesor de una clase de la que te piden que pases asistencia. Cada alumno, según
llega a clase, confirma su asistencia y en la lista aparece su número identificador como un
entero. Sin embargo, el sistema es algo nuevo y a ratos vuelve a aparecer por error en la
lista un alumno ya registrado.
Tu objetivo es, dada la lista de identificadores A con longitud n, obtener el número de
identificadores únicos en ella sin hacer uso de estructuras adicionales (sets, listas, etc).
Entrada
Cada prueba contiene múltiples casos de prueba. La primera línea contiene el número de
casos de prueba t (1≤t≤100). La descripción de los casos de prueba sigue a continuación.
Cada caso de prueba consta de dos líneas. La primera contiene el valor de n (1≤n≤10000) y
la segunda contiene los n valores A1, A2, A3,...,AN con los identificadores de los alumnos.
Salida
Para cada caso de prueba, imprime un solo número: el número de alumnos que han
asistido.
Ejemplo
entrada
3
4
5 2 2 3
6
1 3 5 7 8 2
8
1 1 1 1 1 1 1 1
salida
3
6
1
## B. Prevención de riesgos
Problema
Hay n niños que quieren subir a una noria, y tu tarea es encontrar una góndola para cada
niño.
Cada góndola puede tener uno o dos niños, y además, el peso total en una góndola no
puede exceder x. Conoces el peso de cada niño.
¿Cuál es el número mínimo de góndolas necesarias para los niños?
Entrada
La primera línea contiene un valor n (1≤n≤10000) para la cantidad de niños y el valor x para
el peso máximo.
La segunda línea contiene N enteros A1, A2, A3, ..., AN (1≤Ai≤x).
Salida
Para cada caso de prueba, imprime un solo número: el número de góndolas necesarias
para meter a todos los niños
Ejemplos
entrada
4 10
7 2 3 9
salida
3
entrada
10 2
1 2 2 1 1 2 2 2 2 2
salida
9
## C. SSIFF
Problema
Se está dando lugar el Festival de Cine de San Sebastián. Tienes el abono completo y
quieres ver tantas películas como puedas.
Dispones de todos los horarios con la hora a la que empieza y acaba cada película.
¿Cuántas películas puedes ver como máximo?
Entrada
La primera línea de cada caso de prueba contiene un entero n (1≤n≤100000) — el número
de películas calendarizadas.
Las siguientes n líneas contienen dos valores enteros a y b (1≤a≤b≤1000000000)).
Salida
Para cada caso de prueba, imprime un solo valor: el máximo número de películas a las que
puedes atender, suponiendo que te mueves de una película a otra instantáneamente.
Ejemplo
entrada
6
4 8
2 7
1 5
6 8
8 11
3 6
salida
3
