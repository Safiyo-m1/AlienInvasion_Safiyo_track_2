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
    """Manages the ship's collection of bullets, including firing, updating, and drawing them."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the arsenal's sprite group for holding bullets."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()


    def update_arsenal(self):
        """Update all bullets in the arsenal and remove any that have left the screen."""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Remove bullets from the arsenal once they move above the top of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)


    def draw(self):
        """Draw every active bullet in the arsenal to the screen."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Fire a new bullet if the arsenal hasn't reached its maximum capacity."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
        self.arsenal.add(new_bullet)
        return True
        return False 