import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

fs = 10000  # Sample rate
seconds = 10  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='float32', blocking=True)
# sd.wait()  # Wait until recording is finished
# print(type(myrecording[0][0]))
# print(myrecording.nbytes)     # total bytes = freq_sampling_rate * channels *  time * 4  = (10000 * 2 * 10 * 4) = 800000 bytes / 1024 = 781.25 kb

# myrecording = np.array(myrecording)
myrecording = myrecording[::2]       # downsampling (collecting every 2nd sample)
print(myrecording)
# print(myrecording.shape)
# sf.write('output.flac', myrecording, fs)  # Save file ()
# write('output.wav', fs, myrecording)      # saving to wav file

# df = pd.DataFrame({'x' : [i[0] for i in myrecording],
#                   'y' : [i[1] for i in myrecording]}
#                 )

# df.to_csv('inputs.csv', index=False)
# myrecording = myrecording.tolist()

# print(len(myrecording))
# with open('inputs.txt', 'w') as file:
#     file.write(str(myrecording))

# plt.figure(figsize=(15, 8))
# plt.plot(myrecording)
# # plt.plot(df['x'], df['y'])
# plt.show()


