animals_sounds = {
    'Dog': 'Bow Wow',
    'Cat': 'Meow',
    'Cow': 'Moo',
    'Sheep': 'Meeee',
    'Duck': 'Quack',
    'Frog': 'Kokak',
    'Squirel': 'Squick',
    'Lion': 'Roar'
}


print("Animals and their sounds:", animals_sounds)


fourth_animal = list(animals_sounds.keys())[3]  
print("Sound of the 4th animal ({}): {}".format(fourth_animal, animals_sounds[fourth_animal]))


seventh_animal = list(animals_sounds.keys())[6] 
animals_sounds[seventh_animal] = 'HAHAHA'
print("Updated sound of the 7th animal ({}): {}".format(seventh_animal, animals_sounds[seventh_animal]))

fifth_animal = list(animals_sounds.keys())[4] 
del animals_sounds[fifth_animal]
print("Deleted the 5th animal ({}).".format(fifth_animal))

print("Last key-value pair in the dictionary:", list(animals_sounds.items())[-1])