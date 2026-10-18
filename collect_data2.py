import csv

def collect_data(player, enemies, action):
    num_of_enemies = 5 
    if not enemies:
        return

    enemies.sort(key=lambda enemy: enemy.y, reverse=True)

    row = [player.x]

    for i in range(num_of_enemies):
        if i < len(enemies):
            e = enemies[i]
            row.extend([
                e.x,
                e.y,
                e.x - player.x,
                player.y - e.y
            ])
        else:
            row.extend([-50, -10000, -10000, 10000])

    row.append(action)

    

    file = open('game_data2.csv', 'a', newline='')

    writer = csv.writer(file)

    if file.tell() == 0:

        header = ['p_x']

        for i in range(num_of_enemies):
            header.extend([
                f'e_x{i}',
                f'e_y{i}',
                f'dist_x{i}',
                f'dist_y{i}'
                           ])

        header.append('action')

        writer.writerow(header)

    writer.writerow(row)

    