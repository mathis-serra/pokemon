import pygame
from pathlib import Path


class Settings:
    def __init__(self):
        project_root = Path(__file__).resolve().parents[2]
        font_path = project_root / "Data/Game/Font/pokemon-emerald.ttf"
        if not font_path.exists():
            raise FileNotFoundError(f"Font not found: {font_path}")
        self.font_pokemon = pygame.font.Font(str(font_path), 36)