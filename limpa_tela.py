import os 
import platform

def clear():
  if platform.system() == 'Windows':
    return os.system("cls")
  elif platform.system() == 'Linux':
    return os.system("clear")