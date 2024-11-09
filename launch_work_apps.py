import subprocess
import webbrowser
from pynput import keyboard

# Define the applications to open
applications = [
    "/System/Applications/Notes.app",
    "/Applications/Microsoft Outlook.app",
    "/Applications/WhatsApp.app",
    "/Applications/Mail+ for Gmail.app",
    "/Applications/Slack.app",
]

# Define the websites to open
websites = [
    "https://example-website1.com",
    "https://example-website2.com"
]

# Function to open apps
def open_apps():
    for app in applications:
        subprocess.Popen(["open", app])
    # Open Chrome with the specified tabs
    chrome_path = "/Applications/Google Chrome.app"
    subprocess.Popen(["open", "-a", chrome_path])
    for url in websites:
        webbrowser.get("chrome").open_new_tab(url)

# Key combination we are looking for
COMBO_KEY = {keyboard.Key.cmd, keyboard.Key.shift, keyboard.KeyCode(char='z')}
current_keys = set()

# Listener functions
def on_press(key):
    current_keys.add(key)
    if all(k in current_keys for k in COMBO_KEY):
        open_apps()

def on_release(key):
    if key in current_keys:
        current_keys.remove(key)

# Main block to start listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
