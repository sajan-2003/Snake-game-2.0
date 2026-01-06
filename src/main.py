import curses
from snake import move_snake, check_collision
from food import spawn_food

SCREEN_HEIGHT = 20
SCREEN_WIDTH = 60
SNAKE_CHAR = '#'
FOOD_CHAR = '*'
GAME_SPEED = 100

def play_game(screen):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    sh, sw = SCREEN_HEIGHT, SCREEN_WIDTH
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(True)
    w.timeout(GAME_SPEED)

    w.border()

    snake = [[sh//2, sw//4], [sh//2, sw//4-1], [sh//2, sw//4-2]]
    food = spawn_food(snake, sh, sw)
    current_direction = "RIGHT"
    score = 0

    key_directions = {
        curses.KEY_DOWN: "DOWN", curses.KEY_UP: "UP",
        curses.KEY_LEFT: "LEFT", curses.KEY_RIGHT: "RIGHT",
        ord('s'): "DOWN", ord('w'): "UP",
        ord('a'): "LEFT", ord('d'): "RIGHT"
    }

    opposite_directions = {"UP": "DOWN","DOWN": "UP","LEFT": "RIGHT","RIGHT": "LEFT"}

    while True:
        # Display score
        w.addstr(0, 2, f'Score: {score} ')

        next_key = w.getch()
        if next_key != -1:
            new_direction = key_directions.get(next_key)
            if new_direction and new_direction != opposite_directions[current_direction]:
                current_direction = new_direction

        # Move snake
        snake = move_snake(snake, current_direction)

        # Check collision
        if check_collision(snake, sh, sw):
            w.clear()
            w.border()
            w.addstr(sh//2, sw//2 - 5, "GAME OVER")
            w.addstr(sh//2 + 1, sw//2 - 7, f"Score: {score}")
            w.addstr(sh//2 + 3, sw//2 - 14, "Press any key to replay, Q to quit")
            w.refresh()

            # Wait for key press
            while True:
                key = w.getch()
                if key != -1:
                    if key in [ord('q'), ord('Q')]:
                        return False  # quit game
                    else:
                        return True   # replay

        # Check food
        if snake[0] == food:
            score += 1
            food = spawn_food(snake, sh, sw)
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        # Draw snake
        for y, x in snake:
            w.addch(y, x, SNAKE_CHAR, curses.color_pair(1))

        # Draw food
        w.addch(food[0], food[1], FOOD_CHAR, curses.color_pair(2))

def main(screen):
    while True:
        replay = play_game(screen)
        if not replay:
            break  # exit main loop

curses.wrapper(main)
