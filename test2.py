from pico2d import *


open_canvas()

player = load_image('character.png')
grass = load_image('grass.png')


dis = 0

while dis < 800:
    clear_canvas_now()
    grass. draw_now(400,30)
    player.draw_now(dis,90)


    
    dis += 5
    delay(0.05)


close_canvas()


# Pivot 피붓
