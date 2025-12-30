import time # timestamps
import datetime # for accessing the time(UTC)
import pygame # mainly for audio
import os

# Force pygame to use a dummy audio driver
os.environ['SDL_AUDIODRIVER'] = 'dummy'

def set_alarm(alarm_time):
    print(f"Alarm Set for {alarm_time}")
    sound_file = "DSA/PY_x_DSA/Week-01/Day-05/practice/alarm.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake Up Mf!")

            pygame.mixer.init() # initialize audio driver
            pygame.mixer.music.load(sound_file) # Loads the sound file
            pygame.mixer.music.play() # Plays the Music

            is_running = False

        time.sleep(1)

# Driver Code
if __name__ == "__main__":
    alarm_time = input("Enter the time to wake Up (HH:MM:SS) Format: ")
    set_alarm(alarm_time)