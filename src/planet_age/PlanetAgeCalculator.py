class PlanetAgeCalculator:
    def __init__(self):
        self.earth_age = 31557600
        self.planets = {
            "Earth": 1,
            "Mercury": 0.2408467,
            "Venus": 0.61519726,
            "Mars": 1.8808158,
            "Jupiter": 11.862615,
            "Saturn": 29.447498,
            "Uranus": 84.016846,
            "Neptune": 164.79132
        }

    def calculate_age(self, planet, age_in_sec):
        if type(age_in_sec) == int and type(planet) == str:
            if planet in self.planets and age_in_sec > 0:
                age = age_in_sec / self.planets[planet] / self.earth_age
                return round(age, 2)
            else:
                raise Exception("Error")
        else:
            raise Exception("Error")


