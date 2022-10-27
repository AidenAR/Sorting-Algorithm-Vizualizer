import pygame
import random
import math
from sorting_algorithm_vizualizer_class import VisualRepresentation

##draws/generates background + bars
def vizualize(screen_creation, algo_name, ascending):
  
  ##fills entire screen with a colour
  screen_creation.screen.fill(screen_creation.background_colour)
  
  ##Text to be displayed for user interaction
  curr_algo = screen_creation.big_font.render(
    f"{algo_name}: {'Ascending' if ascending else 'Descending'}", 1, screen_creation.red)

  screen_creation.screen.blit(curr_algo,((screen_creation.width/2 -
                                        curr_algo.get_width()/2) ,5))
  
  actions = screen_creation.reg_font.render("S: Reset | A: Start Sorting\
  | U: Sort in Ascending Order | D: Sort in Descending Order", 1, screen_creation.black)

  screen_creation.screen.blit(actions,((screen_creation.width/2 -
                                        actions.get_width()/2) ,45))
  
  
  algos_names = screen_creation.reg_font.render(
    "I: Insertion Sort | B: Bubble Sort", 1, screen_creation.black)

  screen_creation.screen.blit(algos_names,((screen_creation.width/2 -
                                       algos_names.get_width()/2) ,75))  
  

  ##draw list of bars
  vizualize_lst(screen_creation)

  pygame.display.update()


##generates a random unsorted list
def start_lst(num_ele, min_val, max_val):
  unsorted_lst = []

  for i in range(num_ele):
    value = random.randint(min_val, max_val)
    unsorted_lst.append(value)

  return unsorted_lst


##draws/generates list
def vizualize_lst(screen_creation, colour_pos={},
                  clear_background=False):
  
  unsorted_lst = screen_creation.unsorted_lst

  ##clear rectangles for each screen when sorting
  if clear_background:
    clear_rect = (screen_creation.space_side // 2, screen_creation.space_vert,
                  screen_creation.width - screen_creation.space_side,
                  screen_creation.height - screen_creation.space_vert)

    pygame.draw.rect(screen_creation.screen,
                     screen_creation.background_colour, clear_rect)
                     

  for count, value in enumerate(unsorted_lst):
    ##get x and y coord from top left hand corner
    ##(draw top lhs to bottom right)

    x=screen_creation.begin + count * screen_creation.bar_width

    y=(screen_creation.height - (value - screen_creation.min_val) *
         screen_creation.bar_height)

    ## every 3 elements next to each other to have different colours
    colour=screen_creation.grey_colours[count % 3]

    ##colour of a specific bar
    if count in colour_pos:
      colour=colour_pos[count]

    pygame.draw.rect(screen_creation.screen, colour,
                     (x, y, screen_creation.bar_width, screen_creation.height))

    if clear_background:
      pygame.display.update()


##Bubble sort O(n^2) and O(1)
def bubble_sort(screen_creation, ascending=True):
  unsorted_lst = screen_creation.unsorted_lst
  n = len(unsorted_lst)
  
  for i in range(n):
    swapped = False
    
    ##Last i elements already in place
    for j in range(0, n - i - 1):
      
      ##ascending/descending sort: swap if element found
      ##is greater than next
      
      if ((unsorted_lst[j] > unsorted_lst[j + 1] and ascending)
              or (unsorted_lst[j] < unsorted_lst[j + 1] and not ascending)):
        unsorted_lst[j], unsorted_lst[j +
          1] = unsorted_lst[j + 1], unsorted_lst[j]
        swapped = True

        ##draw list (bars)
        vizualize_lst(screen_creation,
                      {j: screen_creation.red, j + 1: screen_creation.green},
                      True)
        
        ##stop/continue whenever user wants
        yield True
        
    ## no 2 elements swapped by inner loop
    if swapped == False:
      break
        
  return unsorted_lst


##Insertion Sort (O(n^2)), O(1)
def insertion_sort(screen_creation, ascending=True):
  unsorted_lst = screen_creation.unsorted_lst
  
  n = len(unsorted_lst)

  # Traverse through 1 to end of list
  for i in range(1, n):
    curr = unsorted_lst[i]

    # Move elements of lst[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while True:
      ascending_sort = (i >= 0 and curr < unsorted_lst[i - 1]
                        and ascending)
      descending_sort = (i >= 0 and curr > unsorted_lst[i - 1]
                         and not ascending)

      if not ascending_sort and not descending_sort:
        break

      unsorted_lst[i] = unsorted_lst[i - 1]
      i -= 1
      unsorted_lst[i] = curr

      ##draw list (bars)
      vizualize_lst(screen_creation,
                    {i - 1: screen_creation.red,
                      i: screen_creation.green},
                    True)
      
      ##stop/continue whenever user wants
      yield True

  return unsorted_lst


##Merge Sort (O(nlogn)), O(n)
def merge_sort(screen_creation, ascending=True):
  unsorted_lst = screen_creation.unsorted_lst

  if len(unsorted_lst) > 1:

    # Finding the mid of the list
    mid = len(unsorted_lst) // 2
    
    # Dividing the list into 2 halves
    left = unsorted_lst[:mid]

    right = unsorted_lst[mid:]

    # Sorting the first half
    merge_sort(left)

    # Sorting the second half
    merge_sort(right)
    
    i = 0
    j = 0
    k = 0
    # Copy data to temp unsorted_lstays L[] and R[]
    while i < len(left) and j < len(right):
      if ((left[i] <= right[j] and ascending)
              or (left[i] > right[j] and not ascending)):
        unsorted_lst[k] = left[i]
        i += 1

        ##draw list (bars)
        vizualize_lst(screen_creation,
                      {i: screen_creation.red, j: screen_creation.green,
                        k: screen_creation.black},
                      True)
        
        ##stop/continue whenever user wants
        yield True
                
      else:
        unsorted_lst[k] = right[j]
        j += 1

        ##draw list (bars)
        vizualize_lst(screen_creation,
                      {i: screen_creation.red, j: screen_creation.green,
                        k: screen_creation.black},
                      True)
        
        ##stop/continue whenever user wants
        yield True
        
      k += 1

    # Checking if any element was left
    while i < len(left):
      unsorted_lst[k] = left[i]
      i += 1
      k += 1

      ##draw list (bars)
      vizualize_lst(screen_creation,
                    {i: screen_creation.red, j: screen_creation.green,
                      k: screen_creation.black},
                    True)
      
      ##stop/continue whenever user wants
      yield True      

    while j < len(right):
      unsorted_lst[k] = right[j]
      j += 1
      k += 1
      
      ##draw list (bars)
      vizualize_lst(screen_creation,
                    {i: screen_creation.red, j: screen_creation.green,
                      k: screen_creation.black},
                    True)
      
      ##stop/continue whenever user wants
      yield True      

  return unsorted_lst



##Driver (main) function
def main():
  action = True

  ##regulates time for loop
  clock = pygame.time.Clock()

  ##variable to determine whether
  ## sorting is happening
  sorting = False

  ##variable to keep track of method of sorting
  ascending = True
  
  ##stores current sorting algo
  sort_algo = bubble_sort
  sort_algo_name = "Bubble Sort"

  ##generates sorting algorithm
  ##stores generator object when a specific
  ## sorting function is called
  sort_algo_generator = None
  
  total_ele = 50
  min_val = 0
  max_val = 100
  unsorted_lst = start_lst(total_ele, min_val, max_val)

  screen_creation = VisualRepresentation(1500, 900, unsorted_lst)
  
  while action:
    ##speed of visuals
    clock.tick(120)

    if sorting:
      ##call next method for generator
      try:
        next(sort_algo_generator)

      ##for when sorting is done
      except StopIteration:
        sorting = False
        
    else:
      ##draw normally
      vizualize(screen_creation, sort_algo_name, ascending)
      
    ##clear background
    vizualize(screen_creation, sort_algo_name, ascending)

    pygame.display.update()

    ##exit vizualizer/sorting controls
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        action = False

      if e.type != pygame.KEYDOWN:
        continue
      
      ##click s to reset list
      if e.key == pygame.K_s:
        unsorted_lst = start_lst(total_ele, min_val, max_val)
        screen_creation.set_list(unsorted_lst)
        sorting = False

      ##click b for bubble sort
      elif e.key == pygame.K_b and sorting == False:
        sort_algo = bubble_sort
        sort_algo_name = "Bubble Sort"

      ##click I for bubble sort
      elif e.key == pygame.K_i and sorting == False:
        sort_algo = insertion_sort
        sort_algo_name = "Insertion Sort"
        
      ##click m for bubble sort
      elif e.key == pygame.K_m and sorting == False:
        sort_algo = merge_sort
        sort_algo_name = "Merge Sort"

      ##click a to start sorting
      elif e.key == pygame.K_a and sorting == False:
        sorting = True
        sort_algo_generator = sort_algo(screen_creation, ascending)
       # unsorted_lst = start_lst(total_ele, min_val, max_val)
        #screen_creation.set_list(unsorted_lst)

      ##click u to sort in ascending order
      elif e.key == pygame.K_u and sorting == False:
        ascending = True
        
      ##click d to sort in descending order
      elif e.key == pygame.K_d and sorting == False:
        ascending = False


    


  pygame.quit()
  exit()


##ensures we run this module directly
if __name__ == "__main__":
  main()













  
