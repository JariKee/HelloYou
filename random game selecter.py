random_number = 0

def A():
    global random_number
    random_number = randint(1, 6)
    if random_number == 1:
        basic.show_string("CSGO")
    elif random_number == 2:
        basic.show_string("Phasmophobia")
    elif random_number == 3:
        basic.show_string("BONEWORKS VR")
    elif random_number == 4:
        basic.show_string("Pavlov VR")
    elif random_number == 5:
        basic.show_string("FiveM")
    else:
        basic.show_string("EFT")
while True:
    if button_a.is_pressed():
        A()