# Given an age in seconds, calculate how old someone would be on:

#     Mercury: orbital period 0.2408467 Earth years
#     Venus: orbital period 0.61519726 Earth years
#     Earth: orbital period 1.0 Earth years, 365.25 Earth days, or 31557600 seconds
#     Mars: orbital period 1.8808158 Earth years
#     Jupiter: orbital period 11.862615 Earth years
#     Saturn: orbital period 29.447498 Earth years
#     Uranus: orbital period 84.016846 Earth years
#     Neptune: orbital period 164.79132 Earth years

chrono = {
    'Mercury': 0.2408467,
    'Venus': 0.61519726,
    'Earth': 1.0,
    'Mars': 1.8808158,
    'Jupiter': 11.862615,
    'Saturn': 29.447498,
    'Uranus': 84.016846,
    'Neptune': 164.79132,
}


def convertion(second):
    years = second / 60 / 60 / 24 / 365.25
    return years


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return round(convertion(self.seconds) / chrono['Mercury'] , 2)

    def on_venus(self):
        return round(convertion(self.seconds) / chrono['Venus'] , 2)

    def on_earth(self):
        return round(convertion(self.seconds) / chrono['Earth'] , 2)

    def on_mars(self):
        return round(convertion(self.seconds) / chrono['Mars'] , 2)

    def on_jupiter(self):
        return round(convertion(self.seconds) / chrono['Jupiter'] , 2)

    def on_saturn(self):
        return round(convertion(self.seconds) / chrono['Saturn'] , 2)

    def on_uranus(self):
        return round(convertion(self.seconds) / chrono['Uranus'] , 2)

    def on_neptune(self):
        return round(convertion(self.seconds) / chrono['Neptune'] , 2)


print(SpaceAge(2134835688).on_mercury())
