import random
import copy
import os
import pygame
import numpy
import threading
import time

R = 2

maskTransmissionProbas = {
  "True": {
    "True": 0.05,
    "False": 0.11
  },
  "False": {
    "True": 0.7,
    "False": 1
  }
}

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
  def __init__(self, state, masked, age, hasBadHealth, isVaccinated):
    self.state = state
    self.age = age
    self.masked = bool(masked)
    self.hasBadHealth = bool(hasBadHealth)
    self.isVaccinated = bool(isVaccinated)
    self.contaminated = 0
    self.immunity = 0
    self.incubate = 0

#def updateRow(self, ng, y):
#      localR = (0, 0)
#      for x in range(len(self.grid[y])):
#          element = self.grid[y][x]
#          if element.state == 2 or element.state == 0:
#              continue
#          neibh, alives = self.get_neibhors(x, y)
#          if element.state == 1:
#            for tile, nx, ny in [x for x in neibh if x[0].state == 2]:
#              if proba(maskTransmissionProbas[str(element.masked)][str(self.grid[ny][nx].masked)]):
#                ng[ny][nx].state = 1
#                ng[y][x].contaminated += 1
#                self.contaminated += 1
#                self.contaminations += 1
#                self.contaLoc.append((x, y))
#          if hasToGoPurple(element.age):
#            ng[y][x].state = 0
#            self.deaths += 1
#            self.contaminated -= 1
#            self.contaLoc.remove((x, y))
#          elif proba(0.5):
#            ng[y][x].state = 2
#            self.contaminated -= 1
#            self.contaLoc.remove((x, y))
#          localR = ((localR[0]*localR[1]+ng[y][x].contaminated)/(localR[1]+1), localR[1]+1)
#      self.localRs.append(localR)
      
def updateLoc(self, ng, x, y):
      localR = (0, 0)
      element = self.grid[y][x]
      neibh, alives = self.get_neibhors(x, y)
      for tile, nx, ny in [x for x in neibh if x[0].state == 2]:
        if self.grid[ny][nx].immunity != 0:
          continue
        if proba(maskTransmissionProbas[str(element.masked)][str(self.grid[ny][nx].masked)]):
          ng[ny][nx].state = 3
          ng[ny][nx].incubate = 14
          self.incubLoc.append((nx, ny))
          ng[y][x].contaminated += 1
          self.contaminated += 1
          self.contaminations += 1
      if hasToGoPurple(element.age):
        ng[y][x].state = 0
        self.deaths += 1
        self.contaminated -= 1
        self.contaLoc.remove((x, y))
      elif proba(0.2):
        ng[y][x].state = 2
        self.contaminated -= 1
        self.contaLoc.remove((x, y))
        ng[y][x].immunity = random.randint(8, 12)
        self.immuLoc.append((x, y))
      localR = (ng[y][x].contaminated, 1)
      self.localRs.append(localR)

class grid:
  def __init__(self, x, y, nClusters):
    self.grid = [[entity(2, proba(0.8), random.randint(1, 80), proba(0.05), proba(0.9)) for i in range(x)] for j in range(y)]
    self.width = x
    self.height = y
    self.contaminated = nClusters
    self.contaminations = 0
    self.deaths = 0
    self.R = (0, 0)
    self.localRs = []
    self.contaLoc = []
    self.immuLoc = []
    self.incubLoc = []
    for i in range(nClusters):
      randposx = random.randint(0, x-1)
      randposy = random.randint(0, y-1)
      self.grid[randposy][randposx] = entity(1, proba(0.8), random.randint(1, 80), proba(0.05), proba(0.9))
      self.contaLoc.append((randposx, randposy))
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
  def update(self):
    ng = self.grid
    self.localRs = []
    tempContaLoc = copy.deepcopy(self.contaLoc)
    for x, y in self.immuLoc:
        element = ng[y][x]
        element.immunity -= 1
        if element.immunity == 0:
            self.immuLoc.remove((x, y))
    for x, y in self.incubLoc:
        element = ng[y][x]
        element.incubate -= 1
        if element.incubate == 0:
            element.state = 1
            self.incubLoc.remove((x, y))
            self.contaLoc.append((x, y))
    for x, y in tempContaLoc:
        #threading.Thread(target=updateLoc, args=[self, ng, x, y], daemon=True).start()
        updateLoc(self, ng, x, y)
    self.R = (0, 0)
    for rate in self.localRs:
        try:
          self.R = ((self.R[0]*self.R[1]+rate[0]*rate[1])/(self.R[1]+rate[1]), self.R[1]+rate[1])
        except ZeroDivisionError:
          continue
    #self.grid = copy.deepcopy(ng)

class stats:
  def __init__(self, contaminated, contaminations, deaths, R, day):
    self.contaminated = contaminated
    self.contaminations = contaminations
    self.deaths = deaths
    self.R = R
    self.day = day
            

def writeText(text, font, color, pos, highlighted = False):
  textsurface = font.render(text, False, color)
  textRect = textsurface.get_rect()
  textRect.topleft = (pos)
  if highlighted:
    pygame.draw.rect(dis, (75, 75, 75), textRect)
  display.blit(textsurface, textRect)


def updateGridToDisplay(grid, gridToDisplay):
  gridToDisplay = copy.deepcopy(grid.grid)


def displayManager(population, settings):
  dashboardId = 0
  while True:
    display.fill((0, 0, 0))
    for y in range(population.height):
      for x in range(population.width):
        if population.grid[y][x].state == 2:
          color = (0, 0, 0)
        elif population.grid[y][x].state == 1:
            color = (0, 255, 255)
        elif population.grid[y][x].state == 3:
            color = (252, 115, 3)
        else:
          color = (255, 0, 255)
        tile = pygame.Rect((x)*1, (y)*1, 1, 1)
        pygame.draw.rect(display, color, tile)
    if settings["dashboardId"] == 0:
      writeText("Contaminated: {}".format(settings["stats"].contaminated), dashboardFont, (0,128,0), (0, disph-100))
      writeText("Deaths: {}".format(settings["stats"].deaths), dashboardFont, (0,128,0), (0, disph-80))
      writeText("Day: {}".format(settings["stats"].day), dashboardFont, (0,128,0), (0, disph-60))
    elif settings["dashboardId"] == 1:
      writeText("Reproduction rate: {}".format(round(settings["stats"].R[0], 2)), dashboardFont, (0,128,0), (0, disph-100))
      writeText("Contaminations: {}".format(settings["stats"].contaminations), dashboardFont, (0,128,0), (0, disph-80))
    pygame.display.update()
    clock.tick(30)
      

def mainloop(gridw, gridh, settings):
  population = grid(gridw, gridh, 20)
  day = 1
  settings["stats"] = stats(population.contaminated, population.contaminations, population.deaths, population.R, day)
  threading.Thread(target=displayManager, args=[population, settings], daemon=True).start()
  while True:
    population.update()
    day += 1
    settings["stats"] = stats(population.contaminated, population.contaminations, population.deaths, population.R, day)


if __name__ == "__main__":
    pygame.init()
    gridw = 500
    gridh = 500
    dispw = gridw * 1
    disph = gridh * 1 + 100

    display = pygame.display.set_mode((dispw, disph))
    pygame.display.set_caption('Pandemic simulator')
    icon = pygame.image.load('images/icon.png')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    pygame.font.init()
    myfont = pygame.font.SysFont('Times New Roman', 30)
    writeText("Generating population...", myfont, (0,128,0), (0, 0))
    writeText("Please wait", myfont, (0,128,0), (0, 30))
    pygame.display.update()
    dashboardFont = pygame.font.SysFont('Times New Roman', 20)
    settings = {"dashboardId": 0}
    mainProcess = threading.Thread(target=mainloop, args=[gridw, gridh, settings], daemon=True)
    mainProcess.start()
    game_over = False
    dashboard = pygame.Rect(0, gridh, dispw, 100)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    settings["dashboardId"] = 1
                elif event.key == pygame.K_LEFT:
                    settings["dashboardId"] = 0
