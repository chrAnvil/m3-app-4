import anvil.server
from time import sleep
import random

@anvil.server.callable
def level_1():
  sleep(1)
  anvil.server.call('level_2')
  sleep(2)
  anvil.server.call('level_3', random.randint(0, 2))
  anvil.server.call('level_3', 0)
  return 42

@anvil.server.callable
def level_2():
  sleep(1.5)
  anvil.server.call('level_3', random.randint(0, 3))
  sleep(1)
  return 42
  
@anvil.server.callable
def level_3(children):
  sleep(3-children)
  for i in range(children):
    anvil.server.call('level_4')
  return 42

@anvil.server.callable
def level_4():
  sleep(random.randint(1, 7) * 0.2)

@anvil.server.callable
def level_a():
  sleep(6)
  for i in range(random.randint(1, 3)):
    anvil.server.call('level_b')
  sleep(random.randint(1, 7) * 0.4)
  return

@anvil.server.callable
def level_b():
  sleep(random.randint(1, 7) * 0.2)
  for i in range(random.randint(0, 2)):
    anvil.server.call('level_c')
  sleep(random.randint(1, 7) * 0.4)

@anvil.server.callable
def level_c():
  sleep(random.randint(1, 3) * 0.5)
