## puthon 录音

import wave
from pyaudio import PyAudio,paInt16

framerate=16000 #采样率
NUM_SAMPLES=2000
channels=1 #通道数
sampwidth=2
TIME=3 #控制录音时间

def save_wave_file(filename,data):
    '''save the data to the wavfile'''
    wf=wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record():
    pa=PyAudio()
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    print('ready go!')
    count=0
    while count<TIME*8:
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        print('.')
    save_wave_file('001.wav',my_buf)
    stream.close()


my_record()
print('Over!') 


