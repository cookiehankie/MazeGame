import pygame
import config
import math


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
        self.friction = 0.9
        # in the game Coordinate System, clockwise angle
        self.forward_angle = 0
        self.image = pygame.transform.rotate(self.image, -self.forward_angle)

        self.rotate_velocity_limit = 140
        self.rotate_velocity = 0  # Angular velocity

    def update_delta_time(self):
        cur_time = pygame.time.get_ticks()
        self.delta_time = (cur_time - self.last_time) / 1000
        self.last_time = cur_time

    def input(self):
        # W&S: Move forward and backward
        # A&D: Turn left and right
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self.move_velocity += self.move_acc * self.delta_time
            self.move_velocity = min(self.move_velocity_limit, self.move_velocity)
        elif key_pressed[pygame.K_s]:
            self.move_velocity -= self.move_acc * self.delta_time
            self.move_velocity = max(-self.move_velocity_limit, self.move_velocity)
        else:
            self.move_velocity = int(self.move_velocity * self.friction)
        sign = 1
        if self.move_velocity < 0:
            sign = -1
        # turn
        if key_pressed[pygame.K_d]:
            self.rotate_velocity = self.rotate_velocity_limit * sign
        elif key_pressed[pygame.K_a]:
            self.rotate_velocity = -self.rotate_velocity_limit * sign
        else:
            self.rotate_velocity = 0

    def rotate(self):
        self.forward_angle += self.rotate_velocity * self.delta_time

        self.image = pygame.transform.scale(self.image_source, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, -self.forward_angle)
        self.image.set_colorkey("black")

        # make a NORMAL turning
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def move(self):
        if abs(self.move_velocity) > 50:
            self.rotate()  # angle changes only when velocity != 0
        vx = self.move_velocity * math.cos(math.pi * self.forward_angle / 180)
        vy = self.move_velocity * math.sin(math.pi * self.forward_angle / 180)

        self.rect.x += vx * self.delta_time
        self.rect.y += vy * self.delta_time

        # self.rect.y += 200 * self.delta_time

    def update(self):
        self.update_delta_time()
        self.input()
        self.move()
