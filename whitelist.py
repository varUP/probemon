import csv
from subprocess import call
import datetime

def clean(mac_list):
    return sorted(set(mac_list))

def white(macaddr, device):
    with open('/root/Loggin') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        macs = [record[1] for record in reader]
        clean_macs = clean(macs)

    text = str(macaddr)
    # print clean_macs
    
    now = datetime.datetime.now()

    if text in clean_macs:
        print now, "yes, it is here, but passing on:", text, device
        pass
    else:
        text = text.replace(' ', '_')
        cmd_end = '\"'
	spacer = " "
	gnome_says = '\"With my gnomey ways I will tell you a fable, for I shall add your mac address to my table. ' + text + spacer + device + cmd_end
	print now, 'espeak', '-s', '155', '-a', '200', gnome_says
	call(['espeak', '-s', '155', '-a', '200', gnome_says])

# white("4c:0a:rt:85:1q:17", "Apple, Inc.")
