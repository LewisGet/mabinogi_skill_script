skip = [0, 1]

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

for x in range(10000):
    level_up()
    buttons = findAll("1488092147417.png")
    sort_buttons = sorted(buttons, key=order)
    
    for skill_index, skill_button in enumerate(sort_buttons):
        if skill_index not in skip:
            click(skill_button)
            sleep(3.5)
            type(Key.ESC)
