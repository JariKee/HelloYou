from microbit import *

while True:
    if button_a.is_pressed():
        display.scroll('Mijn naam is Jari')
    if button_b.is_pressed():
        display.show(Image('09090:'
                           '90909:'
                           '99099:'
                           '90009:'
                           '09990'))