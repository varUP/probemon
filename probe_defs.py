import csv

def clean(mac_list):
    return sorted(set(mac_list))

with open('Loggin') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    macs = [record[1] for record in reader]
    clean_macs = clean(macs)

print(len(clean_macs))

for mac in clean_macs:
    print(mac)
