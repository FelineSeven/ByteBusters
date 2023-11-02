# Máquina Virtual 
## Introducción
En este proyecto, se busca desarrollar un 'traductor' de lenguaje que debe traducir los comandos de programas escritos en lenguaje VM, a una secuencia de comandos en lenguaje hack, con el fin de que desarrollen la misma tarea que los archivos de comparación.  

El desarrollo de este proyecto se dividió en dos etapas, un traductor sencillo que cumpla con las funciones que se requieren, para luego ampliarlo a un 'traductor' de gran escala.

Las dos etapas se dividieron especificamente de la siguiente forma:
1. El 'traductor' en su etapa inicial debe conseguir hacer la traducción de los comandos aritmeticos de pila y luego los comandos de acceso a la memoria, además de ofrecer los mismos resultaos que los archivos de comparación que facilita el sitio de Nand2Tetris. 
2. En cuanto a la etapa dos, la idea es escalar el 'traductor' hacía la traducción de los comandos de llamada de funciones y bifurcaciones del lenguaje VM, e igualmente deben retornar los mismos resultados que los archivos de comparación brindados por la web de Nand2Tetris.

En forma general, el 'traductor' debe recibir archivos .vm, ejecutar los comandos para el proceso de tradución y luego guardar los resultados en un archivo de salida .asm, este ultimo contendrá el código ensamblador resultante de los archivos .vm que, posteriormente, tendrán lugar a la comparación para verificar el correcto funcionamiento del programa.   

## Desarrollo Proyecto 7

En el Proyecto 7, nos enfocamos en el desarrollo de una máquina virtual que desempeñará un papel crucial en la traducción de código de alto nivel a código de bajo nivel. La máquina virtual se ha desarrollado utilizando el lenguaje de programación Python, aprovechando los principios de la programación orientada a objetos.

La estructura de la máquina virtual comprende dos clases principales: "Parser" y "CodeWriter."

La clase "Parser" es esencial en el proceso de traducción. Comienza por preparar el archivo de entrada para su análisis. La función "abrirArchivo" se encarga de esta tarea, eliminando los comentarios, las líneas en blanco y los espacios innecesarios. Esto resulta en un código limpio y listo para ser procesado.

La función "hasMoreCommands" permite determinar si existen más comandos en el archivo. Esto es fundamental para avanzar a través del archivo y procesar los comandos de manera ordenada. La función "advance" se encarga de leer el siguiente comando en el archivo y convertirlo en el comando actual.

"commandType" es una función crucial que identifica el tipo de comando del comando actual. Puede reconocer si se trata de un comando aritmético, como "add," "sub," "neg," "eq," "gt," "lt," "and," "or," o "not." Además, puede identificar si es un comando "push" o "pop." En caso de que el comando actual no coincida con ninguno de estos tipos, la función generará un error.

"arg1" y "arg2" son funciones que brindan información adicional. "arg1" devuelve el primer argumento del comando actual (excepto para comandos aritméticos). En el caso de comandos aritméticos, devuelve el propio comando. "arg2," por su parte, proporciona el segundo argumento del comando actual, aunque no es válida para comandos aritméticos.

La clase "CodeWriter" se ocupa de configurar el convertidor de código para el archivo de salida. Almacena el nombre del archivo para las referencias de etiquetas estáticas y abre el archivo de salida para escritura. También lleva un contador de etiquetas y define las tablas de símbolos para comandos aritméticos y de ensamblador.

Las funciones de "CodeWriter" incluyen "comment," que escribe el comando actual en el archivo de salida como un comentario, y "write_arithmetics," que se encarga de escribir el código aritmético. Para comandos aritméticos como "add," "sub," "and," "or," establece una estructura base. Para comandos "neg" y "not," la estructura cambia. Cuando se trata de comandos "eq," "gt," y "lt," la estructura se modifica aún más, ya que se deben agregar saltos a etiquetas cuando se cumple una condición.

La función "write_push_pop" se encarga de escribir comandos "push" y "pop." Para estos comandos se maneja una estructura definida que se adapta a diferentes casos, como segmentos constantes o estáticos, así como otros segmentos, como "local," "argument," "this," "that," "temp," y "pointer."

En la función "main," se inicia el proceso verificando si se ha proporcionado un nombre de archivo. A continuación, se definen los nombres de los archivos de entrada y salida. Se crean objetos de tipo "Parser" y "CodeWriter" con los archivos correspondientes. A través de un bucle, se escanea el archivo de entrada en busca de comandos VM y se escriben las traducciones en el archivo de salida, utilizando las funciones de "Parser" y "CodeWriter." Se determina el tipo de comando mediante condicionales y se procede a escribir el comando en el archivo de salida.

## Desarrollo Proyecto 8

El Proyecto 8, que es una extensión del Proyecto 7, mantiene la estructura de clases y la función "main" existente, pero introduce nuevos comandos VM. Entre los nuevos comandos se incluyen "label," "goto," "if-goto," "function," "call," y "return."

En la clase "CodeWriter," se crean funciones específicas para cada uno de estos nuevos comandos siguiendo la estructura proporcionada en el texto guía. Además, se agrega una función llamada "set_file_name" para informar a la grabadora de código sobre el archivo que se está procesando.

La función "write_init" se encarga de escribir el código bootstrap de VM. Este código se utiliza para configurar el entorno de ejecución de la máquina virtual antes de que el programa principal se inicie.

En la función "main," se realizan ajustes para manejar nombres de archivos y se encarga de insertar el código bootstrap. Luego, se realiza el proceso de recorrer los archivos de entrada y convertirlos en un único archivo de ensamblaje. El escaneo del archivo de entrada en busca de comandos VM y la escritura de las traducciones en el archivo de salida se ejecuta de manera similar al proyecto anterior, utilizando las clases "Parser" y "CodeWriter."

Estas modificaciones y extensiones en los proyectos 7 y 8 permiten una comprensión más profunda y clara del proceso y los componentes involucrados. Los comandos VM adicionales agregados en el Proyecto 8 enriquecen aún más la funcionalidad de la máquina virtual. 

## Preguntas
1. Teniendo en cuenta el marco de estas dos prácticas que son las máquinas virtuales. ¿Cuál cree que es el futuro de las máquinas virtuales?
