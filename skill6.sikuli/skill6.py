def click_min():
    click(Pattern("1488167445870.png").similar(0.50).targetOffset(8,65))

def change_weapon():
    pass

def start_skill():
    type(Key.F11)
    click_min()
    sleep(0.3)

for i in range(1000):
    if i % 6 == 0:
        change_weapon()
    start_skill()

    