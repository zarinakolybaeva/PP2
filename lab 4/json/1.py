import json
jsondata = open('sample-data.json').read()
d_json = json.load(jsondata)
print(
    "Interface Status" "\n"
    "=======================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------")
imdata = d_json["imdata"]
for i in range(3):
        dn = imdata[i]["l1PhysIf"]["attributes"]["dn"]
        descr = imdata[i]["l1PhysIf"]["attributes"]["descr"]
        speed = imdata[i]["l1PhysIf"]["attributes"]["speed"]
        mtu = imdata[i]["l1PhysIf"]["attributes"]["mtu"]
        print("{0:50} {1:20} {2:10} {3:6}".format(dn,descr,speed,mtu))