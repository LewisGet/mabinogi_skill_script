import random

for i in range(100000):
    for i in range(7):
        doubleClick(Pattern("1487182236608.png").similar(0.59).targetOffset(115,-2))
        sleep(1.5)
        type(Key.ESC)
        doubleClick(Pattern("1487183684495.png").similar(0.58).targetOffset(114,-3))
        sleep(5)
        type(Key.ESC)
    click(Pattern("1487183786285.png").targetOffset(120,-1))
    sleep(0.2)
    if random.randint(0, 1) == 1:
        doubleClick(Pattern("1487182236608.png").similar(0.60).targetOffset(115,-2))
        sleep(1.5)
        type(Key.ESC)
    doubleClick(Pattern("1487183811128.png").similar(0.60).targetOffset(120,-4))
    sleep(3)
    type(Key.ESC)
