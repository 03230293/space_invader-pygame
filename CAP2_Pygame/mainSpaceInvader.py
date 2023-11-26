#https://youtu.be/FfWpgLFMI7w

# Import modules
import math
import random
import pygame
from pygame import mixer

# Start pygame
pygame.init()

# Make the screen
screen = pygame.display.set_mode((800, 600))

# Load the background image
background = pygame.image.load('background.png')

# Load the background music
mixer.music.load("background.wav")
mixer.music.play(-1)

# Set the title and icon of the window
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Load the player image
playerImg = pygame.image.load('player.png')
playerX = 370 # Initial x-coordinate of the player
playerY = 480 # Initial y-coordinate of the player
playerX_change = 0 # Change in x-coordinate of the player

# Load the enemy images
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6 # Number of enemies

# Create enemies with random positions and speeds
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 736)) # Random x-coordinate of the enemy
    enemyY.append(random.randint(50, 150)) # Random y-coordinate of the enemy
    enemyX_change.append(4)  # Speed of the enemy in x-direction
    enemyY_change.append(40)  # Speed of the enemy in y-direction

# Load the bullet image
bulletImg = pygame.image.load('bullet.png')
bulletX = 0 # Initial x-coordinate of the bullet
bulletY = 480 # Initial y-coordinate of the bullet
bulletX_change = 0 # Change in x-coordinate of the bullet
bulletY_change = 10 # Speed of the bullet in y-direction
bullet_state = "ready" # State of the bullet: ready or fire

# Initialize the score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32) # Font for the score

textX = 10 # x-coordinate of the score text
textY = 10 # y-coordinate of the score text

# Load the game over font
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    # Render the score text
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    # Display the score text on the screen
    screen.blit(score, (x, y))


def game_over_text():
    # Render the game over text
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    # Display the game over text on the screen
    screen.blit(over_text, (200, 250))


def player(x, y):
    # Display the player image on the screen
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    # Display the enemy image on the screen
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire" # Change the bullet state to fire
    # Display the bullet image on the screen
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    # Calculate the distance between the enemy and the bullet
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    # Return True if the distance is less than 27 pixels, otherwise return False
    if distance < 27:
        return True
    else:
        return False


# Main Loop
running = True
while running:

    # Set the screen color to black
    screen.fill((0, 0, 0))
    # Display the background image on the screen
    screen.blit(background, (0, 0))
    # Handle the events in the game
    for event in pygame.event.get():
        # If the user clicks the close button, exit the game
        if event.type == pygame.QUIT:
            running = False

        # Check if a key is pressed, and if it's left, right, or space
        if event.type == pygame.KEYDOWN:
            # If the left arrow key is pressed, move the player to the left
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            # If the right arrow key is pressed, move the player to the right
            elif event.key == pygame.K_RIGHT:
                playerX_change = 5
            # If the space key is pressed, shoot the bullet
            elif event.key == pygame.K_SPACE:
                # If the bullet is ready, play the laser sound and fire the bullet
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x-coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        # Stop player movement when a key is released
        if event.type == pygame.KEYUP:
            # If the left or right arrow key is released, stop the player movement
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Change player position according to the player movement
    playerX += playerX_change

    # Keep the player within the screen boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        # If any enemy reaches the bottom of the screen, end the game
        if enemyY[i] > 440:
            # Move all the enemies off the screen
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            # Display the game over text
            game_over_text()
            break

        # Change enemy position according to the enemy speed
        enemyX[i] += enemyX_change[i]

        # Reverse the enemy direction and move it down when it reaches the edges of the screen
        if enemyX[i] <= 0 or enemyX[i] >= 736:
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_change[i]

        # Check for collision between the enemy and the bullet
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        # If there is a collision, play the explosion sound and reset the bullet and enemy positions
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            # Increase the score by one
            score_value += 1
            # Move the enemy to a random position
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        # Display the enemy on the screen
        enemy(enemyX[i], enemyY[i], i)
        
    # Bullet Movement
    # If the bullet is fired, move it up
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # If the bullet reaches the top of the screen, reset its state and position
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # Display the player on the screen
    player(playerX, playerY)
    # Display the score on the screen
    show_score(textX, textY)
    # Update the display
    pygame.display.update()
