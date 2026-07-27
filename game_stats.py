import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():

    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self) -> None:
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions) -> None:
        # update score
        self._update_score(collisions)

        # update max_score
        self._updtae_max_score()


    def _updtae_max_score(self):
        if self.score > self.max_score:
            self.max_score =  self.score

        

    def _update_score(self, collisions) -> None:
        for alien in collisions.values():
            self.score += self.settings.alien_points

        def update_level(self):
            self.level += 1 
        