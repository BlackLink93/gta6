@namespace
class SpriteKind:
    Coin = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    Coins.set_position(randint(0, 150), randint(0, 110))
sprites.on_overlap(SpriteKind.player, SpriteKind.Coin, on_on_overlap)

def on_on_score():
    game.game_over(True)
info.on_score(15, on_on_score)

def on_on_score2():
    global Enemies
    game.splash("f,e")
    for index in range(2):
        Enemies = sprites.create(img("""
                ........................
                ........................
                ........................
                ........................
                ..........ffff..........
                ........ff1111ff........
                .......fb111111bf.......
                .......f11111111f.......
                ......fd11111111df......
                ......fd11111111df......
                ......fddd1111dddf......
                ......fbdbfddfbdbf......
                ......fcdcf11fcdcf......
                .......fb111111bf.......
                ......fffcdb1bdffff.....
                ....fc111cbfbfc111cf....
                ....f1b1b1ffff1b1b1f....
                ....fbfbffffffbfbfbf....
                .........ffffff.........
                ...........fff..........
                ........................
                ........................
                ........................
                ........................
                """),
            SpriteKind.enemy)
        Enemies.set_position(randint(0, 150), randint(0, 110))
        Enemies.follow(Player1, 20)
info.on_score(10, on_on_score2)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    Enemies.set_flag(SpriteFlag.GHOST, True)
    pause(1000)
    Enemies.set_flag(SpriteFlag.GHOST, False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

Enemies: Sprite = None
Coins: Sprite = None
Player1: Sprite = None
tiles.set_current_tilemap(tilemap("""
    уровень1
    """))
info.set_score(0)
info.set_life(3)
Player1 = sprites.create(img("""
        . . . . f f f f . . . .
        . . f f e e e e f f . .
        . f f e e e e e e f f .
        f f e e e e e e e f f f
        f f e e e e e e e e f f
        f f e e e e e e e e f f
        f e e e e e e e e e e f
        f e e f f e e f f e e f
        f e e e e e e e e e e f
        . f 1 e e b b e e 1 f .
        . f 1 1 e e e e 1 1 f .
        e e f 1 1 1 1 1 1 f e e
        e e f 1 1 1 1 1 1 f e e
        e e f 8 8 8 8 8 8 f e e
        . . . 8 8 8 8 8 8 . . .
        . . . 8 8 . . 8 8 . . .
        """),
    SpriteKind.player)
controller.move_sprite(Player1)
Coins = sprites.create(img("""
        . . b b b b . .
        . b 5 5 5 5 b .
        b 5 d 3 3 d 5 b
        b 5 3 5 5 1 5 b
        c 5 3 5 5 1 d c
        c d d 1 1 d d c
        . f d d d d f .
        . . f f f f . .
        """),
    SpriteKind.Coin)
Coins.set_position(randint(0, 150), randint(0, 110))
Enemies = sprites.create(img("""
        . . . . f f f f . . . .
        . . a a a a a a a a . .
        . a a a a a a a a a a .
        f f a a a a a a a a f f
        f f f e e e e e f f f f
        f f f e e e e e e f f f
        f e e e e e e e e e e f
        f e e f f e e f f e e f
        f e e e e e e e e e e f
        . f e e e b b e e e f .
        . f a a f f f f a a a .
        e e f a a f f a a f e e
        e e f a a a a a a f e e
        e e a f f f f f f a e e
        . . . f f f f f f . . .
        . . . f f . . f f . . .
        """),
    SpriteKind.enemy)
Enemies.set_position(randint(0, 150), randint(0, 110))
Enemies.follow(Player1, 20)