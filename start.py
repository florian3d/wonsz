'''Snake game clone in Python'''

from game import Game
import pygame
import pygame.font

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
fps = 25

game = Game(rows=20, cols=20)

board_width = game.board.cols * (cube+offset) - offset + margin*2
board_height = game.board.rows * (cube+offset) - offset + margin*2
w_width = board_width + info_width
w_height = board_height
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption('W O N S Z')
pygame.mouse.set_visible(True)

pygame.font.init()
game_font = pygame.font.SysFont('Consolas', 48)
osd_font = pygame.font.SysFont('Consolas', 28)

clock = pygame.time.Clock()

pause_surf = get_text_surf('PAUSE', (128, 0, 255))
game_over_surf = get_text_surf('GAME OVER', (255, 128, 0))

col_info = (128, 255, 128)
col_bck = (0, 32, 0)
text_offset = osd_font.get_height()+5

BREAK = False

while not BREAK:
    
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            BREAK = True
        
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x: # x
                BREAK = True

            if event.key == pygame.K_n: # n
                game.restart()

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

    game.update()

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

    window.blit(osd_font.render(f'HIGH SCORE: {game.high_score}', True, col_info), (board_width, margin))
    window.blit(osd_font.render(f'SCORE: {game.score}', True, col_info), (board_width, margin+text_offset))
    window.blit(osd_font.render(f'DIRECTION: {game.wonsz.direction}', True, col_info), (board_width, margin+text_offset*3))
    window.blit(osd_font.render(f'WONSZ: {len(game.wonsz.body)}', True, col_info), (board_width, margin+text_offset*4))
    window.blit(osd_font.render(f'POINTS: {game.points}', True, col_info), (board_width, margin+text_offset*5))
    window.blit(osd_font.render(f'N: NEW GAME', True, col_info), (board_width, margin+text_offset*7))
    window.blit(osd_font.render(f'R: TOGGLE PAUSE', True, col_info), (board_width, margin+text_offset*8))

    if game.pause:
        window.blit(pause_surf, (board_width + info_width//2 - pause_surf.get_width()//2 - margin//2, board_height - pause_surf.get_height() - margin))

    if game.game_over:
        window.blit(game_over_surf, (board_width + info_width//2 - game_over_surf.get_width()//2 - margin//2, board_height - game_over_surf.get_height() - margin))

    pygame.display.update()
    clock.tick(fps)

