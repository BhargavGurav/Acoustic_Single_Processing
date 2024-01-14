#################################### Script for testing paho-mqtt work #############################################

# import paho.mqtt.client as mqtt
# import time
# import numpy as np

# def on_message(client, userdata, message):
#     print('Hello')
#     message = np.array(str(message.payload.decode("utf-8")))
#     print("Message received successfully which is :- {}".format(message))
#     print("type : ", type(message))
#     # print("Message topic is : {}".format(message.topic))
# # sublisher script 

# sub_client = mqtt.Client(client_id="subscriber")
# # sub_client.username_pw_set("edgecomp", "Edge@123#")
# sub_client.username_pw_set("edgecomp", "Edge@123#")
# sub_client.on_message = on_message

# sub_client.connect("192.168.1.4", port=1883)
# sub_client.loop_start()
# sub_client.subscribe("topic/#")
# print("subscribed successfully")

# time.sleep(15)
# sub_client.loop_stop()


####################################################################################################################
import sounddevice as sd

if __name__ == '__main__':
    time_in_seconds = 5              # for what time you want to record
    frequency_rate = 11000           # frequency sampling rate

    # to record (set the parameters according)
    try:
        recording = sd.rec(frames = int( frequency_rate * time_in_seconds), samplerate=frequency_rate, channels=3, dtype='float32', blocking=True)
        print(recording.tolist())
    except sd.PortAudioError:
        print("Invalid number of channels provided. Check number of channels by using command(in terminal enter this )\n windos :- python -m sounddevice \n linux :- python3 -m sounddevice")
    
        
    