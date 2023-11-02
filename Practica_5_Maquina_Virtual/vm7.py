import os
import sys


class Parser:

    def __init__(self, file_name: str):
        """Abre el archivo y lo prepara para el cambio."""
        # se define el comando inicial que debe estar vacio
        self.current_command = ""
        # se define el indice del comando 
        self.current = -1
        # se crea una lista para los comandos 
        self.commands = []
        # Se abre el archivo a utilizar.
        # Se eleiminan todos los comentarios las lineas en blanco y los espacios en blanco 
        file = open(file_name)
        for line in file:
            line = line.partition("//")[0]
            line = line.strip()
            if line:
                self.commands.append(line)
        file.close()

    def hasMoreCommands(self) -> bool:
        # revisa si existen mas comandos 
        return (self.current + 1) < len(self.commands)

    def advance(self) -> None:
        # lee el siguiente comando y lo convierte en el comando actual
        self.current += 1
        self.current_command = self.commands[self.current]

    def commandType(self) -> str:
        # Retorna el tipo del comando actual 
        # Define la lista de comandos conocidos 
        arithmetic_commands = ["add", "sub", "neg",
                               "eq", "gt", "lt", "and", "or", "not"]
        # extrae el comando actual para la linea de entrada
        cmd = self.current_command.split(" ")[0]
        # Determina el tipo de comando que es 
        if cmd in arithmetic_commands:
            return "C_ARITHMETIC"
        elif cmd == "push":
            return "C_PUSH"
        elif cmd == "pop":
            return "C_POP"
        else:
            raise NameError("Unexpected Command Type")

    def arg1(self) -> str:
        # Devuelve el primer argumento del comando actual. Para un comando aritmetico devuelve el propio comando y no debe ser llamada para un comando de retorno
        if self.commandType() == "C_ARITHMETIC":
            return self.current_command.split(" ")[0]
        else:
            return self.current_command.split(" ")[1]

    def arg2(self) -> int:
        # Devuelve el segundo argumento del comando actual esta funcion no es valida para los comandos de tipo aritmetico  
        return int(self.current_command.split(" ")[2])


class CodeWriter:

    def __init__(self, file_name: str):
        # Configura el conversor de codigo 
        # Almacenaremos el nombre del archivo para las referencias de etiquetas estaticas
        self.file_name = file_name[:-4]
        # Abrimos el archivo de salida para escribir 
        self.file = open(file_name, "w")
        # Se crea un contador de etiquetas
        self.label_counter = 0
        # Se definen la tabla de simbolos aritmeticos y de simbolos del ensamblador
        self.symbols = {
            # Operadores aritmeticos
            "add": "M=D+M",
            "sub": "M=M-D",
            "and": "M=D&M",
            "or": "M=D|M",
            "neg": "M=-M",
            "not": "M=!M",
            "eq": "D;JEQ",
            "gt": "D;JGT",
            "lt": "D;JLT",
            # Operadores de ensamblador 
            "local": "@LCL",
            "argument": "@ARG",
            "this": "@THIS",
            "that": "@THAT",
            "constant": "",
            "static": "",
            "pointer": "@3",
            "temp": "@5"
        }

    def comment(self, command: str):
        # Escribe en el archivo de salida el comando actual como un comentario 
        print("// " + command, file=self.file)

    def write_arithmetic(self, command: str):
        # Escribe en el archivo de salida el codigo aritmetico de ensamblaje para el comando dado
        output = []
        if command in ["add", "sub", "and", "or"]:
            output.append("@SP")
            output.append("AM=M-1")
            output.append("D=M")
            output.append("@SP")
            output.append("A=M-1")
            output.append(self.symbols[command])
        elif command in ["neg", "not"]:
            output.append("@SP")
            output.append("A=M-1")
            output.append(self.symbols[command])
        elif command in ["eq", "gt", "lt"]:
            jump_label = "CompLabel" + str(self.label_counter)
            self.label_counter += 1
            output.append("@SP")
            output.append("AM=M-1")
            output.append("D=M")
            output.append("@SP")
            output.append("A=M-1")
            output.append("D=M-D")
            output.append("M=-1")
            output.append("@" + jump_label)
            output.append(self.symbols[command])
            output.append("@SP")
            output.append("A=M-1")
            output.append("M=0")
            output.append("(" + jump_label + ")")
        else:
            raise NameError("Unexpected Arithmetic Command")

        # Agrega una linea vacia 
        output.append("")

    def write_push_pop(self, command: str, segment: str, index: int):
        # Escribe en el archivo de salida el comando push o pop dado
        output = []
        if command == "C_PUSH":
            if segment == "constant":
                output.append("@" + str(index))
                output.append("D=A")
                output.append("@SP")
                output.append("AM=M+1")
                output.append("A=A-1")
                output.append("M=D")
            elif segment in ["local", "argument", "this", "that", "temp", "pointer"]:
                output.append("@" + str(index))
                output.append("D=A")
                if segment == "temp" or segment == "pointer":
                    output.append(self.symbols[segment])
                else:
                    output.append(self.symbols[segment])
                    output.append("A=M")
                output.append("A=D+A")
                output.append("D=M")
                output.append("@SP")
                output.append("A=M")
                output.append("M=D")
                output.append("@SP")
                output.append("M=M+1")
            elif segment == "static":
                output.append("@" + self.file_name + "." + str(index))
                output.append("D=M")
                output.append("@SP")
                output.append("A=M")
                output.append("M=D")
                output.append("@SP")
                output.append("M=M+1")
            else:
                raise NameError("Unexpected Push Segment")
        elif command == "C_POP":
            if segment == "constant":
                raise NameError("Cannot Pop Constant Segment")
            elif segment in ["local", "argument", "this", "that", "temp", "pointer"]:
                output.append("@" + str(index))
                output.append("D=A")
                if segment == "temp" or segment == "pointer":
                    output.append(self.symbols[segment])
                else:
                    output.append(self.symbols[segment])
                    output.append("A=M")
                output.append("D=D+A")
                output.append("@R13")
                output.append("M=D")
                output.append("@SP")
                output.append("AM=M-1")
                output.append("D=M")
                output.append("@R13")
                output.append("A=M")
                output.append("M=D")
            elif segment == "static":
                output.append("@SP")
                output.append("AM=M-1")
                output.append("D=M")
                output.append("@" + self.file_name + "." + str(index))
                output.append("M=D")
            else:
                raise NameError("Unexpected Pop Segment")
        else:
            raise NameError("Unexpected Command Type")

        # Agrega una linea vacia 
        output.append("")


    def close(self):
        # Cierra el archivo de salida 
        self.file.close()


def main():

    # Verifica si tenemos un archivo 
    if len(sys.argv) != 2 or sys.argv[1][-3:] != ".vm":
        print("Error: Please provide a Virtual Machine file.")
        print("Usage: python " + os.path.basename(__file__) + " [file.vm]")
        return

    # Define los nombres de los archivos de entrada y salida 
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[1][:-3] + ".asm"

    #  Crea un parser con el archivo de entrada 
    parser = Parser(input_file_name)

    # crea un code writer con el archivo de salida 
    code_writer = CodeWriter(output_file_name)

    # Escanea el archivo de entrada en busca de comandos VM y escribe las traducciones en el archivo de salida.
    while parser.hasMoreCommands():
        parser.advance()
        # Escribe el comando actual como comentario 
        code_writer.comment(parser.current_command)
        # Determina el tipo de comando actual 
        command_type = parser.commandType()
        if command_type == "C_ARITHMETIC":
            code_writer.write_arithmetic(parser.arg1())
        elif command_type in ["C_PUSH", "C_POP"]:
            argument1 = parser.arg1()
            argument2 = parser.arg2()
            code_writer.write_push_pop(command_type, argument1, argument2)
        else:
            raise NameError("Unsupported Command Type")

    # Cierra el archivo de salida 
    code_writer.close()


if __name__ == "__main__":
    main()