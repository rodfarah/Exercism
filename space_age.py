# based on @smart-alek 's solution

class SpaceAge(object):
       

    planet_ratios = [(k, v * 31557600) for k, v in (
        ('Mercury', 0.2408467),
        ('Venus', 0.61519726),
        ('Earth', 1),
        ('Mars', 1.8808158),
        ('Jupiter', 11.862615),
        ('Saturn', 29.447498),
        ('Uranus', 84.016846),
        ('Neptune', 164.79132)
        )]

    def __init__(self, seconds):
        self.seconds = seconds
        for planet, ratio in self.planet_ratios:
            setattr(self, 'on_' + planet, self._planet_years(ratio))

    def _planet_years(self, ratio):
        return lambda ratio=ratio: round(self.seconds / ratio, 2)


print(SpaceAge(31557600).on_Mercury)