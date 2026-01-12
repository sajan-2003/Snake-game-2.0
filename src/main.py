import pygame # type: ignore
import sys
from snake import move_snake, check_collision
from food import spawn_food

# Game constants
GRID_WIDTH = 20  # Grid cells
GRID_HEIGHT = 20
CELL_SIZE = 30  # Pixels per cell
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE + 50  # Extra space for score
GAME_SPEED = 10  # FPS

# Colors (RGB)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 155, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("🐍 Snake Game")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 50)
        self.font_small = pygame.font.Font(None, 30)
        self.reset_game()

    def reset_game(self):
        self.snake = [[GRID_HEIGHT//2, GRID_WIDTH//4], 
                      [GRID_HEIGHT//2, GRID_WIDTH//4-1], 
                      [GRID_HEIGHT//2, GRID_WIDTH//4-2]]
        self.food = spawn_food(self.snake, GRID_HEIGHT, GRID_WIDTH)
        self.current_direction = "RIGHT"
        self.score = 0
        self.game_over = False

    def handle_events(self):
        opposite_directions = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                key_directions = {
                    pygame.K_UP: "UP",
                    pygame.K_DOWN: "DOWN",
                    pygame.K_LEFT: "LEFT",
                    pygame.K_RIGHT: "RIGHT",
                    pygame.K_w: "UP",
                    pygame.K_s: "DOWN",
                    pygame.K_a: "LEFT",
                    pygame.K_d: "RIGHT",
                }
                
                if event.key in key_directions:
                    new_direction = key_directions[event.key]
                    if new_direction != opposite_directions[self.current_direction]:
                        self.current_direction = new_direction
                
                if event.key == pygame.K_q and self.game_over:
                    return False
                if event.key == pygame.K_SPACE and self.game_over:
                    self.reset_game()
        
        return True

    def update(self):
        if not self.game_over:
            self.snake = move_snake(self.snake, self.current_direction)
            
            if check_collision(self.snake, GRID_HEIGHT, GRID_WIDTH):
                self.game_over = True
            
            if self.snake[0] == self.food:
                self.score += 1
                self.food = spawn_food(self.snake, GRID_HEIGHT, GRID_WIDTH)
            else:
                self.snake.pop()

    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw grid
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, (40, 40, 40), (x, 0), (x, SCREEN_HEIGHT - 50))
        for y in range(0, SCREEN_HEIGHT - 50, CELL_SIZE):
            pygame.draw.line(self.screen, (40, 40, 40), (0, y), (SCREEN_WIDTH, y))
        
        # Draw snake
        for i, (y, x) in enumerate(self.snake):
            rect = pygame.Rect(x * CELL_SIZE + 1, y * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2)
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(self.screen, color, rect)
        
        # Draw food
        food_rect = pygame.Rect(self.food[1] * CELL_SIZE + 1, self.food[0] * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2)
        pygame.draw.circle(self.screen, RED, food_rect.center, CELL_SIZE // 2 - 2)
        
        # Draw score
        score_text = self.font_small.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, SCREEN_HEIGHT - 40))
        
        # Draw game over screen
        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - 50))
            overlay.set_alpha(200)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            game_over_text = self.font_large.render("GAME OVER", True, RED)
            score_final_text = self.font_small.render(f"Final Score: {self.score}", True, WHITE)
            restart_text = self.font_small.render("Press SPACE to restart or Q to quit", True, WHITE)
            
            self.screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, SCREEN_HEIGHT//4))
            self.screen.blit(score_final_text, (SCREEN_WIDTH//2 - score_final_text.get_width()//2, SCREEN_HEIGHT//2))
            self.screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, SCREEN_HEIGHT//2 + 60))
        
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(GAME_SPEED)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
