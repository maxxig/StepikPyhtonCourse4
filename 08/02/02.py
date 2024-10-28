from enum import Enum
class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, code):
        translations = {
            "WINTER": {"en": "winter", "ru": "зима"},
            "SPRING": {"en": "spring", "ru": "весна"},
            "SUMMER": {"en": "summer", "ru": "лето"},
            "FALL": {"en": "fall", "ru": "осень"}
        }
        return translations[self.name][code]

# TEST_2:
for season in Seasons:
    print(season.text_value('en'), '->', season.text_value('ru'))

# TEST_3:
for season in Seasons:
    print(season.name, season.value)