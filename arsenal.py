"""
Fighter Invasion - Custom Assets Track
Author: Safiyo Mohamed
Purpose: Manages the ship's collection of bullets, including firing and updating them.
Starter code: Based on Alien Invasion tutorial, forked from RedBeard41/alien_Invasion_starter
Date: July 26, 2026
"""
import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Arsenal:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()


    def update_arsenal(self):
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)
        

    def draw(self):
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
        self.arsenal.add(new_bullet)
        return True
        return False 