import os
import subprocess

SPOTIFY_URL = "https://open.spotify.com/track/2LMkwUfqC6S6s6qDVlEuzV"
browser_process = None

def open_spotify_windows():
    """
    Opens the Spotify app to the target track (Windows only).
    """
    global browser_process
    if browser_process is None:
        command = 'start spotify:track:2LMkwUfqC6S6s6qDVlEuzV'
        browser_process = subprocess.Popen(command, shell=True)

def close_spotify_windows():
    """
    Closes Spotify by killing its process (Windows).
    """
    global browser_process
    if browser_process is not None:
        os.system("taskkill /IM Spotify.exe /F")
        browser_process = None
