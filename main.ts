namespace SpriteKind {
    export const NPC = SpriteKind.create()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Cursor.overlapsWith(Tile0) && TicTacToe[0][0] == "-") {
        mySprite = sprites.create(assets.image`SnowyForest`, SpriteKind.Player)
        if (TicTacToePlayer == 0) {
            Tile0.setImage(assets.image`X`)
            TicTacToePlayer = 1
            TicTacToe[0][0] = "X"
        } else {
            Tile0.setImage(assets.image`O`)
            TicTacToePlayer = 0
            TicTacToe[0][0] = "O"
        }
    } else if (Cursor.overlapsWith(Tile1) && TicTacToe[0][1] == "-") {
        if (TicTacToePlayer == 0) {
            Tile1.setImage(assets.image`X`)
            TicTacToePlayer = 1
            TicTacToe[0][1] = "X"
        } else {
            Tile1.setImage(assets.image`O`)
            TicTacToePlayer = 0
            TicTacToe[0][1] = "O"
        }
    } else if (Cursor.overlapsWith(Tile2) && TicTacToe[0][2] == "-") {
        if (TicTacToePlayer == 0) {
            Tile2.setImage(assets.image`X`)
            TicTacToePlayer = 1
            TicTacToe[0][2] = "X"
        } else {
            Tile2.setImage(assets.image`O`)
            TicTacToePlayer = 0
            TicTacToe[0][2] = "O"
        }
    } else if (Cursor.overlapsWith(Tile3) && TicTacToe[1][0] == "-") {
        if (TicTacToePlayer == 0) {
            Tile3.setImage(assets.image`X`)
            TicTacToePlayer = 1
            TicTacToe[1][0] = "X"
        } else {
            Tile3.setImage(assets.image`O`)
            TicTacToePlayer = 0
            TicTacToe[1][0] = "O"
        }
    } else if (Cursor.overlapsWith(Tile4) && TicTacToe[1][1] == "-") {
        if (TicTacToePlayer == 0) {
            Tile4.setImage(assets.image`X`)
            TicTacToePlayer = 1
            TicTacToe[1][1] = "X"
        } else {
            Tile4.setImage(assets.image`O`)
            TicTacToePlayer = 0
            TicTacToe[1][1] = "O"
        }
    } else if (Cursor.overlapsWith(Tile5) && TicTacToe[1][2] == "-") {
        if (TicTacToePlayer == 0) {
            Tile5.setImage(assets.image`X`)
            TicTacToePlayer = 1
            TicTacToe[1][2] = "X"
        } else {
            Tile5.setImage(assets.image`O`)
            TicTacToePlayer = 0
            TicTacToe[1][2] = "O"
        }
    } else if (Cursor.overlapsWith(Tile6) && TicTacToe[2][0] == "-") {
        if (TicTacToePlayer == 0) {
            Tile6.setImage(assets.image`X`)
            TicTacToePlayer = 1
            TicTacToe[2][0] = "X"
        } else {
            Tile6.setImage(assets.image`O`)
            TicTacToePlayer = 0
            TicTacToe[2][0] = "O"
        }
    } else if (Cursor.overlapsWith(Tile7) && TicTacToe[2][1] == "-") {
        if (TicTacToePlayer == 0) {
            Tile7.setImage(assets.image`X`)
            TicTacToePlayer = 1
            TicTacToe[2][1] = "X"
        } else {
            Tile7.setImage(assets.image`O`)
            TicTacToePlayer = 0
            TicTacToe[2][1] = "O"
        }
    } else if (Cursor.overlapsWith(Tile8) && TicTacToe[2][2] == "-") {
        if (TicTacToePlayer == 0) {
            Tile8.setImage(assets.image`X`)
            TicTacToePlayer = 1
            TicTacToe[2][2] = "X"
        } else {
            Tile8.setImage(assets.image`O`)
            TicTacToePlayer = 0
            TicTacToe[2][2] = "O"
        }
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Nola.overlapsWith(Dream)) {
        sprites.destroy(Dream)
        Board5 = sprites.create(assets.image`Board`, SpriteKind.Projectile)
        Board5.setScale(3.5, ScaleAnchor.Middle)
        Board5.setPosition(75, 55)
        Cursor = sprites.create(assets.image`Cursed`, SpriteKind.Player)
        Cursor.setPosition(75, 70)
        Cursor.z = 1
        animation.runImageAnimation(
        Cursor,
        assets.animation`Cursor`,
        500,
        true
        )
        controller.moveSprite(Cursor)
        sprites.destroy(Nola)
        Tile0 = sprites.create(assets.image`Tile`, SpriteKind.Enemy)
        Tile0.setPosition(54, 34)
        Tile1 = sprites.create(assets.image`Tile`, SpriteKind.Enemy)
        Tile1.setPosition(75, 34)
        Tile2 = sprites.create(assets.image`Tile`, SpriteKind.Enemy)
        Tile2.setPosition(96, 34)
        Tile3 = sprites.create(assets.image`Tile`, SpriteKind.Enemy)
        Tile3.setPosition(54, 55)
        Tile4 = sprites.create(assets.image`Tile`, SpriteKind.Enemy)
        Tile4.setPosition(75, 55)
        Tile5 = sprites.create(assets.image`Tile`, SpriteKind.Enemy)
        Tile5.setPosition(96, 55)
        Tile6 = sprites.create(assets.image`Tile`, SpriteKind.Enemy)
        Tile6.setPosition(54, 76)
        Tile7 = sprites.create(assets.image`Tile`, SpriteKind.Enemy)
        Tile7.setPosition(75, 76)
        Tile8 = sprites.create(assets.image`Tile`, SpriteKind.Enemy)
        Tile8.setPosition(96, 76)
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    Nola.setImage(assets.image`nola0`)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    Nola.setImage(assets.image`nola`)
})
let interactionCount = 0
let Board5: Sprite = null
let mySprite: Sprite = null
let Tile8: Sprite = null
let Tile7: Sprite = null
let Tile6: Sprite = null
let Tile5: Sprite = null
let Tile4: Sprite = null
let Tile3: Sprite = null
let Tile2: Sprite = null
let Tile1: Sprite = null
let Tile0: Sprite = null
let Cursor: Sprite = null
let Dream: Sprite = null
let TicTacToe: string[][] = []
let TicTacToePlayer = 0
let Nola: Sprite = null
scene.setBackgroundImage(assets.image`rogers house`)
Nola = sprites.create(assets.image`nola`, SpriteKind.Player)
let Roger = sprites.create(assets.image`roger`, SpriteKind.NPC)
Nola.setPosition(28, 91)
Roger.setPosition(136, 91)
controller.moveSprite(Nola, 50, 50)
Nola.z = 1
TicTacToePlayer = 0
TicTacToe = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
let dialogueBank = ["Do you have my dream yet? Yes?  Thank you, mouse man!", "DIET PEPSI! You've fetched me my dream! In return, I will grant you three wishes. Just kidding, heh heh.", "Without dreams, this meager helping of life is nought but an all-consuming void of empty and ebony. My heart yearns for salvation, I hunger for dreams. Thank you for finding me my reverie, jerk."]
music.setVolume(20)
music.play(music.createSong(assets.song`basic track`), music.PlaybackMode.LoopingInBackground)
Dream = sprites.create(img`
    8 
    `, SpriteKind.Food)
Dream.setPosition(0, 0)
forever(function () {
    if (Roger.overlapsWith(Nola)) {
        interactionCount = interactionCount + 1
        if (interactionCount == 1) {
            music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.UntilDone)
            game.showLongText("I'm Roger, and I love trash! Ya know what else I love??? Having dreams. But ever since our dreams were severed from us, everything has just felt pointless. I need you to help me find my dream, mister dreamcatcher!", DialogLayout.Center)
        }
        pause(800)
        if (interactionCount == 2) {
            game.showLongText("Will you catch my dream for me?        Yes! = press A", DialogLayout.Center)
        }
        if (interactionCount == 3) {
            scene.cameraShake(4, 500)
            effects.starField.startScreenEffect()
            scene.setBackgroundImage(assets.image`SnowyForest`)
            Roger.setImage(img`
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
                `)
            Dream.setImage(assets.image`Dream`)
            Dream.setPosition(75, 55)
            pause(500)
            music.stopAllSounds()
            game.showLongText("You made it to the forest! Now it's time to find Roger's dream and bring it home. To use your dreamcatcher net, press B. Be careful, though. Dreams are tricky things, and they're known for challenging people to games like tic tac toe.", DialogLayout.Center)
        }
    }
})
