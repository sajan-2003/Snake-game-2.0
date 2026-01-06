def move_snake(snake, direction):
    """Move the snake in the given direction"""
    head_y, head_x = snake[0]

    if direction == "UP":
        new_head = [head_y - 1, head_x]
    elif direction == "DOWN":
        new_head = [head_y + 1, head_x]
    elif direction == "LEFT":
        new_head = [head_y, head_x - 1]
    elif direction == "RIGHT":
        new_head = [head_y, head_x + 1]
    else:
        new_head = [head_y, head_x]

    snake.insert(0, new_head)
    return snake

def check_collision(snake, screen_height, screen_width):
    """Return True if snake hits wall or itself"""
    head_y, head_x = snake[0]

    # Wall collision (consider border)
    if head_y <= 0 or head_y >= screen_height - 1 or head_x <= 0 or head_x >= screen_width - 1:
        return True

    # Self collision
    if [head_y, head_x] in snake[1:]:
        return True

    return False
