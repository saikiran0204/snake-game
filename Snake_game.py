from pygame import *
from random import randrange


class Cube:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        draw.rect(window, color, (
            self.x * height // number_of_rect, self.y * width // number_of_rect, height // number_of_rect - 2,
            width // number_of_rect - 2))

    def change_color(self, color):
        draw.rect(window, color, (self.x * height // number_of_rect, self.y * width // number_of_rect, height // number_of_rect - 2,width // number_of_rect - 2))
    def head_cube(self):
        draw.rect(window, GREEN, (self.x * height // number_of_rect, self.y * width // number_of_rect, height // number_of_rect - 2,width // number_of_rect - 2))
        draw.circle(window, BLACK, (self.x * height//number_of_rect+height//(number_of_rect*4), self.y*width//number_of_rect+width//(number_of_rect*4)), height//(number_of_rect*8))
        draw.circle(window, BLACK, ((self.x+1)* height//number_of_rect-height//(number_of_rect*4), self.y*width//number_of_rect+width//(number_of_rect*4)), height//(number_of_rect*8))
    def food_cube(self):
        draw.rect(window, BLACK, (self.x * height // number_of_rect, self.y * width // number_of_rect, height // number_of_rect - 2,width // number_of_rect - 2))
        draw.circle(window, RED, (self.x*(height//number_of_rect)+(height//number_of_rect//2), self.y*(width//number_of_rect)+(width//number_of_rect//2)), height//(number_of_rect*2)-2)


def create_food():
    global food
    x = randrange(0, number_of_rect)
    y = randrange(0, number_of_rect)
    if [x, y] not in snake:
        food = [x, y]
        cubes[x][y].food_cube()
    else:
        create_food()


def first():
    global window, cubes, direction, score
    window = display.set_mode((height, width))
    display.set_caption("SNAKE GAME")
    cubes = []
    color = [int(x) for x in input("Enter RBG seperated by space for initial backgound").split()]
    for i in range(number_of_rect):
        cubes.append([])
    for i in range(number_of_rect):
        for j in range(number_of_rect):
            cubes[i].append(Cube(i, j, color))
    create_food()
    for i in range(len(snake)):
        cubes[snake[i][0]][snake[i][1]].change_color(BROWN)
    running = True
    while running:
        if score == number_of_rect * number_of_rect:
            print("score:", score)
            print("winner of the snake GAME")
        for even in event.get():
            if even.type == QUIT:
                running = False
                quit()
            if even.type == MOUSEBUTTONDOWN:
                print(even.pos)
            if even.type == KEYDOWN:
                if even.key == 276 and not direction[0]:
                    direction = [0, 1, 0, 0]  # 'left'
                if even.key == 275 and not direction[1]:
                    direction = [1, 0, 0, 0]  # 'right'
                if even.key == 274 and not direction[2]:
                    direction = [0, 0, 0, 1]  # 'down'
                if even.key == 273 and not direction[3]:
                    direction = [0, 0, 1, 0]  # 'up'
        time.delay(500//score) # delay time for every movement
        temp = list(snake[0])
        if temp == food:
            create_food()
            score += 1
        else:
            if temp in snake[1:]:
                running = False
                print("Score=", score)
                quit()
            temp1 = snake.pop()
            cubes[temp1[0]][temp1[1]].change_color(BLACK)
        if direction[3] == 1:  # down
            if temp[1] == number_of_rect - 1:
                temp[1] = 0
            else:
                temp[1] += 1
        elif direction[1] == 1:  # left
            if temp[0] == 0:
                temp[0] = number_of_rect - 1
            else:
                temp[0] -= 1
        elif direction[2] == 1:  # up)
            if temp[1] == 0:
                temp[1] = number_of_rect - 1
            else:
                temp[1] -= 1
        elif direction[0] == 1:  # right
            if temp[0] == number_of_rect - 1:
                temp[0] = 0
            else:
                temp[0] += 1
        cubes[temp[0]][temp[1]].head_cube()
        snake.insert(0, temp)
        if score >= 2:
            cubes[snake[1][0]][snake[1][1]].change_color(GREEN)
        display.update()


direction = [1, 0, 0, 0]
food = None
number_of_rect =  40 #int(input("Enter number of cubes in each row:")) # setting number of cubes in each row and column
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (210, 105, 30)
snake = [[0, 0]]
width = 800  # setting the width of window
height = 800  # setting the height of the window
score = 1
first()
