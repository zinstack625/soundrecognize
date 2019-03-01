from time import sleep
import pyaudio
played = 0
def replay(buffer):
    p = pyaudio.PyAudio()
    def callback(in_data, frame_count, time_info, status):
        global played
        data = buffer[played:played+frame_count]
        played+=frame_count
        return (data, pyaudio.paContinue)
    
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=48100,
                    output=True,
                    stream_callback=callback)
    
    stream.start_stream()
    while stream.is_active():
        sleep(1)
    stream.stop_stream()
    stream.close()
    p.terminate()
