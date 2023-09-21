
# Aritmetica Booleana y memoria 

El propósito central de este proyecto es la construcción manual de una Unidad Aritmético Lógica (ALU) desde cero, abordando todos los componentes que la componen. Esta iniciativa se enfoca en la comprensión profunda de su funcionamiento y su relevancia en el ámbito informático. Además, se busca avanzar en la concepción y ensamblaje de un solo bit y una unidad de memoria RAM, escalando gradualmente hacia sistemas de memoria RAM de mayor envergadura. Este proceso permitirá no solo explorar su funcionamiento interno, sino también comprender cómo se accede a la memoria en estas estructuras cada vez más complejas.


### 1. ¿Cuál es el objetivo de cada uno de esos proyectos con sus palabras y describa que debe hacer para desarrollarlo?
- El objetivo principal del proyecto 02 es la construcción de todos los chips propuestos con el fin de completar la elaboración de la ALU (Unidad Aritmético-Lógica). Para lograr esto, se debe seguir un proceso de desarrollo que involucra la creación y diseño de los chips necesarios para la ALU, incluyendo la planificación de su funcionalidad y conectividad.Luego, se procederá a implementar estos chips. Finalmente, se realizarán pruebas para garantizar que la ALU funcione correctamente y cumpla con los requisitos específicos del proyecto.
- El objetivo principal del proyecto 03 es la construcción de los chips descritos basándonos en el DFF (Flip-Flop D) y en los chips previamente desarrollados. Para llevar a cabo este proyecto, se debe seguir un proceso de desarrollo que implica la creación de los chips necesarios, tomando como base el diseño del DFF y utilizando los chips que se desarrollaron anteriormente como componentes clave.

### 2. Explique las principales diferencias entre la lógica aritmética y la lógica secuencial.
La lógica aritmética realiza calculos numericos  y aritméticos, como sumas, restas, multiplicaciones, divisiones tambien toma decisiones logicas, mientras que la lógica secuencial almacena y procesa información en secuencia la cual depende de eventos anteriores. Los circuitos de lógica aritmética están diseñados para operadores básicos, utiliza principalmente compuertas lógicas, multiplexores y otros elementos para realizar cálculos y manipulación de datos, mientras que los de lógica secuencial se basan en la memoria, además de compuertas lógicas, involucra elementos como flip-flops, contadores, registros y máquinas de estado para controlar y mantener estados internos a lo largo del tiempo.La lógica aritmética combina varias entradas y produce una salida, en cambio la lógica secuencial puede tener múltiples salidas que dependen del estado del circuito.


## Desarrollo proyecto 02

### HallfAdder:

Para el desarrollo de este componete observamos su tabla de verdad:

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.watelectronics.com%2Fwp-content%2Fuploads%2FHalf-Adder-Truth-Table-1.jpg&f=1&nofb=1&ipt=66a4e9a06dcc793498d146536f5c975ae9ff39b5e9b8872363f9b16de80febeb&ipo=images)

Como se puede observar en la tabla, la salida tiene la forma de un Xor y el carry de salida teine la forma de un and por lo que simplemente realizamos las dos operaciones con las entradas y asignamos las salidas correspondientes:

![](https://circuitglobe.com/wp-content/uploads/2015/12/HALF-ADDER-FULL-ADDER-FIG-1-compressor.jpg)

### FullAdder

Para la realizacion de este componente lo que se hace es realizar una media suma y el resultado obtenido de esa media suma se le realiza otra media suma, esas dos medias sumas nos generaran dos carrys de salida respectivamente, con los cuales realizaremos un or para definir la salida del carry final.

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Funigal.mx%2Fwp-content%2Fuploads%2F2022%2F03%2F1647471765_903_Circuito-de-medio-sumador-y-sumador-completo.jpg&f=1&nofb=1&ipt=8bbf2d9845bb1f9df729ce8fb5a953141a2154180b3d9388a6c776164099b85b&ipo=images)

### Add16

La funcion de este componente es realizar 16 sumas para lo cual para la primera suma se realiza una media suma, dicha suma nos va a generar un carry, de ahi en adelante con ese carry se realizaran las siguientes 15 sumas completas.

### Inc16

Para el desarrollo de esta funcion simplemente se realizara la funcion Add16 pasandole la segunda entrada como un vector de unos, por lo que le realizara un incremento de uno a cada uno de los elementos.

### ALU

Para el desarrollo de la alu necesitamos tener en cuneta los selectores, lo primero que hacemos es analizar los primeros selectores y utilizar un multiplexor para definir si deja la entrada x y la entrada y o si las transforma en un vector de ceros, seguido a esto tendremos un nuevo valor de y y un nuevo valor de x los cuales vamos a negar o no segun el selector para ello, pasamos a un multiplexor el valor de x y x negado y en otro multiplexor el valor de y y y negado, con esto tendremos dos nuevas salidas de x y y, realizamos la funcion add16 y la funcion and16, y las pasamos a otro multiplexor de 16 el cual nos dira si guarda el valor de la add16 o de la and 16, esta salida se negara y se pasara a otro multiplexor el cual elegira si se deja dicha funcion o si se debe negar la funcion, por ultimo se tiene que analizar la salida ya que si es igual a 0 zr debe retornar el valor de 1 y si la salida es menor que 0 la salida ng debe retornar 1.

![](http://zipcpu.com/img/alu-simple.svg)


## Desarrollo proyecto 03

### Bit

la plataforma nand2tetris nos facilita el codigo del DFF el cual almacenara el valor de el bit, dicho DFF mandara una señal cada sierto tiempo lo que mandara la salida a un multiplexor normal y eso definira la entrada al DFF, ese va a ser el valor que almacene el bit.

### Registrer 

El registrer es almacenar 16 bits, por lo que con las entradas llamamos la funcion realizada anteriormente 16 veces.

###RAM8

Como su nombre lo dice, es una memoria que tendrá 8 "slots" para guardar los datos. Para determinar donde se guardan los datos se tiene una entrada llamada "address" que giardará los in de 'in[16]', además del Dmux Que determinará el lugar, El chip Mux se encarga de realizar la impresión del espacio donde está guardado el dato.  

### RAM64 

Así como la RAM8, se utilizarán 8 veces el chip RAM8 para lograr 64 entradas en la memoria, 


RAM512 RAM4K RAM16k
### PC

Para realizar el pc primero definimos que va a realizar dicho PC, en este caso va a realizar un incremento, y va a tener tres funciones, que son load, para cargar lo que ya tiene, set para volver el bit a cero y inc que va a ser la operacion de incrementar, para desarrollar el pc lo primero es con la entrada realizar el incremento, luego con tres multiplexores de dieciseis definimos cual de las tres operaciones se van a realizar, con la operacion realizada se guarda en un register.

