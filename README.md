# Deber3_PA
1. GOL
Para meter gol en el campo de futbol tiene que mover las flechas, puede abrir el programa desde la consola
utilizamos la libreria de tkinter que nos sirve para utilizar objetos graficos multimedia en este caso imagenes.gif
Para utilizar canvas debemos indicar la coordenada en donde se posiiciona el grafico 
anchor establecer el origen de coordenadas de la imagen, NW quiere decir que el origen se encuentra en la esquina superior izquierda.
keysym es una cadena que es el nombre simbólico de la clave (solo para eventos de teclado) 

2. Nombre 
en este caso debemos ir formando las letras deseadas, importamos la libreria turtle; es un cursor al que se le pueden dar órdenes de movimiento (avance, retroceso o giro) y que puede ir dejando un rastro sobre la pantalla; 
Creamos un lapiz con turtle.pen()
para avanzar utilizamos forward y la distancia deseada forward(distancia)
para girar utilizamos left o right (Izquierda y derecha) y en los parametros ponemos los grados que queremos que el cursos gire, recuerde que esta en una  escala de 360° : left(90), right(135)
para levantar el lapiz utilizamos penup()
y para volver a escribir pendown()
