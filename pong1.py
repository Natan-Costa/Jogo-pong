#Jogo pong elaborado Por Natan Costa como projeto de curso da freecodecamp

import turtle # Essa foi a biblioteca utilizada para desenvolver o jogo

wn = turtle.Screen() # Essa função chama a tela por meio de uma janela
wn.title("Pong by Natan Costa") #Título 
wn.bgcolor("black") # Cor de fundo da tela
wn.setup(width=800, height=600) # Tamanho da janela

# Pontuação -> aqui foi definido a variável utilizada para marcar o ponto
score_a = 0 
score_b = 0
# Raquete A -> variáveis que vão ser utilizadas para serem atribuidas à função de execução da raquete A
paddle_a = turtle.Turtle() # Função que vai exibir a raquete na tela
paddle_a.speed(0) # Define a velocidade de exibição da raquete
paddle_a.shape("square") # Define o formato da raquete
paddle_a.color("blue") # Define a cor da raquete
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Tamanho da raquete
paddle_a.penup() #controla a renderização
paddle_a.goto(-350, 0) # controla a posição da raquete

# Raquete B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 4 # Aqui tem somente uma coisa a mais que o comentário da raquete "A". Essa função define a velocidade do movimento da bola no eixo das abscissas 
ball.dy = 4 # Velocidade no eixo das ordenadas.

#Pen -> Vai desenhar o placar na parte superior da tela
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jogador A: 0 Jogador B: 0", align='center', font=("Impact", 24, "normal"))

#Funções

def paddle_a_up(): # Função que define o movimento da raquete para cima
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down(): # Função que define o movimento da raquete para baixo
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#Entrada do teclado
wn.listen()
wn.onkeypress(paddle_a_up, "w") # Atribui a função à execução de uma tecla
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#principal loop do jogo -> vai manter o jogo na tela de forma dinâmica
while True:
    wn.update()

    # Movimento da Bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Delimitando a borda
    if ball.ycor() > 290: # Função que define a margem da página
        ball.sety(290)
        ball.dy *=-1
    
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *=-1
   
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *=-1
        score_a += 1
        pen.clear()
        pen.write(f"Jogador A: {score_a} Jogador B: {score_b}", align='center', font=("Impact", 24, "normal")) # Função que atualiza o placar

    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *=-1
        score_b += 1
        pen.clear()
        pen.write(f"Jogador A: {score_a} Jogador B: {score_b}", align='center', font=("Impact", 24, "normal"))

    
# Batendo a Raquete na bola
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50 ): # Função que rebate a bola
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50 ):
        ball.setx(-340)
        ball.dx *= -1
   
