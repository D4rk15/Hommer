import api, time

from api import *

from main import main

if __name__ == '__main__':
  while True:
    if api.is_needed():
      main()
    else:
      print("Not needed.")

    time.sleep(1)
