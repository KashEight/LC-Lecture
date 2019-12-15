# module/sp_module2.py を読もうとするのでエラー吐く
# from sp_module2 import show_name

from .sp_module1 import show_name as show_name1
from ..p_outside_module import show_name as show_name2

def run():
    print("--- Run by module/package/sub_package/sp_main.py ---")
    print(f"module/package/sub_package/sp_main.py: {__name__}")
    print(f"module/package/sub_package/sp_module1.py: {show_name1()}")
    # print(f"module/package/sub_package/module2.py: {module2.show_name()}")
    print(f"module/package/p_outside_module.py: {show_name2()}")
