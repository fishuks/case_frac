import turtle

def draw_square(length, depth):
    """
    Function for drawing square.
    :param depth: recursion depth
    :param length: step length
    :return:
    """
    if depth > 0:
        for _ in range(4):
            turtle.forward(length)
            turtle.right(90)
        turtle.right(45)
        draw_square(length * 0.707, depth - 1)
def main():
    depth = int(input('Глубина рекурсии:'))
    length  = int(input('Длина стороны:'))
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()

    draw_square(length, depth)

if __name__ == '__main__':
    """
    Main function for drawing square.
    :return:
    """
    main()