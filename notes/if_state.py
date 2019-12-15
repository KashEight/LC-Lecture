"""
引数 i が 20 以上のとき True それ以外は False を返す
"""

def with_if(i):
    if i >= 20:
        return True
    else:
        return False


def with_no_if(i):
    return i >= 20

if __name__ == "__main__":
    num1 = 10
    num2 = 25
    print(with_if(num1))
    print(with_no_if(num1))
    print(with_if(num2))
    print(with_no_if(num2))
    """
    出力:
    False
    False
    True
    True
    """