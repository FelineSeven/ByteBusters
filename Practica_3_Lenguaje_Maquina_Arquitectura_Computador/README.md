# Lenguaje Maquina y arquitectura de computadores 
## Introduccion 
En este proyecto, nos sumergiremos en el emocionante mundo de la programación de bajo nivel en lenguaje de máquina y la plataforma informática Hack. Nuestro viaje nos llevará a través del proceso de ensamblaje, donde traduciremos el lenguaje simbólico al lenguaje de máquina, y nos permitirá apreciar de manera visual cómo el código binario nativo cobra vida en la plataforma de hardware de Hack.

Nuestro objetivo principal es completar la construcción de la CPU Hack y la plataforma de hardware Hack, avanzando hasta el chip de computadora superior. En este proceso, no solo aprenderemos los fundamentos de la programación en lenguaje maquina, sino que también experimentaremos de primera mano cómo se construye una computadora desde sus componentes más básicos. Además, pondremos en práctica nuestros conocimientos al escribir y probar dos programas de bajo nivel.

Este proyecto no solo nos proporcionará un profundo entendimiento de la programación de bajo nivel y la arquitectura de computadoras, sino que también nos preparará para explorar cómo funcionan las computadoras modernas a un nivel más profundo y apreciar la intersección entre hardware y software en el mundo de la informática.

## ¿Por qué el lenguaje de máquina es importante para definir la arquitectura computacional?
El lenguaje de máquina es crucial para establecer la arquitectura computacional, ya que es el idioma que el hardware de la computadora utiliza para procesar instrucciones y datos. Es importante porque permite a la CPU trabajar eficientemente y estructurar los componentes de hardware de manera adecuada. Además, el lenguaje de máquina es el estándar común utilizado para comunicarse con diferentes tipos y modelos de hardware de computadora.

## Proyecto 04 Lenguaje Maquina 
### Desarrollo MULT
En esta actividad, se nos solicita realizar una multiplicación utilizando lenguaje ensamblador. Para lograrlo, accederemos a los valores de memoria ubicados en las posiciones 0, 1 y 2. Las direcciones de memoria 0 y 1 se utilizarán para almacenar los multiplicandos, mientras que la dirección de memoria 2 será reservada para guardar el resultado de la multiplicación.

Para acceder a estas direcciones de memoria, utilizamos el símbolo "@" seguido de la dirección de memoria. La instrucción "M" nos permite acceder al valor almacenado en una dirección de memoria, mientras que "A" se utiliza para almacenar el valor de una dirección de memoria en un registro temporal llamado 'A'. La instrucción "D" se emplea para crear y gestionar una variable temporal. Con estas operaciones básicas, comenzamos a desarrollar la actividad.

El primer paso implica acceder a uno de los multiplicandos y asignarlo como nuestro iterador. Dado que no disponemos de bucles, utilizamos una instrucción de salto ('jump') que nos lleva a una etiqueta de inicio en cada iteración. Este proceso se repite hasta que se cumple una condición específica: que el iterador no supere el valor del otro multiplicando. En cada iteración, sumamos el valor actual en la dirección de memoria 2 al valor del iterador.

Una vez que se han completado todas las iteraciones, utilizamos otra instrucción de salto para dirigirnos a una etiqueta llamada 'end', que marca el final del programa. En este punto, el resultado de la multiplicación se encuentra almacenado en la dirección de memoria 2.

### Desarrollo FILL

En esta actividad, se nos encomienda la tarea de cambiar el estado de la pantalla a negro cuando se presione una tecla y devolverla a blanco cuando la tecla deje de presionarse. Para lograr esto, debemos acceder al valor de memoria específico asignado al teclado, el cual nos proporcionará información importante.

En primer lugar, este valor de memoria nos devolverá un 0 si ninguna tecla está siendo presionada. Sin embargo, cuando una tecla es presionada, obtendremos el valor correspondiente al código ASCII de dicha tecla. Utilizaremos esta información para llenar una variable con lo que llamaremos el 'valor de relleno' (fill value). Si el valor obtenido es diferente de cero, asignaremos a este 'valor de relleno' el valor de -1. En caso contrario, le asignaremos el valor de 0.

Luego, avanzamos a una etiqueta denominada 'draw', la cual se encargará de acceder al último valor de memoria en la dirección correspondiente al píxel de la pantalla. Dependiendo del valor que tenga el 'valor de relleno', este píxel se cambiará o no. La iteración continuará a través de los píxeles de la pantalla, determinada por una instrucción de salto ('jump') que nos indicará si hemos llegado al primer píxel. Este proceso se repetirá indefinidamente, ya que siempre debemos estar monitoreando el valor de memoria asociado al teclado.

Este enfoque garantiza que la pantalla cambie de blanco a negro cuando se presiona una tecla y vuelva a su estado original cuando la tecla se suelta. El programa estará constantemente revisando la actividad del teclado para realizar estos cambios en tiempo real.

## Proyecto 05 Arquitectura de computadores

### DEsarrollo Memory

![](https://github.com/FelineSeven/ByteBusters/blob/8556ef28ad02850aad7d6aa042adc3ead35f5c5c/Imagenes/Imagenes_Tercera_Practica/Imagenes_Quinto_Proyecto/nand2tetris-memory.png)

La memoria resulta de la combinación de tres chips: el chip RAM16k desarrollado en la práctica 03, el chip screen, encargado de mostrar la salida en la pantalla, y el chip keyboard, que detecta si alguna tecla está seleccionada. Para desarrollar esta actividad, primero utilizamos dos demultiplexores para determinar cuál de las entradas se almacenará en la memoria.

Luego, procedemos a cargar la RAM y la pantalla mediante la invocación de las funciones proporcionadas anteriormente. Utilizando una serie de operadores lógicos OR, nos aseguramos de que el valor de keyboard sea cero. Finalmente, con la ayuda de dos multiplexores, obtenemos el valor de salida que se almacenará en la memoria.

Este proceso nos permite gestionar y almacenar información en la memoria, asegurándonos de que la pantalla y otros dispositivos funcionen correctamente. Así, la memoria se convierte en un componente esencial para interactuar con el hardware y generar la salida deseada en la pantalla.

### Desarrollo CPU 

![](https://github.com/FelineSeven/ByteBusters/blob/ecc346057667fe21abd795dd8b59b9206bee1f31/Imagenes/Imagenes_Tercera_Practica/Imagenes_Quinto_Proyecto/nand2tetris-cpu.png)

El desarrollo de la CPU sigue la guía proporcionada por nand2tetris, que establece la estructura de la unidad central de procesamiento. El proceso comienza definiendo el registro A mediante demultiplexores y almacenándolo en un registro interno. Luego, se utiliza un multiplexor para extraer la información del registro, la cual pasa por una serie de funciones lógicas para preparar la entrada de la ALU (Unidad Lógica y Aritmética).

A continuación, la información se envía a la ALU, que procesa las entradas y genera un valor de salida. Luego se determina qué acción realizar con este valor: cargarlo en un registro o escribirlo en la memoria. Posteriormente, se preparan los datos para iniciar el ciclo nuevamente y poder retornar la salida obtenida por la CPU.

Este proceso se repite de manera continua, permitiendo que la CPU procese instrucciones y realice operaciones lógicas y aritméticas de acuerdo con el programa que se esté ejecutando.

### Desarrollo Computer 

![](https://github.com/FelineSeven/ByteBusters/blob/8556ef28ad02850aad7d6aa042adc3ead35f5c5c/Imagenes/Imagenes_Tercera_Practica/Imagenes_Quinto_Proyecto/nand2tetris-computer.jpg)

El computador es el resultado de la combinación de dos componentes esenciales: la ROM32k de la memoria y la CPU. La ROM32k proporciona los datos que la CPU procesará. Luego, con la salida de la CPU, la memoria determina qué información guardar y la envía nuevamente a la CPU para que continúe realizando cálculos, generando así una salida. Este proceso se repite en un ciclo infinito.

Para desarrollar este chip, simplemente llamamos a los chips previamente programados y a la ROM32K que nos proporciona el programa necesario. Esto permite que el computador funcione de manera coordinada y eficiente, procesando datos y generando salidas de manera continua.
