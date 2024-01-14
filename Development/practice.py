import sounddevice as sd         ## importing package
import soundfile as sf 
import paho.mqtt.client as mqtt
import time
import json
#from scipy.io.wavfile import write

# host = "172.17.1.4"
host = "192.168.1.5"
fs = 11000           # sampling rate setting
seconds = 1          # seconds for which recording will go on
# i = 1


def on_connect(client, usrdata, flags, rc):
	print("Connection Established") if rc == 0 else print("Bad Connection") 

client1 = mqtt.Client("publisher")
client1.on_connect = on_connect 
client1.username_pw_set("edgecomp", "Edge@123#")
client1.connect(host, port=1883)
#print("Published Successfully")
client1.loop_start()
while True:
    recording = sd.rec(int(fs * seconds) , samplerate=fs, channels=2, dtype='float32', blocking=True) ## recording ( before recording connect audio card with mic inserted in it)
    recording = recording[::2]      ## downsampling
    # sf.write('output{}.flac'.format(i),recording, fs)
    
    # write("output{}.wav".format(i), fs, recording)
    #i += 1
    
    client1.publish("topic/new", json.dumps(recording.tolist()))
    print("Published Successfully")
    # time.sleep(2)
    client1.loop_stop()
    print(recording)                ##  printing digitized values
