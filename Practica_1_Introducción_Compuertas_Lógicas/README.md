# Practica_1_Introduccion_Compuertas

En la presente práctica, daremos inicio a nuestro recorrido en el fascinante mundo del curso de Arquitectura de Computadoras. Para llevar a cabo este emocionante viaje, nos apoyaremos en una poderosa herramienta: el software Nand2Tetris. Esta plataforma nos brindará la oportunidad de sumergirnos en el maravilloso universo de la lógica booleana a través de la simulación de diversas compuertas lógicas.

Durante esta actividad, exploraremos la construcción y funcionamiento de una variedad de compuertas esenciales, tales como Not, And, Or, Xor, Mux, Dmux, Not16, And16, Or16, Mux16, Or8way, Mux4Way16, Mux8Way16, Dmux4Way y Dmux8Way. Estas piezas fundamentales nos servirán como pilares para comprender los conceptos y principios esenciales de la arquitectura de computadoras.

## Desarrollo de cada una de las compuertas 

### Nand: 
Esta es la compuerta base que nos da el software de la cual se van a derivar el resto de las compuertas

### Not: 
Para implementar esta compuerta, empleamos la compuerta NAND, en la cual ambas entradas siempre poseen el mismo valor, resultando en la negación del valor de entrada original.

### And: 
Para crear esta compuerta, utilizamos la compuerta NOT previamente construida y, de manera sencilla, negamos las salidas del valor NAND.

### Or: 
Para construir esta compuerta, simplemente ejecutamos una operación AND con las entradas Negadas con la .

### Xor: 
Para diseñar esta compuerta, primero invertimos cada una de las entradas. Luego, realizamos dos operaciones AND: una con la primera entrada invertida y la segunda entrada sin invertir, y la otra con la primera entrada sin invertir y la segunda entrada invertida. Finalmente, combinamos los resultados de ambas operaciones AND mediante una operación OR.

### Mux: 
Para crear esta compuerta, comenzamos con la tabla de verdad, a partir de la cual construimos un mapa de Karnaugh. Este mapa nos proporciona una expresión en términos de operaciones AND, OR y NOT, las cuales ya hemos creado previamente. Utilizando esta expresión, construimos el multiplexor necesario para la operación deseada. 

### Dmux: 
Para crear esta compuerta, iniciamos con la tabla de verdad y observamos que la salida "a" puede ser expresada como una operación AND entre la entrada y la negación del selector, mientras que la salida "b" se puede expresar como una operación AND entre la entrada y el selector. Dado que ya hemos creado estas compuertas individuales, podemos proceder a construir el demultiplexor. 

### Not16: 
Para construir esta compuerta, simplemente aplicamos la operación NOT que previamente hemos creado, repetida dieciséis veces.

### And16: 
Para construir esta compuerta, simplemente aplicamos la operación And que previamente hemos creado, repetida dieciséis veces.

### Or16: 
Para construir esta compuerta, simplemente aplicamos la operación Or que previamente hemos creado, repetida dieciséis veces.

### Mux16: 
Para construir esta compuerta, simplemente aplicamos la operación Mux que previamente hemos creado, repetida dieciséis veces.

### Or8Way: 
Para crear esta compuerta, aplicamos la operación OR que hemos construido previamente, realizando una operación OR entre la primera entrada y la segunda, y luego entre el resultado anterior y la siguiente entrada, repitiendo este proceso hasta combinar las ocho compuertas necesarias.

### Mux4Way16: 
Para llevar a cabo esta operación, agrupamos las entradas en pares y aplicamos la operación MUX a cada par. Esto nos proporciona dos resultados diferentes, a los cuales también aplicamos la operación MUX.

### Mux8Way16: 
Para llevar a cabo esta operación, agrupamos las entradas en pares y aplicamos la operación MUX a cada par. Esto nos proporciona dos resultados diferentes, a los cuales también aplicamos la operación MUX.

### DMux4Way: 
Para llevar a cabo esta operación, agrupamos las entradas en pares y aplicamos la operación DMUX a cada par. Esto nos proporciona dos resultados diferentes, a los cuales también aplicamos la operación DMUX.

### Dmux8Way: 
Para llevar a cabo esta operación, agrupamos las entradas en pares y aplicamos la operación DMUX a cada par. Esto nos proporciona dos resultados diferentes, a los cuales también aplicamos la operación DMUX.
