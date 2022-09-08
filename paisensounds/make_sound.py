import simpleaudio as sa


def beep():
    

    wave_obj = sa.WaveObject.from_wave_file("/Users/alessandro/PycharmProjects/ZZZ-Futuristic Computer Sound Effects All Sounds")
    play_obj = wave_obj.play()
    play_obj.wait_done()
