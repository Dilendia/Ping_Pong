# Importing libraries
from pgu import gui
import pygame
import sys
# Initializing Pygame
pygame.init()
# Setting constants for the game
SCORE=5
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 450
FPS = 60
speed_av = 1
# Defining the Paddle class: position (x,y), size (width, height), color, speed (vertical)
class Player:
    def __init__(self,color,x,y,width,height,speed):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.score = 0

    # Class implementation here
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))

    def move_down(self):
            if self.y <= SCREEN_HEIGHT - self.height:
                self.y += self.speed

    def move_up(self):
            if self.y >= 0:
                self.y -= self.speed




# Defining the Ball class: position (x,y), size (radius), color, speed (horizontal, vertical)
class Ball:
    def __init__(self, color, x, y, radius, speedx, speedy):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speedx = speedx
        self.speedy = speedy
# Class implementation here

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def ballmove(self, p1, p2):
        self.y += self.speedy
        self.x += self.speedx

        # Up and Down borders
        if self.y >= SCREEN_HEIGHT - self.radius or self.y <= self.radius:
            self.speedy = -self.speedy

        if self.x >= p2.x - self.radius - p2.width and p2.y <= self.y <= p2.y + p2.height:
            self.speedx = -self.speedx
            self.speedx -= speed_av

        if self.x <= p1.x + self.radius and p1.y <= self.y <= p1.y + p1.height:
            self.speedx = -self.speedx
            self.speedx += speed_av


def draw_score(screen, player1, player2):
    font = pygame.font.Font(None, 74)
    text = font.render(f"{player1.score}:{player2.score}", True, "black", "white")
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 10))

def create_popup(player1, player2, screen, clock):
    if player1.score == SCORE:
        label = gui.Label("Player 1 is the winner!")
    elif player2.score == SCORE:
        label = gui.Label("Player 2 is the winner!")

    btn_restart = gui.Button("Restart Game")
    btn_quit = gui.Button("Quit Game")

    def close_popup(event=None):
        pygame.quit()
        sys.exit()

    def restart_game():
        player1 = Player((0, 0, 255), 5, 160, 5, 150, 5)
        player2 = Player((255, 0, 0), 690, 160, 5, 150, 5)
        ballik = Ball((255, 255, 0), 350, 225, 20, 5, 5)
        game(screen, clock, player1, player2, ballik)

    btn_restart.connect(gui.CLICK, restart_game)
    btn_quit.connect(gui.CLICK, close_popup)
    main_table = gui.Table(width=300, height=200)
    main_table.tr()
    main_table.td(label, colspan=2)
    main_table.tr()
    main_table.td(btn_restart, colspan=1)
    main_table.td(btn_quit, colspan=1)

    dialog = gui.Dialog(gui.Label("Game Over"), main_table)
    dialog.open()
    app = gui.Desktop()
    app.init(widget=dialog, screen=screen, area=screen.get_rect())
    app.run()


# Game loop function
def game(screen, clock, player1, player2, ballik):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                player1.move_up()
            if keys[pygame.K_s]:
                player1.move_down()

            if keys[pygame.K_UP]:
                player2.move_up()
            if keys[pygame.K_DOWN]:
                player2.move_down()

            if ballik.x > SCREEN_WIDTH:
                player1.score += 1
                ballik.x = SCREEN_WIDTH // 2
                ballik.y = SCREEN_HEIGHT // 2
                ballik.speedx = 3
                ballik.speedy = 3

            elif ballik.x < 0:
                player2.score += 1
                ballik.x = SCREEN_WIDTH // 2
                ballik.y = SCREEN_HEIGHT // 2
                ballik.speedx = 3
                ballik.speedy = 3

            if player1.score == SCORE or player2.score == SCORE:
                create_popup(player1, player2, screen, clock)
                return

            ballik.ballmove(player1, player2)

            screen.fill((0, 33, 55))
            player1.draw(screen)
            player2.draw(screen)
            ballik.draw(screen)
            draw_score(screen, player1, player2)
            pygame.display.flip()
            clock.tick(FPS)
# Main function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Ping Pong')
    clock = pygame.time.Clock()
    player1 = Player((0, 0, 255), 5, 160, 5, 150, 10)
    player2 = Player((255, 0, 0), 690, 160, 5, 150, 10)
    ballik = Ball((255, 255, 0), 350, 225, 20, 3, 3)
    game(screen, clock, player1, player2, ballik)

if __name__ == '__main__':
    main()

