use_skill = [5, 6, 9]

def order(v):
    return v.y, v.x

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

for x in range(300000):
    level_up()
    buttons = findAll("1488092147417.png")
    sort_buttons = sorted(buttons, key=order)

    for skill_index, skill_button in enumerate(sort_buttons):
        if skill_index in use_skill:
            doubleClick(skill_button)
            sleep(4.5)
            type(Key.ESC)
