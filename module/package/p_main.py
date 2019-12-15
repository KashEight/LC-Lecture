# module/p_module1.py を読もうとするのでエラー吐く
# import p_module1

from .p_module2 import show_name as show_name1
from .sub_package import sp_main

# __main__ 上のフォルダー (パッケージ) のモジュールは読み込めないのでエラー
# from ..outside_module import show_name as show_name2

def run():
    print("--- Run by module/package/p_main.py ---")
    print(f"module/package/p_main.py: {__name__}")
    # print(f"module/package/module1.py: {p_module1.show_name()}")
    print(f"module/package/p_module2.py: {show_name1()}")
    # print(f"module/outside_module.py: {show_name2()}")
    sp_main.run()
