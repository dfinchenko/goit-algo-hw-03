import turtle

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)

def main():
    t = turtle.Turtle()
    t.speed(0)

    # Позиціонування
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    order = int(input("Введіть рівень рекурсії: "))
    size = 300

    # Створення трьох сторін
    for _ in range(3):
        koch(t, order, size)
        t.right(120)

    turtle.done()

if __name__ == "__main__":
    main()