
def click_empty():
    hover("1488084120372.png")
    keyDown(Key.ALT)
    click(Pattern("1488084060414.png").similar(0.60))
    keyUp(Key.ALT)

def basic_execute():
    type(Key.F10)
    sleep(3)
    click_floor()
    sleep(2)

def click_floor():
    click(Pattern("1487586417411.png").similar(0.23).targetOffset(4,170))

for x in range(1000):
    basic_execute()
    click(Pattern("1487585663882.png").targetOffset(121,-5))
    sleep(0.3)
    click_floor()
    sleep(3)
    click(Pattern("1487587904865.png").targetOffset(121,-1))
    sleep(0.3)
    
    click_floor()
    sleep(12)