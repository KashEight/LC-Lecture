import module1
import package.p_main

from module2 import show_name

print("--- Run by module/main.py (__main__) ---")
print(f"module/main.py: {__name__}")
print(f"module/module1.py: {module1.show_name()}")
print(f"module/module2.py: {show_name()}")
package.p_main.run()

"""
出力:
--- Run by module/main.py (__main__) ---
module/main.py: __main__
module/module1.py: module1
module/module2.py: module2
--- Run by module/package/p_main.py ---
module/package/p_main.py: package.p_main
module/package/p_module2.py: package.p_module2
--- Run by module/package/sub_package/sp_main.py ---
module/package/sub_package/sp_main.py: package.sub_package.sp_main
module/package/sub_package/sp_module1.py: package.sub_package.sp_module1
module/package/p_outside_module.py: package.p_outside_module
"""
