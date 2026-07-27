"""
Fighter Invasion - Custom Assets Track
Author: Safiyo Mohamed
Purpose: Represents the Play button, including its appearance and click detection.
Starter code: Based on Alien Invasion tutorial, forked from RedBeard41/alien_Invasion_starter
Date: July 26, 2026
"""
import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
class Button:
    """Represents a clickable Play button, including its appearance and label."""

    def __init__(self, game: 'AlienInvasion', msg) -> None:
        """Initialize the button's size, position, font, and label text."""
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file,
            self.settings.button_font_size)
        self.rect = pygame.Rect(0,0,self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg) -> None:
        """Render the button's message text and center it within the button."""
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self) -> None:
        """Draw the button's background and label text to the screen."""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos) -> bool:
        """Check whether the given mouse position is within the button's bounds."""
        return self.rect.collidepoint(mouse_pos) 