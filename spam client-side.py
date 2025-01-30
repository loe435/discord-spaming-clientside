import keyboard
import pyautogui
import time
import configparser


config = configparser.ConfigParser()
config.read(filenames="config.ini")

message = config.get("settings", "message")
delay = config.getfloat("settings", "delay")
sequence = config.getint("settings", "sequence") + 1
sequenceDelay = config.getfloat("settings", "sequence-delay")


# État du spammer
spammer_active = False

def toggle_spammer():
    global spammer_active
    spammer_active = not spammer_active
    print(f"Spammer {'activé' if spammer_active else 'désactivé'}")

# Assigner F2 au changement d'état
keyboard.add_hotkey("F2", toggle_spammer)

print("Appuie sur F2 pour activer/désactiver le spam.")

while True:
    if spammer_active:
        for i in range(0, sequence):
            keyboard.write(message)  # Message à envoyer
            pyautogui.press("enter")  # Envoie le message
            time.sleep(delay)  # Délai entre chaque message pour éviter un spam trop rapide
        time.sleep(sequenceDelay)
