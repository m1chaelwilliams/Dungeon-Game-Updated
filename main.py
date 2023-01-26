import pygame as py
import random as r

def draw_player(x):
    screen.blit(eval(x), p_rect)
def draw_level_count(level):
    level_text = font.render(str(level+1), False, (255,255,255))
    level_text_rect = level_text.get_rect(center = (400, 25))
    screen.blit(level_text, level_text_rect)
def draw_bullet_condition():
    bullet_condition_text = mini_font.render(str('bullet status = ' + bullet_condition), False, (255,255,255))
    bullet_condition_text_rect = bullet_condition_text.get_rect(center = (600,25))
    screen.blit(bullet_condition_text, bullet_condition_text_rect)
def update_player(x):
    if x == 'next':
        p_rect.x = 50
    else:
        p_rect.x = 700
def update_light(x):
    if x == 'next':
        light_rect.x = -100
    else:
        light_rect.x = 550
def draw_coin(x):
    if coin_status:
        pass
    else:
        screen.blit(coin_list[x], coin_rect)
def draw_enemy(x):
    if enemy_status:
        enemy_rect.y += x
    else:
        enemy_rect.y += x
        if abs(p_rect.x - enemy_rect.x) < 170 and abs(p_rect.y - enemy_rect.y) < 170:
            screen.blit(enemy, enemy_rect)
def update_coin():
    coin_coord = (r.randint(100,700),r.randint(100,700))
    return coin_coord
def update_enemy():
    enemy_coord = (r.randint(300,700),r.randint(100,700))
    return enemy_coord
def check_coin():
    if bullet_rect.colliderect(coin_rect):
        return True
    return False
def check_enemy():
    if bullet_rect.colliderect(enemy_rect):
        return True
    return False
def draw_dirt(x, num1, num2):
    screen.blit(dirt_list[x], (p_rect.x +num1, p_rect.y + num2))
def fire_weapon():
    if player_direction == 'player_right':
        bullet_rect.x += bullet_vel
    elif player_direction == 'player_left':
        bullet_rect.x -= bullet_vel
    elif player_direction == 'player_up':
        bullet_rect.y -= bullet_vel
    elif player_direction == 'player_down':
        bullet_rect.y += bullet_vel
def draw_weapon():
    screen.blit(bullet, bullet_rect)
def bullet_wall_collision():
    global bullet_condition
    if bullet_rect.y > 750:
        bullet_condition = 'loaded'
        return True
    elif bullet_rect.y < 50:
        bullet_condition = 'loaded'
        return True
    return False
def update_bullet_count(count):
    x = 0
    for a in range(count):
        screen.blit(menu_bullet, (menu_bullet_rect.x +x, menu_bullet_rect.y))
        x += 50
def start_game():
    global level
    global latest_level
    global bullet_count
    global tut_timer
    global bullet_condition
    global coin_status
    global p_rect
    global bullet_rect
    global light_rect
    
    coin_status = False
    p_rect.center = (400,400)
    bullet_rect.center = p_rect.center
    light_rect.center = p_rect.center
    coin_rect.center = (600, 400)
    level = 0
    latest_level = 0
    bullet_count = 3
    tut_timer = 0
    bullet_condition = 'loaded'
def check_enemy_wall_collision(x):
    if enemy_rect.colliderect(wall1_rect):
        return -1 * x
    elif enemy_rect.colliderect(wall2_rect):
        return -1 * x
    return x
def check_player():
    if p_rect.colliderect(enemy_rect):
        if level > 0:
            return True
    return False
def update_bullet_condition():
    global bullet_condition
    bullet_condition = 'loaded'
def draw_plus_one():
    screen.blit(plus_one, plus_one_rect)

py.init()
screen = py.display.set_mode((800,800))
py.display.set_caption('Dungeon Traveller Game')
clock = py.time.Clock()

# game status

game_status = 'start'

# background
background = py.transform.scale(py.image.load('background.png').convert(), (800,800))
bg_rect = background.get_rect(center = (400,400))

# cover

cover = py.transform.scale(py.image.load('cover.png').convert(), (800,800))
cover_rect = cover.get_rect(center = (400,400))
# walls

hor_wall = py.transform.scale(py.image.load('block.png').convert(), (800, 50))
ver_wall = py.transform.scale(py.image.load('block.png').convert(), (50, 350))

wall1_rect = hor_wall.get_rect(center = (400, 25))
wall2_rect = hor_wall.get_rect(center = (400, 775))

# player

player_right = py.transform.scale(py.image.load('player/sprite_0.png').convert_alpha(), (50,50))
player_up = py.transform.scale(py.image.load('player/sprite_1.png').convert_alpha(), (50,50))
player_left = py.transform.scale(py.image.load('player/sprite_2.png').convert_alpha(), (50,50))
player_down = py.transform.scale(py.image.load('player/sprite_3.png').convert_alpha(), (50,50))
p_rect = player_right.get_rect(center = (400,400))

player_direction = 'player_right'

# enemy

enemy = py.transform.scale(py.image.load('enemy.png').convert_alpha(), (50,50))
#enemy_rect = enemy.get_rect(center = (r.randint(50,750), r.randint(50,750)))
enemy_rect = enemy.get_rect(center = (600, 200))

enemy_status = True

enemy_collision = 'top'

# coin

coin0 = py.transform.scale(py.image.load('coin/coin_0.png').convert_alpha(), (50,50))
coin1 = py.transform.scale(py.image.load('coin/coin_1.png').convert_alpha(), (50,50))
coin2 = py.transform.scale(py.image.load('coin/coin_2.png').convert_alpha(), (50,50))
coin_list = [coin0, coin1, coin2]
coin_index = 0
coin_rect = coin1.get_rect(center = (600, 400))

coin_status = False

# dirt

dirt0 = py.transform.scale(py.image.load('dirt/dirt_0.png').convert_alpha(), (50,50))
dirt1 = py.transform.scale(py.image.load('dirt/dirt_1.png').convert_alpha(), (50,50))
dirt2 = py.transform.scale(py.image.load('dirt/dirt_2.png').convert_alpha(), (50,50))
dirt_list = [dirt0,dirt1,dirt2]
dirt_index = 0
dirt_rect = dirt0.get_rect(center = p_rect.center)

# light circle

light = py.transform.scale(py.image.load('light circle.png').convert_alpha(), (350,350))
light_rect = light.get_rect(center = p_rect.center)
# enemy

enemy = py.transform.scale(py.image.load('enemy.png').convert(), (50,50))
enemy_rect = enemy.get_rect()

enemy_direction = 1

# bullet

bullet = py.transform.scale(py.image.load('bullet.png').convert(), (20,20))
bullet_rect = bullet.get_rect(center = p_rect.center)
bullet_vel = 2
hit_status = False
fire_status = False

bullet_count = 3

bullet_condition = 'loaded'

# menu bullets

menu_bullet = py.transform.scale(py.image.load('bullet.png').convert(), (40,20))
menu_bullet_rect = menu_bullet.get_rect(center = (100,25))

# door hitboxes

door = py.transform.scale(py.image.load('door.png').convert(), (50,800))
door1_rect = door.get_rect(center = (800, 400))
door2_rect = door.get_rect(center = (0, 400))

# level counter

level = 0
latest_level = level

# text

font = py.font.Font('ARCADECLASSIC.ttf', 50)
start_font = py.font.Font('ARCADECLASSIC.ttf', 100)
mini_font = py.font.Font('ARCADECLASSIC.ttf', 25)

# +1 asset

plus_one = mini_font.render('plus 1', False, (255,255,255))
plus_one_rect = plus_one.get_rect(center = (100,200))

# timer for tutorial text

tut_timer = 0

while True:
    #screen.blit(background, bg_rect)
    screen.fill('black')
    screen.blit(light, light_rect)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
    
    key = py.key.get_pressed()
    if game_status == 'running':
        if coin_status == False and p_rect.colliderect(door1_rect):
            pass
        else:

            if key[py.K_RIGHT]:
                p_rect.x += 5
                light_rect.x += 5
                player_direction = 'player_right'
                draw_dirt(int(dirt_index), -50, 0)
                if dirt_index < 2.95:
                    dirt_index += 0.05
                else:
                    dirt_index = 0
        if level == 0 and p_rect.colliderect(door2_rect):
            pass
        else:
            if key[py.K_LEFT]:
                p_rect.x -= 5
                light_rect.x -= 5
                player_direction = 'player_left'
                draw_dirt(int(dirt_index), 50, 0)
                if dirt_index < 2.95:
                    dirt_index += 0.05
                else:
                    dirt_index = 0
        if p_rect.colliderect(wall1_rect) == False:
            if key[py.K_UP]:
                p_rect.y -= 5
                light_rect.y -= 5
                player_direction = 'player_up'
                draw_dirt(int(dirt_index), 0, 50)
                if dirt_index < 2.95:
                    dirt_index += 0.05
                else:
                    dirt_index = 0
        if p_rect.colliderect(wall2_rect) == False:
            if key[py.K_DOWN]:
                p_rect.y += 5
                light_rect.y += 5
                player_direction = 'player_down'
                draw_dirt(int(dirt_index), 0, -50)
                if dirt_index < 2.95:
                    dirt_index += 0.05
                else:
                    dirt_index = 0

        if fire_status == False:
            if key[py.K_SPACE]:
                bullet_rect.center = p_rect.center
                fire_status = True
                bullet_condition = 'active'
                bullet_count -= 1
        else:
            if key[py.K_r]:
                fire_status = False
                bullet_rect.center = p_rect.center
                fire_status = False
                update_bullet_condition()

    else:
        if key[py.K_RETURN]:
            tut_timer = 0
            start_game()
            game_status = 'running'
    
    # checking collisions

    enemy_direction = check_enemy_wall_collision(enemy_direction)

    if check_player():
        if enemy_status == False:
            game_status = 'gameover'
    if check_enemy():
        if enemy_status == False:
            bullet_count += 1
            bullet_rect.center = p_rect.center
            fire_status = False
            update_bullet_condition()
        enemy_status = True

        
    if check_coin():
        if coin_status == False:
            bullet_rect.center = p_rect.center
            fire_status = False
            update_bullet_condition()
        coin_status = True

    if p_rect.colliderect(door1_rect):
        if coin_status:
            level += 1
            latest_level = level
            update_player('next')
            update_light('next')
            coin_coord = update_coin()
            coin_rect.center = coin_coord
            enemy_coord = update_enemy()
            enemy_rect.center = enemy_coord
            coin_status = False
            enemy_status = False

            if bullet_rect.x > 800:
                bullet_rect.x -= 800
            else:
                bullet_rect.x = -(800-bullet_rect.x)
        elif latest_level > level:
            update_player('next')
            update_light('next')
            level += 1
            if bullet_rect.x > 800:
                bullet_rect.x -= 800
            else:
                bullet_rect.x = -(800-bullet_rect.x)



    if p_rect.colliderect(door2_rect):
        if level > 0:
            level -= 1
            update_player('previous')
            update_light('previous')


    
    #screen.blit(door, door1_rect)
    #screen.blit(door, door2_rect)

    if bullet_wall_collision():
        fire_status = False
        if bullet_count == 0:
            game_status = 'gameover'
            

    if fire_status:
        fire_weapon()
        draw_weapon()     

    
    if latest_level == level:
        if abs(p_rect.x - coin_rect.x) < 170 and abs(p_rect.y - coin_rect.y) < 170:
            draw_coin(int(coin_index))
            if coin_index < 2.95:
                coin_index += 0.05
            else:
                coin_index = 0

        if abs(p_rect.x - plus_one_rect.x) < 170 and abs(p_rect.y - plus_one_rect.y) < 170:
            if level > 0:
                draw_plus_one()
        if level == 0 and bullet_condition == 'loaded':
            draw_enemy(enemy_direction)
    screen.blit(hor_wall, wall1_rect)
    screen.blit(hor_wall, wall2_rect)
    draw_player(player_direction)
    draw_level_count(level)
    draw_bullet_condition()
    update_bullet_count(bullet_count)

    if bullet_count < 0:
        game_status = 'gameover'

    # game status conditions

    if game_status == 'start':
        screen.blit(cover, cover_rect)
        start_text = start_font.render('Dungeon', False, (255,255,255))
        start_text_rect = start_text.get_rect(center = (400,300))
        start_text2 = start_font.render('Adventure', False, (255,255,255))
        start_text_rect2 = start_text2.get_rect(center = (400,400))
        start_text3 = font.render('Press Enter to start', False, (255,255,255))
        start_text_rect3 = start_text3.get_rect(center = (400,500))
        screen.blit(start_text, start_text_rect)
        screen.blit(start_text2, start_text_rect2)
        screen.blit(start_text3, start_text_rect3)
    
    if game_status == 'running':
        tut_timer += 0.008
        if tut_timer < 5:
            tut_text = mini_font.render('collect coins by pressing space', False, (255,255,255))
            tut_text_rect = tut_text.get_rect(center = (400,200))
            screen.blit(tut_text, tut_text_rect)

    if game_status == 'gameover':
        screen.blit(cover, cover_rect)
        start_text = start_font.render('Game', False, (255,255,255))
        start_text_rect = start_text.get_rect(center = (400,300))
        start_text2 = start_font.render('Over', False, (255,255,255))
        start_text_rect2 = start_text2.get_rect(center = (400,400))
        start_text3 = font.render('Press Enter to Restart', False, (255,255,255))
        start_text_rect3 = start_text3.get_rect(center = (400,500))
        screen.blit(start_text, start_text_rect)
        screen.blit(start_text2, start_text_rect2)
        screen.blit(start_text3, start_text_rect3)


    py.display.update()
    clock.tick(120)