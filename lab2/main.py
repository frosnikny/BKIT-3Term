import random
import math
from turtle import write_docstringdict
import pygame
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def py_game():
    pygame.init()

    #s = pygame.mixer.Sound("bird.mp3")

    width = 400
    heigth = 500

    apple_width = 10
    apple_heigth = 10

    square_width = 60
    square_heigth = 60

    screen = pygame.display.set_mode((width, heigth))
    done = False
    color_red = (255, 0, 0)
    color_white = (255, 255, 255)
    color_black = (0, 0, 0)

    x = 0
    x_last = 0
    y = 0
    y_last = y

    apple_x = x + square_width + (width - x - square_width)/2
    apple_last_x = apple_x
    apple_y = y + square_heigth/2
    apple_last_y = apple_y

    k = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Итоговый счёт: {k}")
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y -= 3
        if pressed[pygame.K_DOWN]:
            y += 3
        if pressed[pygame.K_LEFT]:
            x -= 3
        if pressed[pygame.K_RIGHT]:
            x += 3
        # Скорость по диагонали
        if not (pressed[pygame.K_UP] and pressed[pygame.K_DOWN]) and \
             not (pressed[pygame.K_LEFT] and pressed[pygame.K_RIGHT]):
            if pressed[pygame.K_UP] and pressed[pygame.K_LEFT]:
                x += 3-math.sqrt(3)
                y += 3-math.sqrt(3)
            if pressed[pygame.K_UP] and pressed[pygame.K_RIGHT]:
                x -= 3-math.sqrt(3)
                y += 3-math.sqrt(3)
            if pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:
                x += 3-math.sqrt(3)
                y -= 3-math.sqrt(3)
            if pressed[pygame.K_DOWN] and pressed[pygame.K_RIGHT]:
                x -= 3-math.sqrt(3)
                y -= 3-math.sqrt(3)

        if x + square_width > width:
            x = width - square_width
        if x < 0:
            x = 0
        if y + square_heigth > heigth:
            y = heigth - square_heigth
        if y < 0:
            y = 0

        if ((x+square_width >= apple_x+apple_width/2) and (x <= apple_x+apple_width/2)
                and (y+square_heigth >= apple_y+apple_heigth/2) and (y <= apple_y+apple_heigth/2)) or (k == 0):
            # Generate apple coords
            while (x+square_width >= apple_x+apple_width/2) and (x <= apple_x+apple_width/2) \
                    and (y+square_heigth >= apple_y+apple_heigth/2) and (y <= apple_y+apple_heigth/2):
                apple_x = random.randrange(width-apple_width)
                apple_y = random.randrange(heigth-apple_heigth)
            k += 1
            # s.play()
            if k == 50:
                dog_surf = pygame.image.load('dog.png')
                dog_rect = dog_surf.get_rect(width=width)
                screen.blit(dog_surf, dog_rect)
                
                pygame.display.update()
            print(f"Вы съели яблоко. Итого: {k}")

        pygame.draw.rect(screen, color_black, pygame.Rect(
            apple_last_x, apple_last_y, apple_width, apple_heigth))
        pygame.draw.rect(screen, color_red, pygame.Rect(
            apple_x, apple_y, apple_width, apple_heigth))
        apple_last_x = apple_x
        apple_last_y = apple_y

        pygame.draw.rect(screen, color_black, pygame.Rect(
            x_last, y_last, square_width, square_heigth))
        pygame.draw.rect(screen, color_white, pygame.Rect(
            x, y, square_width, square_heigth))
        x_last = x
        y_last = y

        pygame.time.wait(7)
        pygame.display.flip()


def main():
    r = Rectangle("синего", 15, 15)
    c = Circle("зеленого", 15)
    s = Square("красного", 15)
    print(r)
    print(c)
    print(s)
    if input("Запустить игру? (1/0)") == "1":
        py_game()


if __name__ == "__main__":
    main()
