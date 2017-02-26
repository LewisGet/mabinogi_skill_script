def click_floor():
    click(Pattern("1487586417411.png").similar(0.60).targetOffset(4,170))

for x in range(1000):
    click(Pattern("1487585663882.png").targetOffset(121,-5))
    sleep(0.3)
    click_floor()
    sleep(3)
    click(Pattern("1487587904865.png").targetOffset(121,-1))
    sleep(0.3)
    
    click_floor()
    sleep(17)