from pico2d import *

grass = load_image('grass.png')
animation = load_image('animation_sheet.png')

running = True

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

frame = 0

for x in range(0,800, 10):
    clear_canvas()
    grass.draw(400,30)
    animation.clip_composite_draw(frame * 100, 100, 100,100,x, 90)
    update_canvas()

    handle_events()
    if not running:
        break

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()