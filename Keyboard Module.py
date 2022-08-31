import pygame

def init():
    pygame.init()
    window=pygame.display.set_mode(resolution=(400,400)

    def getkey(keyName):
        answer=False
        for event in pygame.event.get(): pass
        keyInput=pygame.key.get_pressed()
        mykey=getattr(pygame,'k_{}'.format(keyName))
        if keyInput[mykey]:
            answer=True
        pygame.display.update()

        return answer

def main():
    if getkey("LEFT"):
        Print("left key pressed")
    if getkey("RIGHT"):
        print("right key pressed")

if __name__ == "__main__":
    init()
    while True:
        main()