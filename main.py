from bomb_module import Bomb

def main():
    bomb = Bomb(60)
    bomb.setup_modules(5)
    bomb.play()

if __name__ == '__main__':
    main()