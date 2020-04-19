import json

sp_adv = ['100002_013', '100029_02', '100029_03', '100010_04', '110328_01', '110007_02', '100001_08', '100003_07', '110291_01', '110327_01', '110050_02', '100005_02', '100004_010', '110333_01', '110354_01', '100006_09']

f = open('adv_dict.txt','r')
data = f.read()
f.close()
adv_dict = eval(data)

f = open('js/adv_list.js','w')
f.write("const adv = [\n")

s = open('js/sp_adv.js','w')
s.write("const sp_adv = [\n")

comma = False
scomma = False

for entry in adv_dict:
    adv = adv_dict[entry]
    if comma:
        f.write(',\n')
    else:
        comma = True
        
    if len(entry) == 10:
        entry = entry[0:7] + entry[8:]

    f.write('\t{\n')
    f.write('\t\tcid: \'' + entry + '\',\n')
    f.write('\t\tname: \'' + adv["name"].replace('\'s','') + '\',\n')
    f.write('\t\telement: \'' + adv["element"] + '\',\n')
    f.write('\t\tweapon: \'' + adv["weapon"] + '\',\n')
    f.write('\t\trarity: ' + adv["rarity"] + '\n')
    f.write('\t}')

    if entry in sp_adv:
        if scomma:
            s.write(',\n')
        else:
            scomma = True
        s.write('\t{\n')
        s.write('\t\tcid: \'' + entry + '\',\n')
        s.write('\t\tname: \'' + adv["name"].replace('\'s','') + '\',\n')
        s.write('\t\tweapon: \'' + adv["weapon"] + '\'\n')
        s.write('\t}')

f.write('\n];\n')
f.write('export default adv;')
f.close()

s.write('\n];\n')
s.write('export default sp_adv;')
s.close()
