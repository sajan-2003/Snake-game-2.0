#snake logic (movement, collisions)
def move_snake(snake, direction):
    """Move snake in the given direction."""
    head = snake[0].copy()
    if direction == "DOWN":
        head[0] += 1
    elif direction == "UP":
        head[0] -= 1
    elif direction == "LEFT":
        head[1] -= 1
    elif direction == "RIGHT":
        head[1] += 1
    snake.insert(0, head)
    return snake

def check_collision(snake, screen_height, screen_width):
    """Check if snake hits wall or itself."""
    head = snake[0]
    if head in snake[1:] or head[0] in [0, screen_height] or head[1] in [0, screen_width]:
        return True
    return False
