# Importing libraries
import pygame
import sys

# Initializing Pygame
pygame.init()

# Setting constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 450
FPS = 60

# Defining the Paddle class: position (x,y), size (width, height), color, speed (vertical)
class Player:
    def __init__(self,color,x,y,width,height,speed):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    # Class implementation here
    def draw(self,screen):
    # def draw(self, screen,color,x,y,width,height):
        # self.screen = screen
        # self.color = color
        # self.x = x
        # self.y = y
        # self.width = width
        # self.height = height
        pygame.draw.rect(screen,(self.color),(self.x,self.y,self.width,self.height),)

    # def move_down(self):


# Defining the Ball class: position (x,y), size (radius), color, speed (horizontal, vertical)
class Ball:
    def __init__(self,color,x,y,radius):
        self.x = x
        self.y = y
        self.color=color
        self.radius = radius

    # Class implementation here
    def draw(self, screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

# Game loop function
def game(screen, clock):
    player1 = Player("Blue",0, 160, 100, 150, 30)
    player2=Player("Red",600,160,100,150,30)
    ballik=Ball("yellow",350,225,35)
    # here should be initialization objects: player_left, player_right, ball
    # player_left = Player()
    # player_right = Player()
    # ball = Ball()

    while True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                sys.exit()
            # here you should Handle players movement
            screen.fill((0,33,55))
            # player1.draw(screen, "Blue", 0, 160, 100, 150)
            # player2.draw(screen, "Red", 600, 160, 100, 150)
            player1.draw(screen)
            player2.draw(screen)
            ballik.draw(screen)
            #here you should draw objects
            # player_left.draw(screen)
            # player_right.draw(screen)
            # ball.draw(screen)

            pygame.display.flip()
            clock.tick(FPS)

# Main function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Ping Pong')
    clock = pygame.time.Clock()
    game(screen, clock)

if __name__ == '__main__':
    main()