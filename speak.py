#!/usr/bin/env python3

from subprocess import call


cmd_beg = 'espeak -s 155 -a 200 '
gnome_says = 'My gnomey ways to tell a table, I shall add mac address '

cmd_end = ' | aplay /root/temp/wavs/Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
cmd_out = '--stdout > /root/temp/wavs/Text.wav ' # To store the voice file

text = input("Enter MAC Address: ")
print(text)

# Replacing ' ' with '_' to identify words in the text entered
text = text.replace(' ', '_')

# Calls the Espeak TTS Engine to read aloud a Text
print(call([cmd_beg + cmd_out + gnome_says + text + gnome_says2 + cmd_end], shell=True))
