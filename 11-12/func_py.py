def no_function():
    """
    関数を使わない場合
    """
    n = 1
    print("----------")
    print(f"debug: {n}")
    print("----------")
    n += 1
    print("----------")
    print(f"debug: {n}")
    print("----------")
    n += 1
    print("----------")
    print(f"debug: {n}")
    print("----------")


def debug(n):
    """
    今回使う関数
    """
    print("----------")
    print(f"debug: {n}")
    print("----------")


def with_function():
    """
    関数を使う場合
    """
    n = 1
    debug(n)
    n += 1
    debug(n)
    n += 1
    debug(n)


if __name__ == "__main__":
    no_function()
    with_function()
    """
    出力
    ----------
    debug: 1
    ----------
    ----------
    debug: 2
    ----------
    ----------
    debug: 3
    ----------
    """