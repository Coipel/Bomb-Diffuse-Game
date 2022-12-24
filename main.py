#import wire_module as wm
import bomb_module as bm

def main():
    bomb = bm.Bomb(1)
    bomb.setup_modules()
    bomb.play()

if __name__ == '__main__':
    main()