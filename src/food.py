import random

def spawn_food(snake, screen_height, screen_width):
    """Return new food coordinates not on the snake"""
    while True:
        food = [random.randint(1, screen_height - 2),
                random.randint(1, screen_width - 2)]
        if food not in snake:
            return food
