zoo = ('red panda', 'elephant', 'capybara', 'wombat')
zoo.index('elephant')


for value in zoo:
    if value == 'elephant':
        print('it\'s in there')


(lizard, fox, mammoth, something) = zoo
print(fox)

animal_list = list(zoo)

animal_list.extend(['panda', 'bear'])

zoo = tuple(animal_list)

print(zoo)