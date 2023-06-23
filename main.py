import pygame

pygame.init()

size_cells = 167 
start = True
pygame.display.set_caption("Хрестики Нолики")
zero_win = pygame.image.load("image/Zero_win.png")
cross_win = pygame.image.load("image/Cross_win.png")
zero = pygame.image.load("image/Zero.png")
table = pygame.image.load("image/table.png")
cross = pygame.image.load("image/Cross.png")
screen = pygame.display.set_mode((510,510))
count = 0

def check_win(sign):
    zeroes = 0
    win_coords =  []
    for row in cells:
        zeroes = zeroes + row.count(0)
        # рядки
        if row.count(sign)== 3:
            win_coords = [(0, cells.index(row)),(1, cells.index(row)),(2, cells.index(row))]
            return win_coords
    for col in range(3):
        # колонки
        if cells[0][col] == sign and cells[1][col] == sign and cells[2][col] == sign:
            win_coords = [(col,0),(col,1),(col,2)]
            return win_coords
    # диагонали 
    if cells[0][0] == sign and cells[1][1] == sign and cells[2][2] == sign:
        win_coords = [(0,0),(1,1),(2,2)]
        return win_coords
    if cells[0][2] == sign and cells[1][1] == sign and cells[2][0] == sign:
        win_coords = [(2,0),(1,1),(0,2)]
        return win_coords

cells = [[0]*3 for i  in range(3)]
# cells1 = [
#     0, 0, 0,
#     0, 0, 0,
#     0, 0, 0
#]
game = True
while game:
    screen.fill((0,255,0))
    screen.blit(table, (0,0))   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and start == True:
            x,y = pygame.mouse.get_pos() 
            col = x // size_cells
            row = y // size_cells
            if cells [col][row] == 0:
                # переключатель можду крестиком и ноликом
                if count % 2 == 0:
                    cells [col][row] = cross 
                else:
                    cells [col][row] = zero
                count += 1
                
    for row in range(3):
        for col in range(3):
            if cells[col][row] == cross:
                image = cross
            elif cells[col][row] == zero:
                image = zero
            elif cells[col][row] == cross_win:
                image = cross_win
            elif cells[col][row] == zero_win:
                image = zero_win
            else:
                image = table
            x = col*size_cells+(col+1)
            y = row*size_cells+(row+1)    
            screen.blit(table, (x,y))

              
            if image == cross:
                screen.blit(cross, (x+13,y+13))
            elif image == zero:
                screen.blit(zero, (x+13,y+13))
            elif image == cross_win:
                screen.blit(cross_win, (x+13,y+13))
            elif image == zero_win:
                screen.blit(zero_win, (x+13,y+13))


            if (count-1) %2 == 0:
                win_coords = check_win(cross)    
                     
                if win_coords:
                    for coor in win_coords:
                        cells[coor[1]][coor[0]] = cross_win
                
            elif (count-1) %2 != 0:    
                win_coords = check_win(zero)  
                                                
                if win_coords:
                    for coor in win_coords:
                        cells[coor[1]][coor[0]] = zero_win
        
            if win_coords:
                start = False
            if count == 9:
                start = False
                
            if start == False:

                a = 157
                c = 380
                font = pygame.font.SysFont("Aril", 105)
                render = font.render("Reset", 1, "red")
                button = pygame.draw.rect(screen, (150,150,150), ((a, c - 13),(200,90)))
                screen.blit(render,(a,c))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.collidepoint(pygame.mouse.get_pos()):
                        cells = [[0]*3 for i  in range(3)]
                        zero= pygame.image.load("image/Zero.png")
                        cross = pygame.image.load("image/Cross.png")
                        count = 0
                        start = True
                        
    pygame.display.flip()
                    