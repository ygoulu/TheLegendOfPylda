import pygame
from settings import WORLD_MAP, TILESIZE
from tile import Tile
from player import Player


class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x_axis = col_index * TILESIZE
                y_axis = row_index * TILESIZE
                if col == 'x':
                    Tile((x_axis, y_axis), [self.visible_sprites,
                         self.obstacles_sprites])
                if col == 'p':
                    self.player = Player(
                        (x_axis, y_axis), [
                            self.visible_sprites], self.obstacles_sprites)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(1000, 0)

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - \
            (self.display_surface.get_size()[0] / 2)
        self.offset.y = player.rect.centery - \
            (self.display_surface.get_size()[1] / 2)

        for sprite in sorted(self.sprites(),
                             key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)


def debug(info, x_axis=10 ,  y_axis=10):
    font = pygame.font.Font(None, 30)
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x_axis, y_axis))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)
