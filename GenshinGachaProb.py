import random
init_p = 0.006
step_p = 0.06
epochs = int(1e4)

gacha = 0
num = 0
is_guaranteed = False


def has_gacha(a):
    global gacha, num, is_guaranteed, epoch

    gacha += a

    if is_guaranteed:
        is_guaranteed = False
    else:
        tp = random.random()
        if tp < 0.5:
            print(epoch, "Guar!", gacha, num, a)
            return True
        else:
            is_guaranteed = True

    num += 1
    return False


def do_gacha():
    global init_p, step_p
    p = init_p
    i = 0

    while(True):
        i += 1
        if i > 73:
            p += step_p

        tp = random.random()
        if tp < p:
            if has_gacha(i):
                return
            break


for epoch in range(epochs):
    random.seed(epoch)
    do_gacha()


print("Final Gacha: %d, Num: %d" % (gacha, num))
print("Average: %f" % (gacha / num))
print("Average gacha: %f" % (gacha / epochs))
print("Average num: %f" % (num / epochs))
