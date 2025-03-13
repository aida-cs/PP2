import pygame
import os
import threading

pygame.mixer.init()

MUSIC_DIR = "music"
songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
if not songs:
    print("No MP3 files found in the 'music' directory!")
    exit()

current_song_index = 0

def play_music():
    global current_song_index
    pygame.mixer.music.load(os.path.join(MUSIC_DIR, songs[current_song_index]))
    pygame.mixer.music.play()

def music_controls():
    global current_song_index
    while True:
        command = input("Enter command (play, stop, next, prev, quit): ").strip().lower()
        
        if command == "play":
            if not pygame.mixer.music.get_busy():
                play_music()
            else:
                print("Music is already playing!")

        elif command == "stop":
            pygame.mixer.music.stop()

        elif command == "next":
            current_song_index = (current_song_index + 1) % len(songs)
            play_music()

        elif command == "prev":
            current_song_index = (current_song_index - 1) % len(songs)
            play_music()

        elif command == "quit":
            pygame.mixer.music.stop()
            break
        
        else:
            print("Invalid command! Use play, stop, next, prev, or quit.")

print("Music player started. Type 'play' to start music.")
music_thread = threading.Thread(target=music_controls)
music_thread.start()