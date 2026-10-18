import random
import csv

def generate_situsation():
    p_x = random.randint(0, 750)
    p_y = 50
    e_x = random.randint(0, 750)
    e_y = random.randint(0 ,600)
    dist_x = e_x - p_x
    dist_y = p_y - e_y
    action = 'wait'

    if 50 > dist_x > 0:
        action = 'left'
    elif dist_x < 0 and dist_x > -50: 
        action = 'right'
    else:
        action = 'wait'

    if p_x <= 0 and action=="left":
        action = "right"
    if p_x + 50 >= 800 and action == "right":
        action = "left" 

    file = open('generated_data.csv', 'a', newline='')
    
    writer = csv.writer(file)
    
    if file.tell() == 0:
        writer.writerow([
                'p_x',
                'e_x',
                'e_y',
                'dist_x',
                'dist_y',
                'action'
            ])
    
    writer.writerow([
        p_x,
        e_x,
        e_y,
        dist_x,
        dist_y,
        action
    ])


for _ in range(1500):
    generate_situsation()