@namespace
class SpriteKind:
    NPC = SpriteKind.create()

def on_b_pressed():
    global TicTacToePlayer
    if Tic == 1:
        if Cursor.overlaps_with(Tile0) and Board3[0][0] == "-":
            if TicTacToePlayer == 1:
                Tile0.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                Board3[0][0] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
        elif Cursor.overlaps_with(Tile1) and Board3[0][1] == "-":
            if TicTacToePlayer == 1:
                Tile1.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                Board3[0][1] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
        elif Cursor.overlaps_with(Tile2) and Board3[0][2] == "-":
            if TicTacToePlayer == 1:
                Tile2.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                Board3[0][2] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
        elif Cursor.overlaps_with(Tile3) and Board3[1][0] == "-":
            if TicTacToePlayer == 1:
                Tile3.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                Board3[1][0] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
        elif Cursor.overlaps_with(Tile4) and Board3[1][1] == "-":
            if TicTacToePlayer == 1:
                Tile4.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                Board3[1][1] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
        elif Cursor.overlaps_with(Tile5) and Board3[1][2] == "-":
            if TicTacToePlayer == 1:
                Tile5.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                Board3[1][2] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
        elif Cursor.overlaps_with(Tile6) and Board3[2][0] == "-":
            if TicTacToePlayer == 1:
                Tile6.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                Board3[2][0] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
        elif Cursor.overlaps_with(Tile7) and Board3[2][1] == "-":
            if TicTacToePlayer == 1:
                Tile7.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                Board3[2][1] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
        elif Cursor.overlaps_with(Tile8) and Board3[2][2] == "-":
            if TicTacToePlayer == 1:
                Tile8.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                Board3[2][2] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def CheckOver(Board2: List[List[str]]):
    if Board2[0][0] == "X" and Board2[0][1] == "X" and Board2[0][2] == "X":
        return 1
    if Board2[1][0] == "X" and Board2[1][1] == "X" and Board2[1][2] == "X":
        return 1
    if Board2[2][0] == "X" and Board2[2][1] == "X" and Board2[2][2] == "X":
        return 1
    if Board2[0][0] == "X" and Board2[0][0] == "X" and Board2[2][0] == "X":
        return 1
    if Board2[0][1] == "X" and Board2[1][1] == "X" and Board2[2][1] == "X":
        return 1
    if Board2[0][2] == "X" and Board2[1][2] == "X" and Board2[2][2] == "X":
        return 1
    if Board2[0][2] == "X" and Board2[1][1] == "X" and Board2[2][0] == "X":
        return 1
    if Board2[0][0] == "X" and Board2[1][1] == "X" and Board2[2][2] == "X":
        return 1
    if Board2[0][0] == "O" and Board2[0][1] == "O" and Board2[0][2] == "O":
        return -1
    if Board2[1][0] == "O" and Board2[1][1] == "O" and Board2[1][2] == "O":
        return -1
    if Board2[2][0] == "O" and Board2[2][1] == "O" and Board2[2][2] == "O":
        return -1
    if Board2[0][0] == "O" and Board2[0][0] == "O" and Board2[2][0] == "O":
        return -1
    if Board2[0][1] == "O" and Board2[1][1] == "O" and Board2[2][1] == "O":
        return -1
    if Board2[0][2] == "O" and Board2[1][2] == "O" and Board2[2][2] == "O":
        return -1
    if Board2[0][2] == "O" and Board2[1][1] == "O" and Board2[2][0] == "O":
        return -1
    if Board2[0][0] == "O" and Board2[1][1] == "O" and Board2[2][2] == "O":
        return -1
    for row in Board2:
        for elem in row:
            if elem == "-":
                return 2
    return 0

def on_a_pressed():
    global Board5, Cursor, Tile0, Tile1, Tile2, Tile3, Tile4, Tile5, Tile6, Tile7, Tile8
    animation.run_image_animation(Nola, assets.animation("""
        action0
    """), 120, False)
    if Nola.overlaps_with(Dream):
        animation.run_image_animation(Nola, assets.animation("""
            action0
        """), 120, False)
        pause(1080)
        sprites.destroy(Dream)
        Board5 = sprites.create(assets.image("""
            Board
        """), SpriteKind.projectile)
        Board5.set_scale(3.5, ScaleAnchor.MIDDLE)
        Board5.set_position(75, 55)
        Cursor = sprites.create(assets.image("""
            Cursed
        """), SpriteKind.player)
        Cursor.set_position(75, 70)
        Cursor.z = 1
        animation.run_image_animation(Cursor, assets.animation("""
            Cursor
        """), 500, True)
        controller.move_sprite(Cursor)
        sprites.destroy(Nola)
        Tile0 = sprites.create(assets.image("""
            X
        """), SpriteKind.enemy)
        Tile0.set_position(54, 34)
        Tile1 = sprites.create(assets.image("""
            Tile
        """), SpriteKind.enemy)
        Tile1.set_position(75, 34)
        Tile2 = sprites.create(assets.image("""
            Tile
        """), SpriteKind.enemy)
        Tile2.set_position(96, 34)
        Tile3 = sprites.create(assets.image("""
            Tile
        """), SpriteKind.enemy)
        Tile3.set_position(54, 55)
        Tile4 = sprites.create(assets.image("""
            Tile
        """), SpriteKind.enemy)
        Tile4.set_position(75, 55)
        Tile5 = sprites.create(assets.image("""
            Tile
        """), SpriteKind.enemy)
        Tile5.set_position(96, 55)
        Tile6 = sprites.create(assets.image("""
            Tile
        """), SpriteKind.enemy)
        Tile6.set_position(54, 76)
        Tile7 = sprites.create(assets.image("""
            Tile
        """), SpriteKind.enemy)
        Tile7.set_position(75, 76)
        Tile8 = sprites.create(assets.image("""
            Tile
        """), SpriteKind.enemy)
        Tile8.set_position(96, 76)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    Nola.set_image(assets.image("""
        nola0
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    Nola.set_image(assets.image("""
        nola
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

interactionCount = 0
Board5: Sprite = None
mySprite: Sprite = None
Tile8: Sprite = None
Cursor: Sprite = None
Tic = 0
Dream: Sprite = None
Board3: List[List[str]] = []
TicTacToePlayer = 1
Nola: Sprite = None
Tile0: Sprite = None
Tile1: Sprite = None
Tile2: Sprite = None
Tile3: Sprite = None
Tile4: Sprite = None
Tile5: Sprite = None
Tile6: Sprite = None
Tile7: Sprite = None
def Actions(Board: List[List[str]]):
    Acts = []
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            if Board[i][j] == "-":
                Acts.append([i, j])
    return Acts
def Test(Board: List[List[str]]):
    Acts = []
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            if Board[i][j] == "-":
                Acts.append([i, j])
    return Acts
def MaxValue(Board: List[List[str]]):
    if CheckOver(Board) != 2:
        return CheckOver(Board)
    
    Value = -2
    for Act in Actions(Board):
        Value = max(Value, MinValue(Result(Board, Act, "X")))
    return Value

def MinValue(Board: List[List[str]]):
    if CheckOver(Board) != 2:
        return CheckOver(Board)
    Value = 2
    for Act in Actions(Board):
        Value = min(Value, MinValue(Result(Board, Act, "O")))
    return Value

def MiniMax(Board: List[List[str]]):
    Values = []
    Location = 0
    Acts = Actions(Board)
    BestValue = -2
    for Act in Acts:
        Values.append(MinValue(Result(Board, Act, "X")))
    for i in range(len(Values)):
        if Values[i] > BestValue:
            BestValue = Values[i]
            Location = i
    return Acts[Location]

def Result(Board4: List[List[str]], Action: List[int], Player: str):
    CopyBoard = []
    for row in Board4:
        CopyBoard.append(row[:])
    CopyBoard[Action[0]][Action[1]] = Player
    return CopyBoard

def PlaceTile(Location2: List[int]):
    if Location2[0] == [0, 0][0] and Location2[1] == [0, 0][1]:
        Tile0.set_image(assets.image("""
            X
        """))
        Board3[0][0] = "X"
    if Location2[0] == [0, 1][0] and Location2[1] == [0, 1][1]:
        Tile1.set_image(assets.image("""
            X
        """))
        Board3[0][1] = "X"
    if Location2[0] == [0, 2][0] and Location2[1] == [0, 2][1]:
        Tile2.set_image(assets.image("""
            X
        """))
        Board3[0][2] = "X"
    if Location2 == Location2[0] == [1, 0][0] and Location2[1] == [1, 0][1]:
        Tile3.set_image(assets.image("""
            X
        """))
        Board3[1][0] = "X"
    if Location2 == Location2[0] == [1, 1][0] and Location2[1] == [1, 1][1]:
        Tile4.set_image(assets.image("""
            X
        """))
        Board3[1][1] = "X"
    if Location2[0] == [1, 2][0] and Location2[1] == [1, 2][1]:
        Tile5.set_image(assets.image("""
            X
        """))
        Board3[1][2] = "X"
    if Location2[0] == [2, 0][0] and Location2[1] == [2, 0][1]:
        Tile6.set_image(assets.image("""
            X
        """))
        Board3[2][0] = "X"
    if Location2[0] == [2, 1][0] and Location2[1] == [2, 1][1]:
        Tile7.set_image(assets.image("""
            X
        """))
        Board3[2][1] = "X"
    if Location2[0] == [2,2][0] and Location2[1] == [2, 2][1]:
        Tile8.set_image(assets.image("""
            X
        """))
        Board3[2][2] = "X"
scene.set_background_image(assets.image("""
    rogers house
"""))
Nola = sprites.create(assets.image("""
    nola
"""), SpriteKind.player)
Roger = sprites.create(assets.image("""
    roger
"""), SpriteKind.NPC)
Nola.set_position(28, 91)
Roger.set_position(136, 91)
controller.move_sprite(Nola, 50, 50)
Nola.z = 1
TicTacToePlayer = 1
Board3 = [["X", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
dialogueBank = ["Do you have my dream yet? Yes?  Thank you, mouse man!",
    "DIET PEPSI! You've fetched me my dream! In return, I will grant you three wishes. Just kidding, heh heh.",
    "Without dreams, this meager helping of life is nought but an all-consuming void of empty and ebony. My heart yearns for salvation, I hunger for dreams. Thank you for finding me my reverie, jerk."]

Dream = sprites.create(img("""
    8
"""), SpriteKind.food)
Dream.set_position(0, 0)
Tic = 0
music.set_volume(20)
music.play(music.create_song(assets.song("""
        basic track
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
    
def on_forever():
    global interactionCount, Tic
    Nola.set_position(Nola.x, 91)
    if Roger.overlaps_with(Nola):
        interactionCount = interactionCount + 1
        if interactionCount == 1:
            music.play(music.melody_playable(music.ba_ding),
                music.PlaybackMode.UNTIL_DONE)
            game.show_long_text("I'm Roger, and I love trash! Ya know what else I love??? Having dreams. But ever since our dreams were severed from us, everything has just felt pointless. I need you to help me find my dream, mister dreamcatcher!",
                DialogLayout.CENTER)
        pause(800)
        if interactionCount == 2:
            game.show_long_text("Will you catch my dream for me?        Yes! = press A",
                DialogLayout.CENTER)
        if interactionCount == 3:
            scene.camera_shake(4, 500)
            effects.star_field.start_screen_effect()
            scene.set_background_image(assets.image("""
                SnowyForest
            """))
            Roger.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
            """))
            Dream.set_image(assets.image("""
                Dream
            """))
            Dream.set_position(75, 55)
            pause(500)
            music.stop_all_sounds()
            Tic = 1
            game.show_long_text("You made it to the forest! Now it's time to find Roger's dream and bring it home. To use your dreamcatcher net, press B. Be careful, though. Dreams are tricky things, and they're known for challenging people to games like tic tac toe.",
                DialogLayout.CENTER)
forever(on_forever)
