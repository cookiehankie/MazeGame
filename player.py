import pygame
import config


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 50
        self.image_source = pygame.image.load("static/images/car.png").convert()
        self.image = pygame.transform.scale(self.image_source, (self.width, self.height))
        self.image.set_colorkey("black")
        # self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2)
        self.last_time = pygame.time.get_ticks()  # current time: ms
        self.delta_time = 0  # time consumed within every 2 frames

        self.move_velocity_limit = 220
        self.move_velocity = 0  # current speed
        self.move_acc = 600  # increase speed 600 for every second
        self.friction = 0.99

    def update_delta_time(self):
        cur_time = pygame.time.get_ticks()
        self.delta_time = (cur_time - self.last_time) / 1000
        self.last_time = cur_time

    def input(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            pass
        elif key_pressed[pygame.K_s]:
            pass
        elif key_pressed[pygame.K_a]:
            self.move_velocity -= self.move_acc * self.delta_time
            self.move_velocity = max(-self.move_velocity_limit, self.move_velocity)
        elif key_pressed[pygame.K_d]:
            self.move_velocity += self.move_acc * self.delta_time
            self.move_velocity = min(self.move_velocity_limit, self.move_velocity)
        else:
            self.move_velocity = int(self.move_velocity * self.friction)

    def move(self):
        self.rect.x += self.move_velocity * self.delta_time
        # self.rect.y += 200 * self.delta_time

    def update(self):
        self.update_delta_time()
        self.input()
        self.move()
