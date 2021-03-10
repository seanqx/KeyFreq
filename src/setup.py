import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = ["keyUtils"]

build_exe_options = {"includes": additional_modules,
                     "packages": ["os", "json", "time", "uuid", "threading", "pynput", "psutil", "win32process", "win32gui", "tkinter"],
                     "excludes": [],
                     "build_exe": '..\\build\\',
                     "include_files": []}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Key Frequencer",
      version="1.0",
      description="Stats for you key input",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="keyfreq.py", base=base)])