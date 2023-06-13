import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
lit = ['hello', 'World']
lib.print_python_list_info(lit)
del lit[1]
lib.print_python_list_info(lit)
lit = lit + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(lit)
lit = []
lib.print_python_list_info(lit)
lit.append(0)
lib.print_python_list_info(lit)
lit.append(1)
lit.append(2)
lit.append(3)
lit.append(4)
libf.print_python_list_info(lit)
lit.pop()
lib.print_python_list_info(lit)
