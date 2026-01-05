#food generation
import random

def spawn_food(snake, screen_height, screen_width):
    """Generate food position not on the snake."""
    food = None
    while food is None:
        nf = [random.randint(1, screen_height-2), random.randint(1, screen_width-2)]
        if nf not in snake:
            food = nf
    return food
