import random

def basic_execute():
    doubleClick(Pattern("1487183811128.png").similar(0.60).targetOffset(120,-4))
    sleep(3)
    type(Key.ESC)
    sleep(9.3)

for x in range(100000):
    click(Pattern("1487183786285.png").targetOffset(120,-1))

    if random.randint(0, 1) == 1:
        doubleClick(Pattern("1487182236608.png").similar(0.60).targetOffset(115,-2))
        sleep(1.5)
        type(Key.ESC)
    else:
        basic_execute()

    for y in range(3):
        basic_execute()

    sleep(1)
