import pygame as pg
import random
from data.tools import *
from data.defaults import *
from data.scripts.animated import AnimatedSprite
from data.scripts.character import Character

TITLE = "Timestop Game"

# COLORS
GRAY = (125, 125, 125)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
LIGHTBLUE = (0, 128, 255)
BLACK = (0, 0, 0)

# directories
SRC_DIR = "resources"

# Directories
SPRITES_DIR = os.path.join(SRC_DIR, "graphics", "sprites")
BULLETS_DIR = os.path.join(SRC_DIR, "graphics", "bullets")
MAP_DIR = os.path.join(SRC_DIR, "graphics", "maps")


pg.init()
pg.display.set_caption(TITLE)
pg.display.set_mode((WIDTH, HEIGHT))


SCREEN = pg.display.get_surface()
SCREEN_RECT = SCREEN.get_rect()
CENTER = SCREEN_RECT.center
TOPRIGHT = SCREEN_RECT.topright
TOPLEFT = SCREEN_RECT.topleft
BOTTOMRIGHT = SCREEN_RECT.bottomright
BOTTOMLEFT = SCREEN_RECT.bottomleft


_FONT = os.path.join(SRC_DIR, "fonts", "RetroGaming.ttf")
BIG_FONT = pg.font.Font(_FONT, 100)
MEDIUM_FONT = pg.font.Font(_FONT, 50)
SMALL_FONT = pg.font.Font(_FONT, 25)

# Display loading
SCREEN.fill(BLACK)
loading = BIG_FONT.render("LOADING...", 0, WHITE)
SCREEN.blit(loading, loading.get_rect(center=CENTER))
pg.display.update()

SPRITES = load_spt(SPRITES_DIR)
MAPS = load_gfx(MAP_DIR)
BULLETS = load_gfx(BULLETS_DIR)

# Spritegroups
AllSprites = pg.sprite.Group()
PlayerSprite = pg.sprite.Group()
EnemySprite = pg.sprite.Group()
BulletSprites = pg.sprite.Group()
BackgroundSprites = pg.sprite.Group()

# Player Sprite
slime = AnimatedSprite(SPRITES["slime"], CENTER, 12)
PlayerSprite.add(slime)
Player = Character(slime, BULLETS["blue_bullet"], BulletSprites)
