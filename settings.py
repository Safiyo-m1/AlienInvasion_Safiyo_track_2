"""
Fighter Invasion - Custom Assets Track
Author: Safiyo Mohamed
Purpose: Defines game settings including screen size, asset file paths, and difficulty scaling.
Starter code: Based on Alien Invasion tutorial, forked from RedBeard41/alien_Invasion_starter
Date: July 26, 2026
"""
from pathlib import Path


class Settings:
    """Stores all static and dynamic settings for the Alien Invasion game."""

    def __init__(self):
        """Initialize the game's static and default settings, including file paths for assets."""
        self.name: str = 'Fighter Invasion - Track 2'
        self.screen_w = 1000
        self.screen_h = 700
        self.FPS = 60
        self.bg_file = Path.cwd()/ 'Assets'/ 'images' / 'back2.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd()/ 'Assets'/ 'file' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'Images' / 'fighter.png'
        self.ship_w = 40
        self.ship_h = 40

        self.bullet_file = Path.cwd()/ 'Assets'/ 'images' / 'blasterbolt.png'
        self.laser_sound = Path.cwd()/ 'Assets'/ 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd()/ 'Assets'/ 'sound' / 'impactSound.mp3'

        self.alien_file = Path.cwd()/ 'Assets'/ 'images' / 'enemy_4.png'
        self.alien_w = 50
        self.alien_h = 80
        self.fleet_direction = 1

        self.button_w = 200
        self.button_h = 60
        self.button_color = (0,135,50)

        self.text_color = (225, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() /'assets' / 'Fonts' / 'Silkscreen' / 'silkscreen-Bold.ttf'

    def initialize_dynamic_settings(self):
        """Reset settings that change during gameplay, such as speed and difficulty."""
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.starting_ship_count = 3
        self.ship_speed = 5

        self.fleet_speed = 5
        self.fleet_drop_speed = 40
        self.alien_points = 50

    def increase_difficulty(self):
        """Increase game difficulty by scaling ship, bullet, and fleet speed."""
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale 