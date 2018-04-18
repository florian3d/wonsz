'''Snake game clone in Python'''

import pygame
import pygame.font
from game import Game
from game_sound import GameSound

def get_text_surf(text, bck):
    off = 16
    font = pygame.font.SysFont('Consolas', 48)
    txt = font.render(text, True, (255, 255, 255))
    surf = pygame.Surface((txt.get_width()+off, txt.get_height()+off))
    surf.fill(bck)
    surf.blit(txt, (off//2, off//2))
    return surf

margin = 16
offset = 4
cube = 24
info_width = 300
fps = 50

game = Game(rows=20, cols=20)

board_width = game.board.cols * (cube+offset) - offset + margin*2
board_height = game.board.rows * (cube+offset) - offset + margin*2
w_width = board_width + info_width
w_height = board_height
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption('W O N S Z')
pygame.mouse.set_visible(True)

sound = GameSound()

pygame.font.init()
game_font = pygame.font.SysFont('Consolas', 48)
osd_font = pygame.font.SysFont('Consolas', 28)

clock = pygame.time.Clock()

pause_surf = get_text_surf('PAUSE', (128, 0, 255))
game_over_surf = get_text_surf('GAME OVER', (255, 128, 0))

col_info = (128, 255, 128)
info0 = osd_font.render(f'N: NEW GAME', True, col_info)
info1 = osd_font.render(f'R: TOGGLE PAUSE', True, col_info)
info2 = osd_font.render(f'123: CHANGE SPEED', True, col_info)

col_bck = (0, 32, 0)
text_offset = osd_font.get_height()+5

BREAK = False
game_update = False
new = True
snd_game_over_played = False

while not BREAK:
    
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            BREAK = True
            game.high_score.save_high_score()
        
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x: # x
                BREAK = True
                game.high_score.save_high_score()

            if event.key == pygame.K_n: # n
                game.restart()
                new = True
                snd_game_over_played = False

            if event.key == pygame.K_1:
                game.speed.change_speed(game.speed.EASY)
            if event.key == pygame.K_2:
                game.speed.change_speed(game.speed.MEDIUM)
            if event.key == pygame.K_3:
                game.speed.change_speed(game.speed.HARD)

            if not game.game_over:
                
                if event.key == pygame.K_a: # a
                    game.left()
                if event.key == pygame.K_d: # d
                    game.right()
                if event.key == pygame.K_w: # w
                    game.up()
                if event.key == pygame.K_s: # s
                    game.down()
                if event.key == pygame.K_r: # r
                    game.pause = not game.pause

    game_update = game.update()


    window.fill(col_bck)

    for i in range(game.board.cols*game.board.rows):

        row, col = i//game.board.cols, i%game.board.cols

        x, y = col*(cube+offset)+margin, row*(cube+offset)+margin

        color = (0, 64, 0)

        if (row, col) == game.apple:

            color = (255, 0, 0)

        if (row, col) in game.wonsz.body:

            color = (0, 255, 0)
            
            if (row, col) == game.wonsz.body[0]:
            
                color = (255, 255, 0)
        
        pygame.draw.rect(window, color, (x, y, cube, cube), 0)

    window.blit(osd_font.render(f'HIGH SCORE: {game.high_score.value}', True, col_info), (board_width, margin))
    window.blit(osd_font.render(f'SCORE: {game.score}', True, col_info), (board_width, margin+text_offset))
    window.blit(osd_font.render(f'DIRECTION: {game.wonsz.direction}', True, col_info), (board_width, margin+text_offset*3))
    window.blit(osd_font.render(f'WONSZ: {len(game.wonsz.body)}', True, col_info), (board_width, margin+text_offset*4))
    window.blit(osd_font.render(f'POINTS: {game.points}', True, col_info), (board_width, margin+text_offset*5))
    window.blit(osd_font.render(f"SPEED: {game.speed.name}", True, col_info), (board_width, margin+text_offset*6))
    
    window.blit(info0, (board_width, margin+text_offset*8))
    window.blit(info1, (board_width, margin+text_offset*9))
    window.blit(info2, (board_width, margin+text_offset*10))

    if game.pause:
        window.blit(pause_surf, (board_width + info_width//2 - pause_surf.get_width()//2 - margin//2, board_height - pause_surf.get_height() - margin))

    if game.game_over:
        window.blit(game_over_surf, (board_width + info_width//2 - game_over_surf.get_width()//2 - margin//2, board_height - game_over_surf.get_height() - margin))

    pygame.display.update()

    if game_update:

        sound.play_walk()

        if game.eat:

            sound.play_eat()

    if game.game_over and not snd_game_over_played:

        sound.play_game_over()
        snd_game_over_played = True

    if new and game.pause == False:

        new = False
        sound.play_start()

    clock.tick(fps)
