# Copyright (c) 2020 by Nucleartaxi

#script to import outfitted ships from save file
#Output stats to CSV

#Imports
import math
from math import sqrt
import time
import glob
import random
import os

def roundup1000(x):
    return int(math.ceil(x / 1000.0)) * 1000
def roundup100(x):
    return int(math.ceil(x / 100.0)) * 100
def roundup10(x):
    return int(math.ceil(x / 10.0)) * 10
def roundup5(x):
    return int(math.ceil(x / 5.0)) * 5

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#Deletes Files
#filelist = glob.glob(os.path.join("output/", "*.txt"))
#for f in filelist:
#    os.remove(f)

#Ships
def create_ship():
    generate_ships_config = open(ship_config_file, "r")
    ship_output = open("output/ships " + ship_output_file, "w")
    #Searches config file for values and creates variables
    for line in generate_ships_config: #Creates vars from txt file
        if "ship_seed" in line:
            ship_seed = next(generate_ships_config)
            random.seed(int(ship_seed))

        if "ship_category" in line:
            ship_category = next(generate_ships_config).strip('\n')

        if "ship_type_amount" in line:
            ship_type_amount = next(generate_ships_config)

        if "ship_min_cost" in line:
            ship_min_cost = next(generate_ships_config)
        if "ship_max_cost" in line:
            ship_max_cost = next(generate_ships_config)
        if "ship_min_shields" in line:
            ship_min_shields = next(generate_ships_config)
        if "ship_max_shields" in line:
            ship_max_shields = next(generate_ships_config)
        if "ship_min_hull" in line:
            ship_min_hull = next(generate_ships_config)
        if "ship_max_hull" in line:
            ship_max_hull = next(generate_ships_config)
        if "ship_min_crew_percent" in line:
            ship_min_crew_percent = next(generate_ships_config)
        if "ship_max_crew_percent" in line:
            ship_max_crew_percent = next(generate_ships_config)
        if "ship_min_bunks" in line:
            ship_min_bunks = next(generate_ships_config)
        if "ship_max_bunks" in line:
            ship_max_bunks = next(generate_ships_config)
        if "ship_min_mass" in line:
            ship_min_mass = next(generate_ships_config)
        if "ship_max_mass" in line:
            ship_max_mass = next(generate_ships_config)
        if "ship_min_drag" in line:
            ship_min_drag = next(generate_ships_config)
        if "ship_max_drag" in line:
            ship_max_drag = next(generate_ships_config)
        if "ship_min_heat_dissipation" in line:
            ship_min_heat_dissipation = next(generate_ships_config)
        if "ship_max_heat_dissipation" in line:
            ship_max_heat_dissipation = next(generate_ships_config)
        if "ship_min_fuel_capacity" in line:
            ship_min_fuel_capacity = next(generate_ships_config)
        if "ship_max_fuel_capacity" in line:
            ship_max_fuel_capacity = next(generate_ships_config)
        if "ship_min_cargo_space" in line:
            ship_min_cargo_space = next(generate_ships_config)
        if "ship_max_cargo_space" in line:
            ship_max_cargo_space = next(generate_ships_config)
        if "ship_min_outfit_space" in line:
            ship_min_outfit_space = next(generate_ships_config)
        if "ship_max_outfit_space" in line:
            ship_max_outfit_space = next(generate_ships_config)
        if "ship_min_weapon_capacity" in line:
            ship_min_weapon_capacity = next(generate_ships_config)
        if "ship_max_weapon_capacity" in line:
            ship_max_weapon_capacity = next(generate_ships_config)
        if "ship_min_engine_capacity" in line:
            ship_min_engine_capacity = next(generate_ships_config)
        if "ship_max_engine_capacity" in line:
            ship_max_engine_capacity = next(generate_ships_config)

        if "ship_min_guns" in line:
            ship_min_guns = next(generate_ships_config)
        if "ship_max_guns" in line:
            ship_max_guns = next(generate_ships_config)
        if "ship_min_turrets" in line:
            ship_min_turrets = next(generate_ships_config)
        if "ship_max_turrets" in line:
            ship_max_turrets = next(generate_ships_config)
        if "ship_min_fighters" in line:
            ship_min_fighters = next(generate_ships_config)
        if "ship_max_fighters" in line:
            ship_max_fighters = next(generate_ships_config)
        if "ship_min_drones" in line:
            ship_min_drones = next(generate_ships_config)
        if "ship_max_drones" in line:
            ship_max_drones = next(generate_ships_config)

        if "ship_blast_radius_multiplier" in line:
            ship_blast_radius_multiplier = next(generate_ships_config)
        if "ship_shield_damage_multiplier" in line:
            ship_shield_damage_multiplier = next(generate_ships_config)
        if "ship_hull_damage_multiplier" in line:
            ship_hull_damage_multiplier = next(generate_ships_config)
        if "ship_hit_force_multiplier" in line:
            ship_hit_force_multiplier = next(generate_ships_config)

        if "ship_leak_leak" in line:
            ship_leak_leak = next(generate_ships_config)
        if "ship_leak_flame" in line:
            ship_leak_flame = next(generate_ships_config)
        if "ship_leak_big_leak" in line:
            ship_leak_big_leak = next(generate_ships_config)

        if "ship_explode_tiny" in line:
            ship_explode_tiny = next(generate_ships_config)
        if "ship_explode_small" in line:
            ship_explode_small = next(generate_ships_config)
        if "ship_explode_medium" in line:
            ship_explode_medium = next(generate_ships_config)
        if "ship_explode_large" in line:
            ship_explode_large = next(generate_ships_config)
        if "ship_explode_huge" in line:
            ship_explode_huge = next(generate_ships_config)
        if "ship_final_explode" in line:
            ship_final_explode = next(generate_ships_config).strip()




#        if "" in line:
#             = next(generate_ships_config)

    ship_types_generated_count = 1
    while ship_types_generated_count <= int(ship_type_amount):
        #Calculates new values
        ship_cost = roundup1000(random.randint(int(ship_min_cost), int(ship_max_cost)))
        ship_shields = roundup100(random.randint(int(ship_min_shields), int(ship_max_shields)))
        ship_hull = roundup100(random.randint(int(ship_min_hull), int(ship_max_hull)))

        ship_required_crew_percent = round((random.uniform(float(ship_min_crew_percent), float(ship_max_crew_percent))), 1)
        ship_bunks = random.randint(int(ship_min_bunks), int(ship_max_bunks))
        ship_required_crew = round(ship_bunks * ship_required_crew_percent)

        ship_mass = roundup10(random.randint(int(ship_min_mass), int(ship_max_mass)))
        ship_drag = round(random.uniform(float(ship_min_drag), float(ship_max_drag)), 1)
        ship_heat_dissipation = round(random.uniform(float(ship_min_heat_dissipation), float(ship_max_heat_dissipation)), 1)
        ship_fuel_capacity = roundup100(random.randint(int(ship_min_fuel_capacity), int(ship_max_fuel_capacity)))
        ship_cargo_space = roundup5(random.randint(int(ship_min_cargo_space), int(ship_max_cargo_space)))
        ship_outfit_space = roundup10(random.randint(int(ship_min_outfit_space), int(ship_max_outfit_space)))
        ship_weapon_capacity = roundup10(random.randint(int(ship_min_weapon_capacity), int(ship_max_weapon_capacity)))
        ship_engine_capacity = roundup10(random.randint(int(ship_min_engine_capacity), int(ship_max_engine_capacity)))

        ship_guns = round(random.randint(int(ship_min_guns), int(ship_max_guns)))
        ship_turrets = round(random.randint(int(ship_min_turrets), float(ship_max_turrets)))
        ship_fighters = round(random.randint(int(ship_min_fighters), int(ship_max_fighters)))
        ship_drones = round(random.randint(int(ship_min_drones), int(ship_max_drones)))

        ship_blast_radius =round((ship_shields + ship_hull) * .01 * float(ship_blast_radius_multiplier))
        ship_shield_damage = roundup10((ship_shields + ship_hull) * .10 * float(ship_shield_damage_multiplier))
        ship_hull_damage = roundup10((ship_shields + ship_hull) * .05 * float(ship_hull_damage_multiplier))
        ship_hit_force =  roundup10((ship_shields + ship_hull) * .15 * float(ship_hit_force_multiplier))


        #ship Name
        ship_name = random.choice(letters) + random.choice(letters) + random.choice(letters)
        ship_name_int = str(random.choice(numbers)) + str(random.choice(numbers)) + str(random.choice(numbers))
        ship_name = str(ship_name) + "-" + str(ship_name_int)

        print("Created ship " + ship_name)

        #Writes ES code to file, use \n for line break
        ship_output.write('ship "' + ship_name + '"\n')
        ship_output.write('\tsprite "' + str("ship/sparrow") + '"\n')
        ship_output.write('\tthumbnail "' + str("thumbnail/sparrow") + '"\n')
        ship_output.write('\tattributes \n')
        ship_output.write('\t\tcategory "' + ship_category + '"\n')
        ship_output.write('\t\t"cost" ' + str(ship_cost) + "\n")
        ship_output.write('\t\t"shields" ' + str(ship_shields) + "\n")
        ship_output.write('\t\t"hull" ' + str(ship_hull) + "\n")
        ship_output.write('\t\t"required crew" ' + str(ship_required_crew) + "\n")
        ship_output.write('\t\t"bunks" ' + str(ship_bunks) + "\n")
        ship_output.write('\t\t"mass" ' + str(ship_mass) + "\n")
        ship_output.write('\t\t"drag" ' + str(ship_drag) + "\n")
        ship_output.write('\t\t"heat dissipation" ' + str(ship_heat_dissipation) + "\n")
        ship_output.write('\t\t"fuel capacity" ' + str(ship_fuel_capacity) + "\n")
        ship_output.write('\t\t"cargo space" ' + str(ship_cargo_space) + "\n")
        ship_output.write('\t\t"outfit space" ' + str(ship_outfit_space) + "\n")
        ship_output.write('\t\t"weapon capacity" ' + str(ship_weapon_capacity) + "\n")
        ship_output.write('\t\t"engine capacity" ' + str(ship_engine_capacity) + "\n")
        ship_output.write('\t\tweapon ' + "\n")
        ship_output.write('\t\t\t"blast radius" ' + str(ship_blast_radius) + "\n")
        ship_output.write('\t\t\t"shield damage" ' + str(ship_shield_damage) + "\n")
        ship_output.write('\t\t\t"hull damage" ' + str(ship_hull_damage) + "\n")
        ship_output.write('\t\t\t"hit force" ' + str(ship_hit_force) + "\n")
        ship_output.write('\t\toutfits ' + "\n")
        #ship_output.write('          ' + str() + " " + str() + "\n")
        ship_output.write("\n")
        ship_output.write('\t\tengine 0 35' + "\n")

        i = 0
        while i < ship_guns:
            ship_output.write('\t\tgun 0 0' + "\n")
            i += 1
        i = 0
        while i < ship_turrets:
            ship_output.write('\t\tturret 0 0' + "\n")
            i += 1
        i = 0
        while i < ship_fighters:
            ship_output.write('\t\tfighter 0 0' + "\n")
            i += 1
        i = 0
        while i < ship_drones:
            ship_output.write('\t\tdrone 0 0' + "\n")
            i += 1
    #####
        ship_output.write('\t\tleak "leak" ' + str(ship_leak_leak))
        ship_output.write('\t\tleak "flame" ' + str(ship_leak_flame))
        ship_output.write('\t\tleak "big leak" ' + str(ship_leak_big_leak))

        ship_output.write('\t\texplode "tiny explosion" ' + str(ship_explode_tiny))
        ship_output.write('\t\texplode "small explosion" ' + str(ship_explode_small))
        ship_output.write('\t\texplode "medium explosion" ' + str(ship_explode_medium))
        ship_output.write('\t\texplode "large explosion" ' + str(ship_explode_large))
        ship_output.write('\t\texplode "huge explosion" ' + str(ship_explode_huge))
        ship_output.write('\t\t"final explode" "' + str(ship_final_explode) + '"' + "\n")

        ship_output.write('\t\tdescription ""')



        ship_output.write('\n')

        ship_types_generated_count += 1

    generate_ships_config.close()
    ship_output.close()



def load_ship_configs():

    ship_configs_list = glob.glob("config/ship config/*.txt") #Imports files in directory
    ship_configs_amount = len(ship_configs_list) #Gets amount of items in list
    ship_configs_iterations = 0

    while ship_configs_iterations < ship_configs_amount: #Creates ships for each config files
        global ship_config_file #Config File
        ship_config_file = str(ship_configs_list[ship_configs_iterations]).replace("\\", "/")
        global ship_output_file #Output file
        ship_output_file = str(ship_configs_list[ship_configs_iterations]).replace("\\", "/").replace("config/ship config/", "")


        create_ship()


        print("\n")
        ship_configs_iterations += 1



load_ship_configs()

input()