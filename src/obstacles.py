import random

def generate_obstacles(grid_height, grid_width, num_obstacles=5, snake=None, food=None):
    """
    Generate random obstacles on the grid.
    
    Args:
        grid_height: Height of the game grid
        grid_width: Width of the game grid
        num_obstacles: Number of obstacles to create
        snake: List of snake segments to avoid
        food: Food position to avoid
    
    Returns:
        List of obstacle positions [[y, x], ...]
    """
    if snake is None:
        snake = []
    
    obstacles = []
    attempts = 0
    max_attempts = 100
    
    while len(obstacles) < num_obstacles and attempts < max_attempts:
        obs = [random.randint(1, grid_height - 2),
               random.randint(1, grid_width - 2)]
        
        # Avoid placing obstacles on snake, food, or where obstacles already exist
        if obs not in snake and obs != food and obs not in obstacles:
            obstacles.append(obs)
        
        attempts += 1
    
    return obstacles

def add_obstacle(obstacles, position):
    """Add a single obstacle at the given position."""
    if position not in obstacles:
        obstacles.append(position)
    return obstacles

def remove_obstacle(obstacles, position):
    """Remove an obstacle at the given position."""
    if position in obstacles:
        obstacles.remove(position)
    return obstacles

def check_obstacle_collision(snake_head, obstacles):
    """
    Check if snake head collides with any obstacle.
    
    Args:
        snake_head: [y, x] position of snake head
        obstacles: List of obstacle positions
    
    Returns:
        True if collision detected, False otherwise
    """
    return snake_head in obstacles
