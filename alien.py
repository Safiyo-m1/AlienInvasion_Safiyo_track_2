"""
Fighter Invasion - Custom Assets Track
Author: Safiyo Mohamed
Purpose: Represents an individual alien sprite, including its image and position.
Starter code: Based on Alien Invasion tutorial, forked from RedBeard41/alien_Invasion_starter
Date: July 26, 2026
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

class Alien(Sprite):
    """Represents a single alien sprite, including its image, position, and movement."""

    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """Initialize the alien's image and position within the fleet."""
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
                    (self.settings.alien_w, self.settings.alien_h)
                    )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)


    def update(self):
        """Update the alien's horizontal position based on the fleet's direction and speed."""
        temp_speed = self.settings.fleet_speed


        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """Check whether the alien has reached the left or right edge of the screen."""
        return(self.rect.right >= self.boundries.right or self.rect.left <= self.boundries.left)


    def draw_alien(self):
        """Draw the alien to the screen."""
        self.screen.blit(self.image, self.rect) 