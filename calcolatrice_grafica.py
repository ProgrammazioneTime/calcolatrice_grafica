import turtle

draw = turtle.Turtle()
draw.speed(0)

def disegna_assi(x, y, dim):
    #Schermo intero
    screen = turtle.Screen()
    screen.setup(width = 1.0, height = 1.0)
    
    draw.up()
    draw.color("grey")
    for i in range(-400,500,100):
        draw.goto(-500,i)
        draw.down()
        draw.fd(1000)
        draw.up()
    
    draw.rt(90)
    for i in range(-400,500,100):
        draw.goto(i,500)
        draw.down()
        draw.fd(1000)
        draw.up()
    
    draw.lt(90)
    draw.color("green")
    draw.up()
    draw.goto(0,500)
    draw.down()
        
    for i in range(y):
        draw.dot()
        draw.fd(15)
        draw.lt(180)
        draw.fd(30)
        draw.lt(180)
        draw.fd(15)
        draw.rt(90)
        draw.fd(dim)
        draw.lt(90)
    
    draw.dot()
    draw.fd(15)
    draw.lt(180)
    draw.fd(30)
    draw.lt(180)
    
    draw.up()
    draw.goto(-500,0)
    draw.down()
    
    for i in range(x):
        draw.dot()
        draw.lt(90)
        draw.fd(15)
        draw.lt(180)
        draw.fd(30)
        draw.lt(180)
        draw.fd(15)
        draw.rt(90)
        draw.fd(dim)
    
    draw.lt(90)
    draw.dot()
    draw.fd(15)
    draw.lt(180)
    draw.fd(30)
    draw.lt(90)  
    
    
    draw.down()
    
    
def disegna_grafico(g, m, q):
    turtle.tracer(0,0)
    draw.up()
    draw.goto(0,0)
    draw.color("red")
    
    proporzione = 100 * (100**(g-2))
    incremento = 0.005
    
    if g >= 0:
        partenza = 0.0
    else:
        partenza = 0.005
        
    if(g == 0):
        y = q
    else:
        temp = partenza ** g
        y = ((m * temp) / proporzione) + q
    
    draw.goto(partenza,y)
    draw.down()
    
    while partenza <= 500:
        if int(partenza) % 100 == 0:
            draw.dot()
            
        partenza = partenza + incremento
        
        if(g == 0):
            y = q
        else:
            temp = partenza ** g
            y = ((m * temp) / proporzione) + q
            
        if y >= -500 and y <= 500:
            draw.goto(partenza,y)
                
    draw.up()
    
    # Se la funzione ammette valori negativi se:
    # grado  = 0
    # grado >= 1
    # grado <= 1
    if g == 0 or g >= 1 or g <= -1:
        if g >= 0:
            partenza = 0.0
        else:
            partenza = -0.005
        
        if(g == 0):
            y = q
        else:
            temp = partenza ** g
            y = ((m * temp) / proporzione) + q
            
        draw.goto(partenza,y)
        draw.down()
            
        while partenza >= -500:
            if int(partenza) % 100 == 0 and partenza < -1:
                draw.dot()
            
            partenza = partenza - incremento
            
            if(g == 0):
                y = q
            else:
                temp = partenza ** g
                y = ((m * temp) / proporzione) + q
                
            if y >= -500 and y <= 500 and partenza >= -500 and partenza <= 500:
                draw.goto(partenza,y)
    
    turtle.update()
    
        
if __name__ == "__main__":
    # INFORMAZIONI GENERALI
    # Dimensione schermo
    # 2500x1400
    # x = 1250
    # y = 700
    # centro 0,0
    
    turtle.bgcolor("black")
    
    asse_x = 5
    asse_y = 5
    #g = 0
    #m = 0
    #q = 0
    
    # y = m * x^g + q
    
    g = float(input("Inserisci il grado -> "))
    m = float(input("Inserisci il coefficiente angolare -> "))
    q = float(input("Inserisci il termine noto -> "))
    
    disegna_assi(asse_x*2, asse_y*2, float(1000 / (asse_x*2)))
    disegna_grafico(g, m, q*100)

    turtle.exitonclick()

