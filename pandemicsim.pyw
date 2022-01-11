import random
import copy
import os
import pygame

class entity:
  def __init__(self, state, masked, age):
    self.state = state
    self.masked = bool(masked)
    self.age = age

class grid:
  def __init__(self, x, y, nClusters):
    self.grid = [[entity(2, 1, random.randint(15, 30)) for i in range(x)] for j in range(y)]
    #self.grid = [
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(1, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))],
    #  [entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30)), entity(2, random.randint(0, 1), random.randint(15, 30))]
    #]
    self.width = x
    self.height = y
    for i in range(nClusters):
      randposx = random.randint(0, x-1)
      randposy = random.randint(0, y-1)
      self.grid[randposy][randposx] = entity(1, random.randint(0, 1), random.randint(15, 30))
  def print(self):
    for y in self.grid:
      for x in y:
        if x.state == 0:
          print("x", end=" ")
        elif x.state == 1:
          print("▣", end=" ")
        else:
          print("▢", end=" ")
      print()
  def get_neibhors(self, x, y):
    g = self.grid
    n = []
    for ny in range(y-1, y+2):
        for nx in range(x-1, x+2):
            if nx == x and ny == y:
                continue
            if nx < 0 or nx >= len(g[0]) or ny < 0 or ny >= len(g):
                continue
            n.append(g[ny][nx])
    return n
  def update(self, R):
    ng = copy.deepcopy(self.grid)
    for y in range(len(self.grid)):
      for x in range(len(self.grid[y])):
        neibh = self.get_neibhors(x, y)
        alives = 0
        sicks = 0
        deads = 0
        for i in neibh:
          if i.state == 2:
            alives += 1
          elif i.state == 1:
            sicks += 1
          else:
            deads += 1
          element = self.grid[y][x]
          if element.state == 2:
            if element.masked:
              if random.randint(1, 25) <= sicks:
                ng[y][x] = entity(1, element.masked, element.age)
            else:
                if random.randint(1, 10) <= sicks:
                   ng[y][x] = entity(1, element.masked, element.age)
          elif element.state == 1:
            if random.randint(15, 80) < element.age:
              ng[y][x] = entity(0, element.masked, element.age)
            elif random.randint(1, 2) == 1:
              ng[y][x] = entity(2, element.masked, element.age)
          else:
            if random.randint(1, 2) == 1:
              ng[y][x] = entity(2, element.masked, element.age)
              
    self.grid = copy.deepcopy(ng)
            
#while True:
#  os.system("cls")
#  newGrid.update()
#  newGrid.print()

def writeText(text, color, pos, highlighted):
  textsurface = myfont.render(text, False, color)
  textRect = textsurface.get_rect()
  textRect.topleft = (pos)
  if highlighted:
    pygame.draw.rect(dis, (75, 75, 75), textRect)
  display.blit(textsurface, textRect)

if __name__ == "__main__":
    R = 1.09
    pygame.init()
    newGrid = grid(100, 100, 10)
    dispw = newGrid.width * 10
    disph = newGrid.height * 10

    display = pygame.display.set_mode((dispw, disph))
    pygame.display.set_caption('Pandemic simulator')
    icon = pygame.image.load('C:/Users/noefa\Documents/Python lycée/liste2d/images/icon.png')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    pygame.font.init()
    myfont = pygame.font.SysFont('Times New Roman', 30)
    game_over = False
    while not game_over:
        moved = False
        newGrid.update(R)
        for y in range(newGrid.height):
              for x in range(newGrid.width):
                    if newGrid.grid[y][x].state == 2:
                          color = (0, 0, 0)
                    elif newGrid.grid[y][x].state == 1:
                          color = (0, 0, 255)
                    else:
                          color = (255, 0, 255)
                    tile = pygame.Rect((x)*10, (y)*10, 10, 10)
                    pygame.draw.rect(display, color, tile)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        pygame.display.update()
        clock.tick(30)
