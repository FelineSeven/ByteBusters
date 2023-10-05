# Lenguaje Maquina y arquitectura de computadores 
## Introduccion 

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
