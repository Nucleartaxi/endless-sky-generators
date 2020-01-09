# Copyright (c) 2020 by Nucleartaxi

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


#Consolodate outfits into 1 outfit file per config file eg. "outfits"

#Outfits
def create_battery():
    generate_outfits_config = open(outfit_config_file, "r")
    battery_output = open("output/outfits " + outfit_output_file, "a")
    #Searches config file for values and creates variables
    for line in generate_outfits_config: #Creates vars from txt file
        if "outfit_seed" in line:
            outfit_seed = next(generate_outfits_config)
            random.seed(int(outfit_seed))

        if "battery_type_amount" in line:
            battery_type_amount = next(generate_outfits_config)
        if "battery_iterations" in line:
            battery_iterations = next(generate_outfits_config)
        if "battery_cost_curve" in line:
            battery_cost_curve = next(generate_outfits_config)
        if "battery_outfit_curve" in line:
            battery_outfit_curve = next(generate_outfits_config)
        if "battery_energy_curve" in line:
            battery_energy_curve = next(generate_outfits_config)

        if "battery_min_start_cost" in line:
            battery_min_start_cost = next(generate_outfits_config)
        if "battery_max_start_cost" in line:
            battery_max_start_cost = next(generate_outfits_config)
        if "battery_min_outfit_space" in line:
            battery_min_outfit_space = next(generate_outfits_config)
        if "battery_max_outfit_space" in line:
            battery_max_outfit_space = next(generate_outfits_config)

        if "battery_min_energy" in line:
            battery_min_energy = next(generate_outfits_config)
        if "battery_max_energy" in line:
            battery_max_energy = next(generate_outfits_config)

    battery_types_generated_count = 1
    while battery_types_generated_count <= int(battery_type_amount):

        #Calculates new values
        battery_cost = roundup100(random.randint(int(battery_min_start_cost), int(battery_max_start_cost)))
        battery_outfit = random.randint(int(battery_min_outfit_space), int(battery_max_outfit_space))
        battery_energy = roundup10(random.randint(int(battery_min_energy), int(battery_max_energy)))

        #Battery Name
        battery_name = random.choice(letters) + random.choice(letters) + random.choice(letters)
        battery_name_int = str(random.choice(numbers)) + str(random.choice(numbers)) + str(random.choice(numbers))
        battery_name = str(battery_name) + "-" + str(battery_name_int)

        battery_iterations_count = 1
        while battery_iterations_count <= int(battery_iterations):
            #Writes ES code to file, use \n for line break
            battery_output.write('outfit "' + battery_name + ' Battery"' + "\n")
            battery_output.write('\tcategory "Power"\n')
            battery_output.write('\tcost ' + str(battery_cost) + "\n")
            battery_output.write('\tthumbnail "outfit/tiny battery"\n')
            battery_output.write('\t"mass" ' + str(battery_outfit) + "\n")
            battery_output.write('\t"outfit space" -' + str(battery_outfit) + "\n")
            battery_output.write('\t"energy capacity" ' + str(battery_energy) + "\n")
            battery_output.write('\tdescription "Battery"\n')
            battery_output.write('\n')

            outfitter_output.write('\t"' + battery_name + " Battery" + '"\n')

            #Name
            battery_name = ''.join([c for c in battery_name if c not in "1234567890"])
            battery_name_int = int(battery_name_int) + int(battery_name_int)
            battery_name = battery_name + str(battery_name_int)
            print("Created battery " + battery_name + " Battery")

            #Iterate for next run of loop
            battery_cost = roundup100((battery_cost * 2) * float(battery_cost_curve))
            battery_outfit = round((battery_outfit * 2) * float(battery_outfit_curve))
            battery_energy = roundup10((battery_energy * 2) * float(battery_energy_curve))

            battery_iterations_count += 1
        battery_types_generated_count += 1
    battery_output.write('\n')
    generate_outfits_config.close()
    battery_output.close()
def create_cooling():
    generate_outfits_config = open(outfit_config_file, "r")
    cooling_output = open("output/outfits " + outfit_output_file, "a")
    #Searches config file for values and creates variables
    for line in generate_outfits_config: #Creates vars from txt file
        if "cooling_type_amount" in line:
            cooling_type_amount = next(generate_outfits_config)

        if "cooling_iterations" in line:
            cooling_iterations = next(generate_outfits_config)
        if "cooling_cost_curve" in line:
            cooling_cost_curve = next(generate_outfits_config)
        if "cooling_outfit_curve" in line:
            cooling_outfit_curve = next(generate_outfits_config)
        if "cooling_cooling_curve" in line:
            cooling_cooling_curve = next(generate_outfits_config)

        if "cooling_min_start_cost" in line:
            cooling_min_start_cost = next(generate_outfits_config)
        if "cooling_max_start_cost" in line:
            cooling_max_start_cost = next(generate_outfits_config)
        if "cooling_min_outfit_space" in line:
            cooling_min_outfit_space = next(generate_outfits_config)
        if "cooling_max_outfit_space" in line:
            cooling_max_outfit_space = next(generate_outfits_config)

        if "cooling_min_cooling" in line:
            cooling_min_cooling = next(generate_outfits_config)
        if "cooling_max_cooling" in line:
            cooling_max_cooling = next(generate_outfits_config)

    cooling_types_generated_count = 1
    while cooling_types_generated_count <= int(cooling_type_amount):
        #Calculates new values
        cooling_cost = roundup100(random.randint(int(cooling_min_start_cost), int(cooling_max_start_cost)))
        cooling_outfit = random.randint(int(cooling_min_outfit_space), int(cooling_max_outfit_space))
        cooling_cooling = round(((random.randint(float(cooling_min_cooling), float(cooling_max_cooling))) / 25), 1)

        #cooling Name
        cooling_name = random.choice(letters) + random.choice(letters) + random.choice(letters)
        cooling_name_int = str(random.choice(numbers)) + str(random.choice(numbers)) + str(random.choice(numbers))
        cooling_name = str(cooling_name) + "-" + str(cooling_name_int)

        #Iterates Values
        cooling_iterations_count = 1
        while cooling_iterations_count <= int(cooling_iterations):
            #Writes ES code to file, use \n for line break
            cooling_output.write('outfit "' + cooling_name + ' Cooling"' + "\n")
            cooling_output.write('\tcategory "Systems"\n')
            cooling_output.write('\tcost ' + str(cooling_cost) + "\n")
            cooling_output.write('\tthumbnail "outfit/water cooling"\n')
            cooling_output.write('\t"mass" ' + str(cooling_outfit) + "\n")
            cooling_output.write('\t"outfit space" -' + str(cooling_outfit) + "\n")
            cooling_output.write('\t"cooling" ' + str(cooling_cooling) + "\n")
            cooling_output.write('\tdescription "Cooling"\n')
            cooling_output.write('\n')

            outfitter_output.write('\t"' + cooling_name + ' Cooling' + '"\n')

            #Name
            cooling_name = ''.join([c for c in cooling_name if c not in "1234567890"])
            cooling_name_int = int(cooling_name_int) + int(cooling_name_int)
            cooling_name = cooling_name + str(cooling_name_int)
            print('Created cooling ' + cooling_name + ' Cooling')

            #Iterate for next run of loop
            cooling_cost = roundup100((cooling_cost * 2) * float(cooling_cost_curve))
            cooling_outfit = round((cooling_outfit * 2) * float(cooling_outfit_curve))
            cooling_cooling = round((cooling_cooling * 2) * float(cooling_cooling_curve), 1)

            cooling_iterations_count += 1
        cooling_types_generated_count += 1
    cooling_output.write('\n')
    generate_outfits_config.close()
    cooling_output.close()
def create_power():
    generate_outfits_config = open(outfit_config_file, "r")
    power_output = open("output/outfits " + outfit_output_file, "a")
    #Searches config file for values and creates variables
    for line in generate_outfits_config: #Creates vars from txt file
        if "power_type_amount" in line:
            power_type_amount = next(generate_outfits_config)

        if "power_iterations" in line:
            power_iterations = next(generate_outfits_config)
        if "power_cost_curve" in line:
            power_cost_curve = next(generate_outfits_config)
        if "power_outfit_curve" in line:
            power_outfit_curve = next(generate_outfits_config)
        if "power_power_curve" in line:
            power_power_curve = next(generate_outfits_config)
        if "power_heat_curve" in line:
            power_heat_curve = next(generate_outfits_config)

        if "power_min_start_cost" in line:
            power_min_start_cost = next(generate_outfits_config)
        if "power_max_start_cost" in line:
            power_max_start_cost = next(generate_outfits_config)
        if "power_min_outfit_space" in line:
            power_min_outfit_space = next(generate_outfits_config)
        if "power_max_outfit_space" in line:
            power_max_outfit_space = next(generate_outfits_config)

        if "power_min_power" in line:
            power_min_power = next(generate_outfits_config)
        if "power_max_power" in line:
            power_max_power = next(generate_outfits_config)
        if "power_min_heat" in line:
            power_min_heat = next(generate_outfits_config)
        if "power_max_heat" in line:
            power_max_heat = next(generate_outfits_config)

    power_types_generated_count = 1
    while power_types_generated_count <= int(power_type_amount):
        #Calculates new values
        power_cost = roundup100(random.randint(int(power_min_start_cost), int(power_max_start_cost)))
        power_outfit = random.randint(int(power_min_outfit_space), int(power_max_outfit_space))
        power_power = round(((random.randint(float(power_min_power), float(power_max_power))) / 60), 1)
        power_heat = round(((random.randint(float(power_min_heat), float(power_max_heat))) / 60), 1)

        #Power Name
        power_name = random.choice(letters) + random.choice(letters) + random.choice(letters)
        power_name_int = str(random.choice(numbers)) + str(random.choice(numbers)) + str(random.choice(numbers))
        power_name = str(power_name) + "-" + str(power_name_int)

        #Iterates Values
        power_iterations_count = 1
        while power_iterations_count <= int(power_iterations):
            #Writes ES code to file, use \n for line break
            power_output.write('outfit "' + power_name + ' Generator"' + "\n")
            power_output.write('\tcategory "Systems"\n')
            power_output.write('\tcost ' + str(power_cost) + "\n")
            power_output.write('\tthumbnail "outfit/small fuel cell"\n')
            power_output.write('\t"mass" ' + str(power_outfit) + "\n")
            power_output.write('\t"outfit space" -' + str(power_outfit) + "\n")
            power_output.write('\t"energy generation" ' + str(power_power) + "\n")
            power_output.write('\t"heat generation" ' + str(power_heat) + "\n")
            power_output.write('\tdescription "power"\n')
            power_output.write('\n')

            outfitter_output.write('\t"' + power_name + ' Generator' + '"\n')

            #Name
            power_name = ''.join([c for c in power_name if c not in "1234567890"])
            power_name_int = int(power_name_int) + int(power_name_int)
            power_name = power_name + str(power_name_int)
            print("Created power " + power_name + ' Generator')

            #Iterate for next run of loop
            power_cost = roundup100((power_cost * 2) * float(power_cost_curve))
            power_outfit = round((power_outfit * 2) * float(power_outfit_curve))
            power_power = round((power_power * 2) * float(power_power_curve), 1)
            power_heat = round((power_heat * 2) * float(power_heat_curve), 1)

            power_iterations_count += 1
        power_types_generated_count += 1
    power_output.write('\n')
    generate_outfits_config.close()
    power_output.close()
def create_engines():
    generate_outfits_config = open(outfit_config_file, "r")
    engines_output = open("output/outfits " + outfit_output_file, "a")
    #Searches config file for values and creates variables
    for line in generate_outfits_config: #Creates vars from txt file
        if "engine_type_amount" in line:
            engine_type_amount = next(generate_outfits_config)

        if "engines_iterations" in line:
            engines_iterations = next(generate_outfits_config)
        if "engines_cost_curve" in line:
            engines_cost_curve = next(generate_outfits_config)
        if "engines_outfit_curve" in line:
            engines_outfit_curve = next(generate_outfits_config)
        if "engines_energy_curve" in line:
            engines_engines_curve = next(generate_outfits_config)
        if "engines_heat_curve" in line:
            engines_heat_curve = next(generate_outfits_config)
        if "engines_thrust_curve" in line:
            engines_thrust_curve = next(generate_outfits_config)

        if "engines_min_start_cost" in line:
            engines_min_start_cost = next(generate_outfits_config)
        if "engines_max_start_cost" in line:
            engines_max_start_cost = next(generate_outfits_config)
        if "engines_min_outfit_space" in line:
            engines_min_outfit_space = next(generate_outfits_config)
        if "engines_max_outfit_space" in line:
            engines_max_outfit_space = next(generate_outfits_config)

        if "engines_min_thrust" in line:
            engines_min_thrust = next(generate_outfits_config)
        if "engines_max_thrust" in line:
            engines_max_thrust = next(generate_outfits_config)
        if "engines_min_energy" in line:
            engines_min_energy = next(generate_outfits_config)
        if "engines_max_energy" in line:
            engines_max_energy = next(generate_outfits_config)
        if "engines_min_heat" in line:
            engines_min_heat = next(generate_outfits_config)
        if "engines_max_heat" in line:
            engines_max_heat = next(generate_outfits_config)

    engine_types_generated_count = 1
    while engine_types_generated_count <= int(engine_type_amount):
        engines_cost = roundup100(random.randint(int(engines_min_start_cost), int(engines_max_start_cost)))
        engines_outfit = random.randint(int(engines_min_outfit_space), int(engines_max_outfit_space))
        engines_thrust = round(((random.randint(float(engines_min_thrust), float(engines_max_thrust))) / 3600), 1)
        engines_energy = round(((random.randint(float(engines_min_energy), float(engines_max_energy))) / 60), 1)
        engines_heat = round(((random.randint(float(engines_min_heat), float(engines_max_heat))) / 60), 1)

        #engines Name
        engines_name = random.choice(letters) + random.choice(letters) + random.choice(letters)
        engines_name_int = str(random.choice(numbers)) + str(random.choice(numbers)) + str(random.choice(numbers))
        engines_name = str(engines_name) + "-" + str(engines_name_int)

        #Iterates Values
        engines_iterations_count = 1
        while engines_iterations_count <= int(engines_iterations):
            #Writes ES code to file, use \n for line break
            engines_output.write('outfit "' + engines_name + ' Engines"'+ "\n")
            engines_output.write('\tcategory "Engines"\n')
            engines_output.write('\tcost ' + str(engines_cost) + "\n")
            engines_output.write('\tthumbnail "outfit/tiny ion thruster"\n')
            engines_output.write('\t"mass" ' + str(engines_outfit) + "\n")
            engines_output.write('\t"outfit space" -' + str(engines_outfit) + "\n")
            engines_output.write('\t"engine capacity" -' + str(engines_outfit) + "\n")
            engines_output.write('\t"thrust" ' + str(engines_thrust) + "\n")
            engines_output.write('\t"thrusting energy" ' + str(engines_energy) + "\n")
            engines_output.write('\t"thrusting heat" ' + str(engines_heat) + "\n")
            engines_output.write('\t"flare sprite" "effect/ion flare/tiny"\n')
            engines_output.write('\t\t"frame rate" 1.2\n')
            engines_output.write('\t"flare sound" "ion tiny"\n')
            engines_output.write('\tdescription "engines"\n')
            engines_output.write('\n')

            outfitter_output.write('\t"' + engines_name + ' Engines'+ '"\n')

            #Name
            engines_name = ''.join([c for c in engines_name if c not in "1234567890"])
            engines_name_int = int(engines_name_int) + int(engines_name_int)
            engines_name = engines_name + str(engines_name_int)
            print("Created engines " + engines_name + ' Engines')

            #Iterate for next run of loop
            engines_cost = roundup100((engines_cost * 2) * float(engines_cost_curve))
            engines_outfit = round((engines_outfit * 2) * float(engines_outfit_curve))
            engines_thrust = round((engines_thrust * 2) * float(engines_thrust_curve), 1)
            engines_energy = round((engines_energy * 2) * float(engines_engines_curve), 1)
            engines_heat = round((engines_heat * 2) * float(engines_heat_curve), 1)

            engines_iterations_count += 1
        engine_types_generated_count += 1
    engines_output.write('\n')
    generate_outfits_config.close()
    engines_output.close()
def create_steering():
    generate_outfits_config = open(outfit_config_file, "r")
    steering_output = open("output/outfits " + outfit_output_file, "a")
    #Searches config file for values and creates variables
    for line in generate_outfits_config: #Creates vars from txt file
        if "steering_type_amount" in line:
            steering_type_amount = next(generate_outfits_config)

        if "steering_iterations" in line:
            steering_iterations = next(generate_outfits_config)
        if "steering_cost_curve" in line:
            steering_cost_curve = next(generate_outfits_config)
        if "steering_outfit_curve" in line:
            steering_outfit_curve = next(generate_outfits_config)
        if "steering_energy_curve" in line:
            steering_steering_curve = next(generate_outfits_config)
        if "steering_heat_curve" in line:
            steering_heat_curve = next(generate_outfits_config)
        if "steering_thrust_curve" in line:
            steering_thrust_curve = next(generate_outfits_config)

        if "steering_min_start_cost" in line:
            steering_min_start_cost = next(generate_outfits_config)
        if "steering_max_start_cost" in line:
            steering_max_start_cost = next(generate_outfits_config)
        if "steering_min_outfit_space" in line:
            steering_min_outfit_space = next(generate_outfits_config)
        if "steering_max_outfit_space" in line:
            steering_max_outfit_space = next(generate_outfits_config)

        if "steering_min_thrust" in line:
            steering_min_thrust = next(generate_outfits_config)
        if "steering_max_thrust" in line:
            steering_max_thrust = next(generate_outfits_config)
        if "steering_min_energy" in line:
            steering_min_energy = next(generate_outfits_config)
        if "steering_max_energy" in line:
            steering_max_energy = next(generate_outfits_config)
        if "steering_min_heat" in line:
            steering_min_heat = next(generate_outfits_config)
        if "steering_max_heat" in line:
            steering_max_heat = next(generate_outfits_config)

    steering_types_generated_count = 1
    while steering_types_generated_count <= int(steering_type_amount):
        #Calculates new values
        steering_cost = roundup100(random.randint(int(steering_min_start_cost), int(steering_max_start_cost)))
        steering_outfit = random.randint(int(steering_min_outfit_space), int(steering_max_outfit_space))
        steering_thrust = round(((random.randint(float(steering_min_thrust), float(steering_max_thrust))) / 60), 1)
        steering_energy = round(((random.randint(float(steering_min_energy), float(steering_max_energy))) / 60), 1)
        steering_heat = round(((random.randint(float(steering_min_heat), float(steering_max_heat))) / 60), 1)

        #steering Name
        steering_name = random.choice(letters) + random.choice(letters) + random.choice(letters)
        steering_name_int = str(random.choice(numbers)) + str(random.choice(numbers)) + str(random.choice(numbers))
        steering_name = str(steering_name) + "-" + str(steering_name_int)

        #Iterates Values
        steering_iterations_count = 1
        while steering_iterations_count <= int(steering_iterations):
            #Writes ES code to file, use \n for line break
            steering_output.write('outfit "' + steering_name + ' Steering"' + "\n")
            steering_output.write('\tcategory "Engines"\n')
            steering_output.write('\tcost ' + str(steering_cost) + "\n")
            steering_output.write('\tthumbnail "outfit/tiny ion steering"\n')
            steering_output.write('\t"mass" ' + str(steering_outfit) + "\n")
            steering_output.write('\t"outfit space" -' + str(steering_outfit) + "\n")
            steering_output.write('\t"engine capacity" -' + str(steering_outfit) + "\n")
            steering_output.write('\t"turn" ' + str(steering_thrust) + "\n")
            steering_output.write('\t"turning energy" ' + str(steering_energy) + "\n")
            steering_output.write('\t"turning heat" ' + str(steering_heat) + "\n")
            steering_output.write('\tdescription "steering"\n')
            steering_output.write('\n')

            outfitter_output.write('\t"' + steering_name + ' Steering' + '"\n')

            #Name
            steering_name = ''.join([c for c in steering_name if c not in "1234567890"])
            steering_name_int = int(steering_name_int) + int(steering_name_int)
            steering_name = steering_name + str(steering_name_int)
            print("Created steering " + steering_name+ ' Steering')

            #Iterate for next run of loop
            steering_cost = roundup100((steering_cost * 2) * float(steering_cost_curve))
            steering_outfit = round((steering_outfit * 2) * float(steering_outfit_curve))
            steering_thrust = round((steering_thrust * 2) * float(steering_thrust_curve), 1)
            steering_energy = round((steering_energy * 2) * float(steering_steering_curve), 1)
            steering_heat = round((steering_heat * 2) * float(steering_heat_curve), 1)

            steering_iterations_count += 1
        steering_types_generated_count += 1
    steering_output.write('\n')
    generate_outfits_config.close()
    steering_output.close()

def create_shield_generator():
    generate_outfits_config = open(outfit_config_file, "r")
    shield_generator_output = open("output/outfits " + outfit_output_file, "a")
    #Searches config file for values and creates variables
    for line in generate_outfits_config: #Creates vars from txt file
        if "shield_generator_type_amount" in line:
            shield_generator_type_amount = next(generate_outfits_config)

        if "shield_generator_iterations" in line:
            shield_generator_iterations = next(generate_outfits_config)
        if "shield_generator_cost_curve" in line:
            shield_generator_cost_curve = next(generate_outfits_config)
        if "shield_generator_outfit_curve" in line:
            shield_generator_outfit_curve = next(generate_outfits_config)
        if "shield_generator_shield_generation_curve" in line:
            shield_generator_shield_generation_curve = next(generate_outfits_config)
        if "shield_generator_shield_energy_curve" in line:
            shield_generator_shield_energy_curve = next(generate_outfits_config)

        if "shield_generator_min_start_cost" in line:
            shield_generator_min_start_cost = next(generate_outfits_config)
        if "shield_generator_max_start_cost" in line:
            shield_generator_max_start_cost = next(generate_outfits_config)
        if "shield_generator_min_outfit_space" in line:
            shield_generator_min_outfit_space = next(generate_outfits_config)
        if "shield_generator_max_outfit_space" in line:
            shield_generator_max_outfit_space = next(generate_outfits_config)

        if "shield_generator_min_shield_generation" in line:
            shield_generator_min_shield_generation = next(generate_outfits_config)
        if "shield_generator_max_shield_generation" in line:
            shield_generator_max_shield_generation = next(generate_outfits_config)
        if "shield_generator_min_shield_energy" in line:
            shield_generator_min_shield_energy = next(generate_outfits_config)
        if "shield_generator_max_shield_energy" in line:
            shield_generator_max_shield_energy = next(generate_outfits_config)


    shield_generator_types_generated_count = 1
    while shield_generator_types_generated_count <= int(shield_generator_type_amount):
        #Calculates new values
        shield_generator_cost = roundup100(random.randint(int(shield_generator_min_start_cost), int(shield_generator_max_start_cost)))
        shield_generator_outfit = random.randint(int(shield_generator_min_outfit_space), int(shield_generator_max_outfit_space))
        shield_generator_shield_generation = round(random.uniform(float(shield_generator_min_shield_generation), float(shield_generator_max_shield_generation)), 2)
        shield_generator_shield_energy = round(random.uniform(float(shield_generator_min_shield_energy), float(shield_generator_max_shield_energy)), 2)

        #shield_generator Name
        shield_generator_name = random.choice(letters) + random.choice(letters) + random.choice(letters)
        shield_generator_name_int = str(random.choice(numbers)) + str(random.choice(numbers)) + str(random.choice(numbers))
        shield_generator_name = str(shield_generator_name) + "-" + str(shield_generator_name_int)

        #Iterates Values
        shield_generator_iterations_count = 1
        while shield_generator_iterations_count <= int(shield_generator_iterations):
            #Writes ES code to file, use \n for line break
            shield_generator_output.write('outfit "' + shield_generator_name + ' Shield Generator"' + "\n")
            shield_generator_output.write('\tcategory "Systems"\n')
            shield_generator_output.write('\tcost ' + str(shield_generator_cost) + "\n")
            shield_generator_output.write('\tthumbnail "outfit/tiny shield"\n')
            shield_generator_output.write('\t"mass" ' + str(shield_generator_outfit) + "\n")
            shield_generator_output.write('\t"outfit space" -' + str(shield_generator_outfit) + "\n")
            shield_generator_output.write('\t"shield generation" ' + str(shield_generator_shield_generation) + "\n")
            shield_generator_output.write('\t"shield energy" ' + str(shield_generator_shield_energy) + "\n")
            shield_generator_output.write('\tdescription "shield generator"\n')
            shield_generator_output.write('\n')

            outfitter_output.write('\t"' + shield_generator_name + ' Shield Generator' + '"\n')

            #Name
            shield_generator_name = ''.join([c for c in shield_generator_name if c not in "1234567890"])
            shield_generator_name_int = int(shield_generator_name_int) + int(shield_generator_name_int)
            shield_generator_name = shield_generator_name + str(shield_generator_name_int)
            print('Created shield generator ' + shield_generator_name + ' Shield Generator')

            #Iterate for next run of loop
            shield_generator_cost = roundup100((shield_generator_cost * 2) * float(shield_generator_cost_curve))
            shield_generator_outfit = round((shield_generator_outfit * 2) * float(shield_generator_outfit_curve))
            shield_generator_shield_generation = round((shield_generator_shield_generation * 2) * float(shield_generator_shield_generation_curve), 1)
            shield_generator_shield_energy = round((shield_generator_shield_energy * 2) * float(shield_generator_shield_energy_curve), 1)

            shield_generator_iterations_count += 1
        shield_generator_types_generated_count += 1
    shield_generator_output.write('\n')
    generate_outfits_config.close()
    shield_generator_output.close()

def create_weapon():
    generate_weapons_config = open(weapon_config_file, "r")
    weapon_output = open("output/weapon " + weapon_output_file, "a")
    #Searches config file for values and creates variables
    for line in generate_weapons_config: #Creates vars from txt file

        line = line.rstrip('\n')

        if "weapon_seed" in line:
            weapon_seed = next(generate_weapons_config)
            random.seed(int(weapon_seed))
        if "weapon_type" in line:
            weapon_type = int(next(generate_weapons_config))
            if weapon_type in [1]:
                weapon_type = "projectile"
                #print("weapon type: projectile")
            elif weapon_type in [2]:
                weapon_type = "beam"
                #print("weapon type: beam")
            elif weapon_type in [3]:
                weapon_type = "missile"
                #print("weapon type: missile")
            elif weapon_type in [4]:
                weapon_type = "anti-missile"
                #print("weapon type: anti-missile")
            else:
                weapon_type = "projectile"
                #print("weapon type: projectile else")

        if "weapon_amount" in line:
            weapon_amount = next(generate_weapons_config)

        if "weapon_min_start_cost" in line:
            weapon_min_start_cost = next(generate_weapons_config)
        if "weapon_max_start_cost" in line:
            weapon_max_start_cost = next(generate_weapons_config)
        if "weapon_min_outfit_space" in line:
            weapon_min_outfit_space = next(generate_weapons_config)
        if "weapon_max_outfit_space" in line:
            weapon_max_outfit_space = next(generate_weapons_config)

        if "weapon_min_inaccuracy" in line:
            weapon_min_inaccuracy = int(next(generate_weapons_config))
        if "weapon_max_inaccuracy" in line:
            weapon_max_inaccuracy = int(next(generate_weapons_config))
        if "weapon_min_velocity" in line:
            weapon_min_velocity = int(next(generate_weapons_config))
        if "weapon_max_velocity" in line:
            weapon_max_velocity = int(next(generate_weapons_config))
        if "weapon_min_range" in line:
            weapon_min_range = int(next(generate_weapons_config))
        if "weapon_max_range" in line:
            weapon_max_range = int(next(generate_weapons_config))
        if "weapon_min_sps" in line:
            weapon_min_sps = int(next(generate_weapons_config))
        if "weapon_max_sps" in line:
            weapon_max_sps = int(next(generate_weapons_config))
        if "weapon_min_firing_eps" in line:
            weapon_min_firing_eps = int(next(generate_weapons_config))
        if "weapon_max_firing_eps" in line:
            weapon_max_firing_eps = int(next(generate_weapons_config))
        if "weapon_min_firing_hps" in line:
            weapon_min_firing_hps = int(next(generate_weapons_config))
        if "weapon_max_firing_hps" in line:
            weapon_max_firing_hps = int(next(generate_weapons_config))
        if "weapon_min_shield_dps" in line:
            weapon_min_shield_dps = int(next(generate_weapons_config))
        if "weapon_max_shield_dps" in line:
            weapon_max_shield_dps = int(next(generate_weapons_config))
        if "weapon_min_hull_dps" in line:
            weapon_min_hull_dps = int(next(generate_weapons_config))
        if "weapon_max_hull_dps" in line:
            weapon_max_hull_dps = int(next(generate_weapons_config))
        if "weapon_min_hit_force" in line:
            weapon_min_hit_force = int(next(generate_weapons_config))
        if "weapon_max_hit_force" in line:
            weapon_max_hit_force = int(next(generate_weapons_config))

    #Burst arguments
        if "weapon_is_burst" in line:
            weapon_is_burst = next(generate_weapons_config)
            if str(weapon_is_burst) in ['true', 'True', 'true\n', 'True\n']:
                weapon_is_burst = True
                #print("weapon is burst")
            elif weapon_is_burst in ['false', 'False', 'false\n', 'False\n']:
                weapon_is_burst = False
                #print("weapon is not burst")
            else:
                weapon_is_burst = False
                #print("weapon is not burst else")
    #Turret arguments
        if "create_turrets" in line:
            create_turrets = next(generate_weapons_config)
            if str(create_turrets) in ['true', 'True', 'true\n', 'True\n']:
                create_turrets = True
            elif create_turrets in ['false', 'False', 'false\n', 'False\n']:
                create_turrets = False
            else:
                create_turrets = False

        if "turret_iterations" in line:
            turret_iterations = int(next(generate_weapons_config))
        if "turret_curve" in line:
            turret_curve = round(float(next(generate_weapons_config)), 1)
        if "turret_min_turn" in line:
            turret_min_turn = round(float(next(generate_weapons_config)), 1)
        if "turret_max_turn" in line:
            turret_max_turn = round(float(next(generate_weapons_config)), 1)
    #Missile arguments
        #actual missile ammunition
        if "missile_min_cost" in line:
            missile_min_cost = int(next(generate_weapons_config))
        if "missile_max_cost" in line:
            missile_max_cost = int(next(generate_weapons_config))
        if "missile_min_mass" in line:
            missile_min_mass = round(float(next(generate_weapons_config)), 1)
        if "missile_max_mass" in line:
            missile_max_mass = round(float(next(generate_weapons_config)), 1)

        #missile storage
        if "missile_storage_min_capacity" in line:
            missile_storage_min_capacity = int(next(generate_weapons_config))
        if "missile_storage_max_capacity" in line:
            missile_storage_max_capacity = int(next(generate_weapons_config))
        if "missile_storage_min_cost" in line:
            missile_storage_min_cost = int(next(generate_weapons_config))
        if "missile_storage_max_cost" in line:
            missile_storage_max_cost = int(next(generate_weapons_config))
        if "missile_storage_min_mass" in line:
            missile_storage_min_mass = int(next(generate_weapons_config))
        if "missile_storage_max_mass" in line:
            missile_storage_max_mass = int(next(generate_weapons_config))
        if "missile_storage_min_outfit" in line:
            missile_storage_min_outfit = int(next(generate_weapons_config))
        if "missile_storage_max_outfit" in line:
            missile_storage_max_outfit = int(next(generate_weapons_config))

        #missile launcher
        if "missile_tracking_type" in line:
            missile_tracking_type = int(next(generate_weapons_config))
            if missile_tracking_type in [0]:
                missile_tracking_type = "none"
                #print("missile tracking type: none")
            elif missile_tracking_type in [1]:
                missile_tracking_type = "infrared"
                #print("missile tracking type: infrared")
            elif missile_tracking_type in [2]:
                missile_tracking_type = "optical"
                #print("missile tracking type: optical")
            elif missile_tracking_type in [3]:
                missile_tracking_type = "radar"
                #print("missile tracking type: radar")
            elif missile_tracking_type in [4]:
                missile_tracking_type = "tracking"
                #print("missile tracking type: tracking(constant)")
            else:
                missile_tracking_type = "projectile"
                #print("missile tracking type: none")

        if "missile_homing_type" in line:
            missile_homing_type = int(next(generate_weapons_config))
            if missile_homing_type in [0]:
                missile_homing_type = "0"
            elif missile_homing_type in [1]:
                missile_homing_type = "1"
            elif missile_homing_type in [2]:
                missile_homing_type = "2"
            elif missile_homing_type in [3]:
                missile_homing_type = "3"
            elif missile_homing_type in [4]:
                missile_homing_type = "4"
            else:
                missile_homing_type = "0"

        if "missile_min_tracking_amount" in line:
            missile_min_tracking_amount = round(float(next(generate_weapons_config)), 1)
        if "missile_max_tracking_amount" in line:
            missile_max_tracking_amount = round(float(next(generate_weapons_config)), 1)
        if "missile_min_acceleration" in line:
            missile_min_acceleration = round(float(next(generate_weapons_config)), 1)
        if "missile_max_acceleration" in line:
            missile_max_acceleration = round(float(next(generate_weapons_config)), 1)
        if "missile_min_drag" in line:
            missile_min_drag = round(float(next(generate_weapons_config)), 1)
        if "missile_max_drag" in line:
            missile_max_drag = round(float(next(generate_weapons_config)), 1)
        if "missile_min_turn" in line:
            missile_min_turn = round(float(next(generate_weapons_config)), 1)
        if "missile_max_turn" in line:
            missile_max_turn = round(float(next(generate_weapons_config)), 1)

        if "missile_min_strength" in line:
            missile_min_strength = round(float(next(generate_weapons_config)), 1)
        if "missile_max_strength" in line:
            missile_max_strength = round(float(next(generate_weapons_config)), 1)

    #anti-missile arguments
        if "anti_missile_strength" in line:
            anti_missile_strength = int(next(generate_weapons_config))

    #end



#End reading data from config file

    print("Weapon type: " + (str(weapon_type)))

    if weapon_is_burst:
        print("Weapon is burst: True")

    if create_turrets:
        print("Create turrets: True")
    else:
        print("Create turrets: False")

    if weapon_type == "missile":
        if missile_tracking_type == "none":
            print("Missile tracking type: " + str(missile_tracking_type))
        if missile_tracking_type == "infrared":
            print("Missile tracking type: " + str(missile_tracking_type))
        if missile_tracking_type == "optical":
            print("Missile tracking type: " + str(missile_tracking_type))
        if missile_tracking_type == "radar":
            print("Missile tracking type: " + str(missile_tracking_type))
        if missile_tracking_type == "tracking":
            print("Missile tracking type: " + str(missile_tracking_type))



    print("\n")
    weapon_types_generated_count = 1
    while weapon_types_generated_count <= int(weapon_amount):

        #Weapon calculations
        weapon_cost = roundup100(random.randint(int(weapon_min_start_cost), int(weapon_max_start_cost)))
        weapon_outfit = random.randint(int(weapon_min_outfit_space), int(weapon_max_outfit_space))

        weapon_inaccuracy = random.randint(weapon_min_inaccuracy, weapon_max_inaccuracy)
        weapon_velocity = random.randint(weapon_min_velocity, weapon_max_velocity)

        weapon_range = random.randint(weapon_min_range, weapon_max_range)
        weapon_lifetime = weapon_range / weapon_velocity

        if weapon_type != "beam":
            weapon_sps = random.randint(weapon_min_sps, weapon_max_sps)
        elif weapon_type == "beam":
            weapon_sps = 60

        weapon_reload = 60 / weapon_sps

        weapon_firing_eps = random.randint(weapon_min_firing_eps, weapon_max_firing_eps)
        weapon_firing_epshot = weapon_firing_eps / weapon_sps

        weapon_firing_hps = random.randint(weapon_min_firing_hps, weapon_max_firing_hps)
        weapon_firing_hpshot = weapon_firing_hps / weapon_sps

        weapon_shield_dps = random.randint(weapon_min_shield_dps, weapon_max_shield_dps)
        weapon_shield_dpshot = weapon_shield_dps / weapon_sps

        weapon_hull_dps = random.randint(weapon_min_hull_dps, weapon_max_hull_dps)
        weapon_hull_dpshot = weapon_hull_dps / weapon_sps

        weapon_hit_force = random.randint(weapon_min_hit_force, weapon_max_hit_force)


        #Missile Calculations
        missile_cost = random.randint(missile_min_cost, missile_max_cost)
        missile_mass = round(random.uniform(missile_min_mass, missile_max_mass), 1)

        #Missile storage calculations
        missile_storage_capacity = random.randint(missile_storage_min_capacity, missile_storage_max_capacity)
        missile_storage_cost = random.randint(missile_storage_min_cost, missile_storage_max_cost)
        missile_storage_mass = random.randint(missile_storage_min_mass, missile_storage_max_mass)
        missile_storage_outfit = random.randint(missile_storage_min_outfit, missile_storage_max_outfit)

        #Missile launcher calculations
        missile_tracking_amount = round(random.uniform(missile_min_tracking_amount, missile_max_tracking_amount), 1)
        missile_acceleration = round(random.uniform(missile_min_acceleration, missile_max_acceleration), 1)
        missile_drag = round(random.uniform(missile_min_drag, missile_max_drag), 1)
        missile_turn = round(random.uniform(missile_min_turn, missile_max_turn), 1)
        missile_strength = round(random.uniform(missile_min_strength, missile_max_strength), 1)


        #weapon Name
        weapon_name = random.choice(letters)
        weapon_name_int = str(random.choice(numbers)) + str(random.choice(numbers))
        weapon_name = str(weapon_name) + "-" + str(weapon_name_int)

        #Writes ES code to file, use \n for line break
        if weapon_type == "projectile": #Write projectile weapon
            weapon_output.write('outfit "' + weapon_name + '"' + "\n")
            weapon_output.write('\tcategory "Guns"\n')
            weapon_output.write('\tcost ' + str(weapon_cost) + "\n")
            weapon_output.write('\tthumbnail "outfit/blaster"\n')
            weapon_output.write('\t"mass" ' + str(weapon_outfit) + "\n")
            weapon_output.write('\t"outfit space" -' + str(weapon_outfit) + "\n")
            weapon_output.write('\t"weapon capacity" -' + str(weapon_outfit) + "\n")
            weapon_output.write('\t"gun ports" -1' + "\n")
            weapon_output.write('\tweapon' + "\n")
            weapon_output.write('\t\t"sprite" "projectile/blaster"'+ "\n")
            weapon_output.write('\t\tsound "blaster"'+ "\n")
            weapon_output.write('\t\t"hit effect" "blaster impact"'+ "\n")
            weapon_output.write('\t\t"inaccuracy" ' + str(weapon_inaccuracy) + "\n")
            weapon_output.write('\t\t"velocity" ' + str(weapon_velocity) + "\n")
            weapon_output.write('\t\t"lifetime" ' + str(weapon_lifetime) + "\n")
            weapon_output.write('\t\t"reload" ' + str(weapon_reload) + "\n")
            weapon_output.write('\t\t"firing energy" ' + str(weapon_firing_epshot) + "\n")
            weapon_output.write('\t\t"firing heat" ' + str(weapon_firing_hpshot) + "\n")
            weapon_output.write('\t\t"shield damage" ' + str(weapon_shield_dpshot) + "\n")
            weapon_output.write('\t\t"hull damage" ' + str(weapon_hull_dpshot) + "\n")
            weapon_output.write('\t\t"hit force" ' + str(weapon_hit_force) + "\n")
            weapon_output.write('\tdescription "Projectile weapon"\n')
            weapon_output.write('\n')
            print("Created " + str(weapon_type) + " weapon " + weapon_name)

        if weapon_type == "beam": #Write projectile weapon
            weapon_output.write('outfit "' + weapon_name + '"' + "\n")
            weapon_output.write('\tcategory "Guns"\n')
            weapon_output.write('\tcost ' + str(weapon_cost) + "\n")
            weapon_output.write('\tthumbnail "outfit/blaster"\n')
            weapon_output.write('\t"mass" ' + str(weapon_outfit) + "\n")
            weapon_output.write('\t"outfit space" -' + str(weapon_outfit) + "\n")
            weapon_output.write('\t"weapon capacity" -' + str(weapon_outfit) + "\n")
            weapon_output.write('\t"gun ports" -1' + "\n")
            weapon_output.write('\tweapon' + "\n")
            weapon_output.write('\t\t"sprite" "projectile/laser"'+ "\n")
            weapon_output.write('\t\t\t"frame rate" 1'+ "\n")
            weapon_output.write('\t\tsound "laser"'+ "\n")
            weapon_output.write('\t\t"hit effect" "beam laser impact"'+ "\n")
            weapon_output.write('\t\t"inaccuracy" ' + str(weapon_inaccuracy) + "\n")
            weapon_output.write('\t\t"velocity" ' + str(weapon_range) + "\n") #because velocity * lifetime = range
            weapon_output.write('\t\t"lifetime" ' + str(1) + "\n")
            weapon_output.write('\t\t"reload" ' + str(1) + "\n")
            weapon_output.write('\t\t"firing energy" ' + str(weapon_firing_epshot) + "\n")
            weapon_output.write('\t\t"firing heat" ' + str(weapon_firing_hpshot) + "\n")
            weapon_output.write('\t\t"shield damage" ' + str(weapon_shield_dpshot) + "\n")
            weapon_output.write('\t\t"hull damage" ' + str(weapon_hull_dpshot) + "\n")
            weapon_output.write('\t\t"hit force" ' + str(weapon_hit_force) + "\n")
            weapon_output.write('\tdescription "Beam weapon"\n')
            weapon_output.write('\n')
            print("Created " + str(weapon_type) + " weapon " + weapon_name)

        if weapon_type == "missile": #Write missile weapon
            weapon_output.write('outfit "' + weapon_name + ' Missile"' + "\n")
            weapon_output.write('\tcategory "Ammunition"\n')
            weapon_output.write('\tcost ' + str(missile_cost) + "\n")
            weapon_output.write('\tthumbnail "outfit/sidewinder"\n')
            weapon_output.write('\t"mass" ' + str(missile_mass) + "\n")
            weapon_output.write('\t"' + str(weapon_name) + ' missile capacity" -1' + "\n")
            weapon_output.write('\tdescription "Missile"\n')
            weapon_output.write('\n')
            print("Created " + str(weapon_type) + " weapon " + weapon_name + " Missile")

            weapon_output.write('outfit "' + weapon_name + ' Missile Rack"' + "\n")
            weapon_output.write('\tcategory "Ammunition"\n')
            weapon_output.write('\tcost ' + str(missile_storage_cost) + "\n")
            weapon_output.write('\tthumbnail "outfit/sidewinder storage"\n')
            weapon_output.write('\t"mass" ' + str(missile_storage_mass) + "\n")
            weapon_output.write('\t"outfit space" -' + str(missile_storage_outfit) + "\n")
            weapon_output.write('\t"' + str(weapon_name) + ' missile capacity" ' + str(missile_storage_capacity) + "\n")
            weapon_output.write('\tammo "' + str(weapon_name) + ' Missile"' + "\n")
            weapon_output.write('\tdescription "Missile rack"\n')
            weapon_output.write('\n')
            print("Created " + str(weapon_type) + " weapon " + weapon_name + " Missile Rack")

            weapon_output.write('outfit "' + weapon_name + ' Missile Launcher"' + "\n")
            weapon_output.write('\tcategory "Secondary Weapons"\n')
            weapon_output.write('\tcost ' + str(weapon_cost) + "\n")
            weapon_output.write('\tthumbnail "outfit/sidewinder launcher"\n')
            weapon_output.write('\t"mass" ' + str(weapon_outfit) + "\n")
            weapon_output.write('\t"outfit space" -' + str(weapon_outfit) + "\n")
            weapon_output.write('\t"weapon capacity" -' + str(weapon_outfit) + "\n")
            weapon_output.write('\t"gun ports" -1' + "\n")
            weapon_output.write('\t"' + str(weapon_name) + ' missile capacity" ' + str(missile_storage_capacity) + "\n")
            weapon_output.write('\tweapon' + "\n")
            weapon_output.write('\t\t"sprite" "projectile/sidewinder"'+ "\n")
            weapon_output.write('\t\t\t"no repeat"' + "\n")
            weapon_output.write('\t\t\t"frame rate" .25' + "\n")
            weapon_output.write('\t\tsound "sidewinder"'+ "\n")
            weapon_output.write('\t\tammo "' + str(weapon_name) + ' Missile"'+ "\n")
            weapon_output.write('\t\ticon "icon/sidewinder"'+ "\n")
            weapon_output.write('\t\t"fire effect" "sidewinder fire"'+ "\n")
            weapon_output.write('\t\t"die effect" "missile death"'+ "\n")
            weapon_output.write('\t\t"hit effect" "missile hit"'+ "\n")
            weapon_output.write('\t\t"inaccuracy" ' + str(weapon_inaccuracy) + "\n")
            weapon_output.write('\t\t"velocity" ' + str(weapon_velocity) + "\n")
            weapon_output.write('\t\t"lifetime" ' + str(weapon_lifetime) + "\n")
            weapon_output.write('\t\t"reload" ' + str(weapon_reload) + "\n")
            weapon_output.write('\t\t"firing energy" ' + str(weapon_firing_epshot) + "\n")
            weapon_output.write('\t\t"firing heat" ' + str(weapon_firing_hpshot) + "\n")
            weapon_output.write('\t\t"acceleration" ' + str(missile_acceleration) + "\n")
            weapon_output.write('\t\t"drag" ' + str(missile_drag) + "\n")
            weapon_output.write('\t\t"turn" ' + str(missile_turn) + "\n")
            weapon_output.write('\t\t"homing" ' + str(missile_homing_type) + "\n")

            if missile_tracking_type == "none":
                pass
            elif missile_tracking_type == "infrared":
                weapon_output.write('\t\t"infrared tracking" ' + str(missile_tracking_amount) + "\n")
            elif missile_tracking_type == "optical":
                weapon_output.write('\t\t"optical tracking" ' + str(missile_tracking_amount) + "\n")
            elif missile_tracking_type == "radar":
                weapon_output.write('\t\t"radar tracking" ' + str(missile_tracking_amount) + "\n")
            elif missile_tracking_type == "tracking":
                weapon_output.write('\t\t"tracking" ' + str(missile_tracking_amount) + "\n")

            weapon_output.write('\t\t"shield damage" ' + str(weapon_shield_dpshot) + "\n")
            weapon_output.write('\t\t"hull damage" ' + str(weapon_hull_dpshot) + "\n")
            weapon_output.write('\t\t"hit force" ' + str(weapon_hit_force) + "\n")
            weapon_output.write('\t\t"missile strength" ' + str(missile_strength) + "\n")
            weapon_output.write('\tdescription "Missile weapon"\n')
            weapon_output.write('\n')
            print("Created " + str(weapon_type) + " weapon " + weapon_name + " Missile Launcher")

        if weapon_type == "anti-missile": #Write projectile weapon
            weapon_output.write('outfit "' + weapon_name + ' Anti-Missile"' + "\n")
            weapon_output.write('\tcategory "Turrets"\n')
            weapon_output.write('\tcost ' + str(weapon_cost) + "\n")
            weapon_output.write('\tthumbnail "outfit/anti-missile"\n')
            weapon_output.write('\t"mass" ' + str(weapon_outfit) + "\n")
            weapon_output.write('\t"outfit space" -' + str(weapon_outfit) + "\n")
            weapon_output.write('\t"weapon capacity" -' + str(weapon_outfit) + "\n")
            weapon_output.write('\t"turret mounts" -1' + "\n")
            weapon_output.write('\tweapon' + "\n")
            weapon_output.write('\t\t"hardpoint sprite" "hardpoint/anti-missile"'+ "\n")
            weapon_output.write('\t\t"hardpoint offset" 4.'+ "\n")
            weapon_output.write('\t\t"hit effect" "small anti-missile"'+ "\n")
            weapon_output.write('\t\t"anti-missile" ' + str(anti_missile_strength) + "\n")
            weapon_output.write('\t\t"velocity" ' + str(weapon_velocity) + "\n")
            weapon_output.write('\t\t"lifetime" ' + str(weapon_lifetime) + "\n")
            weapon_output.write('\t\t"reload" ' + str(weapon_reload) + "\n")
            weapon_output.write('\t\t"firing energy" ' + str(weapon_firing_epshot) + "\n")
            weapon_output.write('\t\t"firing heat" ' + str(weapon_firing_hpshot) + "\n")
            weapon_output.write('\tdescription "Anti-missile"\n')
            weapon_output.write('\n')
            print("Created " + str(weapon_type) + " weapon " + weapon_name)


        #Write Turret (do turret on second pass or in seperate area)
        weapon_types_generated_count += 1
#    weapon_output.write('\n')
    generate_weapons_config.close()
    weapon_output.close()

def load_outfit_configs():

    outfit_configs_list = glob.glob("config/outfit config/*.txt") #Imports files in directory
    outfit_configs_amount = len(outfit_configs_list) #Gets amount of items in list
    outfit_configs_iterations = 0

    while outfit_configs_iterations < outfit_configs_amount: #Creates outfits for each config files
        global outfit_config_file #Config File
        outfit_config_file = str(outfit_configs_list[outfit_configs_iterations]).replace("\\", "/")
        global outfit_output_file #Output file
        outfit_output_file = str(outfit_configs_list[outfit_configs_iterations]).replace("\\", "/").replace("config/outfit config/", "")

        outfit_output_file_write = open("output/outfits " + outfit_output_file, "w")

        global outfitter_output_file #Output file
        outfitter_output_file = str(outfit_configs_list[outfit_configs_iterations]).replace("\\", "/").replace("config/outfit config/", "")
        global outfitter_output
        outfitter_output = open("output/outfitter " + outfitter_output_file, "w")
        outfitter_output.write("outfitter " + '"' + outfit_output_file.replace(".txt", "") + '"' + "\n")


        create_battery()
        create_cooling()
        create_power()
        create_engines()
        create_steering()
        create_shield_generator()

        print("\n")
        outfit_configs_iterations += 1

    weapon_configs_list = glob.glob("config/weapon config/*.txt") #Imports files in directory
    weapon_configs_amount = len(weapon_configs_list) #Gets amount of items in list
    weapon_configs_iterations = 0

    while weapon_configs_iterations < weapon_configs_amount: #Creates weapons for each config files
        global weapon_config_file #Config File
        weapon_config_file = str(weapon_configs_list[weapon_configs_iterations]).replace("\\", "/")
        global weapon_output_file #Output file
        weapon_output_file = str(weapon_configs_list[weapon_configs_iterations]).replace("\\", "/").replace("config/weapon config/", "")

        weapon_output_file_write = open("output/weapon " + weapon_output_file, "w")

        global weaponter_output_file #Output file
        weaponter_output_file = str(weapon_configs_list[weapon_configs_iterations]).replace("\\", "/").replace("config/weapon config/", "")
        global weaponter_output
        weaponter_output = open("output/outfitter " + outfitter_output_file, "w")
        outfitter_output.write("outfitter " + '"' + outfit_output_file.replace(".txt", "") + '"' + "\n")

        create_weapon()
        print("\n")
        weapon_configs_iterations += 1



load_outfit_configs()

input()