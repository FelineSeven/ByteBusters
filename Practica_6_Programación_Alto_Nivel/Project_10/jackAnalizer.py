import sys
import os
from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine

def generateXMLFile(inputList, jackCodeFileName, option = "parsed"):
    if option == "tokenized":
        outputFileName = jackCodeFileName.replace(".jack", "T.xml")
    else:
        outputFileName = jackCodeFileName.replace(".jack", ".xml")

    with open(outputFileName, mode="w") as f:
        for line in inputList:
            f.write(line + "\n")

    return outputFileName

def main():
    if len(sys.argv) == 2:
        TOKEN_DICTIONARY = {
            "keyword": ("class", "constructor", "function", "method", "field", "static", "var", 
                        "int", "char", "boolean", "void", "true", "false", "null", "this", "let",
                        "do", "if", "else", "while", "return"),
            "symbol": ("{", "}", "(", ")", "[", "]", ".", ",", ";", "+", "-", "*", "/", "&", "|",
                        "<", ">", "=", "~"),
            "integerConstant": range(0, 32768),
            "stringConstant": "^\\S+$",
            "identifier": "^[A-Za-z_]+[A-Za-z_0-9]+$"
        }

        if sys.argv[1].endswith(".jack"):

            fileName = "./" + sys.argv[1]
            jackTokenizedList = JackTokenizer(fileName, TOKEN_DICTIONARY).generateTokens()
            tokenizedFileName = generateXMLFile(jackTokenizedList, fileName, "tokenized")
            jackParsedList = CompilationEngine(tokenizedFileName, TOKEN_DICTIONARY).parseTokens()
            generateXMLFile(jackParsedList, fileName, "parsed")
        else:

            jackCodeDirectory = sys.argv[1]

            for fileName in os.listdir(jackCodeDirectory):
                if fileName.endswith(".jack"):
                    fileName = (jackCodeDirectory if jackCodeDirectory.endswith("/") else jackCodeDirectory + "/") + fileName
                    jackTokenizedList = JackTokenizer(fileName, TOKEN_DICTIONARY).generateTokens()
                    tokenizedFileName = generateXMLFile(jackTokenizedList, fileName, "tokenized")
                    jackParsedList = CompilationEngine(tokenizedFileName, TOKEN_DICTIONARY).parseTokens()
                    generateXMLFile(jackParsedList, fileName, "parsed")
    else:
        print("Mi loco este archivo no le sirve")

if __name__ == "__main__":
    main()