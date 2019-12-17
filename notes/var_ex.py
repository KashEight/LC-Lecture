def function(i):
    if i >= 20:
        pass
        # なにかしたい…

    # なにかする

    if i >= 20:
        pass
        # さっきとは違うなにかをしたい…


def function(i):
    if i >= 20:
        condition = True
    else:
        condition = False

    if condition:
        pass
        # なにかしたい…

    # なにかする

    if condition:
        pass
        # さっきとは違うなにかをしたい…


def function(i):
    condition = i >= 20

    if condition:
        pass
        # なにかしたい…

    # なにかする

    if condition:
        pass
        # さっきとは違うなにかをしたい…


def function(i):
    if i >= 20:
        value = "20 以上らしい いい話"
    else:
        value = "20 未満らしい 悪い話"

    return value


def function(i):
    value = "20 以上らしい いい話" if i >= 20 else "20 未満らしい 悪い話"
    return value


def function(i):
    return "20 以上らしい いい話" if i >= 20 else "20 未満らしい 悪い話"


def function(i):
    return "20 以上らしい" if i >= 20 else "10 以上 20 未満らしい" if i >= 10 else "それ未満"


def function(i):
    if i >= 20:
        return "20 以上らしい"
    elif i >= 10:
        return "10 以上 20 未満らしい"
    else:
        return "それ未満"
