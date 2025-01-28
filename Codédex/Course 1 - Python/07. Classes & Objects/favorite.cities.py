class City: 
  def __init__(self, name, mayor, age, founding_year, country, population, landmarks):
    self.name = name
    self.mayor = mayor
    self.age = age
    self.founding_year = founding_year
    self.country =country
    self.population = population
    self.landmarks = landmarks

nyc = City("New York City", "Eric Adams", 400, 1624, "USA", 8468000, ["Statue of Liberty", "Brooklyn Bridge", "Apollo Theatre"])
print(vars(nyc))
