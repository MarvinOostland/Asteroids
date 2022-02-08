from email.mime import image
import pygame
import os

class Settings(object):
    window_width = 800
    window_height = 500
    fps = 60
    path_image = os.path.join(os.path.dirname(__file__), "images")
    title = "Asteriods"
    spaceship_size = (30, 24)
    border_size = (30)

class Background(object):
    def __init__(self, filename):
        self.image = pygame.image.load(os.path.join(
            Settings.path_image, filename))
        self.image = pygame.transform.scale(
            self.image, (Settings.window_width, Settings.window_height))
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.image_orig = pygame.image.load(os.path.join(Settings.path_image, filename)).convert_alpha()
        self.image = pygame.image.load(os.path.join(Settings.path_image, filename)).convert_alpha()
        self.image = pygame.transform.scale(self.image, Settings.spaceship_size)
        self.rect = self.image.get_rect()
        self.rect.left = Settings.window_width // 2
        self.rect.top =  Settings.window_height // 2
        self.angle = 0
        self.angle_change = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def update(self):
        pass


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Settings.window_width, Settings.window_height))
        self.clock = pygame.time.Clock()
        self.background = Background("background.jpg")
        self.spaceship = Spaceship("3.png")
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(Settings.fps)
            self.watch_for_events()
            self.draw()
            self.update()
            pygame.display.flip()
        pygame.quit() 


    def watch_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.spaceship.image = pygame.transform.rotate(self.spaceship.image, 22.5)

    def update(self):
        pass
    
    def draw(self):
        self.background.draw(self.screen)
        self.spaceship.draw(self.screen)

if __name__ == "__main__":
    os.environ["SDL_VIDEO_WINDOW_POS"] = "500, 50"

    game = Game()
    game.run()