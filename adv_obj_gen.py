import json

f = open('adv_dict.txt','r')
data = f.read()
f.close()
adv_dict = eval(data)

f = open('adv_list.js','w')
f.write("const adv = [\n")

comma = False

for entry in adv_dict:
    adv = adv_dict[entry]
    if comma:
        f.write(',\n')
    else:
        comma = True

    f.write('\t{\n')
    f.write('\t\tcid: \'' + entry + '\',\n')
    f.write('\t\tname: \'' + adv["name"].replace('\'s','') + '\',\n')
    f.write('\t\telement: \'' + adv["element"] + '\',\n')
    f.write('\t\tweapon: \'' + adv["weapon"] + '\',\n')
    f.write('\t\trarity: ' + adv["rarity"] + '\n')
    f.write('\t}')

f.write('\n];\n')
f.write('export default adv;')
f.close()
