import pygame
import random
### Author: Soulacex ###

"""DISCLAIMER: 
    The game is still a work in progress! It's a very simple imatation of the popular 2013 mobile game, "Flappy Bird".
"""


class FlappyBird:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set the window properties
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Flappy Bird")

        # Create the game clock
        self.clock = pygame.time.Clock()

        # Create the game panel
        self.panel = GamePanel(self)

        # Run the game loop
        self.run_game_loop()

    def run_game_loop(self):
        # Run the game loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.panel.handle_event(event)

            # Update the game state
            self.panel.update()

            # Draw the game elements
            self.panel.draw(self.screen)

            # Update the game window
            pygame.display.flip()

            # Limit the frame rate
            self.clock.tick(60)

class GamePanel:
    def __init__(self, game):
        # Initialize game variables here
        self.game = game

        # Set the panel properties
        self.width = 600
        self.height = 800
        self.background_color = (255, 255, 255)

    def handle_event(self, event):
        # Handle key press and release events here
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Handle the space key press here
                pass
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                # Handle the space key release here
                pass

    def update(self):
        # Update game variables here
        pass

    def draw(self, screen):
        # Clear the screen
        screen.fill(self.background_color)

        # Draw game elements here
        screen.blit(self.bird_image, (self.bird_x, self.bird_y))
        screen.blit(self.pipe_image, (self.pipe_x, self.pipe_y))

class GamePanel:
    def __init__(self, game):
        # Initialize game variables here
        self.game = game
        self.bird_x = 50
        self.bird_y = 50
        self.pipe_x = 500
        self.pipe_y = 0
        self.bird_image = pygame.image.load("bird.png")
        self.pipe_image = pygame.image.load("pipe.png")

    def handle_event(self, event):
        # Handle key press and release events here
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Handle the space key press here
                pass
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                # Handle the space key release here
                pass

    def update(self):
        # Update game variables here
        self.bird_x += 1
        self.pipe_x -= 1

        if self.pipe_x < -100:
            self.pipe_x = 500
            self.pipe_y = random.randint(0, 600)

    def draw(self, screen):
        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the game elements
        screen.blit(self.bird_image, (self.bird_x, self.bird_y))
        screen.blit(self.pipe_image, (self.pipe_x, self.pipe_y))

def main():
    # Create an instance of the FlappyBird game
    game = FlappyBird()

if __name__ == "__main__":
    main()