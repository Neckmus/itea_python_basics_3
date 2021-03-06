from random import randint, choice
from characters import CHARACTERS, ENEMIES
from game_objects import GAME_OBJECTS
from game_map import GameMap


def get_trapped(character):

    print('You got trapped')
    damage = randint(5, 25)
    character.get_damaged(damage)


def get_healed(character):

    print('You got healed')
    hp = randint(5, 25)
    character.get_healed(hp)


def fight_with_enemy(character, enemy):

    is_won = True

    while True:

        character.fight(enemy)

        if character.is_dead():
            is_won = False
            break
        elif enemy.is_dead():
            break

    return is_won


print('Welcome to my game!')
name = input('Enter your name: ')
race = input('Choose race [Human, Orc, Elf]: ')
level = input('Difficulty [Hard, Medium, Easy]: ')

if level == 'Hard':
    objects = [choice(GAME_OBJECTS)() for i in range(4)]
    enemies = [choice(ENEMIES)() for i in range(3)]
    objects += enemies
elif level == 'Medium':
    objects = ['trap', 'trap', 'enemy', 'heal']
elif level == 'Easy':
    objects = ['trap', 'enemy', 'heal', 'heal']

x, y = randint(0, 4), randint(0, 4)
char = CHARACTERS[race](name, x, y)
char.show_stats()

game_map = GameMap(5, 5, objects)
game_map.put_char(char, *char.get_coords())

while True:

    print(game_map)
    input('Move? ')
    situation = choice(situations)

    if situation == 'trap':
        
        get_trapped(char)
        if char.is_dead():
            break
        
    elif situation == 'heal':
        
        get_healed(char)
        
    elif situation == 'enemy':
        
        print('ENEMY!!!')
        enemy = choice(ENEMIES)()
        is_won = fight_with_enemy(char, enemy)

        if not is_won:
            break

print('Sorry, you lost.')
print('Game Over')

    
