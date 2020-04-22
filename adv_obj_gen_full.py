import json

f = open('adv_dict.txt','r')
data = f.read()
f.close()
adv_dict = eval(data)

f = open('js/adv_list_full.js','w')
f.write("const adv = [\n")


comma = False
scomma = False

for entry in adv_dict:
    adv = adv_dict[entry]
    if comma:
        f.write(',\n')
    else:
        comma = True

    tmp = entry
    if len(tmp) == 10:
        tmp = tmp[0:7] + tmp[8:]

    f.write('\t{\n')
    f.write('\t\tcid: \'' + tmp + '\',\n')
    f.write('\t\tname: \'' + adv["name"].replace('\'s','') + '\',\n')
    f.write('\t\ttitle: \'' + adv["title"].replace('\'s','') + '\',\n')
    f.write('\t\telement: \'' + adv["element"] + '\',\n')
    f.write('\t\tweapon: \'' + adv["weapon"] + '\',\n')
    f.write('\t\trarity: ' + adv["rarity"] + '\n')
    f.write('\t}')


f.write('\n];\n')
f.write('export default adv;')
f.close()
