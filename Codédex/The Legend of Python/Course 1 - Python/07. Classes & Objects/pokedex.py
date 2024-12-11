class Pokemon:
    def __init__(self, entry, name, types, description, is_caught, height, habitat):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
        self.height = height
        self.habitat = habitat

    def speak(self):
        print(self.name + "!")

    def display_details(self):
        print('Entry Number: ' + str(self.entry))
        print('Name: ' + self.name)

        if len(self.types) == 1:
            print('Type: ' + self.types[0])
        else:
            print('Type: ' + '/'.join(self.types))

        print('Description: ' + self.description)

        if self.is_caught:
            print(self.name + ' has already been caught!')
        else:
            print(self.name + ' hasn\'t been caught yet.')

        print("Height:", self.height)
        print("Habitat: " + self.habitat)


# Ajustando os argumentos na ordem correta
pikachu = Pokemon(
    25, 'Pikachu', ['Electric'],
    'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.',
    True, 0.4, 'Forest'
)

charizard = Pokemon(
    6, 'Charizard', ['Fire', 'Flying'],
    'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.',
    False, 1.7, 'Mountain'
)

# Chamando os métodos
pikachu.speak()
pikachu.display_details()
print()
charizard.speak()
charizard.display_details()