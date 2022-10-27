import pygame
import random
import math

pygame.init()

class VisualRepresentation:
  
  ##colours stored as class attributes (RGB)
  red = 255, 0, 0
  green = 0, 0, 255
  black = 0, 0, 0
  white = 255, 255, 255
  grey = 128, 128, 128

  ##set Background colour
  background_colour = white

  ##Bar colours
  grey_colours = [grey, (160, 160, 160), (192, 192, 192)]

  ##Font for words
  reg_font = pygame.font.SysFont('timesnewroman', 30)
  big_font = pygame.font.SysFont('timesnewroman', 40)
  
  ##Space on either side of the screen
  space_side = 100

  ##Space above/below
  space_vert = 150
  
  ##consumes the height, width and unsorted list

  def __init__(self, width, height, unsorted_lst):
    self.height = height
    self.width = width

    ##window/screen for pygame set as a tuple
    self.screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Vizualization of Sorting Algorithm")

    self.set_list(unsorted_lst)


  def set_list(self, unsorted_lst):
    self.unsorted_lst = unsorted_lst
    self.max_val = max(unsorted_lst)
    self.min_val = min(unsorted_lst)

    
    self.bar_width = round((self.width - self.space_side) / \
        len(unsorted_lst))
    
    self.bar_height = math.floor((self.height - self.space_vert) / \
        (self.max_val - self.min_val))
    
    ##position to begin drawing bars
    self.begin = self.space_side // 2
