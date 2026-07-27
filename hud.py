import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class HUD:

    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.settings = game.settings
        self.game_stats = game.game_stats

        self.font = pygame.font.Font(self.settings.font_file, self.settings.HUD_font_size)
        self.padding = 20

        self._update_max_score()
        self._update_hi_score()
        self._update_score()
        self._update_level()

    def _update_max_score(self):
        max_score_str = f"Max Score: {self.game_stats.max_score:,}"
        self.max_score_image = self.font.render(max_score_str, True, self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_hi_score(self):
        hi_score_str = f"Hi-Score: {self.game_stats.hi_score:,}"
        self.hi_score_image = self.font.render(hi_score_str, True, self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.centerx = self.boundaries.centerx
        self.hi_score_rect.top = self.padding

    def _update_score(self):
        score_str = f"Score: {self.game_stats.score:,}"
        self.score_image = self.font.render(score_str, True, self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + 10

    def _update_level(self):
        level_str = f"Level: {self.game_stats.level}"
        self.level_image = self.font.render(level_str, True, self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.padding

    def _draw_ships(self):
        current_x = self.padding
        current_y = self.level_rect.bottom + 10
        ship_image = pygame.image.load(self.settings.ship_file)
        ship_image = pygame.transform.scale(
            ship_image, (self.settings.ship_w // 2, self.settings.ship_h // 2)
        )
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(ship_image, (current_x, current_y))
            current_x += ship_image.get_width() + 10

    def update_scores(self):
        self._update_max_score()
        self._update_hi_score()
        self._update_score()
        self._update_level()

    def draw(self):
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_ships() 