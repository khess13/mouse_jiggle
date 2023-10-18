from random import randrange
import pyautogui

while True:
  # canvas values 0,0 is upper left corner
  x = randrange(0,40)
  y = randrange(0,40)
  # in seconds
  sleep_time = randrange(0,60)

  pyautogui.dragTo(x=x,y=y)
  pyautogui.click()
  pyautogui.PAUSE = sleep_time
