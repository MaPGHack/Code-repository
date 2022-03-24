<<<<<<< Updated upstream
from operator import truediv
import random
import pygame
from pygame. locals import*
import sys


FPS = 32
scr-width = 289
scr-height = 511
display-screen-window = pygame.display.set_mode((scr_width, scr_height))
play_ground = scr_height * 0.8
game_image = {}
game_audio_sound = {}
player = "images/bird.png"
bcg_image = "images/background.png"
pipe_image = "images/pipe.png"

def welcome_main_screen():
    p_x = int(scr_width / 5)
    p_y = int((scr_height - game_image['player'].get_height()) / 2)
    msgx = int((scr_width - game_image['message'].get_width()) / 2)
    msgy = int(scr_height * 0.13)
    b_x = 0

    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, colse the game_audio_sound
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

#If the user presses space or up key, start th game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                display_screen_window.blit(game_image['background'], (0,0))
                display_screen_window.blit(game_image['player'], (p_x, p_y))
                display_screen_window.blit(game_image['message'], (msgx, msgy))
                display_screen_window.blit(game_image[ ], (b_x, play_ground))
                pygame.display.update()
                time_clock.tick(FPS)

def main_gameplay():
    score = 0
    p_x = int(scr_width / 5)
    p_y = int(scr_width / 2)
    b_x = 0


n_pip1 = get_Random_Pipes()
n_pip2 = get_Random-Pipes()


up_pips = [
{'x': scr_width + 200, 'y': n_pip1[0]['y']},
{'x': scr_width + 200 + (scr_width / 2), 'y': n_pip2[0]['y']},
]

low_pips = [
{'x': scr_width + 200, 'y': n_pip1[1]['y']},
{'x': scr_width + 200 + (scr_width / 2), 'y': n_pip2[1]['y']},
]

pip-Vx = -4

p_vx = -9
p_mvx = 10
p_mvy = -8
p_accuracy = 1

p_flap_accuracy =-8
p_flap = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
            if p_y &gt; 0:
                p_vx = p_flap_accuracy
                p_flap = True
                "game_adudio_sound[ ].play()"

cr_tst = is_Colliding(p_x, p_y, up_pips,
low_pips)
if cr_tst:
    return


p_middle_positions = p_x + game_image['player'].get_width() / 2
for pipe in up_pips:
    pip_middle_positions = pipe['x'] + game_image['pipe'][0].get_width() / 2
if pip_middle_positions &lt;= p_middle_positions &lt; pip_middle_positions + 4:
    score += 1
    print(f"Your score is {score}")
    "game_audio_sound[ ].play()"

if p_vx &lt; p_mvx and not p_p_flap:
    p_vx += p_accuracy

if p_flap:
    p_flap = False
    p_height = game_image['player'].get_height()
    p_y = p_y + min(p_vx, play_ground - p_y - p_height)

for pip_upper, pip_lower in zip(up_pips, low_pips):
    pip_upper['x'] += pip_Vx
    pip_lower['x'] += pip_Vx

if 0 &lt; up_pips[0]['x'] &lt; 5:
    new_pip = get_Random_Pipes()
    up_pips.append(new_pip[0])
    low_pips.append(new_pip[1])


if up_pips[0]['x'] &lt; -game_image['pipe'][0].get_width():
    up_pips.pop(0)
    low_pips.pop(0)


display_screen_window.blitz(game_image['background'], (0,0))
for pip_upper, pip_lower in zip(up_pips,low_pips):
    display_screen_window.blit(game_image['pipe'][0], (pip_upper['x'], pip_upper['y']))
    display_screen_window.blit(game_image['pipe'][1], (pip_lower['x'], pip_lower['y']))


display_screen_window.blit(game_image['base'],(b_x, play_ground) )
display_screen.window.blit(game_image^['player'], (p_x, p_y))
d = [int(x) for x in list(str(score))]
w = 0
for digit in d:
    w += game_image['numbers'][digit].get_width()
    Xoffset = (scr_width - w) / 2

for digit in d:
    display_screen_window.blit(game_image['numbers'][digit], (Xoffset, scr_height * 0.12))
    Xoffset += game_image['numbers'][digit].get_width()
    pygame.display.update()
    time_clock.tick(FPS)

def is_Colliding(p_x, p_y, up_pipes, low_pipes):
    if p_y &gt; play_ground - 25 or p_y &LT; 0:
        game_audio_sound['hit'].play()
        return True

for pipe in up_pipes:
    pip_h = game_image['pipe'][0].get_height()
    if (p_y &lt; pip_h + pipe['y'] and abs(p_x - pipe['x']) &lt; game_image['pipe'][0].get_width())



if __name__ == "__main__":
    main()












=======
from operator import truediv
import random
import pygame
from pygame. locals import*
import sys


FPS = 32
scr-width = 289
scr-height = 511
display-screen-window = pygame.display.set_mode((scr_width, scr_height))
play_ground = scr_height * 0.8
game_image = {}
game_audio_sound = {}
player = "images/bird.png"
bcg_image = "images/background.png"
pipe_image = "images/pipe.png"

def welcome_main_screen():
    p_x = int(scr_width / 5)
    p_y = int((scr_height - game_image['player'].get_height()) / 2)
    msgx = int((scr_width - game_image['message'].get_width()) / 2)
    msgy = int(scr_height * 0.13)
    b_x = 0

    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, colse the game_audio_sound
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

#If the user presses space or up key, start th game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                display_screen_window.blit(game_image['background'], (0,0))
                display_screen_window.blit(game_image['player'], (p_x, p_y))
                display_screen_window.blit(game_image['message'], (msgx, msgy))
                display_screen_window.blit(game_image[ ], (b_x, play_ground))
                pygame.display.update()
                time_clock.tick(FPS)

def main_gameplay():
    score = 0
    p_x = int(scr_width / 5)
    p_y = int(scr_width / 2)
    b_x = 0


n_pip1 = get_Random_Pipes()
n_pip2 = get_Random-Pipes()


up_pips = [
{'x': scr_width + 200, 'y': n_pip1[0]['y']},
{'x': scr_width + 200 + (scr_width / 2), 'y': n_pip2[0]['y']},
]

low_pips = [
{'x': scr_width + 200, 'y': n_pip1[1]['y']},
{'x': scr_width + 200 + (scr_width / 2), 'y': n_pip2[1]['y']},
]

pip-Vx = -4

p_vx = -9
p_mvx = 10
p_mvy = -8
p_accuracy = 1

p_flap_accuracy =-8
p_flap = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
            if p_y &gt; 0:
                p_vx = p_flap_accuracy
                p_flap = True
                "game_adudio_sound[ ].play()"

cr_tst = is_Colliding(p_x, p_y, up_pips,
low_pips)
if cr_tst:
    return


p_middle_positions = p_x + game_image['player'].get_width() / 2
for pipe in up_pips:
    pip_middle_positions = pipe['x'] + game_image['pipe'][0].get_width() / 2
if pip_middle_positions &lt;= p_middle_positions &lt; pip_middle_positions + 4:
    score += 1
    print(f"Your score is {score}")
    "game_audio_sound[ ].play()"

if p_vx &lt; p_mvx and not p_p_flap:
    p_vx += p_accuracy

if p_flap:
    p_flap = False
    p_height = game_image['player'].get_height()
    p_y = p_y + min(p_vx, play_ground - p_y - p_height)

for pip_upper, pip_lower in zip(up_pips, low_pips):
    pip_upper['x'] += pip_Vx
    pip_lower['x'] += pip_Vx

if 0 &lt; up_pips[0]['x'] &lt; 5:
    new_pip = get_Random_Pipes()
    up_pips.append(new_pip[0])
    low_pips.append(new_pip[1])


if up_pips[0]['x'] &lt; -game_image['pipe'][0].get_width():
    up_pips.pop(0)
    low_pips.pop(0)


display_screen_window.blitz(game_image['background'], (0,0))
for pip_upper, pip_lower in zip(up_pips,low_pips):
    display_screen_window.blit(game_image['pipe'][0], (pip_upper['x'], pip_upper['y']))
    display_screen_window.blit(game_image['pipe'][1], (pip_lower['x'], pip_lower['y']))


display_screen_window.blit(game_image['base'],(b_x, play_ground) )
display_screen.window.blit(game_image^['player'], (p_x, p_y))
d = [int(x) for x in list(str(score))]
w = 0
for digit in d:
    w += game_image['numbers'][digit].get_width()
    Xoffset = (scr_width - w) / 2

for digit in d:
    display_screen_window.blit(game_image['numbers'][digit], (Xoffset, scr_height * 0.12))
    Xoffset += game_image['numbers'][digit].get_width()
    pygame.display.update()
    time_clock.tick(FPS)

def is_Colliding(p_x, p_y, up_pipes, low_pipes):
    if p_y &gt; play_ground - 25 or p_y &LT; 0:
        game_audio_sound['hit'].play()
        return True

for pipe in up_pipes:
    pip_h = game_image['pipe'][0].get_height()
    if (p_y &lt; pip_h + pipe['y'] and abs(p_x - pipe['x']) &lt; game_image['pipe'][0].get_width())



if __name__ == "__main__":
    main()












>>>>>>> Stashed changes
