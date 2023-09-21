
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
