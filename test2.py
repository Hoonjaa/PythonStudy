from pico2d import *


open_canvas()

player = load_image('character.png')
grass = load_image('grass.png')
animation = load_image('run_animation.png')

dis = 0
frame = 0

while dis < 800:
    clear_canvas_now()
    grass. draw_now(400,30)
    animation.clip_draw(frame * 100,0,100,100,dis,90)

    update_canvas()
    frame = (frame + 1) % 8
    dis += 5
    delay(0.05)


close_canvas()


# Pivot 피붓
