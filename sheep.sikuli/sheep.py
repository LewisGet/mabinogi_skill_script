
for x in range(100):
    type(Key.TAB)
    doubleClick(Pattern("1487242876065.png").targetOffset(117,-4))
    doubleClick(Pattern("1487242892433.png").targetOffset(117,-3))
    sleep(5)
    type(Key.ESC)
    sleep(0.2)
    type(Key.TAB)
    
    for i in range(12):
        hover("1487245714666.png")
        keyDown(Key.ALT)
        click("1487300323483.png")
        keyUp(Key.ALT)
        keyDown(Key.ALT)
        if (i != 0) or (x != 0):
            for z, z_content in enumerate(findAll("1487242785957.png")):
                if z < 3:
                    click(z_content)
                    # to new location no screen
                    #click("1487242785957.png")
        sleep(1)
        keyUp(Key.ALT)
        sleep(1)
    sleep(2)
