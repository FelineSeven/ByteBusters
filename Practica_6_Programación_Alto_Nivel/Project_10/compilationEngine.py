class CompilationEngine:
    def __init__(self, jackTokenizedFileName, tokenDictionary):
        self.jackTokenizedFileName = jackTokenizedFileName
        self.TOKEN_DICTIONARY = tokenDictionary

    def _readFileAndParseTokens(self):
        jackTokenList = []

        with open(self.jackTokenizedFileName, mode="r") as f:
            lines = f.read().splitlines()[1:-1]

            for line in lines:
                jackTokenList.append(line)

        return jackTokenList
                
    def _parseJackTokens(self, tokenizedList):
        def appendToParsedList(blank):
            nonlocal cursorPosition

            if cursorPosition < len(tokenizedList):
                jackTokenParsedList.append(" " * (blank  + 2) + tokenizedList[cursorPosition])
                cursorPosition += 1

        def getTagContent(tag):
            return tag.split(" ")[1]

        def compileClass(blank):
            nonlocal cursorPosition

            jackTokenParsedList.append(" " * blank + "<class>")

            for _ in range(3):
                appendToParsedList(blank)
            
            while cursorPosition < len(tokenizedList) and \
                    ("static" in getTagContent(tokenizedList[cursorPosition]) or \
                    "field" in getTagContent(tokenizedList[cursorPosition])):
                compielClassVarDec(blank + 2)
            
            while cursorPosition < len(tokenizedList) and \
                    ("constructor" in getTagContent(tokenizedList[cursorPosition]) or \
                    "function" in getTagContent(tokenizedList[cursorPosition]) or \
                    "method" in getTagContent(tokenizedList[cursorPosition])):
                compileSubroutine(blank + 2)

            appendToParsedList(blank)
            jackTokenParsedList.append(" " * blank + "</class>")

        def compielClassVarDec(blank):
            nonlocal cursorPosition

            jackTokenParsedList.append(" " * blank + "<classVarDec>")


            appendToParsedList(blank)

            while cursorPosition < len(tokenizedList) and \
                ";" not in getTagContent(tokenizedList[cursorPosition]):
                appendToParsedList(blank)


            appendToParsedList(blank)


            jackTokenParsedList.append(" " * blank + "</classVarDec>")

        def compileSubroutine(blank):
            nonlocal cursorPosition


            jackTokenParsedList.append(" " * blank + "<subroutineDec>")
            
            for _ in range(4):
                appendToParsedList(blank)
            
            compileParameterList(blank + 2)

            appendToParsedList(blank)

            compileSubroutineBody(blank + 2)

            jackTokenParsedList.append(" " * blank + "</subroutineDec>")
        
        def compileSubroutineBody(blank):
            nonlocal cursorPosition


            jackTokenParsedList.append(" " * blank + "<subroutineBody>")


            appendToParsedList(blank)


            while cursorPosition < len(tokenizedList) and \
                    ("let" not in getTagContent(tokenizedList[cursorPosition]) and \
                    "if" not in getTagContent(tokenizedList[cursorPosition]) and \
                    "while" not in getTagContent(tokenizedList[cursorPosition]) and \
                    "do" not in getTagContent(tokenizedList[cursorPosition]) and \
                    "return" not in getTagContent(tokenizedList[cursorPosition])):
                compileVarDec(blank + 2)


            if cursorPosition < len(tokenizedList) and \
                    ("let" in getTagContent(tokenizedList[cursorPosition]) or \
                    "if" in getTagContent(tokenizedList[cursorPosition]) or \
                    "while" in getTagContent(tokenizedList[cursorPosition]) or \
                    "do" in getTagContent(tokenizedList[cursorPosition]) or \
                    "return" in getTagContent(tokenizedList[cursorPosition])):
                compileStatements(blank + 2)


            appendToParsedList(blank)

            jackTokenParsedList.append(" " * blank + "</subroutineBody>")

        def compileParameterList(blank):
            nonlocal cursorPosition


            jackTokenParsedList.append(" " * blank + "<parameterList>")

            while cursorPosition < len(tokenizedList) and \
                ")" not in getTagContent(tokenizedList[cursorPosition]):

                for _ in range(2):
                    appendToParsedList(blank)


                if cursorPosition < len(tokenizedList) and \
                    "," in getTagContent(tokenizedList[cursorPosition]):
                    appendToParsedList(blank)


            jackTokenParsedList.append(" " * blank + "</parameterList>")


        def compileVarDec(blank):
            nonlocal cursorPosition
            

            jackTokenParsedList.append(" " * blank + "<varDec>")

            for _ in range(3):
                appendToParsedList(blank)


            while cursorPosition < len(tokenizedList) and \
                ";" not in getTagContent(tokenizedList[cursorPosition]):
                for _ in range(2):
                    appendToParsedList(blank)


            appendToParsedList(blank)


            jackTokenParsedList.append(" " * blank + "</varDec>")
        

        def compileStatements(blank):
            nonlocal cursorPosition


            jackTokenParsedList.append(" " * blank + "<statements>")

            while cursorPosition < len(tokenizedList) and \
                "}" not in getTagContent(tokenizedList[cursorPosition]):
                if cursorPosition < len(tokenizedList) and \
                    "let" in getTagContent(tokenizedList[cursorPosition]):
                    compileLet(blank + 2)
                elif cursorPosition < len(tokenizedList) and \
                    "if" in getTagContent(tokenizedList[cursorPosition]):
                    compileIf(blank + 2)
                elif cursorPosition < len(tokenizedList) and \
                    "while" in getTagContent(tokenizedList[cursorPosition]):
                    compileWhile(blank + 2)
                elif cursorPosition < len(tokenizedList) and \
                    "do" in getTagContent(tokenizedList[cursorPosition]):
                    compileDo(blank + 2)
                elif cursorPosition < len(tokenizedList) and \
                    "return" in getTagContent(tokenizedList[cursorPosition]): 
                    compileReturn(blank + 2)
            

            jackTokenParsedList.append(" " * blank + "</statements>")


        def compileDo(blank):
            nonlocal cursorPosition
            

            jackTokenParsedList.append(" " * blank + "<doStatement>")

            appendToParsedList(blank)


            compileSubroutineCall(blank)          


            appendToParsedList(blank)


            jackTokenParsedList.append(" " * blank + "</doStatement>")

        def compileSubroutineCall(blank):
            nonlocal cursorPosition


            if cursorPosition + 1< len(tokenizedList) and \
                "." in getTagContent(tokenizedList[cursorPosition + 1]):
                for _ in range(2):
                    appendToParsedList(blank)
            

            for _ in range(2):
                appendToParsedList(blank)

            compileExpressionList(blank + 2)

            appendToParsedList(blank)


        def compileLet(blank):
            nonlocal cursorPosition
            

            jackTokenParsedList.append(" " * blank + "<letStatement>")


            for _ in range(2):
                appendToParsedList(blank)


            if cursorPosition < len(tokenizedList) and \
                "[" in getTagContent(tokenizedList[cursorPosition]):

                appendToParsedList(blank)

                compileExpression(blank + 2)

                appendToParsedList(blank)
            

            appendToParsedList(blank)


            compileExpression(blank + 2)


            appendToParsedList(blank)


            jackTokenParsedList.append(" " * blank + "</letStatement>")

        def compileWhile(blank):
            nonlocal cursorPosition


            jackTokenParsedList.append(" " * blank + "<whileStatement>")


            for _ in range(2):
                appendToParsedList(blank)


            compileExpression(blank + 2)


            for _ in range(2):
                appendToParsedList(blank)
            

            compileStatements(blank + 2)
            

            appendToParsedList(blank)


            jackTokenParsedList.append(" " * blank + "</whileStatement>")
            

        def compileReturn(blank):
            nonlocal cursorPosition
            

            jackTokenParsedList.append(" " * blank + "<returnStatement>")


            appendToParsedList(blank)

            if cursorPosition < len(tokenizedList) and \
                ";" not in getTagContent(tokenizedList[cursorPosition]):
                compileExpression(blank + 2)
            

            appendToParsedList(blank)


            jackTokenParsedList.append(" " * blank + "</returnStatement>")

        def compileIf(blank):
            nonlocal cursorPosition
            

            jackTokenParsedList.append(" " * blank + "<ifStatement>")


            for _ in range(2):
                appendToParsedList(blank)

            compileExpression(blank + 2)
            

            for _ in range(2):
                appendToParsedList(blank)
            

            compileStatements(blank + 2)
            

            appendToParsedList(blank)


            if cursorPosition < len(tokenizedList) and \
                "else" in getTagContent(tokenizedList[cursorPosition]):

                for _ in range(2):
                    appendToParsedList(blank)

                compileStatements(blank + 2)

                appendToParsedList(blank)


            jackTokenParsedList.append(" " * blank + "</ifStatement>")
            

        def compileExpression(blank):
            nonlocal cursorPosition
            

            jackTokenParsedList.append(" " * blank + "<expression>")


            compileTerm(blank + 2)


            while cursorPosition < len(tokenizedList) and \
                    ("+" in getTagContent(tokenizedList[cursorPosition]) or \
                    "-" in getTagContent(tokenizedList[cursorPosition]) or \
                    "*" in getTagContent(tokenizedList[cursorPosition]) or \
                    "/" in getTagContent(tokenizedList[cursorPosition]) or \
                    "&amp;" in getTagContent(tokenizedList[cursorPosition]) or \
                    "|" in getTagContent(tokenizedList[cursorPosition]) or \
                    "&lt;" in getTagContent(tokenizedList[cursorPosition]) or \
                    "&gt;" in getTagContent(tokenizedList[cursorPosition]) or \
                    "=" in getTagContent(tokenizedList[cursorPosition])):
                appendToParsedList(blank)
                compileTerm(blank + 2)


            jackTokenParsedList.append(" " * blank + "</expression>")


        def compileTerm(blank):
            nonlocal cursorPosition
            

            jackTokenParsedList.append(" " * blank + "<term>")


            if cursorPosition + 1< len(tokenizedList) and \
                "[" in getTagContent(tokenizedList[cursorPosition + 1]):

                for _ in range(2):
                    appendToParsedList(blank)

                compileExpression(blank + 2)

                appendToParsedList(blank)

            elif cursorPosition < len(tokenizedList) and \
                    ("-" in getTagContent(tokenizedList[cursorPosition]) or \
                    "~" in getTagContent(tokenizedList[cursorPosition])):

                appendToParsedList(blank)

                compileTerm(blank + 2)

            elif cursorPosition < len(tokenizedList) and \
                "(" in getTagContent(tokenizedList[cursorPosition]):

                appendToParsedList(blank)

                compileExpression(blank + 2)

                appendToParsedList(blank)

            elif cursorPosition + 1 < len(tokenizedList) and \
                    ("(" in getTagContent(tokenizedList[cursorPosition + 1]) or \
                    "." in getTagContent(tokenizedList[cursorPosition + 1])):
                compileSubroutineCall(blank)

            else:
                appendToParsedList(blank)


            jackTokenParsedList.append(" " * blank + "</term>")


        def compileExpressionList(blank):
            nonlocal cursorPosition
            

            jackTokenParsedList.append(" " * blank + "<expressionList>")

            while cursorPosition < len(tokenizedList) and \
                ")" not in getTagContent(tokenizedList[cursorPosition]):

                compileExpression(blank + 2)


                while cursorPosition < len(tokenizedList) and \
                    "," in getTagContent(tokenizedList[cursorPosition]):
                    appendToParsedList(blank)
                    compileExpression(blank + 2)

            jackTokenParsedList.append(" " * blank + "</expressionList>")

        jackTokenParsedList = []
        cursorPosition = 0
        blank = 0 

        compileClass(blank)

        return jackTokenParsedList

    def parseTokens(self):
        jackTokenList = self._readFileAndParseTokens()

        jackTokenParsedList = self._parseJackTokens(jackTokenList)

        return jackTokenParsedList