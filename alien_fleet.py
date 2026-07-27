"""
Fighter Invasion - Custom Assets Track
Author: Safiyo Mohamed
Purpose: Manages the fleet of aliens, including creation, movement, and collision detection.
Starter code: Based on Alien Invasion tutorial, forked from RedBeard41/alien_Invasion_starter
Date: July 26, 2026
"""
import pygame
from typing import TYPE_CHECKING
from alien import Alien
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """Manages the fleet of aliens, including creation, movement, and collisions."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the fleet's sprite group, direction, and drop speed, then create the fleet."""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """Calculate fleet dimensions and offsets, then build the rectangular alien fleet."""
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w = (screen_w//alien_w)

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offset(alien_w, alien_h, screen_w, fleet_w, fleet_h)


        self.create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Create aliens in a rectangular grid pattern, skipping alternating rows and columns."""
        for row in range (fleet_h):
            for col in range (fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset

                if col % 2 == 0 or row % 2 == 0:
                    continue

                self._create_alien(current_x, current_y)

    def calculate_offset(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """Calculate the x and y offset needed to center the fleet on screen."""
        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space= fleet_h * alien_h
        x_offset = int((screen_w-fleet_horizontal_space)//2)
        y_offset = int((half_screen-fleet_vertical_space)//2)
        return x_offset,y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """Calculate how many aliens fit horizontally and vertically based on screen size."""
        fleet_w =(screen_w//alien_w)
        fleet_h = ((screen_h /2)//alien_h)


        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h %2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2



        return int (fleet_w), int(fleet_h)

    def _create_alien(self, current_x: int, current_y: int):
        """Create a single alien at the given position and add it to the fleet."""
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """Check if any alien has reached the screen edge, and drop and reverse the fleet if so."""
        alien:Alien
        for alien in self.fleet:
            if alien .check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1

                break

    def _drop_alien_fleet(self):
        """Move the entire fleet down by the drop speed."""
        for alien in (self).fleet:
             print('here')
             alien.y += self.fleet_drop_speed
    def update_fleet(self):
        """Check fleet edges and update the position of all aliens."""
        self._check_fleet_edges()
        self.fleet.update()


    def draw(self):
        """Draw every alien in the fleet to the screen."""
        alien:'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Check for collisions between the fleet and another sprite group, removing both on hit."""
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_bottom(self):
        """Check whether any alien has reached the bottom of the screen."""
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False

    def check_destroyed_status(self):
        """Check whether the entire fleet has been destroyed."""
        return not self.fleet 