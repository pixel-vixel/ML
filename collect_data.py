import csv

def collect_data(player, enemies, action):
    if not enemies:
        return

    nearest_enemy = max(enemies, key=lambda enemy: enemy.y)

    file = open('game_data.csv', 'a', newline='')

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
        player.x,
        nearest_enemy.x,
        nearest_enemy.y,
        nearest_enemy.x - player.x,
        player.y - nearest_enemy.y,
        action
    ])