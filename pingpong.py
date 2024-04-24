from pygame import*
init()

back = (200,255,255)
win_width=600
win_heigth = 500
window = display.set_mode((win_width,win_heigth))
background = transform.scale(image.load('ping.jpg'),(win_width,win_heigth))
window. fill(back)
game = True

clock = time.Clock()
FPS = 60

while game: 
    for e in event.get(): 
        if e.type==QUIT: 
            game = False
    window.blit(background,(0,0))
    display.update()
    clock.tick(FPS)