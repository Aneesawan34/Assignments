alien={'x_position': 0,'y_position': 25,'speed': 'medium'}
print("orignal x_position: " + str(alien['x_position']))
print("\n")
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien['x_position'] = alien['x_position'] + x_increment
print("Now x_position: " + str(alien['x_position']))