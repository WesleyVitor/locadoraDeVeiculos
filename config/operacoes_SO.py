import os, platform

def usando_clear():
  if platform.system() == 'Linux':
    os.system('clear')
  elif platform.system() == 'Windows':
    os.system('cls')