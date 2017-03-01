def click_min():
    hover("1488347106668.png")
    keyDown(Key.CTRL)
    click("1488347106668.png")
    keyUp(Key.CTRL)

def change_weapon():
    pass

def start_skill():
    doubleClick(Pattern("1488348198034.png").targetOffset(119,-4))
    click_min()
    sleep(0.3)

def level_up():
    try:
        if find("1488093197899.png"):
            for i in findAll("1488093197899.png"):
                doubleClick(i)
                sleep(1)
                click("1488093218212.png")
                sleep(1)
                click("1488093231068.png")
    except:
        pass

for i in range(1000):
    if i % 6 == 0:
        level_up()
    start_skill()

    