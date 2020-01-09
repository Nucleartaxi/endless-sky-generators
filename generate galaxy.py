# Copyright (c) 2020 by Nucleartaxi

#Imports
import math
import glob
import random

def roundup100(x):
    return int(math.ceil(x / 100.0)) * 100

log_file = open('galaxy generator log.txt','w')
def myprint(text):
    print(text)
    log_file.write(str(text) + '\n')

class system():
    def __init__(self, name, pos, links, galaxy_name, system_layer, planet_list, level):
        self.name = name
        self.pos = pos
        self.links = links
        self.galaxy_name = galaxy_name
        self.system_layer = system_layer
        self.planet_list = []
        self.level = level

class galaxy():
    def __init__(self, name, min_x, max_x, min_y, max_y, layer, is_circle, desc_files, planet_config, government):
        self.name = name
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.layer = layer
        self.is_circle = is_circle
        self.desc_files = desc_files
        self.planet_config = planet_config
        self.government = government

def galaxy_place_systems():
    #this dictionary contains everything related to the system's level.
    level_desc_file_dict = {}

    generate_galaxy_config = open(galaxy_config_file, "r")
    for line in generate_galaxy_config: #reads lines in galaxy config and assigns variables
        if "galaxy_seed" in line:
            galaxy_seed = int(next(generate_galaxy_config))
        if "galaxy_systems" in line:
            galaxy_systems = next(generate_galaxy_config).strip()
        if "galaxy_is_circle" in line:
            galaxy_is_circle = next(generate_galaxy_config)
            if str(galaxy_is_circle) in ['true', 'True', 'true\n', 'True\n']:
                galaxy_is_circle = True
            elif galaxy_is_circle in ['false', 'False', 'false\n', 'False\n']:
                galaxy_is_circle = False
            else:
                galaxy_is_circle = False

        if "galaxy_center_x" in line:
            galaxy_center_x = int(next(generate_galaxy_config))
        if "galaxy_center_y" in line:
            galaxy_center_y = int(next(generate_galaxy_config))
        if "galaxy_radius_x" in line:
            galaxy_radius_x = int(next(generate_galaxy_config))
        if "galaxy_radius_y" in line:
            galaxy_radius_y = int(next(generate_galaxy_config))

        if "system_delete_distance" in line:
            system_delete_distance = next(generate_galaxy_config).strip()

        if "hyperlane_min_distance" in line:
            hyperlane_min_distance = next(generate_galaxy_config)
        if "hyperlane_max_distance" in line:
            hyperlane_max_distance = next(generate_galaxy_config)

        if "system_namelist_file" in line:
            system_namelist_file = next(generate_galaxy_config)
        if "galaxy_government" in line:
            galaxy_government = next(generate_galaxy_config).strip()


        if "planet_name_list" in line:
            level_desc_file_dict['planet_namelist_file'] = next(generate_galaxy_config)
        if "galaxy_government" in line:
            level_desc_file_dict['galaxy_government'] = next(generate_galaxy_config)

        if "system_level_generation_type" in line:
            system_level_generation_type = next(generate_galaxy_config).strip().lower()
            if 'random' in system_level_generation_type:
                system_level_generation_type = 'random'
            if 'radial' in system_level_generation_type:
                system_level_generation_type = 'radial'
            else:
                system_level_generation_type = 'random'

        if "num_points_level_5" in line:
            num_points_level_5 = int(next(generate_galaxy_config))
        if "effect_radius_level_5" in line:
            effect_radius_level_5 = int(next(generate_galaxy_config))

        if "min_radius_from_center_level_5" in line:
            min_radius_from_center_level_5 = int(next(generate_galaxy_config))
        if "max_radius_from_center_level_5" in line:
            max_radius_from_center_level_5 = int(next(generate_galaxy_config))

        if "level_1_description" in line:
            level_desc_file_dict[1] = next(generate_galaxy_config).replace('.txt', '').strip()
        if "level_2_description" in line:
            level_desc_file_dict[2] = next(generate_galaxy_config).replace('.txt', '').strip()
        if "level_3_description" in line:
            level_desc_file_dict[3] = next(generate_galaxy_config).replace('.txt', '').strip()
        if "level_4_description" in line:
            level_desc_file_dict[4] = next(generate_galaxy_config).replace('.txt', '').strip()
        if "level_5_description" in line:
            level_desc_file_dict[5] = next(generate_galaxy_config).replace('.txt', '').strip()

        if "level_1_spaceport" in line:
            level_desc_file_dict['sp1'] = next(generate_galaxy_config).replace('.txt', '').strip()
        if "level_2_spaceport" in line:
            level_desc_file_dict['sp2'] = next(generate_galaxy_config).replace('.txt', '').strip()
        if "level_3_spaceport" in line:
            level_desc_file_dict['sp3'] = next(generate_galaxy_config).replace('.txt', '').strip()
        if "level_4_spaceport" in line:
            level_desc_file_dict['sp4'] = next(generate_galaxy_config).replace('.txt', '').strip()
        if "level_5_spaceport" in line:
            level_desc_file_dict['sp5'] = next(generate_galaxy_config).replace('.txt', '').strip()

        if "level_1_fleet" in line:
            level_desc_file_dict['fleet1'] = next(generate_galaxy_config).strip().replace(', ', ',').split(',')
        if "level_2_fleet" in line:
            level_desc_file_dict['fleet2'] = next(generate_galaxy_config).strip().replace(', ', ',').split(',')
        if "level_3_fleet" in line:
            level_desc_file_dict['fleet3'] = next(generate_galaxy_config).strip().replace(', ', ',').split(',')
        if "level_4_fleet" in line:
            level_desc_file_dict['fleet4'] = next(generate_galaxy_config).strip().replace(', ', ',').split(',')
        if "level_5_fleet" in line:
            level_desc_file_dict['fleet5'] = next(generate_galaxy_config).strip().replace(', ', ',').split(',')
            
        if "system_level_debug" in line:
            system_level_debug = next(generate_galaxy_config)
            if str(system_level_debug) in ['true', 'True', 'true\n', 'True\n']:
                system_level_debug = True
            elif system_level_debug in ['false', 'False', 'false\n', 'False\n']:
                system_level_debug = False
            else:
                system_level_debug = False

        if "planet_sprites_config" in line:
            planet_sprites_config = next(generate_galaxy_config).strip()
    generate_galaxy_config.close()

    global system_layer #puts each galaxy on a seperate system layer each time a new galaxy is created
    system_layer += 1

    if galaxy_is_circle is True:
        myprint("Galaxy is circle")
    else:
        myprint("Galaxy is not circle")

    global planet_sprites_config_dict
    planet_sprites_config_dict = {}

    planet_sprites_config_list = []
    planet_sprites_config_file = open('config/planet config/planet sprites config/' + str(planet_sprites_config) + '.txt', 'r')
    for line in planet_sprites_config_file:
        line = line.strip('\n').replace(', ', ',').split(',')
        planet_sprites_config_list.append((line[0], float(line[1]), float(line[2])))
    planet_sprites_config_dict[planet_sprites_config] = planet_sprites_config_list

    galaxy_min_x = galaxy_center_x - abs(galaxy_radius_x) #abs() is to ensure the radius is positive
    galaxy_max_x = galaxy_center_x + abs(galaxy_radius_x)
    galaxy_min_y = galaxy_center_y - abs(galaxy_radius_y)
    galaxy_max_y = galaxy_center_y + abs(galaxy_radius_y)
    myprint('galaxy min (' + str(galaxy_min_x) + ', ' + str(galaxy_min_y) + ') galaxy max (' + str(galaxy_max_x) + ', ' + str(galaxy_max_y) + ')')

    galaxy_name = galaxy_config_file.replace("config/galaxy config/", "").replace(".txt", "")
    galaxy_list.append(galaxy(galaxy_name, galaxy_min_x, galaxy_max_x, galaxy_min_y, galaxy_max_y, system_layer, galaxy_is_circle, level_desc_file_dict, planet_sprites_config, galaxy_government))

    if 'auto' in galaxy_systems:
        galaxy_systems = int(round(((galaxy_radius_x * 2) * (galaxy_radius_y * 2))/ 3000))
        myprint('Auto systems amount: ' + str(galaxy_systems))

    random.seed(galaxy_seed)

    #Creates Coordinates
    myprint('Creating coordinates...')
    system_coordinates = []
    system_count = 1
    while system_count <= int(galaxy_systems):
        system_x_value = round(random.uniform(int(galaxy_min_x), int(galaxy_max_x)))
        system_y_value = round(random.uniform(int(galaxy_min_y), int(galaxy_max_y)))
        system_coordinates.append((system_x_value, system_y_value))
        system_count += 1

    #Deletes extra systems that are too close together 
    myprint("Deleting extraneous systems... please wait. This may take some time depending on how many systems are generated.\n...")
    for pt in system_coordinates:
        for PT in system_coordinates:
            if (abs(pt[0]-PT[0])+abs(pt[1]-PT[1]))!=0 and abs(pt[0]-PT[0])< int(system_delete_distance) and abs(pt[1]-PT[1]) < int(system_delete_distance):
                system_coordinates.remove(PT)
                #myprint("Removed system at coordinates " + str(PT))

    #Deletes systems outside circle if the galaxy is a circle
    myprint("Deleting extraneous systems outside circle... please wait. This may take some time depending on how many systems are generated.\n...")
    if galaxy_is_circle is True:
        #a and b are denominators of x and y
        a = galaxy_radius_x * galaxy_radius_x
        b = galaxy_radius_y * galaxy_radius_y
        h = galaxy_center_x
        k = galaxy_center_y
        #(x-h)^2/a + (y-k)^2/b = 1
        systems_to_delete = []
        for pt in system_coordinates:
            if ((pt[0] - h) **2)/a + ((pt[1] - k) **2)/b  >= 1:
                systems_to_delete.append(pt)
                #myprint("Removed system at coordinates circle " + str(pt))
            else:
                #myprint('coord in circle ' + str(pt))
                pass
        for pt in systems_to_delete:
            system_coordinates.remove(pt)

    #Reads in names and adds them to a list, if one has already been used, remove it
    myprint('Reading namelist...')
    system_namelist_file = open("names/" + str(system_namelist_file).replace('\n', '') + '.txt', "r")
    system_name_list = []
    i = 0
    for line in system_namelist_file:
        system_name = (str(line).strip('\n'))
        if system_name not in system_used_namelist:
            system_name_list.append(str(system_name))
            #myprint('system name ' + system_name + ' in namelist')

    #Calculates and assigns hyperlanes
    dict_coordinates_links = {}
    hyperlane_check_count = 0
    #myprint("system coordinates " + str(system_coordinates))
    while hyperlane_check_count < 1:
        for pt in system_coordinates:
            for PT in system_coordinates:
                hypot = int(math.hypot(pt[0] - PT[0], pt[1] - PT[1]))
                if hypot <= int(hyperlane_max_distance) and hypot >= int(hyperlane_min_distance):
                    #myprint("Confirmed hyperlane at " + str(PT) + " and " + str(pt))
                    if pt in dict_coordinates_links.keys(): # If key is in dict
                        dict_coordinates_links[pt].append(PT)
                        #myprint("key in dictionary")
                    else: # If key isn't in dict
                        dict_coordinates_links[pt] = []
                        dict_coordinates_links[pt].append(PT)
                        #myprint("key not in dictionary")

                    if PT in dict_coordinates_links.keys(): # If key is in dict
                        dict_coordinates_links[PT].append(pt)
                        #myprint("key in dictionary")
                    else: # If key isn't in dict
                        dict_coordinates_links[PT] = []
                        dict_coordinates_links[PT].append(pt)
                        #myprint("key not in dictionary")

        hyperlane_check_count += 1
    #chances
    #generate given number of points within min and max x and y
        #if point is outside radius, delete it and try again (i = i to continue the loop)
        #if point is in radius (i + 1)
        #if random.uniform() <= .05      - 5% chance of happening
        #if random.uniform() <= .9       - 90% chance of happening

    #Selects system level generation type and assigns coordinates to system level centers
    if system_level_generation_type == 'random':
        myprint('System level generation type: random')
    elif system_level_generation_type == 'radial':
        myprint('System level generation type: radial')
        myprint('Generating center points...')
        system_level_points = []
        i = 0
        math_hypot = math.hypot(galaxy_center_x, galaxy_center_y)
        min_radius = min_radius_from_center_level_5 + math_hypot
        max_radius = max_radius_from_center_level_5 + math_hypot
        while i < num_points_level_5:
            x = int(random.randint(-max_radius_from_center_level_5, max_radius_from_center_level_5) + galaxy_center_x)
            y = int(random.randint(-max_radius_from_center_level_5, max_radius_from_center_level_5) + galaxy_center_y)
            distance = int(math.hypot(x, y))
            
            if distance >= min_radius and distance <= max_radius:
                myprint("\tx: " + str(x) + " y: " + str(y))
                system_level_points.append((x, y))
                i += 1
            else:
                myprint('\tpoint ('  + str(x) + ', ' + str(y) + ') not within radii, generating another')
        #myprint('generated ' + str(num_points_level_5) + ' points')

    #Assigns coordinates and system levels to system names
    dict_pos_name = {}
    for key in dict_coordinates_links:
        if system_level_generation_type == 'random':
            system_level = random.randint(1, 5)
        if system_level_generation_type == 'radial':
            x1 = key[0]
            y1 = key[1]
            possible_system_levels = []
            for item in system_level_points:
                x2 = item[0]
                y2 = item[1]
                #myprint("x: " + str(x2) + " y: " + str(y2))
                distance = int(math.hypot(x2 - x1, y2 - y1))
                #myprint("distance: " + str(distance))
                percent_distance = round((1 - (distance / effect_radius_level_5)), 2)
                #myprint('percent distance: ' + str(percent_distance))
                if percent_distance >= .8:
                    possible_system_levels.append(5)
                elif percent_distance >= .6:
                    possible_system_levels.append(4)
                elif percent_distance >= .4:
                    possible_system_levels.append(3)
                elif percent_distance >= .2:
                    possible_system_levels.append(2)
                else:
                    possible_system_levels.append(1)
            try:
                system_level = max(possible_system_levels)
            except: #number of level 5 points is 0, so every system gets a system level of 1
                system_level = 1
            #myprint("System level: " + str(system_level))
        if system_level_debug is True:
            name = system_name_list.pop(random.randint(0, len(system_name_list) - 1))
            system_used_namelist.append(name)
            dict_pos_name[key] = (name + ' [' + str(system_level) + ']', system_level) #puts name and level in tuple (name, level)
        else:
            name = system_name_list.pop(random.randint(0, len(system_name_list) - 1))
            system_used_namelist.append(name)
            dict_pos_name[key] = (name, system_level)

        

    #myprint("dict pos name         " + str(dict_pos_name))           Useful for debugging
    #myprint("dict coordinates list " + str(dict_coordinates_links))

    #Commodities
    myprint('Creating commodities...')
    commodity_file_list = glob.glob("config/planet config/commodities/*.txt") #Imports files in directory
    commodity_line_dict = {}
    names_list = []
    for item in commodity_file_list:
        name = item.replace("config/planet config/commodities\\", "").replace(".txt", "")
        names_list.append(name)

        i = 1
        commodity_line_list = []
        commodity_file = open(item, 'r')
        for line in commodity_file:
            lines = line.split(',')
            line2 = (int(lines[0].strip()), int(lines[1].strip()))
            commodity_line_list.append(line2)
        commodity_line_dict[name] = commodity_line_list
        commodity_file.close()
    #myprint('commodity line dict: ' + str(commodity_line_dict))
    
    global commodity_dict
    commodity_dict = {}
    i = 1
    while i <= 5:
        commodity_list = []
        for name in names_list:
            commodity = (name, commodity_line_dict[name][i - 1][0], commodity_line_dict[name][i - 1][1]) #commodity, min for i level, max for i level
            commodity_list.append(commodity)
        commodity_dict[i] = commodity_list
        i += 1
    #myprint(commodity_dict)

    #Fleets
    myprint('Creating fleets...')
    fleet_file_list = glob.glob("config/planet config/fleets/*.txt") #Imports files in directory
    global fleet_dict
    fleet_dict = {}
    names_list = []
    for item in fleet_file_list:
        name = item.replace("config/planet config/fleets\\", "").replace(".txt", "")
        names_list.append(name)

        i = 1
        fleet_line_list = []
        fleet_file = open(item, 'r')
        for line in fleet_file:
            line = line.replace(', ', ',').strip()
            lines = line.split(',')
            fleet_line_list.append(lines)
        fleet_dict[name] = fleet_line_list
        fleet_file.close()
    #myprint('fleet line dict: ' + str(fleet_dict))

    #Renames keys and dict data from coordinates to system names
    myprint('Assigning names to coordinates and finalizing systems...')
    for key in dict_coordinates_links.keys():
        list1 = dict_coordinates_links[key]
        links_name_list = []
        links_name_list.clear()
        links_name_list = []
        i = 0
        while i < len(list1):
            item_from_list1 = list1.pop()
            links_name_list.append(str(dict_pos_name[item_from_list1][0]))
        system_name = str(dict_pos_name[key][0])
        system_level = dict_pos_name[key][1]

        system_list.append(system(system_name, key, links_name_list, galaxy_name, system_layer, [], system_level))

    myprint("Galaxy finished.\n\n\n")
    #myprint(system_used_namelist)
    
def galaxy_delete_overlapping_systems():
    #deletes overlapping systems in overlapping galaxies
    myprint("Deleting systems in overlapping galaxies... please wait. This may take some time.")

    generate_galaxy_config = open(galaxy_config_file, "r")
    for line in generate_galaxy_config:
        if "system_delete_distance" in line:
            system_delete_distance = int(next(generate_galaxy_config))

    system_list_to_be_deleted = []

    for galaxy in galaxy_list:
        galaxy_name = str(galaxy.name)
        galaxy_min_x = int(galaxy.min_x)
        galaxy_max_x = int(galaxy.max_x)
        galaxy_min_y = int(galaxy.min_y)
        galaxy_max_y = int(galaxy.max_y)
        galaxy_layer = int(galaxy.layer)

        myprint('\t' + galaxy_name)

        #Deletes system coordinates that are too close together
        #galaxy_name_current = [galaxy_name]
        #works

        for system in system_list:
            if system.system_layer < galaxy_layer:
                pt = system.pos
                #myprint("less than layer")
                #myprint(str(pt[0]) +" "+ str(pt[1]))
                if pt[0] >= galaxy_min_x - system_delete_distance and pt[0] <= galaxy_max_x + system_delete_distance and pt[1] >= galaxy_min_y - system_delete_distance and pt[1] <= galaxy_max_y + system_delete_distance:
                    #myprint("in area")
                    if system in system_list:
                        system_list_to_be_deleted.append(system)
                        #myprint("Removed system " + "layer " + str(system.system_layer) + " coordinates " + str(system.pos))
            elif system.system_layer >= galaxy_layer:
                #myprint("skipped system layer " + str(system.system_layer) + " coordinates " + str(system.pos))
                pass

    for system in system_list_to_be_deleted:
        if system in system_list:
            system_list.remove(system)
        else:
            pass

    generate_galaxy_config.close()
    myprint("\n\n")

class planet_properties():
    def __init__(self, attribute, shipyard, outfitter, required_reputation, bribe, security, tribute, threshold, fleet, name, sprite, landscape):
        self.attribute = attribute
        self.shipyard = shipyard
        self.outfitter = outfitter
        self.required_reputation = required_reputation
        self.bribe = bribe
        self.security = security 
        self.tribute = tribute
        self.threshold = threshold
        self.fleet = fleet
        self.name = name
        self.sprite = sprite
        self.landscape = landscape

class planet():
    def __init__(self, sprite, distance, period, is_habitable, name, planet_properties, descriptions):
        self.sprite = sprite
        self.distance = distance
        self.period = period
        self.is_habitable = is_habitable
        self.name = name
        self.planet_properties = planet_properties
        self.descriptions = descriptions

def load_description_data():
    myprint("loading description data...")
    planet_desc_list = glob.glob("config/description config/descriptions/*.txt") #Imports files in directory

    global planet_desc_dict
    planet_desc_dict = {}
    global planet_desc_dict_keys
    planet_desc_dict_keys = []

    for item in planet_desc_list:
        name = item.replace("config/description config/descriptions\\", "").replace(".txt", "")
        temp_items_list = []
        item = open(item, "r")
        for line in item:
            temp_items_list.append(line.strip('\n'))
        item.close()
        planet_desc_dict_keys.append(name)
        planet_desc_dict[name] = temp_items_list

    #myprint("keys " + str(planet_desc_dict_keys))
    #myprint("dict " + str(planet_desc_dict))
    #myprint("\n")


    myprint("loading word data...")
    planet_word_list = glob.glob("config/description config/words/*.txt") #Imports files in directory

    global planet_word_dict
    planet_word_dict = {}
    global planet_word_dict_keys
    planet_word_dict_keys = []

    for item in planet_word_list:
        name = item.replace("config/description config/words\\", "").replace(".txt", "")
        temp_items_list = []
        item = open(item, "r")
        for line in item:
            temp_items_list.append(line.strip('\n'))
        item.close()
        if "_properties" in str(item):
            pass
        else:
            planet_word_dict_keys.append(name)
            planet_word_dict[name] = temp_items_list

    #myprint("keys " + str(planet_word_dict_keys))
    #myprint("dict " + str(planet_word_dict))

    myprint("loading planet names...")
    global planet_name_dict
    planet_name_dict = {}
    for galaxy in galaxy_list:
        temp_items_list = []
        name_list_file = open('names/' + str(galaxy.desc_files['planet_namelist_file'].strip('\n')) + '.txt', "r")
        for line in name_list_file:
            temp_items_list.append(line.rstrip('\n'))
        name_list_file.close()
        planet_name_dict[galaxy.desc_files['planet_namelist_file']] = temp_items_list


    myprint("loading landscapes...")
    landscape_desc_list = glob.glob("config/planet config/landscape images/*.txt") #Imports files in directory
    global landscape_dict
    landscape_dict = {}

    for item in landscape_desc_list:
        name = item.replace("config/planet config/landscape images\\", "").replace(".txt", "")
        temp_items_list = []
        item = open(item, "r")
        for line in item:
            temp_items_list.append(line.strip('\n'))
        item.close()
        landscape_dict[str(name)] = temp_items_list

    #myprint("Landscape dict: " + str(landscape_dict) + '\n')


    myprint("loading stars...")
    global available_star_list
    available_star_list = []

    star_config = open(star_config_file, "r")
    for line in star_config:
        star = line.split(',')
        available_star_list.append(("star/" + star[0], int(star[1].strip())))


    myprint("loading planet sprites...")
    global planet_sprite_dict
    planet_sprite_dict = {}

    planet_sprite_list = glob.glob("config/planet config/planet sprites/*.txt") #Imports files in directory

    for item in planet_sprite_list:
        name = item.replace("config/planet config/planet sprites\\", "").replace(".txt", "")
        temp_items_list = []
        item = open(item, "r")
        for line in item:
            temp_items_list.append(line.strip('\n'))
        item.close()
        planet_sprite_dict[name] = temp_items_list
    myprint('Successfully loaded data.\n\n\n')
        
def planet_desc_word_replace(description):
    appending_characters = False
    this_desc_words_list = []
    for char in description:
        if char == ">":
            appending_characters = False
            temp_string = ""
            for item in chars_list:
                temp_string = temp_string + item
            this_desc_words_list.append(temp_string)
        if appending_characters is True:
            chars_list.append(char)
        if char == "<":
            appending_characters = True
            chars_list = []

    this_planets_properties_list = []
    for item in this_desc_words_list:
        if item in planet_word_dict_keys:
            if len(planet_word_dict[item]) != 0:
                len_description = random.randint(0, len(planet_word_dict[item]) - 1)
                description = description.replace("<"+str(item)+">", str(planet_word_dict[item][len_description]))
            else:
                description = description.replace("<"+str(item)+">", '')

        else:
            myprint("!!!word <" + str(item) + "> not in list!!!")
        
        try: #Get properties from file
            sprite_list_list = []
            landscape_list_list = []
            attribute_list = []
            shipyard_list = []
            outfitter_list = []
            word_properties_file = open("config/description config/words/" + item + "_properties.txt", "r")
            for line in word_properties_file:
                #if "name_list" in line:      #This was so each <word> could have a different namelist file, this has changed so all planets in one galaxy share a master planet name list
                #    name_list = next(word_properties_file).strip()
                name_list = ''
                if "sprite_list" in line:
                    for item2 in next(word_properties_file).strip().replace(', ', ',').split(','):
                        sprite_list_list.append(item2)
                    sprite_list = sprite_list_list
                if "landscape_list" in line:
                    for item2 in next(word_properties_file).strip().replace(', ', ',').split(','):
                        landscape_list_list.append(item2)
                    landscape_list = landscape_list_list
                if "attribute" in line:
                    for item2 in next(word_properties_file).strip().replace(', ', ',').split(','):
                        attribute_list.append(item2)
                    attribute = attribute_list
                if "shipyard" in line:
                    for item2 in next(word_properties_file).strip().replace(', ', ',').split(','):
                        shipyard_list.append(item2)
                    shipyard = shipyard_list
                if "outfitter" in line:
                    for item2 in next(word_properties_file).strip().replace(', ', ',').split(','):
                        outfitter_list.append(item2)
                    outfitter = outfitter_list
                if "required_reputation" in line:
                    required_reputation = next(word_properties_file).strip()
                if "bribe" in line:
                    bribe = next(word_properties_file).strip()
                if "security" in line:
                    security = next(word_properties_file).strip()
                if "tribute" in line:
                    tribute = next(word_properties_file).strip()
                if "threshold" in line:
                    threshold = next(word_properties_file).strip()
                if "fleet" in line:
                    fleet = next(word_properties_file).strip()

            this_planets_properties_list.append(planet_properties(attribute, shipyard, outfitter, required_reputation, bribe, security, tribute, threshold, fleet, name_list, sprite_list, landscape_list))
            myprint("\tadded properties from <" + item + ">")
            word_properties_file.close()
        except: #Property file does not exist, do nothing (this is intended, not an error)
            myprint("\tno properties from <" + item + ">")
            pass
        
    return description, this_planets_properties_list

def create_planet_properties(system, galaxy):
    i = 0
    is_spaceport = False
    descriptions_temp = []
    properties_list = []
    while i < 2:
        if is_spaceport is False:
            key = planet_desc_dict[galaxy.desc_files[system.level]] #key = lines within the description file (were added to dict earlier in load_description_data)
            description = key[random.randint(0, len(key) - 1)] #gets a random description
            #description = planet_desc_dict[system.level][random.randint(0, len(planet_desc_dict[description_key]) - 1)]
        else:
            key = planet_desc_dict[galaxy.desc_files['sp' + str(system.level)]] #gets the spaceport description file used for this system level
            description = key[random.randint(0, len(key) - 1)] 

        while i > -1:
            if "<" and ">" in description:
                previous_description = description
                description = planet_desc_word_replace(description)
                properties_list.append(description[1])
                description = description[0]
                if previous_description is description:
                    break    
            else:
                break
        descriptions_temp.append(description)
        is_spaceport = True
        i += 1
    #properties_list2 = filter(None, properties_list)
    return descriptions_temp, properties_list

def condense_planet_properties(properties_list):
    #myprint("Condensing planet properties...")
    properties_list = [x for x in properties_list if x != []]
    if len(properties_list) == 0:
        myprint("No properties to add. Continuing.")
        pass
    else:
        attribute_list = []
        shipyard_list = []
        outfitter_list = []
        for list1 in properties_list:
            for item in list1:
                for item2 in item.attribute:
                    attribute_list.append(item2)
                attribute = attribute_list
                for item2 in item.shipyard:
                    shipyard_list.append(item2)
                shipyard = shipyard_list
                for item2 in item.outfitter:
                    outfitter_list.append(item2)
                outfitter = outfitter_list
                required_reputation = item.required_reputation
                bribe = item.bribe
                security = item.security
                tribute = item.tribute
                threshold = item.threshold
                fleet = item.fleet
                name = item.name
                landscape = landscape_dict[item.landscape[random.randint(0, len(item.landscape) - 1)]][random.randint(0, len(landscape_dict[item.landscape[random.randint(0, len(item.landscape) - 1)]]) - 1)]
                sprite = planet_sprite_dict[item.sprite[random.randint(0, len(item.sprite) - 1)]][random.randint(0, len(planet_sprite_dict[item.sprite[random.randint(0, len(item.sprite) - 1)]]) - 1)]

        #myprint("Planet properties condensed.")
        return planet_properties(attribute, shipyard, outfitter, required_reputation, bribe, security, tribute, threshold, fleet, name, sprite, landscape)

def system_planets(system, galaxy): #Generates planets in system
    #myprint("Working on planets in system " + str(system.name))
    sprite_controls = planet_sprites_config_dict[galaxy.planet_config]

    system_level = system.level
    
    #https://en.wikipedia.org/wiki/Stellar_classification#Luminosity_class
    #Habitable inner: sqrt(Luminosity/1.1) outer: sqrt(Luminosity/.53)
    #belt 1000 to 2000
    #Generate basic planets from in to out based on hab zone: molten, desert, forest/water if right conditions, gas giants with moons
    #Invisible fence = 10,000 units
    this_system_planet_list = []    #list of planets for this system, resets each time function called, contains planet object

    star = available_star_list[random.randint(0, len(available_star_list) - 1)]

    habitable_zone = star[1]
    star = star[0]
    #myprint(star)

    this_system_planet_list.append(planet(star, None, 10, False, None, None, None))

    min_distance_from_center = 50
    planet_radius = 120
    max_habitable_planets = 1
    is_habitable_chance = 1
    number_of_planets = random.randint(4, 5)

    distance = min_distance_from_center
    habitable_planets = 0
    i = 0
    while i < number_of_planets:
        #Determines habitable planets
        #distance = distance + random.randint(abs(distance - 100), distance * random.randint(1,2))
        distance = distance + (planet_radius * 2) + random.randint(50, 100)
        fraction = round(distance / habitable_zone, 2)
        if fraction > 2:
            planet_radius = 200

        
        if fraction > .5 and fraction < 2:
            if random.uniform(0, 1) < is_habitable_chance and habitable_planets < max_habitable_planets:
                is_habitable = True
                habitable_planets += 1
            else:
                is_habitable = False
        else:
            is_habitable = False

        possible_sprites = []
        if not is_habitable:
            for item in sprite_controls:
                if fraction >= item[1] and fraction <= item[2]:
                    possible_sprites.append(planet_sprite_dict[item[0]])

            if len(possible_sprites) == 0:
                myprint('!!! WARNING !!! Planet was not assigned a sprite from the planet sprite config file, assigning rock0 as default sprite')
                possible_sprites.append('rock0')

            popped_sprite_list = possible_sprites[random.randint(0, len(possible_sprites) - 1)]
            sprite = "planet/" + str(popped_sprite_list[random.randint(0, len(popped_sprite_list) - 1)])
        #the period calculation is WIP, trying to figure out a good way to do it
        #period = (2 * math.pi) * sqrt((distance * distance * distance)/266470)
        period = round((distance ** 2) ** (1 / 3), 4)

        if not is_habitable:
            this_system_planet_list.append(planet(sprite, distance, period, is_habitable, None, None, None))        ##########################################################
            pass
        if is_habitable:
            planet_properties_returned = create_planet_properties(system, galaxy)
            descriptions_temp = planet_properties_returned[0]
            properties_list = planet_properties_returned[1]
            condensed_properties = condense_planet_properties(properties_list)     #sorts and overrides properties

            i2 = 0
            while i2 < 1:
                name = planet_name_dict[galaxy.desc_files['planet_namelist_file']][random.randint(0, len(planet_name_dict[galaxy.desc_files['planet_namelist_file']]) - 1)]
                if name not in planet_used_namelist:
                    planet_used_namelist.append(name)
                    i2 += 1
                else:
                    #myprint('!!! planet name ' + name + ' not in dict, choosing another')
                    pass
                    
            sprite = 'planet/' + str(condensed_properties.sprite)
            this_system_planet_list.append(planet(sprite, distance, period, is_habitable, name, condensed_properties, descriptions_temp))   #Adds this planet to the planet list for this system
            planet_names_list.append(planet(condensed_properties.sprite, distance, period, is_habitable, name, condensed_properties, descriptions_temp))
            #planet_names_dict["Name!"] = planet_properties("Name!") #for "Name!" add it to dict with planet_properties(properties) as properties for that planet when its name is called from planet_names_dict
        i += 1

    for item in this_system_planet_list:
        system.planet_list.append(item)
        #myprint("Appended " + str(item))

def galaxy_write_systems(galaxy):
    myprint('Writing systems for galaxy ' + str(galaxy.name) + '...')
    galaxy_output = open("output/galaxy" + galaxy_output_file + ".txt", "w")
    for item in system_list:                #W R I T E S   S Y S T E M S
        #name
        galaxy_output.write('system ' + '"' + str(item.name) + '"' + "\n")
        #position
        galaxy_output.write('\tpos ' + str(item.pos).replace('(', '').replace(')', '').replace(',', '') + "\n")

        #government
        galaxy_output.write('\tgovernment ' + '"' + galaxy.government + '"' + "\n")

        #habitable
        #belt

        galaxy_output.write('\tbelt ' + str(random.randint(1000, 1500)) + "\n")

        links_temp_list = item.links
        links_temp_list_write = list(set([str(e) for e in links_temp_list ]))
        for str1 in links_temp_list_write:
            galaxy_output.write('\tlink ' + '"' + str(str1) + '"' + "\n")
        
        #asteroids
        #mineables

        #commodities
        for commodity in commodity_dict[item.level]:
            galaxy_output.write('\ttrade ' + '"' + str(commodity[0]) + '"' + ' ' + str(random.randint(commodity[1], commodity[2])) + "\n")

        #fleet
        fleet_properties = galaxy.desc_files['fleet' + str(item.level)]
        fleet_amount = random.randint(int(fleet_properties[1]), int(fleet_properties[2]))
        fleets_list = fleet_dict[fleet_properties[0]]
        if fleet_amount > len(fleets_list):
            fleet_amount = len(fleets_list)

        random.shuffle(fleets_list) #ensures that fleets at the top of the fleets file don't get priority over lower ones
        i = 0
        while i < fleet_amount:
            galaxy_output.write('\tfleet "' + str(fleets_list[i][0]) + '" ' + str(roundup100(random.randint(int(fleets_list[i][1]), int(fleets_list[i][2])))) + "\n")
            i += 1

        #planets
        for planet in item.planet_list:
            if planet.name is None:
                galaxy_output.write('\tobject' + "\n")
            else:
                galaxy_output.write('\tobject "' + str(planet.name) + '"\n')
            galaxy_output.write('\t\tsprite ' + str(planet.sprite)+ "\n")
            if "star" in planet.sprite:
                pass
            else:
                galaxy_output.write('\t\tdistance ' + str(planet.distance)+ "\n")
            galaxy_output.write('\t\tperiod ' + str(planet.period)+ "\n")
        galaxy_output.write('\n')

    for planet in planet_names_list:
        galaxy_output.write('planet "' + planet.name + '"\n')
        #myprint(planet.planet_properties.attribute)
        if planet.planet_properties.attribute[0] != '':
            galaxy_output.write('\tattributes ' + str(planet.planet_properties.attribute).replace('[','').replace(']','').replace("'","").replace(',','').strip() + '\n')
        galaxy_output.write('\tlandscape land/' + str(planet.planet_properties.landscape).strip('\n') + '\n')
        galaxy_output.write('\tdescription `' + str(planet.descriptions[0]) + '`\n')
        galaxy_output.write('\tspaceport `' + str(planet.descriptions[1]) + '`\n')

        if planet.planet_properties.shipyard[0] != '':
            for item in planet.planet_properties.shipyard:
                galaxy_output.write('\tshipyard ' + str(item) + '\n')
        if planet.planet_properties.outfitter[0] != '':
            for item in planet.planet_properties.outfitter:
                galaxy_output.write('\toutfitter ' + str(item) + '\n')

        if planet.planet_properties.required_reputation != '':
            galaxy_output.write('\t"required reputation" ' + str(planet.planet_properties.required_reputation) + '\n')
        if planet.planet_properties.bribe != '':
            galaxy_output.write('\tbribe ' + str(planet.planet_properties.bribe) + '\n')
        if planet.planet_properties.security != '':
            galaxy_output.write('\tsecurity ' + str(planet.planet_properties.security) + '\n')
        if planet.planet_properties.tribute != '':
            galaxy_output.write('\ttribute ' + str(planet.planet_properties.tribute) + '\n')
        if planet.planet_properties.threshold != '':
            galaxy_output.write('\t\tthreshold ' + str(planet.planet_properties.threshold) + '\n')
        if planet.planet_properties.fleet != '':
            galaxy_output.write('\t\tfleet ' + str(planet.planet_properties.fleet) + '\n')


        galaxy_output.write('\n')

    #    myprint("Wrote system data " + str(system_list[system_write_count].name))
        
    #myprint("Wrote all systems")
    galaxy_output.close()

def load_galaxy_configs():

    galaxy_configs_list = glob.glob("config/galaxy config/*.txt") #Imports files in directory
    galaxy_configs_amount = len(galaxy_configs_list) #Gets amount of items in list

    global system_list
    system_list = []
    global galaxy_list
    galaxy_list = []
    global system_used_namelist
    system_used_namelist = []
    global system_layer
    system_layer = -1

    global planet_names_list
    planet_names_list = []

    galaxy_configs_iterations = 0
    while galaxy_configs_iterations < galaxy_configs_amount: #Creates galaxies for each config files
        global galaxy_config_file #Config File
        galaxy_config_file = str(galaxy_configs_list[galaxy_configs_iterations]).replace("\\", "/")

        global galaxy_output_file #Output file
        galaxy_output_file = ""
        #galaxy_output_file = str(galaxy_configs_list[galaxy_configs_iterations]).replace("\\", "/").replace("config/galaxy config/", "")   #This is for dynamic galaxy output with a seperate file for each galaxy config
        
        global star_config_file
        star_config_file = "config/planet config/planet sprites/000 stars.txt"

        galaxy_place_systems()

        
        galaxy_configs_iterations += 1

    galaxy_delete_overlapping_systems()

    #Generates planets for each system in system list
    load_description_data()

    global planet_used_namelist
    planet_used_namelist = []

    for galaxy in galaxy_list:
        myprint('Creating planets in galaxy ' + galaxy.name)
        galaxy_layer = galaxy.layer
        for system in system_list:
            if system.system_layer is galaxy_layer:
                system_planets(system, galaxy)
        myprint('\n\n\n')
        galaxy_write_systems(galaxy)

    myprint("Success!")
    input()

load_galaxy_configs()