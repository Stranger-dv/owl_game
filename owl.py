import os
import keyboard

maps = {
     "level_1":[
     [".",".","#",".",".","."],
     ["#",".",".","#","b","."],
     [".",".",".",".",".","d"],
     [".","d","#",".","#","."],
     ["#",".","b",".","b","."],
     ["#",".",".",".","d","."],
    ],      
     "level_2":[
     [".","d","#",".","b","."],
     ["#",".",".","#",".","d"],
     [".","b",".",".",".","."],
     [".",".","#",".","#","."],
     ["#","#",".",".",".","d"],
     ["#",".",".","b",".","."],

    ],      
     "level_3":[
     [".",".","#",".",".","."],
     ["#","d",".","#","b","."],
     ["b",".",".",".",".","."],
     [".",".","#","d","#","b"],
     ["#","#",".",".",".","."],
     ["#",".",".",".","d","."],
    ],       
}

levels = {
    1 : "level_1",
    2 : "level_2",
    3 : "level_3",
}
# map = [
#     [".",".","#",".",".","."],
#     ["#",".",".","#","f","."],
#     [".",".",".",".",".","."],
#     [".",".","#",".","#","."],
#     ["#",".","f",".","f","."],
#     ["#",".",".",".",".","."],
# ]

new_level = 1
size_rows = len(maps[levels[new_level]])
size_cols = len(maps[levels[new_level]][0])
avatar_y = 1
avatar_x = 1
counting_bones = 0
counting_diamonds = 0


def fn_clear_map(): #
    os.system("cls" if os.name == "nt" else "clear")

def fn_render_map():
    fn_clear_map()
    for rows in maps[levels[new_level]]:
        tiles = []
        for cols in rows:
            if cols == ".":
               tiles.append("⬜")
            if cols == "#":
               tiles.append("♏")
            if cols == "@":
               tiles.append("🦉")
            if cols == "b":
               tiles.append("🦴")
            if cols == "d":
               tiles.append("💎")
            if cols == "g":
               tiles.append("🎁")
        print(" ".join(tiles))
    print(f"Level {new_level}")
    print(f"Huesos recogidos: {counting_bones}")
    print(f"Diamantes recogidos: {counting_diamonds}")

def fn_move_avatar(): #
    global avatar_x, avatar_y, counting_bones, new_level, counting_diamonds
    new_x = avatar_x
    new_y = avatar_y

    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "w":
               new_y -= 1
            elif event.name == "s":
               new_y += 1
            elif event.name == "a":
               new_x -= 1
            elif event.name == "d":
               new_x += 1
            elif event.name == "q":
            #    print("Juego terminado")
               break
            if (new_x >= 0 and new_x <= size_rows and new_y >= 0 and new_y <= size_cols and maps[levels[new_level]][new_y][new_x] != "#"):
                maps[levels[new_level]][avatar_y][avatar_x] = "."
                avatar_x = new_x
                avatar_y = new_y
                if maps[levels[new_level]][avatar_y][avatar_x] == "b":
                    counting_bones += 1
                if maps[levels[new_level]][avatar_y][avatar_x] == "d":
                    counting_diamonds += 1
                if counting_bones == 3 and counting_diamonds == 3:
                    fn_render_map()
                    break
                        
                maps[levels[new_level]][avatar_y][avatar_x] = "@"
            else:
                new_x = avatar_x
                new_y = avatar_y
            fn_render_map()


def fn_star_game():
    global counting_bones, counting_diamonds, new_level
    player_answer = input("Bienvenido a tu juego personal, quieres jugar y o n: ")
    if player_answer == "y":
        new_level = 1
        while new_level <= 3:
            fn_render_map()
            counting_bones = 0
            fn_move_avatar()
            if new_level < 3:
                answer = input("Deseas continuar: ")
                if answer == "y":
                    new_level += 1
                    counting_bones = 0
                    counting_diamonds = 0
                elif answer == "n":
                    break
            elif new_level == 3:
                print("Ganaste!!!")
                break
    else:
        print("En otra ocacion")

if __name__ == "__main__":
    fn_star_game()
#     fn_render_map()
#     fn_move_avatar()
