from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
background = load_image('TUK_GROUND.png')
grass = load_image('grass.png')
animation = load_image('animation_sheet.png')

def handle_events():
    global running
    global x,y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:     #이벤트 x, y는 윈도우 api != pico2d좌표
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
frame = 0
x, y = TUK_WIDTH/2, TUK_HEIGHT/2
hide_cursor()

while running:
    clear_canvas()
    background.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    animation.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    handle_events()

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()