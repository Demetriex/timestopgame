import json
import os
from itertools import chain

import pygame as pg


def load_data(basedir, directories):

    data = {}
    for dir in directories:
        data[dir] = load_json(os.path.join(basedir, dir))

    return data


def load_json(directory, accept=(".json")):

    data = {}
    for file in os.listdir(directory):
        name, ext = os.path.splitext(file)

        if ext.lower() in accept:
            with open(os.path.join(directory, file)) as f:
                data[name] = json.loads(f.read())

    return data


def load_spt(directory, colorkey=(0, 0, 0), accept=(".png", ".jpg", ".bmp")):

    graphics = {}
    gfx_group = set()

    for subdir in os.listdir(directory):
        path = os.path.join(directory, subdir)
        sprite_group = []

        for pic in os.listdir(path):
            name, ext = os.path.splitext(pic)

            if ext.lower() in accept:
                img = pg.image.load(os.path.join(path, pic))
                if img.get_alpha():
                    img = img.convert_alpha()
                else:
                    img = img.convert()
                    img.set_colorkey(colorkey)
                sprite_group.append(img)

        graphics[subdir] = sprite_group

    return graphics


def load_gfx(directory, colorkey=(0, 0, 0), accept=(".png", ".jpg", ".bmp")):

    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img

    return graphics
