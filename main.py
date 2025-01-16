@namespace
class SpriteKind:
    NPC = SpriteKind.create()

def on_b_pressed():
    global mySprite, TicTacToePlayer
    if Tic == 1:
        if Cursor.overlaps_with(Tile0) and TicTacToe[0][0] == "-":
            mySprite = sprites.create(assets.image("""
                SnowyForest
            """), SpriteKind.player)
            if TicTacToePlayer == 0:
                Tile0.set_image(assets.image("""
                    X
                """))
                TicTacToePlayer = 1
                TicTacToe[0][0] = "X"
            else:
                Tile0.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                TicTacToe[0][0] = "O"
        elif Cursor.overlaps_with(Tile1) and TicTacToe[0][1] == "-":
            if TicTacToePlayer == 0:
                Tile1.set_image(assets.image("""
                    X
                """))
                TicTacToePlayer = 1
                TicTacToe[0][1] = "X"
            else:
                Tile1.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                TicTacToe[0][1] = "O"
        elif Cursor.overlaps_with(Tile2) and TicTacToe[0][2] == "-":
            if TicTacToePlayer == 0:
                Tile2.set_image(assets.image("""
                    X
                """))
                TicTacToePlayer = 1
                TicTacToe[0][2] = "X"
            else:
                Tile2.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                TicTacToe[0][2] = "O"
        elif Cursor.overlaps_with(Tile3) and TicTacToe[1][0] == "-":
            if TicTacToePlayer == 0:
                Tile3.set_image(assets.image("""
                    X
                """))
                TicTacToePlayer = 1
                TicTacToe[1][0] = "X"
            else:
                Tile3.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                TicTacToe[1][0] = "O"
        elif Cursor.overlaps_with(Tile4) and TicTacToe[1][1] == "-":
            if TicTacToePlayer == 0:
                Tile4.set_image(assets.image("""
                    X
                """))
                TicTacToePlayer = 1
                TicTacToe[1][1] = "X"
            else:
                Tile4.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                TicTacToe[1][1] = "O"
        elif Cursor.overlaps_with(Tile5) and TicTacToe[1][2] == "-":
            if TicTacToePlayer == 0:
                Tile5.set_image(assets.image("""
                    X
                """))
                TicTacToePlayer = 1
                TicTacToe[1][2] = "X"
            else:
                Tile5.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                TicTacToe[1][2] = "O"
        elif Cursor.overlaps_with(Tile6) and TicTacToe[2][0] == "-":
            if TicTacToePlayer == 0:
                Tile6.set_image(assets.image("""
                    X
                """))
                TicTacToePlayer = 1
                TicTacToe[2][0] = "X"
            else:
                Tile6.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                TicTacToe[2][0] = "O"
        elif Cursor.overlaps_with(Tile7) and TicTacToe[2][1] == "-":
            if TicTacToePlayer == 0:
                Tile7.set_image(assets.image("""
                    X
                """))
                TicTacToePlayer = 1
                TicTacToe[2][1] = "X"
            else:
                Tile7.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                TicTacToe[2][1] = "O"
        elif Cursor.overlaps_with(Tile8) and TicTacToe[2][2] == "-":
            if TicTacToePlayer == 0:
                Tile8.set_image(assets.image("""
                    X
                """))
                TicTacToePlayer = 1
                TicTacToe[2][2] = "X"
            else:
                Tile8.set_image(assets.image("""
                    O
                """))
                TicTacToePlayer = 0
                TicTacToe[2][2] = "O"
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def MaxValue(Board2: List[any]):
    pass
def Actions(Board4: List[any]):
    Actions = []
    for i in range(len(Board4)):
        for j in range(len(Board4[j])):
            if Board4 == "-":
                Actions.append([i, j])
    return Actions
    
def on_a_pressed():
    global Board52, Cursor, Tile0, Tile1, Tile2, Tile3, Tile4, Tile5, Tile6, Tile7, Tile8
    animation.run_image_animation(Nola, assets.animation("""
        action0
    """), 120, False)
    if Nola.overlaps_with(Dream):
        animation.run_image_animation(Nola, assets.animation("""
            action0
        """), 120, False)
        pause(1080)
        sprites.destroy(Dream)
        Board52 = sprites.create(assets.image("""
            Board
        """), SpriteKind.projectile)
        Board52.set_scale(3.5, ScaleAnchor.MIDDLE)
        Board52.set_position(75, 55)
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

def Minimax(Board3: List[any], Player: number):
    pass

def on_right_pressed():
    Nola.set_image(assets.image("""
        nola
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def CheckBoard(Board5: List[any]):
    pass
interactionCount = 0
Board52: Sprite = None
mySprite: Sprite = None
Tile8: Sprite = None
Tile7: Sprite = None
Tile6: Sprite = None
Tile5: Sprite = None
Tile4: Sprite = None
Tile3: Sprite = None
Tile2: Sprite = None
Tile1: Sprite = None
Tile0: Sprite = None
Cursor: Sprite = None
Tic = 0
Dream: Sprite = None
TicTacToe: List[List[str]] = []
TicTacToePlayer = 0
Nola: Sprite = None
Value = 0
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
TicTacToe = [["X", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
dialogueBank = ["Do you have my dream yet? Yes?  Thank you, mouse man!",
    "DIET PEPSI! You've fetched me my dream! In return, I will grant you three wishes. Just kidding, heh heh.",
    "Without dreams, this meager helping of life is nought but an all-consuming void of empty and ebony. My heart yearns for salvation, I hunger for dreams. Thank you for finding me my reverie, jerk."]
music.set_volume(20)
music.play(music.create_song(assets.song("""
        basic track
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
Dream = sprites.create(img("""
    8
"""), SpriteKind.food)
Dream.set_position(0, 0)
Tic = 0

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
