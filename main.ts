namespace SpriteKind {
    export const NPC = SpriteKind.create()
}

controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    
    if (Tic == 1) {
        if (Cursor.overlapsWith(Tile0) && Board3[0][0] == "-") {
            if (TicTacToePlayer == 1) {
                Tile0.setImage(assets.image`
                    O
                `)
                TicTacToePlayer = 0
                Board3[0][0] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
            }
            
        } else if (Cursor.overlapsWith(Tile1) && Board3[0][1] == "-") {
            if (TicTacToePlayer == 1) {
                Tile1.setImage(assets.image`
                    O
                `)
                TicTacToePlayer = 0
                Board3[0][1] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
            }
            
        } else if (Cursor.overlapsWith(Tile2) && Board3[0][2] == "-") {
            if (TicTacToePlayer == 1) {
                Tile2.setImage(assets.image`
                    O
                `)
                TicTacToePlayer = 0
                Board3[0][2] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
            }
            
        } else if (Cursor.overlapsWith(Tile3) && Board3[1][0] == "-") {
            if (TicTacToePlayer == 1) {
                Tile3.setImage(assets.image`
                    O
                `)
                TicTacToePlayer = 0
                Board3[1][0] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
            }
            
        } else if (Cursor.overlapsWith(Tile4) && Board3[1][1] == "-") {
            if (TicTacToePlayer == 1) {
                Tile4.setImage(assets.image`
                    O
                `)
                TicTacToePlayer = 0
                Board3[1][1] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
            }
            
        } else if (Cursor.overlapsWith(Tile5) && Board3[1][2] == "-") {
            if (TicTacToePlayer == 1) {
                Tile5.setImage(assets.image`
                    O
                `)
                TicTacToePlayer = 0
                Board3[1][2] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
            }
            
        } else if (Cursor.overlapsWith(Tile6) && Board3[2][0] == "-") {
            if (TicTacToePlayer == 1) {
                Tile6.setImage(assets.image`
                    O
                `)
                TicTacToePlayer = 0
                Board3[2][0] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
            }
            
        } else if (Cursor.overlapsWith(Tile7) && Board3[2][1] == "-") {
            if (TicTacToePlayer == 1) {
                Tile7.setImage(assets.image`
                    O
                `)
                TicTacToePlayer = 0
                Board3[2][1] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
            }
            
        } else if (Cursor.overlapsWith(Tile8) && Board3[2][2] == "-") {
            if (TicTacToePlayer == 1) {
                Tile8.setImage(assets.image`
                    O
                `)
                TicTacToePlayer = 0
                Board3[2][2] = "O"
                PlaceTile(MiniMax(Board3))
                TicTacToePlayer = 1
            }
            
        }
        
    }
    
    if (CheckOver(Board3) == 1) {
        game.gameOver(false)
    }
    
    if (CheckOver(Board3) == 0) {
        game.gameOver(true)
    }
    
})
function CheckOver(Board2: string[][]): number {
    if (Board2[0][0] == "X" && Board2[0][1] == "X" && Board2[0][2] == "X") {
        return 1
    }
    
    if (Board2[1][0] == "X" && Board2[1][1] == "X" && Board2[1][2] == "X") {
        return 1
    }
    
    if (Board2[2][0] == "X" && Board2[2][1] == "X" && Board2[2][2] == "X") {
        return 1
    }
    
    if (Board2[0][0] == "X" && Board2[1][0] == "X" && Board2[2][0] == "X") {
        return 1
    }
    
    if (Board2[0][1] == "X" && Board2[1][1] == "X" && Board2[2][1] == "X") {
        return 1
    }
    
    if (Board2[0][2] == "X" && Board2[1][2] == "X" && Board2[2][2] == "X") {
        return 1
    }
    
    if (Board2[0][2] == "X" && Board2[1][1] == "X" && Board2[2][0] == "X") {
        return 1
    }
    
    if (Board2[0][0] == "X" && Board2[1][1] == "X" && Board2[2][2] == "X") {
        return 1
    }
    
    if (Board2[0][0] == "O" && Board2[0][1] == "O" && Board2[0][2] == "O") {
        return -1
    }
    
    if (Board2[1][0] == "O" && Board2[1][1] == "O" && Board2[1][2] == "O") {
        return -1
    }
    
    if (Board2[2][0] == "O" && Board2[2][1] == "O" && Board2[2][2] == "O") {
        return -1
    }
    
    if (Board2[0][0] == "O" && Board2[0][0] == "O" && Board2[2][0] == "O") {
        return -1
    }
    
    if (Board2[0][1] == "O" && Board2[1][1] == "O" && Board2[2][1] == "O") {
        return -1
    }
    
    if (Board2[0][2] == "O" && Board2[1][2] == "O" && Board2[2][2] == "O") {
        return -1
    }
    
    if (Board2[0][2] == "O" && Board2[1][1] == "O" && Board2[2][0] == "O") {
        return -1
    }
    
    if (Board2[0][0] == "O" && Board2[1][1] == "O" && Board2[2][2] == "O") {
        return -1
    }
    
    for (let row of Board2) {
        for (let elem of row) {
            if (elem == "-") {
                return 2
            }
            
        }
    }
    return 0
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    animation.runImageAnimation(Nola, assets.animation`
        action0
    `, 120, false)
    if (Nola.overlapsWith(Dream)) {
        animation.runImageAnimation(Nola, assets.animation`
            action0
        `, 120, false)
        pause(1080)
        sprites.destroy(Dream)
        Board5 = sprites.create(assets.image`
            Board
        `, SpriteKind.Projectile)
        Board5.setScale(3.5, ScaleAnchor.Middle)
        Board5.setPosition(75, 55)
        Cursor = sprites.create(assets.image`
            Cursed
        `, SpriteKind.Player)
        Cursor.setPosition(75, 70)
        Cursor.z = 1
        animation.runImageAnimation(Cursor, assets.animation`
            Cursor
        `, 500, true)
        controller.moveSprite(Cursor)
        sprites.destroy(Nola)
        Tile0 = sprites.create(assets.image`
            X
        `, SpriteKind.Enemy)
        Tile0.setPosition(54, 34)
        Tile1 = sprites.create(assets.image`
            Tile
        `, SpriteKind.Enemy)
        Tile1.setPosition(75, 34)
        Tile2 = sprites.create(assets.image`
            Tile
        `, SpriteKind.Enemy)
        Tile2.setPosition(96, 34)
        Tile3 = sprites.create(assets.image`
            Tile
        `, SpriteKind.Enemy)
        Tile3.setPosition(54, 55)
        Tile4 = sprites.create(assets.image`
            Tile
        `, SpriteKind.Enemy)
        Tile4.setPosition(75, 55)
        Tile5 = sprites.create(assets.image`
            Tile
        `, SpriteKind.Enemy)
        Tile5.setPosition(96, 55)
        Tile6 = sprites.create(assets.image`
            Tile
        `, SpriteKind.Enemy)
        Tile6.setPosition(54, 76)
        Tile7 = sprites.create(assets.image`
            Tile
        `, SpriteKind.Enemy)
        Tile7.setPosition(75, 76)
        Tile8 = sprites.create(assets.image`
            Tile
        `, SpriteKind.Enemy)
        Tile8.setPosition(96, 76)
    }
    
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    Nola.setImage(assets.image`
        nola0
    `)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    Nola.setImage(assets.image`
        nola
    `)
})
let interactionCount = 0
let Board5 : Sprite = null
let mySprite : Sprite = null
let Tile8 : Sprite = null
let Cursor : Sprite = null
let Tic = 0
let Dream : Sprite = null
let Board3 : string[][] = []
let TicTacToePlayer = 1
let Nola : Sprite = null
let Tile0 : Sprite = null
let Tile1 : Sprite = null
let Tile2 : Sprite = null
let Tile3 : Sprite = null
let Tile4 : Sprite = null
let Tile5 : Sprite = null
let Tile6 : Sprite = null
let Tile7 : Sprite = null
function Actions(Board: string[][]): any[] {
    let Acts = []
    for (let i = 0; i < Board.length; i++) {
        for (let j = 0; j < Board[i].length; j++) {
            if (Board[i][j] == "-") {
                Acts.push([i, j])
            }
            
        }
    }
    return Acts
}

function Test(Board: string[][]): any[] {
    let Acts = []
    for (let i = 0; i < Board.length; i++) {
        for (let j = 0; j < Board[i].length; j++) {
            if (Board[i][j] == "-") {
                Acts.push([i, j])
            }
            
        }
    }
    return Acts
}

function MaxValue(Board: string[][]): number {
    if (CheckOver(Board) != 2) {
        return CheckOver(Board)
    }
    
    let Value = -2
    for (let Act of Actions(Board)) {
        Value = Math.max(Value, MinValue(Result(Board, Act, "X")))
    }
    return Value
}

function MinValue(Board: string[][]): number {
    if (CheckOver(Board) != 2) {
        return CheckOver(Board)
    }
    
    let Value = 2
    for (let Act of Actions(Board)) {
        Value = Math.min(Value, MaxValue(Result(Board, Act, "O")))
    }
    return Value
}

function MiniMax(Board: string[][]) {
    let Values = []
    let Location = 0
    let Acts = Actions(Board)
    let BestValue = -2
    for (let Act of Acts) {
        Values.push(MinValue(Result(Board, Act, "X")))
    }
    for (let i = 0; i < Values.length; i++) {
        if (Values[i] > BestValue) {
            BestValue = Values[i]
            Location = i
        }
        
    }
    return Acts[Location]
}

function Result(Board4: string[][], Action: number[], Player: string): any[] {
    let CopyBoard = []
    for (let row of Board4) {
        CopyBoard.push(row.slice(0))
    }
    CopyBoard[Action[0]][Action[1]] = Player
    return CopyBoard
}

function PlaceTile(Location2: any[]) {
    if (Location2[0] == [0, 0][0] && Location2[1] == [0, 0][1]) {
        Tile0.setImage(assets.image`
            X
        `)
        Board3[0][0] = "X"
    }
    
    if (Location2[0] == [0, 1][0] && Location2[1] == [0, 1][1]) {
        Tile1.setImage(assets.image`
            X
        `)
        Board3[0][1] = "X"
    }
    
    if (Location2[0] == [0, 2][0] && Location2[1] == [0, 2][1]) {
        Tile2.setImage(assets.image`
            X
        `)
        Board3[0][2] = "X"
    }
    
    if (Location2 == Location2[0] && Location2[0] == [1, 0][0] && Location2[1] == [1, 0][1]) {
        Tile3.setImage(assets.image`
            X
        `)
        Board3[1][0] = "X"
    }
    
    if (Location2 == Location2[0] && Location2[0] == [1, 1][0] && Location2[1] == [1, 1][1]) {
        Tile4.setImage(assets.image`
            X
        `)
        Board3[1][1] = "X"
    }
    
    if (Location2[0] == [1, 2][0] && Location2[1] == [1, 2][1]) {
        Tile5.setImage(assets.image`
            X
        `)
        Board3[1][2] = "X"
    }
    
    if (Location2[0] == [2, 0][0] && Location2[1] == [2, 0][1]) {
        Tile6.setImage(assets.image`
            X
        `)
        Board3[2][0] = "X"
    }
    
    if (Location2[0] == [2, 1][0] && Location2[1] == [2, 1][1]) {
        Tile7.setImage(assets.image`
            X
        `)
        Board3[2][1] = "X"
    }
    
    if (Location2[0] == [2, 2][0] && Location2[1] == [2, 2][1]) {
        Tile8.setImage(assets.image`
            X
        `)
        Board3[2][2] = "X"
    }
    
}

scene.setBackgroundImage(assets.image`
    rogers house
`)
Nola = sprites.create(assets.image`
    nola
`, SpriteKind.Player)
let Roger = sprites.create(assets.image`
    roger
`, SpriteKind.NPC)
Nola.setPosition(28, 91)
Roger.setPosition(136, 91)
controller.moveSprite(Nola, 50, 50)
Nola.z = 1
TicTacToePlayer = 1
Board3 = [["X", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
let dialogueBank = ["Do you have my dream yet? Yes?  Thank you, mouse man!", "DIET PEPSI! You've fetched me my dream! In return, I will grant you three wishes. Just kidding, heh heh.", "Without dreams, this meager helping of life is nought but an all-consuming void of empty and ebony. My heart yearns for salvation, I hunger for dreams. Thank you for finding me my reverie, jerk."]
Dream = sprites.create(img`
    8
`, SpriteKind.Food)
Dream.setPosition(0, 0)
Tic = 0
music.setVolume(20)
music.play(music.createSong(assets.song`
        basic track
    `), music.PlaybackMode.LoopingInBackground)
forever(function on_forever() {
    
    Nola.setPosition(Nola.x, 91)
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
            scene.setBackgroundImage(assets.image`
                SnowyForest
            `)
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
            Dream.setImage(assets.image`
                Dream
            `)
            Dream.setPosition(75, 55)
            pause(500)
            music.stopAllSounds()
            Tic = 1
            game.showLongText("You made it to the forest! Now it's time to find Roger's dream and bring it home. To use your dreamcatcher net, press B. Be careful, though. Dreams are tricky things, and they're known for challenging people to games like tic tac toe.", DialogLayout.Center)
        }
        
    }
    
})
