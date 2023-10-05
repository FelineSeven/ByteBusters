// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program BLACKens the screen,
// i.e. writes "BLACK" in every pixel;
// the screen should remain fully BLACK as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "WHITE" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(BEGIN)
	// Cambia la direccion de el keyboard por el valor que tenga 
	@24576
	D=A
	@keyboard
	M=D
(CHECK_KEYBOARD)
	//Nos centramos en el valor de memoria que define si el teclado esta presionado
	@24575
	D=A
	@current
	M=D
	// define si la tecla se encuentra presionada y rellena la pantalla 
	@keyboard
    A=M
	D=M
	@fillvalue
	M=-1
	@DRAW
	D;JNE
	// de otro modo limpia la pantalla
	@fillvalue
	M=0
(DRAW)
	// rellena o borra el pixel actual dependiendo del valor que tenga 
	@fillvalue
	D=M
	@current
	A=M
	M=D
	// Si el mapa de píxeles actual es el primer mapa de píxeles no queda nada por dibujar, así que vuelve a comprobar el teclado 
	@current
	D=M
	@16384
	D=D-A
	@CHECK_KEYBOARD
	D;JLE
	// disminuimos el valor de la posicion de el pixel actual 
	@current
	M=M-1
	// continua dibujando el sihuiente pixel 
	@DRAW
	0;JMP
