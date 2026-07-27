"""
Fighter Invasion - Custom Assets Track
Author: Safiyo Mohamed
Purpose: Manages the player's ship, its image, position, movement, and collisions.
Starter code: Based on Alien Invasion tutorial, forked from RedBeard41/alien_Invasion_starter
Date: July 26, 2026
"""
import pygame
from typing import TYPE_CHECKING 

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    """Represents the player's ship, handling movement, firing, and collision detection."""

    def __init__(self, game: "AlienInvasion", arsenal: 'Arsenal'):
        """Initialize the ship's image, position, and movement state."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_w, self.settings.ship_h)
        )

        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False

        self.arsenal = arsenal

    def _center_ship(self):
        """Reposition the ship to the bottom-center of the screen."""
        self.rect.midbottom = self.boundries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position and refresh its arsenal of bullets."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Calculate and apply the ship's horizontal movement based on input."""
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        """Draw the ship and its active bullets to the screen."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """Attempt to fire a bullet from the ship's arsenal."""
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group):
        """Check whether the ship has collided with a sprite group, recentering if so."""
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False