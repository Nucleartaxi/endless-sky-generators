lines = sorted(set(open('star names 3 massive.txt', 'r').readlines()))
output = open('output.txt', 'w')
for item in lines:
    output.write(item)
