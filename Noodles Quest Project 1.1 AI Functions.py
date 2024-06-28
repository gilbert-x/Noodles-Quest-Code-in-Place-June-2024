from __future__ import absolute_import, division, print_function
import pygame
import random
import time
import math
from itertools import cycle
from pygame.locals import *
from sys import exit

BLINK_EVENT = pygame.USEREVENT + 0 #sets up the blink timer for the starting screen

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
# Pink Sand Colors

# Palette 1
blossom_pink = (255, 183, 197)
light_pink = (255, 182, 193)
pale_pink = (250, 218, 221)
pastel_pink = (255, 209, 220)
spanish_pink = (247, 191, 190)
baby_pink = (244, 194, 194)

pink_sand_list_1 = (
   blossom_pink,
   light_pink,
   pale_pink,
   pastel_pink,
   spanish_pink,
   baby_pink
)

# Palette 2
flamingo_pink = (252, 142, 172)
persian_pink = (247, 127, 190)
brink_pink = (251, 96, 127)
ultra_pink = (255, 111, 255)
tickle_me_pink = (252, 137, 172)
light_crimson = (245, 105, 145)

pink_sand_list_2 = (
   flamingo_pink,
   persian_pink,
   brink_pink,
   ultra_pink,
   tickle_me_pink,
   light_crimson
)

# Yellow Sand Colors

# Palette 3
light_gold = (255, 236, 139)
light_khaki = (240, 230, 140)
banana_mania = (250, 231, 181)
cream = (255, 253, 208)
pastel_yellow = (253, 253, 150)
light_yellow = (255, 255, 224)

yellow_sand_list_3 = (
   light_gold,
   light_khaki,
   banana_mania,
   cream,
   pastel_yellow,
   light_yellow
)

# Palette 4
maize = (251, 236, 93)
jasmine = (248, 222, 126)
buff = (240, 220, 130)
mellow_yellow = (248, 222, 126)
lemon_chiffon = (255, 250, 205)
light_butter = (255, 236, 179)

yellow_sand_list_4 = (
   maize,
   jasmine,
   buff,
   mellow_yellow,
   lemon_chiffon,
   light_butter
)

# Black Sand Colors

# Palette 5
jet = (52, 52, 52)
charcoal = (54, 69, 79)
onyx = (53, 56, 57)
ebony = (85, 93, 80)
dark_charcoal = (35, 35, 35)
outer_space = (65, 74, 76)

black_sand_list_5 = (
   jet,
   charcoal,
   onyx,
   ebony,
   dark_charcoal,
   outer_space
)

# Palette 6
black_coral = (44, 50, 50)
jet_stream = (46, 50, 50)
raisin_black = (36, 33, 36)
charcoal_black = (54, 69, 79)
eerie_black_alt = (30, 30, 30)
night_black = (21, 21, 21)

black_sand_list_6 = (
   black_coral,
   jet_stream,
   raisin_black,
   charcoal_black,
   eerie_black_alt,
   night_black
)

# Pink Sand Colors

# Palette 7
coral_pink = (248, 131, 121)
salmon_pink = (255, 145, 164)
orchid_pink = (255, 131, 186)
neon_pink = (254, 51, 204)
blush_pink = (255, 193, 204)
fuchsia_pink = (255, 119, 255)

pink_sand_list_7 = (
   coral_pink,
   salmon_pink,
   orchid_pink,
   neon_pink,
   blush_pink,
   fuchsia_pink
)

# Palette 8
rose_quartz = (170, 152, 169)
bubblegum_pink = (255, 193, 204)
hot_pink = (255, 105, 180)
amaranth_pink = (242, 169, 191)
baby_pink_alt = (255, 182, 193)
magenta = (255, 0, 255)

pink_sand_list_8 = (
   rose_quartz,
   bubblegum_pink,
   hot_pink,
   amaranth_pink,
   baby_pink_alt,
   magenta
)

# Yellow Sand Colors

# Palette 9
mustard = (255, 219, 88)
daffodil = (255, 255, 49)
lemon = (255, 247, 0)
gold = (255, 215, 0)
yellow_orange = (255, 174, 66)
gold_crayola = (255, 182, 83)

yellow_sand_list_9 = (
   mustard,
   daffodil,
   lemon,
   gold,
   yellow_orange,
   gold_crayola
)

# Palette 10
cyber_yellow = (255, 211, 0)
mellow_yellow_alt = (248, 222, 126)
cream_alt = (255, 253, 208)
butter = (255, 241, 151)
pale_goldenrod = (238, 232, 170)
light_goldenrod_yellow = (250, 250, 210)

yellow_sand_list_10 = (
   cyber_yellow,
   mellow_yellow_alt,
   cream_alt,
   butter,
   pale_goldenrod,
   light_goldenrod_yellow
)

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

'''
An old color palette
color_list = (
   sand_color,
   mushikuri_iro_color,
   burlywood_color,
   coral_color,
   chrysler_coral_color
   )
'''

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
   black_sand_list,
   pink_sand_list_1,
   pink_sand_list_2,
   yellow_sand_list_3,
   yellow_sand_list_4,
   black_sand_list_5,
   black_sand_list_6,
   pink_sand_list_7,
   pink_sand_list_8,
   yellow_sand_list_9,
   yellow_sand_list_10
   )

# Coral Themed Palettes

# Palette 1
coral_sunset = (255, 127, 80)
sea_pink = (236, 128, 152)
coral_blush = (248, 131, 121)
light_coral = (240, 128, 128)
salmon_coral = (233, 150, 122)
deep_coral = (204, 78, 92)

coral_list_1 = (
   coral_sunset,
   sea_pink,
   coral_blush,
   light_coral,
   salmon_coral,
   deep_coral
)

# Palette 2
coral_red = (255, 64, 64)
peach_coral = (255, 182, 141)
faded_coral = (231, 142, 129)
soft_coral = (245, 104, 91)
shell_coral = (255, 153, 153)
warm_coral = (248, 114, 114)

coral_list_2 = (
   coral_red,
   peach_coral,
   faded_coral,
   soft_coral,
   shell_coral,
   warm_coral
)

# Ocean Themed Palettes

# Palette 3
sea_green = (46, 139, 87)
turquoise = (64, 224, 208)
teal_blue = (0, 128, 128)
ocean_blue = (28, 107, 160)
deep_sea_blue = (0, 105, 148)
aquamarine = (127, 255, 212)

ocean_list_3 = (
   sea_green,
   turquoise,
   teal_blue,
   ocean_blue,
   deep_sea_blue,
   aquamarine
)

# Palette 4
marine_blue = (0, 123, 167)
aqua_marine = (127, 255, 212)
light_sea_green = (32, 178, 170)
pacific_blue = (28, 169, 201)
seafoam_green = (159, 226, 191)
sea_wave = (72, 209, 204)

ocean_list_4 = (
   marine_blue,
   aqua_marine,
   light_sea_green,
   pacific_blue,
   seafoam_green,
   sea_wave
)

# Cosmic Themed Palettes

# Palette 5
nebula_purple = (104, 34, 139)
star_yellow = (255, 223, 0)
cosmic_blue = (66, 66, 111)
starlight_silver = (192, 192, 192)
galaxy_pink = (255, 105, 180)
deep_space_black = (10, 10, 25)

cosmic_list_5 = (
   nebula_purple,
   star_yellow,
   cosmic_blue,
   starlight_silver,
   galaxy_pink,
   deep_space_black
)

# Palette 6
meteor_orange = (255, 69, 0)
black_hole_black = (0, 0, 0)
nova_white = (245, 245, 245)
interstellar_green = (29, 177, 158)
cosmic_latte = (255, 248, 231)
comet_blue = (29, 172, 214)

cosmic_list_6 = (
   meteor_orange,
   black_hole_black,
   nova_white,
   interstellar_green,
   cosmic_latte,
   comet_blue
)

# Coral Themed Palettes

# Palette 7
flamingo_pink = (252, 142, 172)
peach_coral = (255, 182, 141)
living_coral = (255, 111, 97)
coral_peach = (255, 138, 128)
watermelon = (255, 99, 71)
coral_rose = (240, 128, 128)

coral_list_7 = (
   flamingo_pink,
   peach_coral,
   living_coral,
   coral_peach,
   watermelon,
   coral_rose
)

# Palette 8
salmon = (250, 128, 114)
dark_salmon = (233, 150, 122)
light_salmon = (255, 160, 122)
pale_violet_red = (219, 112, 147)
medium_violet_red = (199, 21, 133)
hot_pink = (255, 105, 180)

coral_list_8 = (
   salmon,
   dark_salmon,
   light_salmon,
   pale_violet_red,
   medium_violet_red,
   hot_pink
)

# Ocean Themed Palettes

# Palette 9
blue_lagoon = (0, 150, 136)
coral_reef = (242, 133, 0)
ocean_mist = (197, 224, 221)
sand_dollar = (255, 248, 231)
sea_shell = (255, 245, 238)
sea_breeze = (157, 255, 212)

ocean_list_9 = (
   blue_lagoon,
   coral_reef,
   ocean_mist,
   sand_dollar,
   sea_shell,
   sea_breeze
)

# Palette 10
atlantic_deep = (0, 51, 102)
tidal_teal = (72, 191, 145)
marine_tide = (67, 170, 139)
coral_sea = (255, 127, 80)
pearl_white = (234, 224, 212)
seaweed_green = (46, 139, 87)

ocean_list_10 = (
   atlantic_deep,
   tidal_teal,
   marine_tide,
   coral_sea,
   pearl_white,
   seaweed_green
)


coral_palette_list = (
   pink_coral_list,
   rainbow_coral_list,
   coral_list_1,
   coral_list_2,
   ocean_list_3,
   ocean_list_4,
   cosmic_list_5,
   cosmic_list_6,
   coral_list_7,
   coral_list_8,
   ocean_list_9,
   ocean_list_10
   )

sand_list = random.choice(sand_palette_list)

coral_list = random.choice(coral_palette_list)

#MAZE_CENTER_X = int(side_dimension + (gameboard_dimension / 2) - (CELL_SIZE / 2)) old way to calculate center
MAZE_CENTER_X = int(side_dimension + (gameboard_dimension / 2) - CELL_SIZE)
MAZE_CENTER_Y = int((y_dimension / 2) - CELL_SIZE)

nudi_x = MAZE_CENTER_X #puts Noodles in the center
nudi_y = MAZE_CENTER_Y
noodles_lives = 3

spider_last_direction = {}

paused = True #starts the game paused
level = 1 #starts the game at level 1
high_score = 0 #sets the high score

'''
HERE IS THE MAIN FUNCTION! WAHOO!
'''

def main(CELL_SIZE, nudi_x, nudi_y, done, paused):
   '''
   Description: This is the main function for Noodles' Quest. It draws the start screen, prepares a game and gets the spiders information,
   sets up the score/level/lives ect, gets the spiders ready to move, then begins its while loop to run the game

   Input: Takes the global variables CELL_SIZE, nudi_x, nudi_y, done, paused

   Output: Runs the game
   '''
   draw_start_screen()
   spiders = prepare_game()
   #print(spiders)
   spider_list = spiders[0]
   spider_cells = spiders[1]
   #print(spider_list)
   #print(spider_cells)
   score_font = pygame.font.SysFont("PressStart2P-vaV7.ttf", 32)
   rules_font = pygame.font.SysFont("PressStart2P-vaV7.ttf", 20)
   
   score_count = 0
   score_board = score_font.render(f"Score: {score_count}", False, (255,255,255))
   global high_score
   high_score_board = score_font.render(f"High Score: {high_score}", False, (255,255,255))
   global level
   #level = 1
   level_board = score_font.render(f'Level: {level}', False, (255,255,255))
   escape_key_text = rules_font.render("Press 'esc' key to quit", False, (255,255,255))
   r_key_text = rules_font.render("Press 'r' key to re-roll level", False, (255,255,255))
   p_key_text = rules_font.render("Press 'p' key to pause/unpause", False, (255, 255, 255))
   draw_left_score_and_text(score_board, high_score_board, level_board, escape_key_text, r_key_text, p_key_text)

   #noodles_lives = 3
   life_board = score_font.render(f'Lives: {noodles_lives}', False, (255, 255, 255))
   draw_right_life(life_board)
   
   icon_img = icon_img_right
   screen.blit(icon_img, (nudi_x, nudi_y))

   spider_move_event = pygame.USEREVENT + 0 #sets up the spider timer for movement
   spider_time = int(500 // (1.2 * level)) #spiders should get faster and faster as you level up
   pygame.time.set_timer(spider_move_event, spider_time)
   
   while not done:
      pygame.display.flip() #updates the screen
      for event in pygame.event.get(): #sets up the events
         if event.type == pygame.QUIT: #the never true quit event
            done = True
         if event.type == KEYDOWN: #the pause key event
            if event.key == pygame.K_p:# Pausing/Unpausing
               paused = not paused
            elif event.key == K_r: #creates the reroll key 'r'
                  noodles_position = reset_noodles()
                  nudi_x = noodles_position[0]
                  nudi_y = noodles_position[1]
                  spiders = prepare_game()
                  spider_list = spiders[0]
                  spider_cells = spiders[1]
                  draw_left_score_and_text(score_board, high_score_board, level_board, escape_key_text, r_key_text, p_key_text)
                  life_board = score_font.render(f'Lives: {noodles_lives}', False, (255, 255, 255))
                  draw_right_life(life_board)
                  paused = True
                  screen.blit(icon_img, (nudi_x, nudi_y)) #draws Noodles
         if paused == True: #if the game is paused, the loop breaks here until it is unpaused
            break
         if event.type == spider_move_event: #spider movement event
            old_spider_data = spiders[0]
            for spider in range(len(old_spider_data)): #goes through each spider in the spiders list and makes them move
               #print(f'Moving spider #{spider}') old debug print
               noodles_position = [nudi_x, nudi_y]
               spiders = move_spider(spider, spiders, noodles_position, screen)
               pygame.display.flip() #updates the screen after all the moves
            gamestate = spider_bite_check(noodles_position, spiders, life_board) #did Noodles get bit by a spider moving onto her?
            paused = gamestate[0]
            nudi_x = gamestate[1][0]
            nudi_y = gamestate[1][1]
            spiders = gamestate[2]
         if event.type == KEYDOWN:
            key_press = event.key
            if event.key == K_ESCAPE: #creates the quit key 'esc'
                 pygame.quit()
                 return
            elif event.key == K_r: #creates the reroll key 'r'
                  noodles_position = reset_noodles()
                  nudi_x = noodles_position[0]
                  nudi_y = noodles_position[1]
                  spiders = prepare_game()
                  spider_list = spiders[0]
                  spider_cells = spiders[1]
                  draw_left_score_and_text(score_board, high_score_board, level_board, escape_key_text, r_key_text, p_key_text)
                  life_board = score_font.render(f'Lives: {noodles_lives}', False, (255, 255, 255))
                  draw_right_life(life_board)
                  paused = True
                  screen.blit(icon_img, (nudi_x, nudi_y)) #draws Noodles
                  
            if check_for_collision_and_edge(key_press, CELL_SIZE, nudi_x, nudi_y): #checks for collision if the keypress was not 'esc', 'r', or 'p'
               break
            else: #if there was no possible collision detected, continue with the game loop response to a key press
               is_algae = check_for_algae(key_press, CELL_SIZE, nudi_x, nudi_y) #if no collision, checks for algae at the future move spot
               if is_algae:
                  score_count = score_points(score_count) #update the score
                  score_board = score_font.render(f"Score: {score_count}", False, (255,255,255)) #updates the scoreboard
                  pygame.draw.rect(screen, side_screen_color, pygame.Rect(0, 0, side_dimension, y_dimension/12))
                  screen.blit(score_board, (8, 16))
                  high_score_board = score_font.render(f"High Score: {high_score}", False, (255,255,255))
                  screen.blit(high_score_board, (8, 48))
                  future_nudi_x = move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[0] #checks to see where Noodles will be
                  future_nudi_y = move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[1]
                  draw_sand(future_nudi_x, future_nudi_y, screen) #draws sand/ deletes the algae so that algae_remainging can't see it
                  if not is_algae_remaining(screen):
                     #the current win result; re-rolls the game
                      print("You win!")
                      level = level +1
                      level_board = score_font.render(f'Level: {level}', False, (255,255,255)) #updates the level_board text after the level value has been updated
                      noodles_position = reset_noodles() #puts Noodles back in the center
                      nudi_x = noodles_position[0]
                      nudi_y = noodles_position[1]
                      spiders = prepare_game() #launches the next map and set of spiders
                      spider_list = spiders[0]
                      spider_cells = spiders[1]
                      draw_sand(future_nudi_x, future_nudi_y, screen)
                      draw_left_score_and_text(score_board, high_score_board, level_board, escape_key_text, r_key_text, p_key_text)
                      life_board = score_font.render(f'Lives: {noodles_lives}', False, (255, 255, 255))
                      draw_right_life(life_board)
                      spider_time = int(500 // (1.2 * level))
                      paused = True
                      screen.blit(icon_img, (nudi_x, nudi_y)) #draws Noodles
                      break
                      #victory_dance(nudi_x, nudi_y, screen)
                      
                  
               draw_sand(nudi_x, nudi_y, screen) #erases Noodles from current position

               #checks to see if Noodles will move left or right
               #and then changes the icon to point left or right accordingly
               #and then draws the icon
               old_nudi_x = nudi_x #needed to tell if Noodles changed direction below
               nudi_x = move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[0]
               nudi_y = move_nude(key_press, CELL_SIZE, nudi_x, nudi_y)[1]
               noodles_position = [nudi_x, nudi_y]
               gamestate = spider_bite_check(noodles_position, spiders, life_board) #did Noodles get bit by a spider moving onto her?
               paused = gamestate[0]
               nudi_x = gamestate[1][0]
               nudi_y = gamestate[1][1]
               spiders = gamestate[2]
               
               if old_nudi_x < nudi_x: #checks to see if Noodles has changed orientations and is pointing left or right
                  icon_img = icon_img_right
               elif old_nudi_x > nudi_x:
                  icon_img = icon_img_left
               else:
                  pass
               
               screen.blit(icon_img, (nudi_x, nudi_y)) #draws Noodles
               print(nudi_x, nudi_y) #debug print to see what cell Noodles occupies
               '''
               old_spider_data = spiders[0]
               for spider in range(len(old_spider_data)):
                  #print(f'Moving spider #{spider}')
                  spiders = move_spider(spider, spiders, screen)
                  '''

'''
This is a future function
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
   '''
   Description: This function combines a lot of other functions to generate the game map, populate the map with algae,
   set up the spiders, and clean up the board.
   
   Input: None, it uses the global variables CELL_SIZE, screen, nudi_x, and nudi_y

   Output: It returns spider_list and spider_cells which contain the spiders location information and the information necessary to reset the cell after a spider moves
   '''
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
   '''
   Description: This function is used after the spiders move to check if they jumped onto Noodles and bit her.
   
   Input: This function takes Noodles' position, the spiders information, and the life_board (so that it may be updated)

   Output: This function returns 'gamestate', which is a list of the game's updated paused state, Noodles' location, and the spiders list
   '''
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
   '''
   Description: This function removes the spider graphic of the sea spiders after the spider list is reset
   
   Input: The location of the spiders where they need to be erased. Spiders should be passed to this function before the new spiders are generated.

   Output: None, but it does draw sand where the spiders were. This may erase algae there too. Need to look into this.
   '''
   spider_list = spiders[0]
   for spider in range(len(spider_list)):
      spider_cell = spider_list[spider]
      draw_sand(spider_cell[0], spider_cell[1], screen)

def reset_noodles():
   '''
   Description: A simple function that puts Noodles position back in the center of the game map.
   
   Input: None, but it does work with the global variables nudi_x, nudi_y, MAZE_CENTER_X, and MAZE_CENTER_Y

   Output: Returns Nooodles' updated position, i.e. the center of the maze.
   '''
   nudi_x = MAZE_CENTER_X
   nudi_y = MAZE_CENTER_Y
   noodles_position = (nudi_x, nudi_y)
   return noodles_position

def lose_a_life(life_board):
   '''
   Description: Reduces the life total by 1 and updates the displayed lives information.
   Ends the game with the game_over function if you lose the last life.
   
   Input: Takes the life_board rendered text variable.

   Output: None, but it does update the displayed Lives information and the noodles_lives variable.
   '''
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
   '''
   Description: Draws a game over screen when Noodles loses the last life and sends the player back to the start screen.
   
   Input: None are required. It does use the global variables screen, PressStart2P font, CELL_SIZE, nudi_x, nudi_y, done, and paused.

   Output: None, but it does start a new loop of main to play a new game.
   '''
   #draw a black rect over the whole screen
   screen.fill(black)
   #write game over in the center of the screen
   white = (255, 255, 255)
   font_header = pygame.font.Font("PressStart2P-vaV7.ttf", 64)
   game_over_message = font_header.render("GAME OVER", False, white)
   screen.blit(game_over_message, ((x_dimension / 2) - (game_over_message.get_width() // 2), (y_dimension / 2) - (game_over_message.get_height() // 2)))
   pygame.display.update()
   time.sleep(2)
   #on any key, restart the game
   global done
   while not done:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            done = True
         if event.type == KEYDOWN:
            main(CELL_SIZE, nudi_x, nudi_y, done, paused)

def move_spider(spider, spiders, noodles_position, screen):
    '''
    Description: Goes through a series of steps to pick a direction and determine a legal move for the spiders. Then, it moves the spiders.
   
    Input: This function takes the spider, spiders, noodles_position, and screen variables. 

    Output: Before it returns, it draws the spider on the screen in the new position and erases it from the old position.
    It returns the updated spiders list with the new spider information in it that describes the move. 
    '''
    spider_list = spiders[0]
    spider_cells = spiders[1]
   
    # Get spider location from spider_list
    spider_x = spider_list[spider][0]
    spider_y = spider_list[spider][1]

    # Define possible directions
    possible_dir = [K_KP6, K_KP4, K_KP8, K_KP2, K_KP7, K_KP9, K_KP3, K_KP1]

    # Get the last move direction for the current spider, if it exists
    last_move_dir = spider_last_direction.get(spider, None)

    # Choose the last direction first if it exists
    if last_move_dir:
        move_dir = last_move_dir
    else:
        random.shuffle(possible_dir)
        move_dir = possible_dir.pop()

    future_spider_x = move_nude(move_dir, CELL_SIZE, spider_x, spider_y)[0]
    future_spider_y = move_nude(move_dir, CELL_SIZE, spider_x, spider_y)[1]

    potential_position = [future_spider_x, future_spider_y]
   
    # Check for collisions or edges
    while check_for_collision_and_edge(move_dir, CELL_SIZE, spider_x, spider_y) or potential_position in spider_list:
        if len(possible_dir) == 0:
            return spiders  # Return unupdated spiders if there are no possible moves
        if last_move_dir:
            possible_dir.remove(last_move_dir)
            last_move_dir = None
        random.shuffle(possible_dir)
        move_dir = possible_dir.pop()
        future_spider_x = move_nude(move_dir, CELL_SIZE, spider_x, spider_y)[0]
        future_spider_y = move_nude(move_dir, CELL_SIZE, spider_x, spider_y)[1]
        potential_position = [future_spider_x, future_spider_y]

    future_spider_x = move_nude(move_dir, CELL_SIZE, spider_x, spider_y)[0]
    future_spider_y = move_nude(move_dir, CELL_SIZE, spider_x, spider_y)[1]
   
    copied_cell = {}
    copied_cell = copy_cell(future_spider_x, future_spider_y)
   
    current_cell = spider_cells[spider]
    paste_cell(current_cell)

    # Move spider to new cell and update spider_list
    spider_x = future_spider_x
    spider_y = future_spider_y
    screen.blit(sea_spider_img, (spider_x, spider_y))  # Draw the spider
    spider_list[spider][0] = spider_x  # Update the spider_list x 
    spider_list[spider][1] = spider_y  # Update the spider_list y
               
    # Save the copied cell as old cell
    spider_cells[spider] = copied_cell

    # Update spiders
    spiders = [spider_list, spider_cells]

    # Update the last move direction for the current spider
    spider_last_direction[spider] = move_dir

    return spiders  # Return the updated spider list
   
def copy_cell(icon_x,icon_y):
   '''
   Description: Creates a dictionary of [x,y] keys with rgb values. This data is used to erase spiders as they move around.
   
   Input: This function takes the [x,y] coordinate for the cell the object is currently in.

   Output: Returns a dictionary of [x,y]:rgbs for a 32x32 pixel cell.
   '''
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
   '''
   Description: This uses a copied_cell dictionary to erase an icon from its old position with the data for where it was located.
   
   Input: This function takes a copied_cell dictonary. 

   Output: There is no output, but it does perform the erasing/pasting function.
   '''
   cell_dict = cell_rgb_dict
   for key in cell_dict:
      rgb_paste = cell_rgb_dict[key]
      screen.set_at(key, rgb_paste)
   
 
def draw_spiders(screen, spider_list):
   '''
   Description: A simple function that draws each spider in its location.
   
   Input: The screen and spider_list. Problaby doesn't need screen since it is global.

   Output: No output, but it does perform the operation of blit-ing the spiders onto the screen.
   '''
   for spider in spider_list:
      screen.blit(sea_spider_img, spider)

def generate_spiders():
   '''
   Description: Creates the spiders by generating a list of valid positions and then copying the cells at those positions
   so that the spiders can be erased when they move.
   
   Input: None, but it does use the global variables level, CELL_SIZE, side_dimension, screen.

   Output: It outputs the spider_list of locations and the spider_cell list of cell dictionaries. 
   '''
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
   '''
   Description: Checks to see if there is any algae left on the map.
   
   Input: The screen variable. 

   Output: It returns as True or False.
   '''
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
   '''
   Description: This is the function that main() and gameover() use to begin the game with a start screen.
   
   Input: None, but it does use some global variables; BLINK_EVENT, screen, the font,  

   Output: None, but it performs the operation of drawing the starting screen.
   '''
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
   '''
   Description: A simple function that updates the score.
   
   Input: It takes the score_count.

   Output: It returns the updated score_count.
   '''
   #updates the score by 10, returns the score_count
   score_count = score_count + 10
   global high_score
   if score_count >= high_score:
      high_score = score_count
   return score_count


def check_for_algae(key_press, CELL_SIZE, nudi_x, nudi_y):
   '''
   Description: This function checks to see if Noodles is eating an algae as she moves onto a cell.
   
   Input: The key press, CELL_SIZE (global?), nudi_x (global?), and nudi_y (global?). 

   Output: This returns True or False to guide an if/else statement.
   '''
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
   '''
   Description: This function checks to see if Noodles can move onto the potential future cell
   
   Input: The key press, CELL_SIZE (global?), nudi_x (global?), and nudi_y (global?).

   Output: This returns True or False to guide an if/else statement.
   '''
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
   '''
   Description: Specifically checks for coral.
   
   Input: The key press, CELL_SIZE (global?), nudi_x (global?), and nudi_y (global?).

   Output: This returns True or False to guide an if/else statement. 
   '''
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
   '''
   Description: Specifically checks for a map edge.
   
   Input: The key press, CELL_SIZE (global?), nudi_x (global?), and nudi_y (global?).

   Output: This returns True or False to guide an if/else statement. 
   '''
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

def draw_left_score_and_text(score_board, high_score_board, level_board, escape_key_text, r_key_text, p_key_text):
   '''
   Description: This simple function draws all the text on the left hand side of the board.
   
   Input: It takes all the variables for the text to be printed on the left: score_board, level_board, escape_key_text, r_key_text, p_key_text.

   Output: None, performs the operation of drawing the text.
   '''
   screen.blit(score_board, (8, 16))
   screen.blit(high_score_board, (8, 48))
   screen.blit(level_board, (8, 80))
   screen.blit(escape_key_text, (8, 800))
   screen.blit(r_key_text, (8, 816))
   screen.blit(p_key_text, (8, 832))

def draw_right_life(life_board):
   '''
   Description: This simple function draws all the text on the right hand side of the board.
   
   Input: It takes all the variables for the text to be printed on the right: life_board

   Output: None, performs the operation of drawing the text.
   '''
   x = side_dimension + gameboard_dimension + 8
   print(x)
   pygame.draw.rect(screen, side_screen_color, pygame.Rect(x, 16, life_board.get_width() +16, life_board.get_height() +16))
   screen.blit(life_board,(x, 16))

def draw_map(CELL_SIZE):
#def draw_voronoi_maze(CELL_SIZE):
    '''
    Description: Creates a gameboard filled with randomly shaped and sized rooms connected in a maze-like fashion.
    
    Input: CELL_SIZE (global?)

    Output: None, performs the operation of drawing the gameboard.
    '''
    global sand_list
    sand_list = random.choice(sand_palette_list)
    global coral_list
    coral_list = random.choice(coral_palette_list)

    # Initialize the gameboard dimensions
    gameboard_cells = gameboard_dimension // CELL_SIZE
    width, height = gameboard_cells, gameboard_cells

    # Create a blank gameboard
    gameboard = [[0 for _ in range(width)] for _ in range(height)]

    # Generate random rooms
    num_rooms = 16
    min_size, max_size = 2, 5
    rooms = []
    center_room_size = 2  # Ensuring a central room of size 4x4
    center_x, center_y = width // 2, height // 2
    center_room = pygame.Rect(center_x - center_room_size // 2, center_y - center_room_size // 2, center_room_size, center_room_size)
    rooms.append(center_room)

    for _ in range(num_rooms - 1):  # Adjusting num_rooms since we've already added the central room
        w, h = random.randint(min_size, max_size), random.randint(min_size, max_size)
        x, y = random.randint(0, width - w - 1), random.randint(0, height - h - 1)
        rooms.append(pygame.Rect(x, y, w, h))

    # Place rooms on the gameboard
    for room in rooms:
        for i in range(room.x, room.x + room.width):
            for j in range(room.y, room.y + room.height):
                gameboard[i][j] = 1

    # Connect rooms with corridors
    def connect_rooms(room1, room2):
        x1, y1 = room1.center
        x2, y2 = room2.center
        if random.choice([True, False]):
            h_corridor(gameboard, x1, x2, y1)
            v_corridor(gameboard, y1, y2, x2)
        else:
            v_corridor(gameboard, y1, y2, x1)
            h_corridor(gameboard, x1, x2, y2)

    def h_corridor(board, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            board[x][y] = 1

    def v_corridor(board, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            board[x][y] = 1

    for i in range(len(rooms) - 1):
        connect_rooms(rooms[i], rooms[i + 1])

    # Debugging: Print the gameboard grid as a list
    gameboard_debug = []
    for row in gameboard:
        gameboard_debug.append(''.join(['#' if cell == 0 else '.' for cell in row]))

    print('\n'.join(gameboard_debug))

    # Draw the gameboard
    for x in range(width):
        for y in range(height):
            screen_x = side_dimension + x * CELL_SIZE
            screen_y = y * CELL_SIZE
            if gameboard[x][y] == 1:
                draw_sand(screen_x, screen_y, screen)
            else:
                draw_coral(screen_x, screen_y, screen)

    # Draw the side display areas
    pygame.draw.rect(screen, side_screen_color, pygame.Rect(0, 0, side_dimension, y_dimension))
    pygame.draw.rect(screen, side_screen_color, pygame.Rect(side_dimension + gameboard_dimension, 0, side_dimension, y_dimension))
    pygame.display.update()


def draw_symmetrical_maze_with_rooms(CELL_SIZE):
    '''
    Description: Creates a symmetrical maze with an open starting area in the center and rooms throughout the maze.
    
    Input: CELL_SIZE (global?)

    Output: None, performs the operation of drawing the maze.
    '''
    global sand_list
    sand_list = random.choice(sand_palette_list)
    global coral_list
    coral_list = random.choice(coral_palette_list)

    # Initialize the maze grid with walls
    gameboard_cells = gameboard_dimension // CELL_SIZE
    maze = [[0 for _ in range(gameboard_cells)] for _ in range(gameboard_cells)]

    # Create the central room (2x4 sand tiles)
    center_x, center_y = gameboard_cells // 2, gameboard_cells // 2
    for i in range(center_x - 1, center_x + 1):
        for j in range(center_y - 2, center_y + 2):
            maze[i][j] = 1

    def add_rooms(maze, room_size, num_rooms):
        for _ in range(num_rooms):
            room_x = random.randint(1, gameboard_cells - room_size - 1)
            room_y = random.randint(1, gameboard_cells - room_size - 1)
            for i in range(room_x, room_x + room_size):
                for j in range(room_y, room_y + room_size):
                    maze[i][j] = 1

    def carve_paths(maze, x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            nnx, nny = x + 2*dx, y + 2*dy
            if 0 <= nnx < gameboard_cells and 0 <= nny < gameboard_cells and maze[nnx][nny] == 0:
                maze[nx][ny] = 1
                maze[nnx][nny] = 1
                carve_paths(maze, nnx, nny)

    # Add rooms throughout the maze
    room_size = 2
    num_rooms = 16
    add_rooms(maze, room_size, num_rooms)

    # Carve the maze paths starting from the center
    carve_paths(maze, center_x, center_y)

    # Debugging: Print the maze grid as a list
    maze_debug = []
    for row in maze:
        maze_debug.append(''.join(['#' if cell == 0 else '.' for cell in row]))
    
    print('\n'.join(maze_debug))

    # Draw the maze
    for x in range(gameboard_cells):
        for y in range(gameboard_cells):
            screen_x = side_dimension + x * CELL_SIZE
            screen_y = y * CELL_SIZE
            if maze[x][y] == 1:
                draw_sand(screen_x, screen_y, screen)
            else:
                draw_coral(screen_x, screen_y, screen)
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

    # Draw the side display areas
    pygame.draw.rect(screen, side_screen_color, pygame.Rect(0, 0, side_dimension, y_dimension))
    pygame.draw.rect(screen, side_screen_color, pygame.Rect(side_dimension + gameboard_dimension, 0, side_dimension, y_dimension))
    pygame.display.update()
    
def draw_symmetrical_maze_with_rooms(CELL_SIZE):
    '''
    Description: Creates a symmetrical maze with an open starting area in the center and rooms throughout the maze.
    
    Input: CELL_SIZE (global?)

    Output: None, performs the operation of drawing the maze.
    '''
    global sand_list
    sand_list = random.choice(sand_palette_list)
    global coral_list
    coral_list = random.choice(coral_palette_list)

    # Initialize the maze grid with walls
    gameboard_cells = gameboard_dimension // CELL_SIZE
    maze = [[0 for _ in range(gameboard_cells)] for _ in range(gameboard_cells)]

    # Create the central room (2x4 sand tiles)
    center_x, center_y = gameboard_cells // 2, gameboard_cells // 2
    for i in range(center_x - 1, center_x + 1):
        for j in range(center_y - 2, center_y + 2):
            maze[i][j] = 1

    def add_rooms(maze, room_size, num_rooms):
        for _ in range(num_rooms):
            room_x = random.randint(1, gameboard_cells - room_size - 1)
            room_y = random.randint(1, gameboard_cells - room_size - 1)
            for i in range(room_x, room_x + room_size):
                for j in range(room_y, room_y + room_size):
                    maze[i][j] = 1

    def carve_paths(maze, x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            nnx, nny = x + 2*dx, y + 2*dy
            if 0 <= nnx < gameboard_cells and 0 <= nny < gameboard_cells and maze[nnx][nny] == 0:
                maze[nx][ny] = 1
                maze[nnx][nny] = 1
                carve_paths(maze, nnx, nny)

    # Add rooms throughout the maze
    room_size = 4
    num_rooms = 8
    add_rooms(maze, room_size, num_rooms)

    # Carve the maze paths starting from the center
    carve_paths(maze, center_x, center_y)

    # Debugging: Print the maze grid as a list
    maze_debug = []
    for row in maze:
        maze_debug.append(''.join(['#' if cell == 0 else '.' for cell in row]))
    
    print('\n'.join(maze_debug))

    # Draw the maze
    for x in range(gameboard_cells):
        for y in range(gameboard_cells):
            screen_x = side_dimension + x * CELL_SIZE
            screen_y = y * CELL_SIZE
            if maze[x][y] == 1:
                draw_sand(screen_x, screen_y, screen)
            else:
                draw_coral(screen_x, screen_y, screen)

    # Draw the side display areas
    pygame.draw.rect(screen, side_screen_color, pygame.Rect(0, 0, side_dimension, y_dimension))
    pygame.draw.rect(screen, side_screen_color, pygame.Rect(side_dimension + gameboard_dimension, 0, side_dimension, y_dimension))
    pygame.display.update()

  
def draw_maze_with_rooms_map(CELL_SIZE):
    '''
    Description: Creates the map based on an algorithm for placing sand and coral tiles. Draws a maze-like structure of coral tiles with multi-cell open rooms and a central room where the player starts.
    
    Input: CELL_SIZE (global?)

    Output: None, performs the operation of drawing the maze/map.
    '''
    global sand_list
    sand_list = random.choice(sand_palette_list)
    global coral_list
    coral_list = random.choice(coral_palette_list)

    def carve_maze_with_rooms(maze, x, y):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N, E, S, W
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < gameboard_cells and 0 <= ny < gameboard_cells and maze[nx][ny] == 0:
                maze[nx][ny] = 1
                maze[x + dx][y + dy] = 1
                carve_maze_with_rooms(maze, nx, ny)

    # Initialize the maze grid with walls
    gameboard_cells = gameboard_dimension // CELL_SIZE
    maze = [[0 for _ in range(gameboard_cells)] for _ in range(gameboard_cells)]

    # Create random rooms
    num_rooms = random.randint(3, 6)
    for _ in range(num_rooms):
        room_width = random.randint(2, 4)
        room_height = random.randint(2, 4)
        room_x = random.randint(0, gameboard_cells - room_width - 1)
        room_y = random.randint(0, gameboard_cells - room_height - 1)
        for rx in range(room_width):
            for ry in range(room_height):
                maze[room_x + rx][room_y + ry] = 1

    # Create the central room
    center_x, center_y = gameboard_cells // 2, gameboard_cells // 2
    room_width, room_height = 3, 3  # Adjust size as needed
    for rx in range(-room_width//2, room_width//2 + 1):
        for ry in range(-room_height//2, room_height//2 + 1):
            maze[center_x + rx][center_y + ry] = 1

    # Ensure the starting point is within bounds and on a clear cell
    start_x, start_y = center_x, center_y
    maze[start_x][start_y] = 1

    # Carve the maze
    carve_maze_with_rooms(maze, start_x, start_y)

    # Draw the maze
    for x in range(gameboard_cells):
        for y in range(gameboard_cells):
            screen_x = side_dimension + x * CELL_SIZE
            screen_y = y * CELL_SIZE
            if maze[x][y] == 1:
                draw_sand(screen_x, screen_y, screen)
            else:
                draw_coral(screen_x, screen_y, screen)

    # Draw the side display areas
    pygame.draw.rect(screen, side_screen_color, pygame.Rect(0, 0, side_dimension, y_dimension))
    pygame.draw.rect(screen, side_screen_color, pygame.Rect(side_dimension + gameboard_dimension, 0, side_dimension, y_dimension))
    pygame.display.update()

def draw_maze_with_rooms(CELL_SIZE):
    '''
    Description: Creates the map based on an algorithm for placing sand and coral tiles. Draws a maze-like structure of coral tiles with multi-cell open rooms.
    
    Input: CELL_SIZE (global?)

    Output: None, performs the operation of drawing the maze/map.
    '''
    global sand_list
    sand_list = random.choice(sand_palette_list)
    global coral_list
    coral_list = random.choice(coral_palette_list)

    def carve_maze_with_rooms(maze, x, y):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N, E, S, W
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < gameboard_cells and 0 <= ny < gameboard_cells and maze[nx][ny] == 0:
                maze[nx][ny] = 1
                maze[x + dx][y + dy] = 1
                carve_maze_with_rooms(maze, nx, ny)

    # Initialize the maze grid with walls
    gameboard_cells = gameboard_dimension // CELL_SIZE
    maze = [[0 for _ in range(gameboard_cells)] for _ in range(gameboard_cells)]

    # Create random rooms
    num_rooms = random.randint(6, 12)
    for _ in range(num_rooms):
        room_width = random.randint(2, 4)
        room_height = random.randint(2, 4)
        room_x = random.randint(0, gameboard_cells - room_width - 1)
        room_y = random.randint(0, gameboard_cells - room_height - 1)
        for rx in range(room_width):
            for ry in range(room_height):
                maze[room_x + rx][room_y + ry] = 1

    # Starting point for the maze
    start_x, start_y = random.randint(0, gameboard_cells // 2) * 2, random.randint(0, gameboard_cells // 2) * 2
    maze[start_x][start_y] = 1

    # Carve the maze
    carve_maze_with_rooms(maze, start_x, start_y)

    # Draw the maze
    for x in range(gameboard_cells):
        for y in range(gameboard_cells):
            screen_x = side_dimension + x * CELL_SIZE
            screen_y = y * CELL_SIZE
            if maze[x][y] == 1:
                draw_sand(screen_x, screen_y, screen)
            else:
                draw_coral(screen_x, screen_y, screen)

    # Draw the side display areas
    pygame.draw.rect(screen, side_screen_color, pygame.Rect(0, 0, side_dimension, y_dimension))
    pygame.draw.rect(screen, side_screen_color, pygame.Rect(side_dimension + gameboard_dimension, 0, side_dimension, y_dimension))
    pygame.display.update()

def draw_maze_map(CELL_SIZE):
    '''
    Description: Creates the map based on an algorithm for placing sand and coral tiles. Draws a maze-like structure of coral tiles.
    
    Input: CELL_SIZE (global?)

    Output: None, performs the operation of drawing the maze/map.
    '''
    global sand_list
    sand_list = random.choice(sand_palette_list)
    global coral_list
    coral_list = random.choice(coral_palette_list)

    def carve_maze(maze, x, y):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N, E, S, W
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < gameboard_cells and 0 <= ny < gameboard_cells and maze[nx][ny] == 0:
                maze[nx][ny] = 1
                maze[x + dx][y + dy] = 1
                carve_maze(maze, nx, ny)

    # Initialize the maze grid with walls
    gameboard_cells = gameboard_dimension // CELL_SIZE
    maze = [[0 for _ in range(gameboard_cells)] for _ in range(gameboard_cells)]

    # Starting point for the maze
    start_x, start_y = random.randint(0, gameboard_cells // 2) * 2, random.randint(0, gameboard_cells // 2) * 2
    maze[start_x][start_y] = 1

    # Carve the maze
    carve_maze(maze, start_x, start_y)

    # Draw the maze
    for x in range(gameboard_cells):
        for y in range(gameboard_cells):
            screen_x = side_dimension + x * CELL_SIZE
            screen_y = y * CELL_SIZE
            if maze[x][y] == 1:
                draw_sand(screen_x, screen_y, screen)
            else:
                draw_coral(screen_x, screen_y, screen)

    # Draw the side display areas
    pygame.draw.rect(screen, side_screen_color, pygame.Rect(0, 0, side_dimension, y_dimension))
    pygame.draw.rect(screen, side_screen_color, pygame.Rect(side_dimension + gameboard_dimension, 0, side_dimension, y_dimension))
    pygame.display.update()
   

def draw_mirror_map(CELL_SIZE):
   '''
   Description: Creates the map based on an algorithm for placing sand and algae tiles. Draws a quadrilaterally symetrical map.
   
   Input: CELL_SIZE (global?)

   Output: None, performs the operation of drawing the maze/map. 
   '''
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
   '''
   Description: Creates the map based on an algorithm for placing sand and algae tiles. Draws a random map.
   
   Input: CELL_SIZE (global?)

   Output: None, performs the operation of drawing the maze/map. 
   '''
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
   '''
   Description: Draws a cell full of 2x2 pixel sand grains.
   
   Input: The x and y of the cell that needs to be made into sand, the screen (global?)

   Output: None, performs the operation of drawing sand tiles.
   '''
   div_var = 16 #cell division variable
   mini_cell = CELL_SIZE / div_var
   for x in range(div_var):
      for y in range(div_var):
         pygame.draw.rect(screen, random.choice(sand_list), pygame.Rect(x_coord + (x * CELL_SIZE / div_var), y_coord + (y * CELL_SIZE / div_var), mini_cell, mini_cell))


def draw_fan_coral(x, y, screen):
   '''
   Description: Draws a cell of coral with a 'fan fractal' pattern.
   
   Input: The x and y of the cell that needs to be made into coral, the screen (global?)

   Output: None, performs the operation of drawing coral tiles. 
   '''
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
   '''
   Description: Draws a cell of coral with a 'row by column' pattern.
   
   Input: The x and y of the cell that needs to be made into coral, the screen (global?)

   Output: None, performs the operation of drawing coral tiles. 
   '''
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


def draw_fractal_maze_coral(x, y, screen):
    '''
    Description: Draws a cell of coral with a 'fractal maze' pattern.
    
    Input: The x and y of the cell that needs to be made into coral, the screen (global?)

    Output: None, performs the operation of drawing coral tiles. 
    '''
    maze_var = random.randint(10, 20)
    step = (CELL_SIZE / 2) / maze_var
    tile_adjust = (CELL_SIZE / 2)

    coral_1 = random.choice(coral_list)
    coral_2 = random.choice(coral_list)
    while coral_2 == coral_1:
        coral_2 = random.choice(coral_list)
    coral_colors = cycle([coral_1, coral_2])
    coral_color = next(coral_colors)

    pygame.draw.rect(screen, coral_color, pygame.Rect((x, y, CELL_SIZE, CELL_SIZE)))
    for i in range(maze_var):
        y_adjust = i * step
        x_adjust = i * step
        small_cell = CELL_SIZE / (i + 1)
        coral_color = next(coral_colors)
        
        # Draw unicursal maze pattern using lines
        pygame.draw.line(screen, coral_color, (x + x_adjust, y + y_adjust), (x + x_adjust + small_cell, y + y_adjust + small_cell), 1)
        pygame.draw.line(screen, coral_color, (x + x_adjust + small_cell, y + y_adjust), (x + x_adjust, y + y_adjust + small_cell), 1)

        # Draw additional fractal lines to enhance the pattern
        pygame.draw.line(screen, coral_color, (x + x_adjust, y + y_adjust + small_cell / 2), (x + x_adjust + small_cell, y + y_adjust + small_cell / 2), 1)
        pygame.draw.line(screen, coral_color, (x + x_adjust + small_cell / 2, y + y_adjust), (x + x_adjust + small_cell / 2, y + y_adjust + small_cell), 1)

        # Repeat the pattern in the other quadrants
        pygame.draw.line(screen, coral_color, (x + x_adjust + tile_adjust, y + y_adjust), (x + x_adjust + small_cell + tile_adjust, y + y_adjust + small_cell), 1)
        pygame.draw.line(screen, coral_color, (x + x_adjust + small_cell + tile_adjust, y + y_adjust), (x + x_adjust + tile_adjust, y + y_adjust + small_cell), 1)
        pygame.draw.line(screen, coral_color, (x + x_adjust + tile_adjust, y + y_adjust + small_cell / 2), (x + x_adjust + small_cell + tile_adjust, y + y_adjust + small_cell / 2), 1)
        pygame.draw.line(screen, coral_color, (x + x_adjust + small_cell / 2 + tile_adjust, y + y_adjust), (x + x_adjust + small_cell / 2 + tile_adjust, y + y_adjust + small_cell), 1)

        pygame.draw.line(screen, coral_color, (x + x_adjust, y + y_adjust + tile_adjust), (x + x_adjust + small_cell, y + y_adjust + small_cell + tile_adjust), 1)
        pygame.draw.line(screen, coral_color, (x + x_adjust + small_cell, y + y_adjust + tile_adjust), (x + x_adjust, y + y_adjust + small_cell + tile_adjust), 1)
        pygame.draw.line(screen, coral_color, (x + x_adjust, y + y_adjust + small_cell / 2 + tile_adjust), (x + x_adjust + small_cell, y + y_adjust + small_cell / 2 + tile_adjust), 1)
        pygame.draw.line(screen, coral_color, (x + x_adjust + small_cell / 2, y + y_adjust + tile_adjust), (x + x_adjust + small_cell / 2, y + y_adjust + small_cell + tile_adjust), 1)

        pygame.draw.line(screen, coral_color, (x + x_adjust + tile_adjust, y + y_adjust + tile_adjust), (x + x_adjust + small_cell + tile_adjust, y + y_adjust + small_cell + tile_adjust), 1)
        pygame.draw.line(screen, coral_color, (x + x_adjust + small_cell + tile_adjust, y + y_adjust + tile_adjust), (x + x_adjust + tile_adjust, y + y_adjust + small_cell + tile_adjust), 1)
        pygame.draw.line(screen, coral_color, (x + x_adjust + tile_adjust, y + y_adjust + small_cell / 2 + tile_adjust), (x + x_adjust + small_cell + tile_adjust, y + y_adjust + small_cell / 2 + tile_adjust), 1)
        pygame.draw.line(screen, coral_color, (x + x_adjust + small_cell / 2 + tile_adjust, y + y_adjust + tile_adjust), (x + x_adjust + small_cell / 2 + tile_adjust, y + y_adjust + small_cell + tile_adjust), 1)


def draw_sierpinski_triangle_coral(x, y, screen):
    '''
    Description: Draws a cell of coral with a Sierpinski triangle pattern.
    
    Input: The x and y of the cell that needs to be made into coral, the screen (global?)

    Output: None, performs the operation of drawing coral tiles. 
    '''
    def draw_triangle(screen, color, vertices):
        pygame.draw.polygon(screen, color, vertices)

    def sierpinski(screen, color, vertices, depth):
        if depth == 0:
            draw_triangle(screen, color, vertices)
        else:
            midpoints = [
                ((vertices[0][0] + vertices[1][0]) // 2, (vertices[0][1] + vertices[1][1]) // 2),
                ((vertices[1][0] + vertices[2][0]) // 2, (vertices[1][1] + vertices[2][1]) // 2),
                ((vertices[2][0] + vertices[0][0]) // 2, (vertices[2][1] + vertices[0][1]) // 2)
            ]
            sierpinski(screen, color, [vertices[0], midpoints[0], midpoints[2]], depth - 1)
            sierpinski(screen, color, [vertices[1], midpoints[0], midpoints[1]], depth - 1)
            sierpinski(screen, color, [vertices[2], midpoints[1], midpoints[2]], depth - 1)

    coral_1 = random.choice(coral_list)
    coral_2 = random.choice(coral_list)
    while coral_2 == coral_1:
        coral_2 = random.choice(coral_list)

    background_color = coral_1
    triangle_color = coral_2

    # Fill the background with the background color
    pygame.draw.rect(screen, background_color, pygame.Rect((x, y, CELL_SIZE, CELL_SIZE)))

    # Draw the Sierpinski triangles with the triangle color
    vertices = [(x, y + CELL_SIZE), (x + CELL_SIZE // 2, y), (x + CELL_SIZE, y + CELL_SIZE)]
    sierpinski(screen, triangle_color, vertices, 4)  # Adjust the depth as needed

def draw_symmetrical_fan_coral(x, y, screen):
    '''
    Description: Draws a cell of coral with a symmetrical fan pattern.
    
    Input: The x and y of the cell that needs to be made into coral, the screen (global?)

    Output: None, performs the operation of drawing coral tiles. 
    '''
    def draw_branch(screen, color, start_pos, length, angle, depth):
        if depth == 0:
            return

        end_pos = (
            start_pos[0] + int(length * pygame.math.Vector2(1, 0).rotate(angle).x),
            start_pos[1] + int(length * pygame.math.Vector2(1, 0).rotate(angle).y)
        )

        pygame.draw.line(screen, color, start_pos, end_pos, 2)

        new_length = length * 0.7
        new_depth = depth - 1
        draw_branch(screen, color, end_pos, new_length, angle - 30, new_depth)
        draw_branch(screen, color, end_pos, new_length, angle + 30, new_depth)

    coral_1 = random.choice(coral_list)
    coral_2 = random.choice(coral_list)
    while coral_2 == coral_1:
        coral_2 = random.choice(coral_list)

    background_color = coral_1
    branch_color = coral_2

    # Fill the background with the background color
    pygame.draw.rect(screen, background_color, pygame.Rect((x, y, CELL_SIZE, CELL_SIZE)))

    # Draw the symmetrical fan pattern
    start_pos = (x + CELL_SIZE // 2, y + CELL_SIZE)
    initial_length = CELL_SIZE // 4
    initial_angle = -90  # Start branches pointing upwards
    max_depth = 4

    draw_branch(screen, branch_color, start_pos, initial_length, initial_angle, max_depth)
    draw_branch(screen, branch_color, start_pos, initial_length, initial_angle - 45, max_depth)
    draw_branch(screen, branch_color, start_pos, initial_length, initial_angle + 45, max_depth)

def draw_symmetrical_fan_coral_2(x, y, screen):
    '''
    Description: Draws a cell of coral with a symmetrical fan pattern using three colors.
    
    Input: The x and y of the cell that needs to be made into coral, the screen (global?)

    Output: None, performs the operation of drawing coral tiles. 
    '''
    def draw_branch(screen, colors, start_pos, length, angle, depth):
        if depth == 0:
            return

        end_pos = (
            start_pos[0] + int(length * pygame.math.Vector2(1, 0).rotate(angle).x),
            start_pos[1] + int(length * pygame.math.Vector2(1, 0).rotate(angle).y)
        )

        color = next(colors)
        pygame.draw.line(screen, color, start_pos, end_pos, 2)

        new_length = length * 0.7
        new_depth = depth - 1
        draw_branch(screen, colors, end_pos, new_length, angle - 30, new_depth)
        draw_branch(screen, colors, end_pos, new_length, angle + 30, new_depth)

    coral_colors = random.sample(coral_list, 3)
    colors_cycle = cycle(coral_colors)

    background_color = next(colors_cycle)
    branch_color_1 = next(colors_cycle)
    branch_color_2 = next(colors_cycle)

    # Fill the background with the background color
    pygame.draw.rect(screen, background_color, pygame.Rect((x, y, CELL_SIZE, CELL_SIZE)))

    # Draw the symmetrical fan pattern with branching
    start_pos = (x + CELL_SIZE // 2, y + CELL_SIZE)
    initial_length = CELL_SIZE // 4
    initial_angle = -90  # Start branches pointing upwards
    max_depth = 5

    # Draw main branches
    draw_branch(screen, cycle([branch_color_1, branch_color_2]), start_pos, initial_length, initial_angle, max_depth)
    draw_branch(screen, cycle([branch_color_1, branch_color_2]), start_pos, initial_length, initial_angle - 45, max_depth)
    draw_branch(screen, cycle([branch_color_1, branch_color_2]), start_pos, initial_length, initial_angle + 45, max_depth)

import pygame
import random
from itertools import cycle

def draw_symmetrical_fan_coral_mirrored(x, y, screen):
    '''
    Description: Draws a cell of coral with a symmetrical fan pattern using three colors,
    and then mirrors the pattern vertically.
    
    Input: The x and y of the cell that needs to be made into coral, the screen (global?)

    Output: None, performs the operation of drawing coral tiles. 
    '''
    def draw_branch(screen, colors, start_pos, length, angle, depth):
        if depth == 0:
            return

        end_pos = (
            start_pos[0] + int(length * pygame.math.Vector2(1, 0).rotate(angle).x),
            start_pos[1] + int(length * pygame.math.Vector2(1, 0).rotate(angle).y)
        )

        color = next(colors)
        pygame.draw.line(screen, color, start_pos, end_pos, 2)

        new_length = length * 0.7
        new_depth = depth - 1
        draw_branch(screen, colors, end_pos, new_length, angle - 30, new_depth)
        draw_branch(screen, colors, end_pos, new_length, angle + 30, new_depth)

    coral_colors = random.sample(coral_list, 3)
    colors_cycle = cycle(coral_colors)

    background_color = next(colors_cycle)
    branch_color_1 = next(colors_cycle)
    branch_color_2 = next(colors_cycle)

    # Fill the background with the background color
    pygame.draw.rect(screen, background_color, pygame.Rect((x, y, CELL_SIZE, CELL_SIZE)))

    # Create a surface to draw the pattern
    pattern_surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
    pattern_surface.fill((0, 0, 0, 0))  # Make the surface transparent

    # Draw the symmetrical fan pattern with branching on the surface
    start_pos = (CELL_SIZE // 2, CELL_SIZE)
    initial_length = CELL_SIZE // 3
    initial_angle = -90  # Start branches pointing upwards
    max_depth = 4

    # Draw main branches
    draw_branch(pattern_surface, cycle([branch_color_1, branch_color_2]), start_pos, initial_length, initial_angle, max_depth)
    draw_branch(pattern_surface, cycle([branch_color_1, branch_color_2]), start_pos, initial_length, initial_angle - 45, max_depth)
    draw_branch(pattern_surface, cycle([branch_color_1, branch_color_2]), start_pos, initial_length, initial_angle + 45, max_depth)

    # Mirror the pattern vertically
    mirrored_surface = pygame.transform.flip(pattern_surface, False, True)

    # Blit both the original and mirrored patterns onto the screen
    screen.blit(pattern_surface, (x, y))
    screen.blit(mirrored_surface, (x, y + CELL_SIZE // 2))

def draw_unicursal_labyrinth_coral(x, y, screen):
    '''
    Description: Draws a cell of coral with a unicursal labyrinth pattern.
    
    Input: The x and y of the cell that needs to be made into coral, the screen (global?)

    Output: None, performs the operation of drawing coral tiles. 
    '''
    def create_unicursal_labyrinth(width, height):
        maze = [[0 for _ in range(width)] for _ in range(height)]
        x, y = width // 2, height // 2
        maze[y][x] = 1
        
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        
        stack = [(x, y)]
        
        while stack:
            cx, cy = stack[-1]
            found = False
            
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0:
                    if maze[cy + dy // 2][cx + dx // 2] == 0:
                        maze[cy + dy // 2][cx + dx // 2] = 1
                        maze[ny][nx] = 1
                        stack.append((nx, ny))
                        found = True
                        break
            
            if not found:
                stack.pop()
                
        return maze

    def draw_labyrinth(screen, color, x, y, cell_size, labyrinth):
        rows = len(labyrinth)
        cols = len(labyrinth[0])
        for i in range(rows):
            for j in range(cols):
                if labyrinth[i][j] == 1:
                    pygame.draw.rect(screen, color, pygame.Rect((x + j * cell_size, y + i * cell_size, cell_size, cell_size)))

    coral_1 = random.choice(coral_list)
    coral_2 = random.choice(coral_list)
    while coral_2 == coral_1:
        coral_2 = random.choice(coral_list)

    background_color = coral_1
    path_color = coral_2

    # Fill the background with the background color
    pygame.draw.rect(screen, background_color, pygame.Rect((x, y, CELL_SIZE, CELL_SIZE)))

    # Create and draw the unicursal labyrinth
    labyrinth = create_unicursal_labyrinth(16, 16)  # Adjust the size as needed
    draw_labyrinth(screen, path_color, x, y, CELL_SIZE // 16, labyrinth)

def draw_spiral_coral(x, y, screen):
    '''
    Description: Draws a spiral within a 32x32 pixel cell, using a gradient of coral colors.
    
    Input: The x and y of the cell that needs to be made into coral, the screen (global)

    Output: None, performs the operation of drawing coral tiles.
    '''
    def interpolate_color(color1, color2, t):
        """Interpolates between two colors."""
        return (
            int(color1[0] * (1 - t) + color2[0] * t),
            int(color1[1] * (1 - t) + color2[1] * t),
            int(color1[2] * (1 - t) + color2[2] * t)
        )

    coral_colors = random.sample(coral_list, 3)
    color_start = coral_colors[0]
    color_end = coral_colors[2]

    background_color = coral_colors[1]
    
    # Fill the background with the background color
    pygame.draw.rect(screen, background_color, pygame.Rect((x, y, CELL_SIZE, CELL_SIZE)))

    # Center of the cell
    center_x, center_y = x + CELL_SIZE // 2, y + CELL_SIZE // 2

    # Spiral parameters
    num_turns = 10
    max_radius = CELL_SIZE // 2
    num_segments = 200

    for i in range(num_segments):
        t = i / num_segments
        angle = num_turns * 2 * math.pi * t
        radius = max_radius * t
        color = interpolate_color(color_start, color_end, t)

        point_x = center_x + int(radius * math.cos(angle))
        point_y = center_y + int(radius * math.sin(angle))

        pygame.draw.circle(screen, color, (point_x, point_y), 2)

def draw_unicursal_labyrinth_coral_2(x, y, screen):
    '''
    Description: Draws a cell of coral with a unicursal labyrinth pattern and a gradient of coral colors.
    
    Input: The x and y of the cell that needs to be made into coral, the screen (global)

    Output: None, performs the operation of drawing coral tiles.
    '''
    def create_unicursal_labyrinth(width, height):
        maze = [[0 for _ in range(width)] for _ in range(height)]
        x, y = width // 2, height // 2
        maze[y][x] = 1
        
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        
        stack = [(x, y)]
        
        while stack:
            cx, cy = stack[-1]
            found = False
            
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0:
                    if maze[cy + dy // 2][cx + dx // 2] == 0:
                        maze[cy + dy // 2][cx + dx // 2] = 1
                        maze[ny][nx] = 1
                        stack.append((nx, ny))
                        found = True
                        break
            
            if not found:
                stack.pop()
                
        return maze

    def interpolate_color(color1, color2, t):
        """Interpolates between two colors."""
        return (
            int(color1[0] * (1 - t) + color2[0] * t),
            int(color1[1] * (1 - t) + color2[1] * t),
            int(color1[2] * (1 - t) + color2[2] * t)
        )

    coral_colors = random.sample(coral_list, 3)
    color_start = coral_colors[0]
    color_end = coral_colors[2]

    background_color = coral_colors[1]
    
    # Fill the background with the background color
    pygame.draw.rect(screen, background_color, pygame.Rect((x, y, CELL_SIZE, CELL_SIZE)))

    # Create and draw the unicursal labyrinth
    labyrinth = create_unicursal_labyrinth(16, 16)  # Adjust the size as needed
    
    # Draw the labyrinth with a gradient
    width, height = len(labyrinth[0]), len(labyrinth)
    cell_size = CELL_SIZE // max(width, height)
    path_points = [(i, j) for i in range(height) for j in range(width) if labyrinth[i][j] == 1]
    num_points = len(path_points)

    for index, (i, j) in enumerate(path_points):
        t = index / num_points
        color = interpolate_color(color_start, color_end, t)
        pygame.draw.rect(screen, color, pygame.Rect((x + j * cell_size, y + i * cell_size, cell_size, cell_size)))

def draw_sierpinski_triangle_coral_2(x, y, screen):
    '''
    Description: Draws a cell of coral with a Sierpinski triangle pattern using a gradient of coral colors.
    
    Input: The x and y of the cell that needs to be made into coral, the screen (global)

    Output: None, performs the operation of drawing coral tiles.
    '''
    def draw_triangle(screen, color, vertices):
        pygame.draw.polygon(screen, color, vertices)

    def sierpinski(screen, colors, vertices, depth, current_depth=0):
        if depth == 0:
            draw_triangle(screen, next(colors), vertices)
        else:
            midpoints = [
                ((vertices[0][0] + vertices[1][0]) // 2, (vertices[0][1] + vertices[1][1]) // 2),
                ((vertices[1][0] + vertices[2][0]) // 2, (vertices[1][1] + vertices[2][1]) // 2),
                ((vertices[2][0] + vertices[0][0]) // 2, (vertices[2][1] + vertices[0][1]) // 2)
            ]
            sierpinski(screen, colors, [vertices[0], midpoints[0], midpoints[2]], depth - 1, current_depth + 1)
            sierpinski(screen, colors, [vertices[1], midpoints[0], midpoints[1]], depth - 1, current_depth + 1)
            sierpinski(screen, colors, [vertices[2], midpoints[1], midpoints[2]], depth - 1, current_depth + 1)

    def interpolate_color(color1, color2, t):
        """Interpolates between two colors."""
        return (
            int(color1[0] * (1 - t) + color2[0] * t),
            int(color1[1] * (1 - t) + color2[1] * t),
            int(color1[2] * (1 - t) + color2[2] * t)
        )

    coral_colors = random.sample(coral_list, 3)
    color_start = coral_colors[0]
    color_end = coral_colors[2]

    background_color = coral_colors[1]
    
    # Fill the background with the background color
    pygame.draw.rect(screen, background_color, pygame.Rect((x, y, CELL_SIZE, CELL_SIZE)))

    # Draw the Sierpinski triangles with a gradient
    vertices = [(x, y + CELL_SIZE), (x + CELL_SIZE // 2, y), (x + CELL_SIZE, y + CELL_SIZE)]
    max_depth = 4  # Adjust the depth as needed

    colors = [interpolate_color(color_start, color_end, i / (3 ** max_depth)) for i in range(3 ** max_depth)]
    colors_cycle = cycle(colors)
    sierpinski(screen, colors_cycle, vertices, max_depth)
    
def draw_coral(x, y, screen):
   '''
   Description: Randomly selects between the coral drawing methods to make a coral tile.
   
   Input: The x and y of the cell that needs to be made into coral, the screen (global?)

   Output: None, performs the operation of drawing coral tiles.   
   '''
   coral_methods = [
      draw_rows_and_columns_coral,
      draw_fan_coral,
      draw_symmetrical_fan_coral_mirrored,
      draw_unicursal_labyrinth_coral_2,
      draw_sierpinski_triangle_coral_2
      ]
   random.choice(coral_methods)(x, y, screen)
         
def grow_algae():
   '''
   Description: Adds increasingly more algae to the map each level.
   
   Input: None, uses the global screen and CELL_SIZE variables.

   Output: None, performs the operation of drawing algae balls. (Should probably do something like make a list of cells that contain algae for easier interactions.)
   '''
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
   '''
   Description: Checks to see if a particular tile is sand.
   
   Input: The x and y of the tile in question. 

   Output: Returns True or False.
   '''
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
   '''
   Description: Moves Noodles around when the num pad is used by updating the nudi_x and nudi_y global variables.
   
   Input: The key pressed, the move_space is = CELL_SIZE, and nudi_x/nudi_y

   Output: A list of updated nudi_x and nudi_y. 
   '''
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
