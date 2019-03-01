import pyaudio
from time import sleep

def recognize(time):
    io = pyaudio.PyAudio()
    stream = io.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=48100,
                    input=True,
                    frames_per_buffer=1024)
    recording = []
    samples = 48100 * time
    for i in range(0, int(samples/1024)):
        data = stream.read(1024)
        recording.append(data)
    stream.stop_stream()
    stream.close()
    io.terminate()
    return (recording, samples)
