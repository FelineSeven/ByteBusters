import re

class JackTokenizer:
    def __init__(self, jackCodeFileName, tokenDictionary):
        self.inputFileName = jackCodeFileName
        self.TOKEN_DICTIONARY = tokenDictionary

    def _readFileAndParseProgram(self):
        regxMultilineComment = "/\\*+[^*]*\\*+(?:[^/*][^*]*\\*+)*/"
        multiLineCommentShownFlag = False
        jackProgramParsedList = []

        with open(self.inputFileName, mode="r") as f:
            lines = f.read().splitlines()

            for line in lines:
                line = line.strip() 
                if not line: 
                    continue
                elif multiLineCommentShownFlag and "*/" not in line:
                    continue
                elif line.startswith("//"):
                    continue
                else:
                    if "//" in line:
                        line = line.split("//")[0]
                    
                    parsedOutputList = re.split(regxMultilineComment, line)
                    for parsedOutput in parsedOutputList:
                        if parsedOutput:
                            if "/*" in parsedOutput or "/**" in parsedOutput:
                                multiLineCommentShownFlag = True
                            elif "*/" in parsedOutput:
                                multiLineCommentShownFlag = False
                            else:
                                jackProgramParsedList.append(parsedOutput)
        
        return jackProgramParsedList

    def _generateTokenizedList(self, jackProgramParsedList):
        jackProgramTokenizedList = ["<tokens>"]

        for code in jackProgramParsedList:
            self._mapCodeToTokens(code, jackProgramTokenizedList)

        jackProgramTokenizedList.append("</tokens>")

        return jackProgramTokenizedList

    def _mapCodeToTokens(self, code, tokenizedList):
        currentCode = ""
        stringTag = False

        for char in code:
            if char != " ":
                if char in self.TOKEN_DICTIONARY["symbol"]:
                    if currentCode in self.TOKEN_DICTIONARY["keyword"]:
                        tokenizedList.append("<keyword> " + currentCode + " </keyword>")
                    elif currentCode.isdigit() and int(currentCode) in self.TOKEN_DICTIONARY["integerConstant"]:
                        tokenizedList.append("<integerConstant> " + currentCode + " </integerConstant>")
                    elif currentCode and currentCode[-1] == "\"" and not stringTag:
                        tokenizedList.append("<stringConstant> " + currentCode.split("\"")[1] + " </stringConstant>")
                    elif currentCode:
                        tokenizedList.append("<identifier> " + currentCode + " </identifier>")
                    currentCode = ""
                    if char == "<":
                        tokenizedList.append("<symbol> &lt; </symbol>")
                    elif char == ">":
                        tokenizedList.append("<symbol> &gt; </symbol>")
                    elif char == "&":
                        tokenizedList.append("<symbol> &amp; </symbol>")
                    else:  
                        tokenizedList.append("<symbol> " + char + " </symbol>")
                else:
                    if char == "\"":
                        if not stringTag:
                            stringTag = True
                        else:
                            stringTag = False
                    currentCode += char
            else:
                if currentCode in self.TOKEN_DICTIONARY["keyword"]:
                    tokenizedList.append("<keyword> " + currentCode + " </keyword>")
                    currentCode = ""
                elif currentCode in self.TOKEN_DICTIONARY["symbol"]:
                    if currentCode == "<":
                        tokenizedList.append("<symbol> &lt; </symbol>")
                    elif currentCode == ">":
                        tokenizedList.append("<symbol> &gt; </symbol>")
                    elif char == "&":
                        tokenizedList.append("<symbol> &amp; </symbol>")
                    else:  
                        tokenizedList.append("<symbol> " + currentCode + " </symbol>")
                    currentCode = ""
                elif currentCode.isdigit() and int(currentCode) in self.TOKEN_DICTIONARY["integerConstant"]:
                    tokenizedList.append("<integerConstant> " + currentCode + " </integerConstant>")
                    currentCode = ""
                elif currentCode and currentCode[-1] == "\"" and not stringTag:
                    tokenizedList.append("<stringConstant> " + currentCode.split("\"")[1] + "</stringConstant>")
                    currentCode = ""
                elif currentCode and stringTag:
                    currentCode += char
                elif currentCode:
                    tokenizedList.append("<identifier> " + currentCode + " </identifier>")
                    currentCode = ""


    def generateTokens(self):

        jackProgramParsedList = self._readFileAndParseProgram()
        
        jackProgramTokenizedList = self._generateTokenizedList(jackProgramParsedList)

        return jackProgramTokenizedList