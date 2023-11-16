# Programación de Alto Nivel: Juego en Jack
## Introducción:
La presente práctica consiste en el uso de un lenguaje de programación simple conocido como 'Jack', utilizado para conseguir implementar un juego simple, como snake, pongo o inclusive tetris. 

El proyecto busca crear o 'adoptar' una idea de algun juego o aplicación interactiva de preferencia.

## Preguntas: 
1. Desarrolle más el concepto de lenguaje de alto nivel, teniendo en cuenta la diferencia entre lenguajes de programación propiamente dichos e interpretadores.

## Bonus:
¿Qué se debe considerar para proponer un nuevo y buen lenguaje de programación, teniendo en cuenta la arquitectura de computador completa? Justifique su respuesta.

La idea de un nuevo lenguaje de programación debe basarse en diversos aspectos que atiendan a las necesidades de su creación y sus motivos, los que clasificariamos así:

- Objetivo del lenguaje: Los lenguajes de programación suelen tener un enfoque especifico, como es el caso de MatLab para el computo númerico o

## Proyecto 09

El objetivo central de este proyecto es comprender el funcionamiento del lenguaje Jack. Para lograr esto, se propone la creación de un juego en este lenguaje. En este caso, se implementará el juego del cuadrado, donde se generará un cuadrado móvil en la pantalla. Este cuadrado podrá ajustar su tamaño y desplazarse tanto horizontal como verticalmente. Además, se incluirá la capacidad de eliminar el cuadrado.

En la fase inicial de esta actividad, se creará el archivo "cuadrado.jack," que contendrá la clase Square. Esta clase se encargará de la representación gráfica del cuadrado y definirá sus métodos. Incluirá un constructor que establecerá su tamaño y posición por defecto. Asimismo, contará con un método dispose que liberará la memoria asociada al objeto cuando sea necesario eliminarlo. También se implementarán funciones como draw, utilizada para mostrar el cuadrado en pantalla, y erase, para dejar de mostrarlo. Además, se incluirán las funciones incSize y decSize para aumentar y disminuir el tamaño del cuadrado en 2 píxeles, respectivamente. Finalmente, se agregarán cuatro funciones (moveUp, moveDown, moveLeft y moveRight) que desplazarán el cuadrado en dos píxeles en las direcciones correspondientes.

Luego, se procederá a la creación del archivo "juegoCuadrado.jack." Este archivo, al igual que el anterior, representará una clase, en este caso, la clase SquareGame. En esta clase, se definirá un objeto cuadrado y una dirección. Se implementará un constructor encargado de crear el cuadrado y establecer su dirección inicial en cero. También se incluirá una función dispose para liberar la memoria cuando sea necesario. La función run será el núcleo del juego, configurando un bucle infinito que esperará la presión de una tecla. Una vez presionada, el valor de la tecla cambiará, y dependiendo de la tecla seleccionada, se llamará a una de las funciones del objeto cuadrado. La función auxiliar moveSquare se encargará de mover el cuadrado en una dirección específica según el valor proporcionado: 1 para arriba, 2 para abajo, 3 para la izquierda y 4 para la derecha.

Finalmente, se creará el archivo "Main.jack," encargado de instanciar el SquareGame y ejecutarlo.

## Proyecto 10

El propósito fundamental de este proyecto es generar un archivo .VM a partir de un archivo .Jack para facilitar la lectura del código en la máquina virtual. Con este objetivo, se desarrollarán tres clases en Python, cada una cumpliendo un papel específico en la tarea.

La primera clase a implementar se denomina "CompilationEngine," y su función principal es emitir un archivo XML según la gramática Jack dada, tomando como entrada un JackTokenizer. En su método de inicialización, llamado "init," se define el archivo en Jack y se establece el tokendictionary como parámetros de entrada. El siguiente método se encarga de leer el archivo y realizar el análisis léxico de los tokens seleccionados. El método más extenso es el encargado de realizar el análisis sintáctico de los tokens Jack, parseándolos de manera diferente según el formato de la línea de código y agregándolos a la lista de tokens parseados. Este método devuelve la lista resultante. Finalmente, el método "parseTokens" llama a los dos métodos anteriores para generar la lista de tokens parseados.

La siguiente clase a crear es "JackTokenizer," cuya responsabilidad es ignorar los comentarios, las líneas en blanco y serializar el flujo de entrada en tokens del lenguaje Jack. Sus tres métodos incluyen la lectura del archivo, la generación de la lista de tokens, y el mapeo final. Además, se proporciona un método llamado "generateTokens" que recopila y ejecuta estos métodos.

Por último, se encuentra la clase principal denominada "JackAnalyzer," que se encargará de reunir y coordinar las dos clases anteriores.

Estas clases forman la primera fase del proceso para transformar un lenguaje de alto nivel a su versión en máquina virtual, estableciendo las bases para un análisis más profundo y la posterior generación del archivo .VM.
