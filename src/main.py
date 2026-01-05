#main entry point, runs the game

import curses
from snake import move_snake, check_collision
from food import spawn_food

# Game settings
SCREEN_HEIGHT = 20
SCREEN_WIDTH = 60
SNAKE_CHAR = '#'
FOOD_CHAR = '*'
GAME_SPEED = 100  # milliseconds

def main(screen):
    curses.curs_set(0)  # hide cursor
    sh, sw = SCREEN_HEIGHT, SCREEN_WIDTH
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(GAME_SPEED)

    # Initial snake
    snake = [[sh//2, sw//4], [sh//2, sw//4-1], [sh//2, sw//4-2]]

    # Initial food
    food = spawn_food(snake, sh, sw)
    w.addch(food[0], food[1], FOOD_CHAR)

    key = curses.KEY_RIGHT
    score = 0

    directions = {
        curses.KEY_DOWN: "DOWN",
        curses.KEY_UP: "UP",
        curses.KEY_LEFT: "LEFT",
        curses.KEY_RIGHT: "RIGHT"
    }

    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        # Move snake
        snake = move_snake(snake, directions.get(key, "RIGHT"))

        # Check collision
        if check_collision(snake, sh, sw):
            curses.endwin()
            print(f"Game Over! Score: {score}")
            break

        # Check if food eaten
        if snake[0] == food:
            score += 1
            food = spawn_food(snake, sh, sw)
            w.addch(food[0], food[1], FOOD_CHAR)
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        # Draw snake head
        w.addch(snake[0][0], snake[0][1], SNAKE_CHAR)

curses.wrapper(main)

