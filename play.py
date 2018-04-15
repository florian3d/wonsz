'''Snake game clone in Python'''

from game import Game
import pygame
import pygame.font

offset = 8
cube = 20
info_width = 300
fps = 25

game = Game(rows=20, cols=20)

board_width = game.board.cols*cube+offset//2*game.board.cols+offset*2
board_height = game.board.rows*cube+offset//2*game.board.rows+offset*2
w_width = board_width+info_width+offset
w_height = board_height
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption('W O N S Z')
pygame.mouse.set_visible(True)

pygame.font.init()
game_font = pygame.font.SysFont('Consolas', 48)
osd_font = pygame.font.SysFont('Consolas', 28)

clock = pygame.time.Clock()

pause = game_font.render('PAUSE', True, (255, 255, 255))
pause_surf = pygame.Surface((pause.get_width()+20, 60))
pause_surf.fill((128, 0, 255))
pause_surf.blit(pause, (offset, offset))

go = game_font.render('GAME OVER', True, (255, 255, 255))
game_over_surf = pygame.Surface((go.get_width()+20, 60))
game_over_surf.fill((255, 128, 0))
game_over_surf.blit(go, (offset, offset))

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
        x, y = col*(cube+offset//2), row*(cube+offset//2)

        color = (0, 64, 0)

        if (row, col) == game.apple:

            color = (255, 0, 0)

        if (row, col) in game.wonsz.body:

            color = (0, 255, 0)
            
            if (row, col) == game.wonsz.body[0]:
            
                color = (255, 255, 0)
        
        pygame.draw.rect(window, color, (x+offset, y+offset, cube, cube), 0)

    window.blit(osd_font.render(f'HIGH SCORE: {game.high_score}', True, col_info), (board_width, offset))
    window.blit(osd_font.render(f'SCORE: {game.score}', True, col_info), (board_width, offset+text_offset))
    window.blit(osd_font.render(f'Direction: {game.wonsz.direction}', True, col_info), (board_width, offset+text_offset*3))
    window.blit(osd_font.render(f'Wonsz: {len(game.wonsz.body)}', True, col_info), (board_width, offset+text_offset*4))
    window.blit(osd_font.render(f'Points: {game.points}', True, col_info), (board_width, offset+text_offset*5))
    window.blit(osd_font.render(f'N: new game', True, col_info), (board_width, offset+text_offset*7))
    window.blit(osd_font.render(f'R: toggle pause', True, col_info), (board_width, offset+text_offset*8))

    if game.pause:
        window.blit(pause_surf, (board_width//2 - pause_surf.get_width()//2, board_height//2-pause_surf.get_height()//2))

    if game.game_over:
        window.blit(game_over_surf, (board_width//2 - game_over_surf.get_width()//2, board_height//2-game_over_surf.get_height()//2))

    pygame.display.update()
    clock.tick(fps)
