# screen settings
TOP_BOT_BUFF = 50
WIDTH, HEIGHT = 224*2, 288*2 +TOP_BOT_BUFF
MAZE_WIDTH, MAZE_HEIGHT = WIDTH, HEIGHT - TOP_BOT_BUFF
FPS = 60

#colour settings
BLACK = (0, 0, 0) #BLACK RGB
RED = (202, 52, 51)
GRAY = (107, 107, 107)
WHITE =(255, 255, 255)
YELLOW =(255, 255, 0)
ORANJE = (240, 134, 37)

#source settings
TEXT_SIZE = 16
START_SOURCE = "arial black"

# playes settings
DIAMETROx = int(MAZE_WIDTH/19) - 2
DIAMETRO = int(MAZE_HEIGHT/21) -2

POWER_DURATION = 7000 #miliseconds 

RADIOS = DIAMETROx/2
START_POINT =[MAZE_WIDTH/2 -    DIAMETROx/2 ,TOP_BOT_BUFF/2 + 15.5 * MAZE_HEIGHT/21 - DIAMETRO/2]

vel_x = RADIOS/2 - 0.70 * MAZE_WIDTH/19/2/3                #tenho que ajustar a velocidade
vel_y = RADIOS/2 - 0.70 * MAZE_WIDTH/19/2/3 #RADIOS/2 - 0.75 * MAZE_HEIGHT/21/3/2


MAZE_LIMITS =tuple(tuple(x)for x in (
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],    #0 == points, 1 == walls , 2 == big points, 3 = nothing 5 = only for ghost
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
    [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,0,1,1,1,3,1,3,1,1,1,0,1,1,1,1],
    [1,1,1,1,0,1,3,3,3,3,3,3,3,1,0,1,1,1,1],
    [1,1,1,1,0,1,3,1,1,5,1,1,3,1,0,1,1,1,1],
    [3,3,3,3,0,3,3,1,5,5,5,1,3,3,0,3,3,3,3],
    [1,1,1,1,0,1,3,1,1,1,1,1,3,1,0,1,1,1,1],
    [1,1,1,1,0,1,3,3,3,3,3,3,3,1,0,1,1,1,1],
    [1,1,1,1,0,1,3,1,1,1,1,1,3,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
    [1,2,0,1,0,0,0,0,0,3,0,0,0,0,0,1,0,2,1],
    [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))



BLOCKS_POS = [[-1, 8], [-1, 10], [21,8], [21,10], [-2, 8], [-2, 10], [22,8], [22,10]]
for y in range(len(MAZE_LIMITS)):
    for x in range(len(MAZE_LIMITS[y])):
        if MAZE_LIMITS[y][x] == 1 or MAZE_LIMITS[y][x] == 5:
            BLOCKS_POS.append([x,y])
            
PATH = [[x, y] for x in range(0, 19) for y in range(0, 21) if MAZE_LIMITS[y][x] != 1 ]

# mob settings
BLOCKS = [[-1, 8], [-1, 10], [21,8], [21,10], [-2, 8], [-2, 10], [22,8], [22,10]]
for y in range(len(MAZE_LIMITS)):
    for x in range(len(MAZE_LIMITS[y])):
        if MAZE_LIMITS[y][x] == 1: # or MAZE_LIMITS[y][x] == 5:
            BLOCKS.append([x,y])
MOB_BLOCKS = BLOCKS.copy()   
      
MOB_DIAMETROx , MOB_DIAMETRO = DIAMETROx - 2 , DIAMETRO - 2
            
MOB_START_POINT = [MAZE_WIDTH/2 - DIAMETROx/2 ,TOP_BOT_BUFF + 6.5* (MAZE_HEIGHT/21) - MOB_DIAMETRO/2]
INKY_START_POINT = [MAZE_WIDTH/2 - DIAMETROx/2, MAZE_HEIGHT/2 - MOB_DIAMETRO/2]
PINKY_START_POINT = [MAZE_WIDTH/2 - DIAMETROx/2 - MAZE_WIDTH/19 , MAZE_HEIGHT/2 - MOB_DIAMETRO/2]
CLYDE_START_POINT = [MAZE_WIDTH/2 - DIAMETROx/2 + MAZE_WIDTH/19 , MAZE_HEIGHT/2 - MOB_DIAMETRO/2]

mob_vel_x = vel_x * (3/4)
mob_vel_y = vel_y *(3/4)


#   File "C:\Users\Utilizador\Desktop\Projeto_PacMan\Mob.py", line 178, in move
#     if not self.power_up_mob and self.count == 0 and self.app.map_matrix[int((self.mob_start_point[1] - TOP_BOT_BUFF/2 + MOB_DIAMETRO/2 )//(MAZE_HEIGHT/21))][int((self.mob_start_point[0] + MOB_DIAMETRO/2)//(MAZE_WIDTH/19))] ==5:

# IndexError: list index out of range