# Real Life Survival Simulator!
import random
import sys
import time

biome = ['Forest','Desert','Snowy Area','Swamp']

food = ['fish','meat','berries']

forest_predators = ['bears','wolves','coyotes','foxes']

desert_predators = ['snakes','vultures','coyotes','bobcats']

snowy_predators = ['wolves','bears','tigers']

swamp_predators = ['alligators','mosquitos']

forest_shelter = ['cave','tree','hut']

desert_shelter = ['hut','small cave']

snow_shelter = ['igloo','cave']

swamp_shelter = ['cave','tree','hut']

how_long = ['1 day', '2 days','3 days','4 days','5 days','6 days','1 week','2 weeks','3 week', '1 month']

biome_choice = random.choice(biome)
food_choice = random.choice(food)
how_long_choice = random.choice(how_long)

if biome_choice == 'Forest':
	predator_choice = random.choice(forest_predators)
	shelter_choice = random.choice(forest_shelter)
if biome_choice == 'Desert':
	predator_choice = random.choice(desert_predators)
	shelter_choice = random.choice(desert_shelter)
if biome_choice == 'Snowy Area':
	predator_choice = random.choice(snowy_predators)
	shelter_choice = random.choice(snow_shelter)
if biome_choice == 'Swamp':
	predator_choice = random.choice(swamp_predators)
	shelter_choice = random.choice(swamp_shelter)
def live():
	live_choice = random.randint(1,4)
	if live_choice == 4:
		print('You did not Survive, Cause of Death: The ' + food_choice + ' was poisionous')
	if live_choice == 3:
		print('You did not Survive, Cause of Death: ' + predator_choice + ' attacked you!')
	if live_choice == 2:
		print('You did not Survive, Cause of Death: Water Pollution')
	if live_choice == 1:
	   print('You survived! The ' + food_choice + ' were a good source of food and the ' + predator_choice + ' left you alone')

def main():
   print('SURVIVAL')
   print('')
   print('You are lost in a ' + biome_choice)
   print('You are living in a ' + shelter_choice)
   print('Your main food source is ' + food_choice)
   print('The main predator in the surrounding area are ' + predator_choice)
   print(how_long_choice + ' later')
   live()
main()
	
	
	
		
		
		


