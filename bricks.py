import pygame

# Initialize Pygame
pygame.init()
# Window dimensions
width = 800
height = 600
# Background color
bg_color = (0, 0, 0)

# Create the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaker")

# Paddle dimensions
paddle_width = 100
paddle_height = 10

# Paddle color
paddle_color = (255, 255, 255)

# Paddle position
paddle_x = (width - paddle_width) // 2
paddle_y = height - 50

# Draw the paddle on the game window
pygame.draw.rect(window, paddle_color, (paddle_x, paddle_y, paddle_width, paddle_height))

# Inside the game loop
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            paddle_x -= 5
        elif event.key == pygame.K_RIGHT:
            paddle_x += 5
# Draw the updated paddle position on the game window
pygame.draw.rect(window, paddle_color, (paddle_x, paddle_y, paddle_width, paddle_height))

# Ball dimensions
ball_radius = 10

# Ball color
ball_color = (255, 255, 255)

# Ball position
ball_x = width // 2
ball_y = height // 2

# Draw the ball on the game window
pygame.draw.circle(window, ball_color, (ball_x, ball_y), ball_radius)
# Inside the game loop
ball_x += 2
ball_y += 2

# Draw the updated ball position on the game window
pygame.draw.circle(window, ball_color, (ball_x, ball_y), ball_radius)

# Inside the game loop
# Collisions with walls
if ball_x >= width - ball_radius or ball_x <= ball_radius:
    # Reverse ball direction
    ball_x_speed *= -1
if ball_y <= ball_radius:
    # Reverse ball direction
    ball_y_speed *= -1

# Collision with paddle
if ball_y >= paddle_y - ball_radius and paddle_x - ball_radius <= ball_x <= paddle_x + paddle_width + ball_radius:
    # Reverse ball direction
     ball_y_speed *= -1

# Brick dimensions
brick_width = 80
brick_height = 20

# Brick color
brick_color = (255, 0, 0)

# Create bricks
bricks = []
for row in range(5):
    for col in range(10):
        brick_x = col * (brick_width + 10)
        brick_y = row * (brick_height + 10)
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# Draw bricks on the game window
for brick in bricks:
    pygame.draw.rect(window, brick_color, brick)

# Inside the game loop
for brick in bricks:
    if brick.collidepoint(ball_x, ball_y):
        bricks.remove(brick)
        ball_y_speed *= -1
        break

# Inside the game loop
pygame.display.flip()
pygame.time.delay(5000)

# After the game loop
if ball_y < height:
    pygame.quit()