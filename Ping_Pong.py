import turtle

#pantalla del juego
wn = turtle.Screen()
wn.title("Ping Pong")
wn.setup(width=800, height=600)
wn.bgcolor("black")
wn.tracer(0)

#jugadores
MarcadorA = 0
MarcadorB = 0

#caracteristicas jugador A
JugadorA = turtle.Turtle()
JugadorA.speed(0)
JugadorA.shape("square")
JugadorA.color("white")
JugadorA.penup()
JugadorA.goto(-350,0)
JugadorA.shapesize(stretch_wid=5, stretch_len=1)  

#caracteristicas jugador B 
JugadorB = turtle.Turtle()
JugadorB.speed(0)
JugadorB.shape("square")
JugadorB.color("white")
JugadorB.penup()
JugadorB.goto(350, 0)
JugadorB.shapesize(stretch_wid=5, stretch_len=1)  

#linea de division
division = turtle.Turtle()
division.color("white")
division.goto(0,450)
division.goto(0,-450)

#carteles donde diga jugadorA y jugadorB
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write('Jugador A: 0          Jugador B: 0', align="center", font=("arial", 24))

#pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)

#velocidad de la pelota
pelota.dy = 0.5
pelota.dx = 0.5

#funciones para el movimiento de los jugadores
def JugadorA_up():
    y = JugadorA.ycor()
    y += 20
    JugadorA.sety(y)
 
def JugadorA_down():
    y = JugadorA.ycor()
    y -= 20
    JugadorA.sety(y)
    
def JugadorB_up():
    y = JugadorB.ycor()
    y += 20
    JugadorB.sety(y)

def JugadorB_down():
    y = JugadorB.ycor()
    y -= 20
    JugadorB.sety(y)
    
#conectar con el teclado
wn.listen()
wn.onkeypress(JugadorA_up, "w")   
wn.onkeypress(JugadorA_down, "s") 
wn.onkeypress(JugadorB_up, "Up") 
wn.onkeypress(JugadorB_down, "Down")

 
# Bucle principal del juego
while True:
    # Actualizar la pantalla
     wn.update()
     #movimiento de la pelota
     pelota.setx(pelota.xcor() + pelota.dx)
     pelota.sety(pelota.ycor() + pelota.dy)
     
     #colisiones con los bordes de arriba y abajo
     if pelota.ycor() > 290:
         pelota.sety(290)
         pelota.dy *= -1
         MarcadorA += 1
         texto.clear()
         texto.write('JugadorA : {} 		JugadorB : {}'.format(MarcadorA, MarcadorB),
			align = 'center', font = ('Courier', 24, 'normal'))
         
         
     if pelota.ycor() < -290:
         pelota.sety(-290)
         pelota.dy *= -1
         MarcadorB += 1
         texto.clear()
         texto.write('JugadorA : {} 		JugadorB : {}'.format(MarcadorA, MarcadorB),
			align = 'center', font = ('Courier', 24, 'normal'))
         
         
     #colisiones con los bordes de izquierda y derecha
     if pelota.xcor() > 390:
         pelota.goto(0,0)
         pelota.dx *= -1
         
     if pelota.xcor() < -390:
         pelota.goto(0,0)
         pelota.dx *= -1
    
    #colisiones de los jugadores con la pelota
     if ((pelota.xcor() > 330 and pelota.xcor() < 340) and
     (pelota.ycor() < JugadorB.ycor() + 50 and pelota.ycor() > JugadorB.ycor() - 50)):
         pelota.setx(330)
         pelota.dx *= -1

     if ((pelota.xcor() < -330 and pelota.xcor() > -340) and
         (pelota.ycor() < JugadorA.ycor() + 50 and pelota.ycor() > JugadorA.ycor() - 50)):
         pelota.setx(-330)
         pelota.dx *= -1
         
         
         
    
         
