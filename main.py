from pygame import *
from random import randint
from collect_data2 import collect_data
import joblib
import pandas as pd

model_data = joblib.load("my_smartpants.joblib")
bot = model_data['model']
features = model_data['feature_columns']

FPS = 60
PLAYER_SPEED = 5
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50

obstacle_speed = 3
is_game_over = False

window_size = 800, 600
window = display.set_mode(window_size)
clock = time.Clock()


def spawn_obstacle(count, obstacles):
    for _ in range(count):
        obstacles.append(
            Rect(randint(0, window_size[0] - OBSTACLE_SIZE),
                 randint(-600, -100),
                 OBSTACLE_SIZE, OBSTACLE_SIZE))
    return obstacles


player = Rect(window_size[0]//2, window_size[1]-PLAYER_SIZE, 50, 50)
obstacles = spawn_obstacle(5, [])

frame_count = 0

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
    keys = key.get_pressed()
    if not is_game_over:
        window.fill('light green')

        
        
        #'''
        obstacles.sort(key=lambda e: e.y, reverse=True)
        data = [{
            'p_x': player.x,
        }]

        for i in range(5):
            if i < len(obstacles):
                data[0][f'e_x{i}'] = obstacles[i].x
                data[0][f'e_y{i}'] = obstacles[i].y
                data[0][f'dist_x{i}'] = obstacles[i].x - player.x
                data[0][f'dist_y{i}'] = player.y - obstacles[i].y
            else:
                data[0][f'e_x{i}'] = -50
                data[0][f'e_y{i}'] = -10000
                data[0][f'dist_x{i}'] = -10000
                data[0][f'dist_y{i}'] = 10000
        state = pd.DataFrame(data) [features]

        action = bot.predict(state)[0]
        print(action)
        if action == "right" and player.x < window_size[0] - PLAYER_SIZE:
            player.x += PLAYER_SPEED
        if action == "left" and player.x > 0:
            player.x -= PLAYER_SPEED

        ''' 
        action = 'wait'

        if keys[K_d]:
            player.x += PLAYER_SPEED
            action = 'right'

        if keys[K_a]:
            player.x -= PLAYER_SPEED
            action = 'left'

        frame_count += 1

        if frame_count % 10 == 0:
            collect_data(player, obstacles, action)
        '''

        draw.rect(window, 'sky blue', player)

        for obstacle in obstacles[:]:
            obstacle.y += obstacle_speed
            draw.rect(window, 'red', obstacle)
            if obstacle.colliderect(player):
                is_game_over = True
            if obstacle.y >= window_size[1]:
                obstacles.remove(obstacle)
        if not obstacles: obstacles = spawn_obstacle(5, obstacles)

    if is_game_over:
        window.fill('red')
        if keys[K_r]:
            is_game_over = False
            obstacles = spawn_obstacle(5, [])
            player.x = 0

    display.update()
    clock.tick(FPS) 