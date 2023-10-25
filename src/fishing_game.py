import csv
import os
from random import randint

ASSETS_FOLDER = "assets"

class Fish:
    def __init__(self, name, keeper, fish, points_if_kept, points_if_released):
        self.name = name
        self.keeper = keeper
        self.fish = fish
        self.points_if_kept = points_if_kept
        self.points_if_released = points_if_released

    def __str__(self):
        return f"{self.name}, {self.keeper}, {self.fish}, {self.points_if_kept}, {self.points_if_released}"

    def read_fish_csv():
        objects = []

        file_path = os.path.join(ASSETS_FOLDER, 'fish.csv')