# importiruetsya neobhodimie biblioteki
import os
import random
import time

# zadaem visotu i shirinu igrovogo polya v yacheikah
WIDTH, HEIGHT = 20, 10

# funktsiya ochistki ekrana,gde uslovie true or false.
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# funktsiya igrovogo polya s parametrami snake i food
def draw_board(snake, food):
    # funktsiya ochistki ekrana
    clear_screen()
    # sozdaem stroki igrovogo polya s dvumya dopolnitelnimi yacheikami dlya otrisovki gorizontalnih granits
    for y in range(HEIGHT + 2):
        # sozdaem yacheiki v strokah
        for x in range(WIDTH + 2):
            # yacheiki granits
            if y == 0 or y == HEIGHT + 1 or x == 0 or x == WIDTH + 1:
                # pechataem symbol yacheiki(#), ukazivaya chto symbol perenosa stroki (end) doljen otsutstvovat'
                print("#", end="")
            # risuem yacheiki snake(█) imeya vvidu chto pervii symbol kajdoi stroki i pervaya stroka ne yavlyautsya chast'u polya, a granitsami polya
            elif (x - 1, y - 1) in snake:
                print("█", end="")
            # risuem yacheiki food(*) imeya vvidu chto pervii symbol kajdoi stroki i pervaya stroka ne yavlyautsya chast'u polya, a granitsami polya
            # dopustim food imeet koordinati x=4,y=3 (nado schitat' s levoi vverhnei stroki), i eti koordinati budut schitat'sya s granitsei vmeste,
            # to est' nachinaya s reshetki, poetomu nado minusovat' x-1,y-1
            elif (x - 1, y - 1) == food:
                print("*", end="")
            else:
                # pechataem pustuyu yacheiku polya s pomosh'u probela, to est' ostal'naya pustota krome food i snake
                print(" ", end="")
        # perehodim k sleduushei stroke ispolzuya po umolchaniyu end=\n
        print()
    # pechataem score
    # {len(snake)-1} - zdes' dlina snake minus odin, tak kak pri nachale igri snake uje imeet odnu yacheiku, a score=0,poetomu munisuem odnu yacheiku 
    print(f"SCORE: {len(snake) - 1}")

# funktsiya generatsii polojeniya food s isklucheniem (iskluchaem koordinati snake, to est' sovpadeniya koordinat snake i food)
def generate_food_position(exluded_list):
    # food poyavlyaetsya randomno v igrovom pole
    food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    # esli food v excluded list (v dannom sluchae v polojenii koordinat snake, 63 stroka)
    if food in exluded_list:
        # esli food popadet v polojenie koordinat snake, to napechataetsya wrong food: "food"
        print(f"wrong_food: {food}")
        # rekursiya. probuem eshe raz sgenerirovat' koordinati food
        food = generate_food_position(exluded_list)
    # vipolnyaetsya snova food randomno
    return food

# osnovnaya funktsiya igri
def snake_game():
    # obyavlyaem knopki napravleniy
    DIRECTION_KEYS = {"w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}
    # ustanavlivaem startovie koordinati pervoi yacheiki snake v seredine polya
    snake = [(WIDTH // 2, HEIGHT // 2)]
    # ustanavlivaem startovoe napravlenie(+1 po x)
    direction = (1, 0)
    # ustanavlivaem startovie koordinati food randomno (skormili snake v funktsiyu generate_food_position(snake))
    food = generate_food_position(snake)


    # loop(tsikl)
    while True:
        # funktciya igrovogo polya s parametrami snake i food
        draw_board(snake, food)
        # strip obrezaet(ubiraet) probeli s obeih storon (vdrug esli sluchaino)
        cmd = input("wasd: ").strip()
        # funktsiya get daet dvijenie snake ishodya chto napechatal v input"wasd:"
        direction = DIRECTION_KEYS.get(cmd, direction)

        # opredelyaem koordinati novogo polojeniya golovi soglasno najatoi klavishi 
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        # pribavlyaem novuyu golovu udalyaya poslednyuyu yacheiku hvosta imitiruya dvijenie
        snake = [new_head] + snake[:-1]
        
        if (
            # proveryaem sushestvuet li v spiske koordinat yacheek snake takie je koordinati kak u novoi golovi, ne uchitivaya koordinati samoi golovi 
            new_head in snake[1:]
            # stolknovenie s levoi ili pravoi granitsami
            or new_head[0] < 0 or new_head[0] >= WIDTH
            # stolknovenie s vverhnei ili nijnei granitsami
            or new_head[1] < 0 or new_head[1] >= HEIGHT
        ):
            # risuem poslednee polojenie igrovogo polya s parametrami snake i food
            draw_board(snake, food)
            # pechataem "game over"
            print("game over")
            # zakonchili tsikl
            break

        # esli golova popala v polojenie food
        if new_head == food:
            # append - ego zadacha dobavit' v konets snake odnu yacheiku
            snake.append(snake[-1])
            # to food randomno poyavlyaetsya v igrovom pole iskluchaya snake
            food = generate_food_position(snake)
    
        # vremya zaderjki shaga zmeiki
        time.sleep(0.3)

# zapuskaem igru
snake_game()

