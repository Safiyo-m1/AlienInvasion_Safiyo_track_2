"""
Fighter Invasion - Custom Assets Track
Author: Safiyo Mohamed
Purpose: Tracks game statistics such as score, high score, and remaining ships/lives.
Starter code: Based on Alien Invasion tutorial, forked from RedBeard41/alien_Invasion_starter
Date: July 26, 2026
"""
import json 
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """Tracks game statistics such as score, high score, level, and remaining ships."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize game stats and load any previously saved high score."""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """Load the saved high score from file, or create a new file if none exists."""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat().st_size > 0:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)

        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        """Save the current high score to file in JSON format."""
        scores = {
            'hi_score': self.hi_score

        }
        contents = json.dumps(scores, indent=4)

        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:

            print (f'FileNotFoundError:{e}')


    def reset_stats(self) -> None:
        """Reset ships remaining, score, and level to their starting values."""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions) -> None:
        """Update the current score, max score, and high score based on collisions."""
        self._update_score(collisions)

        self._update_max_score()

        self._update_hi_score()


    def _update_max_score(self):
        """Update the max score if the current score exceeds it."""
        if self.score > self.max_score:
            self.max_score =  self.score

    def _update_hi_score(self):
        """Update the high score and save it if the current score exceeds it."""
        if self.score > self.hi_score:
            self.hi_score =  self.score



    def _update_score(self, collisions) -> None:
        """Increase the score based on the number of aliens hit."""
        for alien in collisions.values():
            self.score += self.settings.alien_points

    def update_level(self):
        """Increase the current level by one."""
        self.level += 1 