import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = row_index * TILESIZE
                y = col_index * TILESIZE
                if col == 'x':
                    Tile((y,x),[self.visible_sprites, self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((y,x),[self.visible_sprites], self.obstacles_sprites)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(1000,0)
    
    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - (self.display_surface.get_size()[0] / 2)
        self.offset.y = player.rect.centery - (self.display_surface.get_size()[1] / 2)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)