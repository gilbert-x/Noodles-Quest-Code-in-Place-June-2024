from __future__ import absolute_import, division, print_function
import pygame
import random
import time
from itertools import cycle
from pygame.locals import *
from sys import exit

BLINK_EVENT = pygame.USEREVENT + 0

pygame.init()

#The game area dimensions
#The nudibranch/player icon needs to match the CELL_SIZE in pixel x pixel
CELL_SIZE = 32
gameboard_dimension = CELL_SIZE * 28
side_dimension = 216
x_dimension = gameboard_dimension + (2 * side_dimension)
y_dimension = gameboard_dimension
screen = pygame.display.set_mode((x_dimension, y_dimension))
pygame.display.set_caption("Noodles' Quest")
player_icon_right = 'noodles_icon_right.png'
#player_icon_left = 'noodles_icon_left.png'
start_screen_img_filename = 'noodles_start_screen.png'
icon_img_right = pygame.image.load(player_icon_right)
icon_img_left = icon_img_right
icon_img_left = pygame.transform.flip(icon_img_left, True, False)
icon_img = icon_img_right
sea_spider_icon = 'sea_spider_icon.png'
sea_spider_img = pygame.image.load(sea_spider_icon)
done = False

black = (0, 0, 0)
side_screen_color = black

#yellow sand colors
sand_color = (210, 170, 109)
mushikuri_iro_color = (211, 177, 125)
burlywood_color = (222, 184, 135)
crayola_gold_color = (230, 190, 138)
mellow_apricot_color = (248, 184, 120)
isabelline_color = (244, 240, 236)


#black sand colors
clark_kensington_black_sand = (59, 63, 68)
crayola_outer_space = (45, 56, 58)
outer_space = (65, 74, 76)
charcoal = (54, 69, 79)
onando_iro = (54, 65, 65)
onyx = (53, 56, 57)
jet = (52, 52, 52)
vampire_black = (8, 8, 8)
eerie_black = (27, 27, 27)
black_mica = (64, 66, 68)
smoky_black_color = (16, 12, 8)
chiense_black = (20, 20, 20)
black_chocolate = (27, 24, 17)
white_sand = (219, 213, 209)
drifted_sand = (246, 245, 234)

#pink coral colors
coral_color = (231, 62, 1)
chrysler_coral_color = (157, 74, 63)
black_coral_color = (84, 98, 111)
rosa_coral_color = (235, 99, 107)
purple_fire_color = (121, 92, 142)
benimidori_color = (120, 119, 155)

#rainbow coral colors
red = (204, 0, 2)
orange = (255, 136, 0)
yellow = (225, 189, 39)
green = (83, 155, 70)
blue = (0, 102, 204)
indigo = (121, 28, 248)
violet = (50, 23, 77)

#water colors
ruri_iro_color = (31, 71, 136)

#algae colors
dark_algae_color = (94, 104, 69)
algae_green_color = (97, 125, 72)
algae_red_color = (152, 61, 83)
maximum_green_color = (94, 140, 49)
fresh_onion_color = (91, 137, 48)
may_green_color = (76, 145, 65)

color_list = (
   sand_color,
   mushikuri_iro_color,
   burlywood_color,
   coral_color,
   chrysler_coral_color
   )

black_sand_list = (
   #clark_kensington_black_sand,
   #crayola_outer_space,
   #outer_space,
   #charcoal,
   #onando_iro,
   #onyx,
   #jet,
   vampire_black,
   eerie_black,
   black_mica,
   smoky_black_color,
   #white_sand,
   #drifted_sand,
   chiense_black,
   black_chocolate
   )

yellow_sand_list = (
   sand_color,
   mushikuri_iro_color,
   burlywood_color,
   crayola_gold_color,
   mellow_apricot_color,
   isabelline_color
   )

pink_coral_list = (
   coral_color,
   chrysler_coral_color,
   black_coral_color,
   rosa_coral_color,
   purple_fire_color,
   benimidori_color
   )

rainbow_coral_list = (
   red,
   orange,
   yellow,
   green,
   blue,
   indigo,
   violet
   )

algae_list = (
   dark_algae_color,
   algae_green_color,
   algae_red_color,
   maximum_green_color,
   fresh_onion_color,
   may_green_color
   )

sand_palette_list = (
   yellow_sand_list,
   black_sand_list
   )

coral_palette_list = (
   pink_coral_list,
   rainbow_coral_list
   )

sand_list = random.choice(sand_palette_list)

coral_list = random.choice(coral_palette_list)

#MAZE_CENTER_X = int(side_dimension + (gameboard_dimension / 2) - (CELL_SIZE / 2))
MAZE_CENTER_X = int(side_dimension + (gameboard_dimension / 2) - CELL_SIZE)
MAZE_CENTER_Y = int((y_dimension / 2) - CELL_SIZE)
nudi_x = MAZE_CENTER_X
nudi_y = MAZE_CENTER_Y
noodles_lives = 3

paused = False
level = 1

'''
HERE IS THE MAIN FUNCTION! WAHOO!
'''

def main(CELL_SIZE, nudi_x, nudi_y, done, paused):
   draw_start_screen()
   spiders = prepare_game()
   #print(spiders)
   spider_list = spiders[0]
   spider_cells = spiders[1]
   #print(spider_list)
   #print(spider_cells)
   score_font = pygame.font.SysFont("PressStart2P-vaV7.ttf", 48)
   rules_font = pygame.font.SysFont("PressStart2P-vaV7.ttf", 20)
   
   score_count = 0
   score_board = score_font.render(f"Score: {score_count}", False, (255,255,255))
   global level
   level_board = score_font.render(f'Level: {level}', False, (255,255,255))
   escape_key_text = rules_font.render("Press 'esc' key to quit", False, (255,255,255))
   r_key_text = rules_font.render("Press 'r' key to re-roll level", False, (255,255,255))
   p_key_text = rules_font.render("Press 'p' key to pause/unpause", False, (255, 255, 255))
   draw_left_score_and_text(score_board, level_board, escape_key_text, r_key_text, p_key_text)

   #noodles_lives = 3
   life_board = score_font.render(f'Lives: {noodles_lives}', False, (255, 255, 255))
   draw_right_life(life_board)
   
   icon_img = icon_img_right
   screen.blit(icon_img, (nudi_x, nudi_y))

   spider_move_event = pygame.USEREVENT + 0
   spider_time = int(500 // (1.2 * level))
   pygame.time.set_timer(spider_move_event, spider_time)
   
   while not done:
      pygame.display.flip()
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            done = True
         if event.type == KEYDOWN:
            if event.key == pygame.K_p:# Pausing/Unpausing
               paused = not paused
         if paused == True:
            break
         if event.type == spider_move_event:
            old_spider_data = spiders[0]
            for spider in range(len(old_spider_data)):
               #print(f'Moving spider #{spider}')
               noodles_position = [nudi_x, nudi_y]
               spiders = move_spider(spider, spiders, noodles_position, screen)
               pygame.display.flip()
            gamestate = spider_bite_check(noodles_position, spiders, life_board)
            paused = gamestate[0]
            nudi_x = gamestate[1][0]
            nudi_y = gamestate[1][1]
            spiders = gamestate[2]
         if event.type == KEYDOWN:
            key_press = event.key
            if event.key == K_ESCAPE:
                 pygame.quit()
                 return
            elif event.key == K_r:
                  noodles_position = reset_noodles()
                  nudi_x = noodles_position[0]
                  nudi_y = noodles_position[1]
                  spiders = prepare_game()
                  spider_list = spiders[0]
                  spider_cells = spiders[1]
                  draw_left_score_and_text(score_board, level_board, escape_key_text, r_key_text, p_key_text)
                  life_board = score_font.render(f'Lives: {noodles_lives}', False, (255, 255, 255))
                  draw_right_life(life_board)
                  paused = True
                  
            if check_for_collision_and_edge(key_press, CELL_SIZE, nudi_x, nudi_y): #checks for collision
               break
            else:
               is_algae = check_for_algae(key_press, CELL_SIZE, nudi_x, nudi_y) #if no collision, checks for algae
               if is_algae:
                  score_count = score_points(score_count) #update the score
                  score_board = score_font.render(f"Score: {score_count}", False, (255,255,255)) #updates the scoreboard
                  pygame.draw.rect(screen, side_screen_color, pygame.Rect(0, 0, side_dimension, y_dimension/12))
                  screen.blit(score_board, (16, 16))
                  future_nudi_x = move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[0] #checks to see where Noodles will be
                  future_nudi_y = move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[1]
                  draw_sand(future_nudi_x, future_nudi_y, screen) #draws sand/ deletes the algae so that algae_remainging can't see it
                  if not is_algae_remaining(screen):
                     #the current win result; re-rolls the game
                      print("You win!")
                      level = level +1
                      level_board = score_font.render(f'Level: {level}', False, (255,255,255))
                      noodles_position = reset_noodles()
                      nudi_x = noodles_position[0]
                      nudi_y = noodles_position[1]
                      spiders = prepare_game()
                      spider_list = spiders[0]
                      spider_cells = spiders[1]
                      draw_sand(future_nudi_x, future_nudi_y, screen)
                      draw_left_score_and_text(score_board, level_board, escape_key_text, r_key_text, p_key_text)
                      life_board = score_font.render(f'Lives: {noodles_lives}', False, (255, 255, 255))
                      draw_right_life(life_board)
                      spider_time = int(500 // (1.2 * level))
                      paused = True
                      #victory_dance(nudi_x, nudi_y, screen)
                      
                  
               draw_sand(nudi_x, nudi_y, screen) #erases Noodles from current position

               #checks to see if Noodles will move left or right
               #and then changes the icon to point left or right accordingly
               #and then draws the icon
               old_nudi_x = nudi_x
               nudi_x = move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[0]
               nudi_y = move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[1]
               
               if old_nudi_x < nudi_x:
                  icon_img = icon_img_right
               elif old_nudi_x > nudi_x:
                  icon_img = icon_img_left
               else:
                  pass
               
               screen.blit(icon_img, (nudi_x, nudi_y))
               print(nudi_x, nudi_y)
               '''
               old_spider_data = spiders[0]
               for spider in range(len(old_spider_data)):
                  #print(f'Moving spider #{spider}')
                  spiders = move_spider(spider, spiders, screen)
                  '''

'''
def victory_dance(nudi_x, nudi_y, screen):
   for i in  range(12):
      draw_sand(nudi_x, nudi_y, screen)
      screen.blit(icon_img, (nudi_x, nudi_y))
      pygame.display.flip()
      draw_sand(nudi_x, nudi_y, screen)
      screen.blit(icon_img_flip, (nudi_x, nudi_y))
      pygame.display.flip()
'''
def prepare_game():
   draw_map(CELL_SIZE)
   grow_algae()
   spiders = generate_spiders()
   spider_list = spiders[0]
   spider_cells = spiders[1]
   print(spider_list)
   #print(spider_cells)
   draw_spiders(screen, spider_list)
   draw_sand(nudi_x, nudi_y, screen) #ensures the nudibranch doesn't start on an algae
   return spider_list, spider_cells

def spider_bite_check(noodles_position, spiders, life_board):
   if noodles_position in spiders[0]:
      lose_a_life(life_board)
      #you_got_bit_text()
      noodles_position = reset_noodles()
      erase_old_spiders(spiders)
      spiders = generate_spiders()
      paused = True
      screen.blit(icon_img, noodles_position)
      spider_list = spiders[0]
      draw_spiders(screen, spider_list)
      #erase_got_bit_text()
      gamestate = [paused, noodles_position, spiders]
      return gamestate
   else:
      paused = False
      gamestate = [paused, noodles_position, spiders]
      return gamestate

def erase_old_spiders(spiders):
   spider_list = spiders[0]
   for spider in range(len(spider_list)):
      spider_cell = spider_list[spider]
      draw_sand(spider_cell[0], spider_cell[1], screen)

def reset_noodles():
   nudi_x = MAZE_CENTER_X
   nudi_y = MAZE_CENTER_Y
   noodles_position = (nudi_x, nudi_y)
   return noodles_position

def lose_a_life(life_board):
   global noodles_lives
   noodles_lives = noodles_lives - 1
   if noodles_lives == 0:
      game_over()
   else:
      score_font = pygame.font.SysFont("PressStart2P-vaV7.ttf", 48)
      life_board = score_font.render(f'Lives: {noodles_lives}', False, (255, 255, 255))
      print(noodles_lives)
      draw_right_life(life_board)
      print('Spider bite!')

def game_over():
   #draw a black rect over the whole screen
   screen.fill(black)
   #write game over in the center of the screen
   white = (255, 255, 255)
   font_header = pygame.font.Font("PressStart2P-vaV7.ttf", 64)
   game_over_message = font_header.render("GAME OVER", False, white)
   screen.blit(game_over_message, ((x_dimension / 2) - (game_over_message.get_width() // 2), (y_dimension / 2) - (game_over_message.get_height() // 2)))
   pygame.display.update()
   time.sleep(1)
   #on any key, restart the game
   global done
   while not done:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            done = True
         if event.type == KEYDOWN:
            main(CELL_SIZE, nudi_x, nudi_y, done, paused)

def move_spider(spider, spiders, noodles_position, screen):
   spider_list = spiders[0]
   spider_cells = spiders[1]
   
   #get spider location from spider_list
   spider_x = spider_list[spider][0]
   spider_y = spider_list[spider][1]

   #choose a random direction
   possible_dir = [K_KP6, K_KP4, K_KP8, K_KP2, K_KP7, K_KP9, K_KP3, K_KP1]
   random.shuffle(possible_dir)
   move_dir = possible_dir.pop()

   #print(f'The spider will try to move {move_dir}')   

   #edge/coral check
   future_spider_x = move_nude(move_dir, CELL_SIZE, spider_x, spider_y)[0]
   future_spider_y = move_nude(move_dir, CELL_SIZE, spider_x, spider_y)[1]
   #print(f'The spider wants to move from {spider_x}, {spider_y} to {future_spider_x}, {future_spider_y}')

   potential_position = [future_spider_x, future_spider_y]
   
   while check_for_collision_and_edge(move_dir, CELL_SIZE, spider_x, spider_y) or potential_position in spider_list:
      if len(possible_dir) == 0:
         return spiders #returns an unupdated spiders if there are no possible 
      move_dir = possible_dir.pop()
      #print(f'Cannot go that way, try {move_dir}')   
      future_spider_x = move_nude(move_dir, CELL_SIZE, spider_x, spider_y)[0]
      future_spider_y = move_nude(move_dir, CELL_SIZE, spider_x, spider_y)[1]
      potential_position = [future_spider_x, future_spider_y]
   
   future_spider_x = move_nude(move_dir, CELL_SIZE, spider_x, spider_y)[0]
   future_spider_y = move_nude(move_dir, CELL_SIZE, spider_x, spider_y)[1]
   
   #copy the target cell
   #target_cell = (future_spider_x, future_spider_y)
   copied_cell = {}
   copied_cell = copy_cell(future_spider_x, future_spider_y)
   
   #erase the spider from the old cell
   current_cell = spider_cells[spider]
   #print(current_cell)
   paste_cell(current_cell)

   
   #move spider to new cell and update spider_list
   spider_x = future_spider_x
   spider_y = future_spider_y
   screen.blit(sea_spider_img, (spider_x, spider_y))
   spider_list[spider][0] = spider_x #update the spider_list x 
   spider_list[spider][1] = spider_y #update the spider_list y
               
   #save the copied cell as old cell
   spider_cells[spider] = copied_cell

   #update spiders
   spiders = [spider_list, spider_cells]

   return spiders #returns the updated spider list
   
def copy_cell(icon_x,icon_y):
   copied_cell = {} #create a dictionary for the cell with (x,y) as keys and (R, G, B) as values
   for x in range(icon_x, (icon_x + CELL_SIZE)): #from x to x +32
      for y in range(icon_y, icon_y + CELL_SIZE): #from y to y +32, making a full cell
         #print(f'about to copy {x}, {y}')
         copy_color = screen.get_at((x, y)) #copy the color of that pixel
         copied_cell[(x, y)] = copy_color # add the x,y key and set its value as the copied pixel
   #print(f'The cell being copied is at {icon_x}, {icon_y}')
   #print(f'The dictionary is {copied_cell}')
   return copied_cell

def paste_cell(cell_rgb_dict):
   cell_dict = cell_rgb_dict
   for key in cell_dict:
      rgb_paste = cell_rgb_dict[key]
      screen.set_at(key, rgb_paste)
   
 
def draw_spiders(screen, spider_list):
   for spider in spider_list:
      screen.blit(sea_spider_img, spider)

def generate_spiders():
   spider_list = []
   spider_cells = []
   global level
   num_spider = level
   
   for i in range(num_spider):
      x = (random.randint(0, 27) * CELL_SIZE) + side_dimension
      y = (random.randint(0, 27) * CELL_SIZE)

      #ensure no spiders generate on coral
      coral_check = screen.get_at((x, y))
      while coral_check in coral_list or (x,y) == (nudi_x,nudi_y):
         x = (random.randint(0, 27) * CELL_SIZE) + side_dimension
         y = (random.randint(0, 27) * CELL_SIZE)
         coral_check = screen.get_at((x, y))
      spider_list.append([x, y])
      print(f'spider at {x}, {y}')
      spider_cells.append(copy_cell(x,y))
   return spider_list, spider_cells

def is_algae_remaining(screen):
    is_algae = False
    for x in range(int(gameboard_dimension / CELL_SIZE)):
        for y in range(int(y_dimension / CELL_SIZE)):
            color_check_x = int((x * CELL_SIZE) + (CELL_SIZE / 2) + side_dimension)
            color_check_y = int((y * CELL_SIZE) + (CELL_SIZE / 2))
            color_check = screen.get_at((color_check_x, color_check_y))
            #print(f"The color is {color_check}")
            if color_check in algae_list:
                is_algae = True
                #print("Algae found")
                return is_algae
            else:
                 pass
    return is_algae


def draw_start_screen():
   #set font
   #reset to level to 1
    global level
    level = 1
    #reset lives to 1
    global noodles_lives
    noodles_lives = 3
    white = (255, 255, 255)
    black = (0, 0, 0)
    pearl_aqua = (136, 216, 192)
    font_header = pygame.font.Font("PressStart2P-vaV7.ttf", 64)
    font_normal = pygame.font.Font("PressStart2P-vaV7.ttf", 20)
    start_message_header = font_header.render("Noodles' Quest", False, white)
    #start_instructions_1 = font_normal.render("Control Noodles the nudibranch with the numpad", False, white)
    #start_instructions_2 = font_normal.render("Move Noodles around and eat all the algae", False, white)
    start_instructions_3 = font_normal.render("Press any key to start", False, white)

    screen_rect = screen.get_rect()
    
    clock = pygame.time.Clock() 

    blink_rect = start_instructions_3.get_rect()
    blink_rect.center = (x_dimension / 2, 720)
    off_text_surface = pygame.Surface(blink_rect.size)
    off_text_surface.fill(black)
        
    blink_surfaces = cycle([start_instructions_3, off_text_surface])
    blink_surface = next(blink_surfaces)
    pygame.time.set_timer(BLINK_EVENT, 1000)
    
    
    start_img = pygame.image.load(start_screen_img_filename)
    for x in range(side_dimension):
       screen.fill(black)
       screen.blit(start_img, (x, 0))
       pygame.display.update()
    
    
    
    screen.blit(start_message_header, ((x_dimension / 2) - (start_message_header.get_width() // 2), (y_dimension / 16)))
    pygame.display.update()
    time.sleep(1)
    #screen.blit(start_instructions_1, ((x_dimension / 2) - (start_instructions_1.get_width() // 2), 40))
    #pygame.display.update()
    #time.sleep(1)
    #screen.blit(start_instructions_2, ((x_dimension / 2) - (start_instructions_2.get_width() // 2), 60))
    #pygame.display.update()
    #time.sleep(1)

    global done
    while not done:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            done = True
         if event.type == BLINK_EVENT:
            blink_surface = next(blink_surfaces)
         if event.type == KEYDOWN:
            return
      screen.blit(blink_surface, blink_rect)
      pygame.display.update()
      clock.tick(60)

def score_points(score_count):
   #updates the score by 10, returns the score_count
   score_count = score_count + 10
   return score_count


def check_for_algae(key_press, CELL_SIZE, nudi_x, nudi_y):
   #checks the center of the cell to see if algae is present; returns True or False
   algae_x = int(move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[0] + CELL_SIZE/2)
   algae_y = int(move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[1] + CELL_SIZE/2)
   color_check = screen.get_at((algae_x, algae_y))
   #print(f"The color is {color_check}")
   if color_check in algae_list:
      print("Algae!")
      return True
   else:
      return False

def check_for_collision_and_edge(key_press, CELL_SIZE, nudi_x, nudi_y):
   #first checks to see if the nudibranch is hitting an edge, then checks to see if there is a coral cell; returns True or False
   edge_check = check_for_edge(key_press, CELL_SIZE, nudi_x, nudi_y)
   if edge_check:
      return True
   else:
      coral_check = check_for_coral(key_press, CELL_SIZE, nudi_x, nudi_y)
      if coral_check:
         return True
      else:
         False



def check_for_coral(key_press, CELL_SIZE, nudi_x, nudi_y):
   #checks the future potential cell to see if it is coral
   nudi_x = move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[0]
   nudi_y = move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[1]
   color_check = screen.get_at((nudi_x, nudi_y))
   #print(f"The color is {color_check}")
   if color_check in coral_list:
      #print("Coral!")
      return True
   else:
      return False

def check_for_edge(key_press, CELL_SIZE, nudi_x, nudi_y):
   #checks the future potential cell to see if it is over an edge
   nudi_x = move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[0]
   nudi_y = move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[1]
   east_edge_check = nudi_x >= side_dimension + gameboard_dimension
   west_edge_check = nudi_x < side_dimension
   north_edge_check = nudi_y < 0
   south_edge_check = nudi_y >= gameboard_dimension
   if east_edge_check or west_edge_check or north_edge_check or south_edge_check:
      return True
   else:
      return False

def draw_left_score_and_text(score_board, level_board, escape_key_text, r_key_text, p_key_text):
   screen.blit(score_board, (8, 16))
   screen.blit(level_board, (8, 80))
   screen.blit(escape_key_text, (8, 800))
   screen.blit(r_key_text, (8, 816))
   screen.blit(p_key_text, (8, 832))

def draw_right_life(life_board):
   x = side_dimension + gameboard_dimension + 8
   print(x)
   pygame.draw.rect(screen, side_screen_color, pygame.Rect(x, 16, life_board.get_width() +16, life_board.get_height() +16))
   screen.blit(life_board,(x, 16))

def draw_map(CELL_SIZE):
   global sand_list
   sand_list = random.choice(sand_palette_list)
   global coral_list
   coral_list = random.choice(coral_palette_list)
   
   #draws the upper left quadrant of the map
   x = side_dimension
   y = 0
   coral_chance = 0.4
   while y < y_dimension/2:
      sand_or_coral = random.uniform(0, 1.0)
      if sand_or_coral > coral_chance:
         draw_sand(x, y, screen)
      else:
         draw_coral(x, y, screen)
         #draw_map_colors = coral_list
         #pygame.draw.rect(screen, random.choice(draw_map_colors), pygame.Rect(x, y, CELL_SIZE, CELL_SIZE))
      
      if x <= (x_dimension)/2 - 2*CELL_SIZE:
         x = x + CELL_SIZE
      else:
         x = side_dimension
         y = y + CELL_SIZE

   #mirrors the upper left quadrant onto each other quadrant
   x = side_dimension
   y = 0
   coord_adjust = int(gameboard_dimension/2)
   for x in range(side_dimension, int((x_dimension)/2)):
      for y in range(0, int(y_dimension/2)):
         copy_color = screen.get_at((x, y))
         screen.set_at((gameboard_dimension + side_dimension - (x -side_dimension +1), y), copy_color)
         screen.set_at((x, gameboard_dimension - y -1), copy_color)
         screen.set_at((gameboard_dimension + side_dimension - (x -side_dimension +1), gameboard_dimension - y -1), copy_color)

   #draws a sand area of sand rectangles in the center
   x = MAZE_CENTER_X - CELL_SIZE*2
   y = MAZE_CENTER_Y - CELL_SIZE
   while y < MAZE_CENTER_Y + CELL_SIZE*3 - 1:
      draw_sand(x, y, screen)
      if x <= MAZE_CENTER_X + CELL_SIZE*2:
         x = x + CELL_SIZE
      else:
         x = MAZE_CENTER_X - CELL_SIZE*2
         y = y + CELL_SIZE
   #draw the side display areas
   pygame.draw.rect(screen, side_screen_color, pygame.Rect(0, 0, side_dimension, y_dimension))
   pygame.draw.rect(screen, side_screen_color, pygame.Rect(side_dimension + gameboard_dimension, 0, side_dimension, y_dimension))
   pygame.display.update()


   
def draw_map_random(CELL_SIZE):
   #draws the map, leaving space on the edges equals to the side_dimension
   x = side_dimension
   y = 0
   coral_chance = 0.4
   while y < y_dimension - 1:
      sand_or_coral = random.uniform(0, 1.0)
      if sand_or_coral > coral_chance:
         draw_sand(x, y, screen)
      else:
         draw_coral(x, y, screen)
         #draw_map_colors = coral_list
         #pygame.draw.rect(screen, random.choice(draw_map_colors), pygame.Rect(x, y, CELL_SIZE, CELL_SIZE))
      
      if x <= x_dimension - CELL_SIZE - side_dimension:
         x = x + CELL_SIZE
      else:
         x = side_dimension
         y = y + CELL_SIZE
   #draws a sand area of sand rectangles in the center
   x = MAZE_CENTER_X - CELL_SIZE*3
   y = MAZE_CENTER_Y - CELL_SIZE*2
   while y < MAZE_CENTER_Y + CELL_SIZE*2 - 1:
      #pygame.draw.rect(screen, random.choice(sand_list), pygame.Rect(x, y, CELL_SIZE, CELL_SIZE))
      draw_sand(x, y, screen)
      if x <= MAZE_CENTER_X + CELL_SIZE*3:
         x = x + CELL_SIZE
      else:
         x = MAZE_CENTER_X - CELL_SIZE*3
         y = y + CELL_SIZE
   #draw the side display areas
   pygame.draw.rect(screen, side_screen_color, pygame.Rect(0, 0, side_dimension, y_dimension))
   pygame.draw.rect(screen, side_screen_color, pygame.Rect(side_dimension + gameboard_dimension, 0, side_dimension, y_dimension))
   pygame.display.update()

def draw_sand(x_coord, y_coord, screen):
   div_var = 16 #cell division variable
   mini_cell = CELL_SIZE / div_var
   for x in range(div_var):
      for y in range(div_var):
         pygame.draw.rect(screen, random.choice(sand_list), pygame.Rect(x_coord + (x * CELL_SIZE / div_var), y_coord + (y * CELL_SIZE / div_var), mini_cell, mini_cell))


def draw_fan_coral(x, y, screen):
   fan_var = random.randint(12,24)
   step = (CELL_SIZE / 2) / fan_var
   tile_adjust = (CELL_SIZE / 2)
   
   #print(f"{rows} # of rows, {columns} # of columns")
   coral_1 = random.choice(coral_list)
   coral_2 = random.choice(coral_list)
   while coral_2 == coral_1:
      coral_2 = random.choice(coral_list)
   coral_colors = cycle([coral_1, coral_2])
   coral_color = next(coral_colors)
   #print(f"{coral_1} and {coral_2} selected")
   pygame.draw.rect(screen, coral_color, pygame.Rect((x, y, CELL_SIZE, CELL_SIZE)))
   for i in range(fan_var):
      y_adjust = i * step
      x_adjust = i * step
      small_cell = CELL_SIZE / (i +1)
      coral_color = next(coral_colors)
      pygame.draw.rect(screen, coral_color, pygame.Rect((x + x_adjust, y + y_adjust, small_cell, small_cell)))
      pygame.draw.rect(screen, coral_color, pygame.Rect((x + x_adjust + tile_adjust, y + y_adjust, small_cell, small_cell)))
      pygame.draw.rect(screen, coral_color, pygame.Rect((x + x_adjust, y + y_adjust + tile_adjust, small_cell, small_cell)))
      pygame.draw.rect(screen, coral_color, pygame.Rect((x + x_adjust + tile_adjust, y + y_adjust + tile_adjust, small_cell, small_cell)))



def draw_rows_and_columns_coral(x, y, screen):
   rows = random.randint(2 , 8)
   columns = random.randint(2, 8)
   
   small_cell_size = (CELL_SIZE / (rows + columns)) *1.2
   
   columns_by_small = columns * small_cell_size
   rows_by_small = rows * small_cell_size
   
   offset_x = CELL_SIZE - rows_by_small
   x_adjust = offset_x / (rows + 1)
   
   
   offset_y = CELL_SIZE - columns_by_small
   y_adjust = offset_y / (columns + 1)
   
   small_coral_x = x + x_adjust
   small_coral_y = y + y_adjust
   
   #print(f"{rows} # of rows, {columns} # of columns")
   coral_1 = random.choice(coral_list)
   coral_2 = random.choice(coral_list)
   while coral_2 == coral_1:
      coral_2 = random.choice(coral_list)
   #print(f"{coral_1} and {coral_2} selected")
   pygame.draw.rect(screen, coral_1, pygame.Rect((x, y, CELL_SIZE, CELL_SIZE))) 
   for row in range(rows):
      for column in range(columns):
         row_increment = (row * CELL_SIZE / (rows))
         column_increment = (column * CELL_SIZE / (columns))
         pygame.draw.ellipse(screen, coral_2, pygame.Rect(((small_coral_x + row_increment), (small_coral_y + column_increment), small_cell_size, small_cell_size)))
         pygame.draw.ellipse(screen, coral_1, pygame.Rect(((small_coral_x + row_increment +small_cell_size/4), (small_coral_y + column_increment +small_cell_size/2), small_cell_size/2, small_cell_size/2)))
         #pygame.draw.ellipse(screen, coral_2, pygame.Rect(((small_coral_x + row_increment + (small_cell_size/3)), (small_coral_y + column_increment +(small_cell_size *(2/3))), small_cell_size/3, small_cell_size/3)))
         #print("Drawing little coral bits")

def draw_coral(x, y, screen):
   coral_methods = [
      draw_rows_and_columns_coral,
      draw_fan_coral
      ]
   random.choice(coral_methods)(x, y, screen)
         
def grow_algae():
   #populates the maze with algae bits
   global level
   algae_chance = 0.05 * level
   for x in range(int(x_dimension / CELL_SIZE)):
      #print(f"x is {x}")
      for y in range(int(y_dimension / CELL_SIZE)):
         #print(f"y is {y}")
         if check_for_sand(x * CELL_SIZE, y * CELL_SIZE):
            algae_roll = random.uniform(0, 1.0)
            center_of_cell = (x * CELL_SIZE + CELL_SIZE / 2 - 8, y * CELL_SIZE + CELL_SIZE / 2)
            #print(center_of_cell)
            if algae_roll >= 1 - algae_chance:
               pygame.draw.circle(screen, random.choice(algae_list), center_of_cell, 8)
               pygame.draw.circle(screen, random.choice(algae_list), center_of_cell, 6)
               pygame.draw.circle(screen, random.choice(algae_list), center_of_cell, 4)
               pygame.draw.circle(screen, random.choice(algae_list), center_of_cell, 2)
            else:
               pass
         else:
            pass

def check_for_sand(x, y):
   #tells if there is sand color at a certain pixel
   color_check = screen.get_at((x, y))
   #print(f"The color is {color_check}")
   if color_check in sand_list:
      #print("True")
      return True
   else:
      #print("False")
      return False


def move_nude(key_press, move_space, nudi_x, nudi_y):
   #updates the nudibranch x and y values based on the num pad key press
   if key_press == K_KP6:
      nudi_x = nudi_x + move_space
   elif key_press == K_KP4:
      nudi_x = nudi_x - move_space
   elif key_press == K_KP8:
      nudi_y = nudi_y - move_space
   elif key_press == K_KP2:
      nudi_y = nudi_y + move_space
   elif key_press == K_KP7:
      nudi_x = nudi_x - move_space
      nudi_y = nudi_y - move_space
   elif key_press == K_KP9:
      nudi_x = nudi_x + move_space
      nudi_y = nudi_y - move_space
   elif key_press == K_KP3:
      nudi_x = nudi_x + move_space
      nudi_y = nudi_y + move_space
   elif key_press == K_KP1:
      nudi_x = nudi_x - move_space
      nudi_y = nudi_y + move_space
   return [nudi_x, nudi_y]

#def erase_nude(screen, nudi_x, nudi_y, CELL_SIZE):
   #gets the color of the cell the nudibranch is leaving then draws a rectangle in that color to erase the nudibranch's image
   #erase_color = screen.get_at((nudi_x, nudi_y))
   #erase_coords = [nudi_x, nudi_y, CELL_SIZE, CELL_SIZE]
   #pygame.draw.rect(screen, erase_color, pygame.Rect(erase_coords))
   #draw_sand(nudi_x, nudi_y, screen)

   
main(CELL_SIZE, nudi_x, nudi_y, done, paused)
