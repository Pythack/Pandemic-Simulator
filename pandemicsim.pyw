import random
import copy
import os
import pygame
import numpy

R = 2

def proba(prob):
      if prob > 1:
            prob = 1
      return bool(numpy.random.choice(numpy.arange(0, 2), p=[1-prob, prob]))

def hasToGoPurple(age):
      probas = {
        17: 0.006,
        44: 0.039,
        64: 0.224,
        74: 0.249
      }
      prob = 0
      for k, v in probas.items():
            if age > k:
                  continue
            else:
                  prob = v
                  break
      if prob == 0:
            prob = 0.487
      return proba(prob)
            
            

class entity:
  def __init__(self, state, masked, age):
    self.state = state
    self.masked = bool(masked)
    self.age = age
    self.transmitted = R

class grid:
  def __init__(self, x, y, nClusters):
    self.grid = [[entity(2, 0, random.randint(1, 80)) for i in range(x)] for j in range(y)]
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
    self.contaminated = 0
    self.contaminations = 0
    for i in range(nClusters):
      randposx = random.randint(0, x-1)
      randposy = random.randint(0, y-1)
      self.grid[randposy][randposx] = entity(1, random.randint(0, 1), random.randint(1, 80))
  def get_neibhors(self, x, y):
    g = self.grid
    n = []
    alives = 0
    for ny in range(y-1, y+2):
        for nx in range(x-1, x+2):
            if nx == x and ny == y:
                continue
            if nx < 0 or nx >= len(g[0]) or ny < 0 or ny >= len(g):
                continue
            n.append((g[ny][nx], nx, ny))
            if g[ny][nx].state == 2:
                  alives += 1
    return n, alives
  def update(self, R):
    ng = copy.deepcopy(self.grid)
    for y in range(len(self.grid)):
      for x in range(len(self.grid[y])):
        element = self.grid[y][x]
        if element.state == 2 or element.state == 0:
            continue
        neibh, alives = self.get_neibhors(x, y)
        if element.state == 1:
          if element.transmitted > 0:
            for tile, nx, ny in [x for x in neibh if x[0].state == 2]:
              if proba(R/alives):
                ng[ny][nx].state = 1
                ng[y][x].transmitted -= 1
                self.contaminated += 1
                self.contaminations += 1
                if ng[y][x].transmitted < 0:
                      break
          if hasToGoPurple(element.age):
            ng[y][x].state = 0
            self.contaminated -= 1
          elif proba(0.5):
            ng[y][x].state = 2
            self.contaminated -= 1
              
    self.grid = copy.deepcopy(ng)
            

def writeText(text, color, pos, highlighted = False):
  textsurface = myfont.render(text, False, color)
  textRect = textsurface.get_rect()
  textRect.topleft = (pos)
  if highlighted:
    pygame.draw.rect(dis, (75, 75, 75), textRect)
  display.blit(textsurface, textRect)

if __name__ == "__main__":
    pygame.init()
    newGrid = grid(500, 500, 20)
    newGrid.sicks = 20
    dispw = newGrid.width * 1
    disph = newGrid.height * 1 + 100

    display = pygame.display.set_mode((dispw, disph))
    pygame.display.set_caption('Pandemic simulator')
    icon = pygame.image.load('C:/Users/noefa\Documents/pandemicsim/images/icon.png')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    pygame.font.init()
    myfont = pygame.font.SysFont('Times New Roman', 30)
    game_over = False
    while not game_over:
        moved = False
        newGrid.update(R)
        display.fill((0, 0, 0))
        for y in range(newGrid.height):
              for x in range(newGrid.width):
                    if newGrid.grid[y][x].state == 2:
                          continue
                    elif newGrid.grid[y][x].state == 1:
                          color = (0, 0, 255)
                    else:
                          color = (255, 0, 255)
                    tile = pygame.Rect((x)*1, (y)*1, 1, 1)
                    pygame.draw.rect(display, color, tile)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        writeText("Contaminated: {}".format(newGrid.contaminated), (255, 255, 255), (0, disph-100))
        writeText("Contaminations: {}".format(newGrid.contaminations), (255, 255, 255), (0, disph-50))
        pygame.display.update()
        clock.tick(30)
