import time
start_end_dict = {}
start_end_dict["time"] = time.time()

import atexit
import simpleaudio

def all_done():

    GREEN = '\033[92m'

    t = time.time() - start_end_dict["time"]

    if t < 1:
        exec_time = f"\n{GREEN}Execution time: {t} seconds{GREEN}"
    else:
        secs = round(t)
        mins = int(secs / 60)
        hours = int(mins / 60)

        mins2 = mins - (hours*60)
        secs = secs - (mins*60)

        hours_str = ""
        if hours > 0:
            hours_str = f"{hours}h "
        mins2_str = ""
        if mins2 > 0:
            mins2_str = f"{mins2}m "
        secs_str = f"{secs}s"

        exec_time = f'\n{GREEN}Execution time: {hours_str}{mins2_str}{secs_str}{GREEN}'

    print(exec_time)
    wave_obj = simpleaudio.WaveObject.from_wave_file("/Users/alessandro/PycharmProjects/ZZZ-Futuristic Computer Sound Effects All Sounds.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

atexit.register(all_done)

