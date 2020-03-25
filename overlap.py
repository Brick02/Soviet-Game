import pygame as pg
from pygame.locals import *
pg.display.init()
screen = pg.display.set_mode((1000,800))
cache_img = {}
cache_mask = {}
cache_rect = {}

def cache(item,type):
    if type==1:  
        if item in cache_img:
            return cache_img[item]
        if item not in cache_img:
            cache_img[item]=pg.image.load(item)
            return cache_img[item]
    if type==2:
        if item in cache_mask:
            return cache_mask[item]
        if item not in cache_mask:
            cache_mask[item]= pg.mask.from_surface(cache_img[item], 50)
            return cache_mask[item]
    if type==3:
        if item in cache_rect:
            return cache_rect[item]
        if item not in cache_rect:
            cache_rect[item] = cache_img[item].get_rect()
            return cache_rect[item]
Range = 100 
def collisions(x1,y1,x2,y2,Img1,Img2):
    if round(((x2 - x1)**2 + (y2 - y1)**2)**0.5)>Range:
        return False
    
    terrain1 = cache(Img1,1)
    balloon =  cache(Img2,1)
    
    terrain1_mask = cache(Img1,2)
    balloon_mask = cache(Img2,2)

    terrain1_rect = cache(Img1,3)
    balloon_rect = cache(Img2,3)
  
    terrain1_rect[0] = x2
    terrain1_rect[1] = y2
    balloon_rect.x = x1
    balloon_rect.y = y1
    bx, by = (balloon_rect[0], balloon_rect[1])
    offset_x = bx - terrain1_rect[0]
    offset_y = by - terrain1_rect[1]
    overlap = terrain1_mask.overlap(balloon_mask, (offset_x, offset_y))
    last_bx, last_by = bx, by
    if overlap:
        return True
