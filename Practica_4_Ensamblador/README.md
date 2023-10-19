# Ensamblador
## Introducción
En este proyecto estaremos realizando el programa de un ensamblador que traduzca programas escritos en el lenguaje ensamblador simbolico Hack a codigo abierto que pueda ejecutarse en la plataforma de hardware construida en proyectos anteriores.

Para profundizar un poco más explicaremos el uso de este. Dependiendo del lenguaje de programación que se utilice (python), el ensamblador debe invocarse usando algo como un "NombreArchivoEnsamblador.asm" donde este es la entrada del ensamblador. El ensamblador crea un archivo de texto de salida llamado fileName.hack, cada linea del archivo de salida consta de dieciséis caracteres de 0 y 1.

El desarrollo de este ensamblador se realizo en 2 etapas, en las cuales se hicieron uso de programas de prueba que se proporcionaron para respaldar la implementación por etapas y asegurarnos que el ensamblador funcione correctamente.

## Desarrollo 
En el proceso de desarrollo de esta actividad, haremos uso del lenguaje Python y aplicaremos el paradigma de programación orientada a objetos. Uno de los objetos clave es el "SymbolTable" (Tabla de Símbolos), que contendrá los símbolos fundamentales del lenguaje, como las 16 direcciones de memoria, el código del teclado, la pantalla, y otros elementos. Este objeto debe ser dinámico para permitir la adición de nuevas direcciones, dependiendo de lo que se encuentre en el código.

Otro componente central es el "Parser" (Analizador), que se encargará de abrir, leer y analizar el archivo. Detectará si una línea corresponde a una instrucción o a un comentario, lo cual hará comparando si la línea comienza con "//". Si se trata de un comentario, eliminará la línea correspondiente. Además, buscará eliminar espacios innecesarios para simplificar la posterior conversión a binario.

El analizador determinará el tipo de instrucción en función de la primera letra de la línea. Si encuentra un símbolo "@", se considera una instrucción de tipo A. Si la línea contiene "(", se trata de una etiqueta y se clasifica como instrucción de tipo L. En caso de cualquier otro símbolo, se considera una instrucción de tipo C. Para instrucciones de tipo C, el analizador definirá si hay un salto (jump) y extraerá los componentes del código, las destinos de memoria y las variables.

Además, contamos con la clase "Code", que almacena los destinos, los componentes de las operaciones y los códigos para los saltos.

Con todas estas clases definidas, podemos construir nuestra clase principal, que funcionará como el ensamblador. Esta clase leerá el archivo y, con la ayuda de las clases auxiliares, generará un archivo en lenguaje "hack". La clase principal cuenta con funciones específicas para diferentes tipos de instrucciones. Por ejemplo, si es de tipo A, escribirá la dirección de memoria en binario, convirtiendo el símbolo si este no existe en la tabla de símbolos, creando la dirección y luego escribiendo la instrucción. Si es de tipo L, generará una nueva dirección de memoria para la siguiente posición y la agregará a la tabla de símbolos. Finalmente, si es de tipo C, añadirá tres unos al principio, seguidos de los componentes, destino y salto, y luego escribirá la instrucción.

El ensamblador también debe tener una condición que permita procesar solo archivos con extensión ".asm". El ejemplo que se encuentra en el repositorio de Git contiene el código "Add.asm", pero puede reemplazarse por cualquier otro archivo ".asm" para generar el correspondiente ".hack".

Este proceso de ensamblado nos permitirá convertir el código en lenguaje ensamblador a código máquina comprensible por la arquitectura de la computadora.
