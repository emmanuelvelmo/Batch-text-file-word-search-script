from cx_Freeze import setup, Executable

setup(name="Batch text file word search", executables=[Executable("Batch text file word search script.py")], options={"build_exe": {"excludes": ["tkinter"]}})
