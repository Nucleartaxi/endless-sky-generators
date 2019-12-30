
import random

file_name = "map.txt"
map_file = open(file_name, "r")

system_dict = {}
line_list = []
links_list = []
system_dict_names = []

started = False
is_reading = False

for line in map_file:
    line = line.strip('\n')
    print(line)
    
    if 'system' in line:
        system_name = line.replace('system ', '')
        is_reading = True
        started = True

    if len(line) == 0:
        is_reading = False
    
    if is_reading:
        if 'link' not in line:
            line_list.append(line)
        elif 'link' in line:
            links_list.append(line.replace('link ', '').strip('\t'))

    elif is_reading is False and started is True:
        system_dict[system_name] = (links_list, line_list)
        system_dict_names.append(system_name)
#        print(line_list)
#        print(links_list)
        line_list = []
        links_list = []

map_file.close()

#Creates inter-system wormholes
wormhole_list = []
wormhole_temp_list = []


print("Please wait, generating wormholes.....")
for pt in system_dict_names:
    for PT in system_dict_names:
#        print("\n")
#        print("pt | " + pt + " ||||| " + str(system_dict[pt][0]))
#        print("PT | " + PT + " ||||| " + str(system_dict[PT][0]))
        if PT in system_dict[pt][0] and pt in system_dict[PT][0]:
#            print("-=-=- PT in pt")
#            print("-=-=- pt in PT")

            points = [PT, pt]
            points.sort()
            wormhole = points[0] + "-" + points[1]
            wormhole = wormhole.replace('"', '')
            wormhole_list.append(wormhole)
            wormhole_temp_list.append(wormhole)
        system_dict[pt] = (system_dict[pt][0], system_dict[pt][1], wormhole_temp_list)
    wormhole_temp_list = []
            
print(wormhole_list)



#Writes to file
map_output_file = open(file_name + "output.txt", "w")

for name in system_dict_names:
    for item in system_dict[name][1]:
        map_output_file.write(item + '\n')
    for wormhole in system_dict[name][2]:
            map_output_file.write('\tobject ' + '"' + str(wormhole) + '"' + '\n')
            map_output_file.write('\t\tsprite planet/wormhole' + '\n')
            map_output_file.write('\t\tdistance ' + str(random.randint(1000, 5000)) + '\n')
            map_output_file.write('\t\tperiod ' + str(random.randint(1000, 10000)) + '\n')
    map_output_file.write('\n')

wormhole_list = list(set(wormhole_list))
for wormhole in wormhole_list:
    map_output_file.write('planet ' + '"' + wormhole + '"' + '\n')
    map_output_file.write('\tdescription ""'+ '\n')
    map_output_file.write('\n')

