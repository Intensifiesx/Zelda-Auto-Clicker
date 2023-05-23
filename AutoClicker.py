import pydirectinput
import time


def dropItem():
    pydirectinput.press('e')  # Select item
    pydirectinput.press('s')  # Go down 1 to drop
    pydirectinput.press('e')  # Drop item


pydirectinput.PAUSE = 0.09
i = 0
while True:
    time.sleep(0.3)
    pydirectinput.press('shift')  # Unequip item
    time.sleep(0.3)

    pydirectinput.press('m')  # Get bow ready
    time.sleep(0.3)

    pydirectinput.keyDown('o')  # Equip iteme
    pydirectinput.keyUp('o')
    time.sleep(1.5)

    pydirectinput.press('v')  # Open inventory
    if i > 0:
        pydirectinput.press('a')  # Go left 1
        dropItem()
    else:
        dropItem()

    pydirectinput.press('d')  # Go right 1aeo
    pydirectinput.press('e')  # Select item
    pydirectinput.press('e')  # Equip item

    pydirectinput.PAUSE = 0.031
    pydirectinput.press('v')  # Close inventory
    pydirectinput.press('v')  # Open ionventory
    pydirectinput.PAUSE = 0.09

    pydirectinput.press('a')  # Go left 1
    dropItem()

    pydirectinput.press('v')  # Close inventory

    pydirectinput.press('s')  # Move character down
    pydirectinput.press('e')  # Grab item
    pydirectinput.press('e')  # Grab item
    pydirectinput.press('w')  # Move character up
    i += 1
