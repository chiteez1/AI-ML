import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame

# function to play music
def play(mu: str) -> None:
    try:
        pygame.mixer.music.load(mu)
        pygame.mixer.music.play()
    except Exception:
        print("An error occured!")
    return

pygame.init()
if __name__ == '__main__':
    print("Welcome to command-line music player!")
    print("Type 'exit' to Exit.")
    os.chdir("Music")
    while True:
        # ask user to input command and music name(if any)
        a = input(">> ").lower().split(' ')
        cmd = a[0]  # extract command keyword
        if cmd == 'exit':
            break
        elif cmd == 'play':
            mu = a[1]  # extract music name
            if os.path.exists(mu):  # check if music file exists
                play(mu)
            else:
                print("Music file doesn't exist. Maybe the file name is incorrect?")
        elif cmd == 'stop':
            pygame.mixer.music.stop()  # stop the music
        elif cmd == 'pause':
            pygame.mixer.music.pause()  # pause the music
        elif cmd == 'resume':
            pygame.mixer.music.unpause()  # resume the music
        else:
            print("Invalid command!")
    print("Thanks for using our music player.")
