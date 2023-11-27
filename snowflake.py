import turtle

def koch_curve(size, n):
    """
    Function for drawing Koch_curve.
    :param n: recursion depth
    :param size: step length
    :return:
    """
    if n == 0:
        turtle.forward(size)
    else:
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
        turtle.right(120)
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)

def draw_koch_snowflake(size, n):
    """
    Function for drawing koch snowflake.
    :param n: recursion depth
    :param size: step length
    :return:
    """
    turtle.speed(10)
    for i in range(3):
        koch_curve(size, n)
        turtle.right(120)

def main():
    """
    Main function for drawing koch snowflake.
    :return:
    """
    n = int(input('Глубина рекурсии:'))
    size = int(input('Длина стороны:'))
    draw_koch_snowflake(size,n)

if __name__ == '__main__':
    main()