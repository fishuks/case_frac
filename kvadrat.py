import turtle

def draw_square(size, depth):
    """
    Function for drawing square.
    :param depth: recursion depth
    :param size: step length
    :return:
    """
    if depth > 0:
        for _ in range(4):
            turtle.forward(size)
            turtle.right(90)
        turtle.fd(size*0.1)
        turtle.right(10)
        draw_square(size*0.93, depth - 1)

def main():
    """
    Main function for drawing square.
    :return:
    """
    depth = int(input('Глубина рекурсии:'))
    size = int(input('Длина стороны:'))
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()

    draw_square(size, depth)

if __name__ == '__main__':
    main()