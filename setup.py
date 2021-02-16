from cx_Freeze import setup, Executable

setup(name = "space-invaders-2.0" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("space-invaders.py")])