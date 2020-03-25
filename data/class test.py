import math
 
BULLET_SPEED=2
start_x = 0
start_y = 400
dest_x = 600
dest_y = 500
x_diff = dest_x - start_x
y_diff = dest_y - start_y
angle = math.atan2(y_diff, x_diff)
bulletcenter_x = start_x
bulletcenter_y = start_y
                
bulletchange_x = math.cos(angle) * BULLET_SPEED
bulletchange_y = math.sin(angle) * BULLET_SPEED

print(bulletchange_x)
print(bulletchange_y)



        
