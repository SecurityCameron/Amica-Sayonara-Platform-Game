import pygame
pygame.init()

screen_width = 800
screen_height = 800


screen = pygame.display.set_mode((screen_width,screen_height))

# Amica is friend in latin
pygame.display.set_caption("Indie Game Dev - Sayonara Amica")

def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2): 
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
        return True

    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
        return True

    elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
        return True

    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
        return True

    else:
        return False

#Class 1b:
class enemies:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

        # Player is now the medium sprite size to match the background size
        self.i2 = pygame.image.load("zombie1.png")

    def draw(self,collision):
        if (collision == True):
            player.x -= moveX
            player.y -= moveY
            
        #render object to the screen
        screen.blit(self.i2,(self.x,self.y))
        

      
#Class 3
class Missile:
    #create missile
    def __init__(self,x,y,width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15
        speed = 0
        self.i3 = pygame.image.load('laser.png') 
 
    def draw(self,collision):
        
        speed +=10
        #updating position
        screen.blit(self.i3,(self.x,self.y))


moveX,moveY = 0,0

bullet = Missile(5,5,moveX,moveY)
zombie = enemies(400,300,100,100)
points = 0
x = 150
y = 660
width = 40
height = 40
vel = 15
jumpCount = 10

isJump = False
run = True

# Levels
level_one = True
level_two = False
level_three = False
level_four = False

while run:
    player = pygame.image.load('Knight.png')
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        # Attacking
        elif (event.type==pygame.KEYDOWN):
            if (event.key== ord('x')):
                Missile(5,5,moveX,moveY)
                print ("attack.")
                pygame.mixer.music.load('sword_noise.mp3')
                pygame.mixer.music.play(0)
                player = pygame.image.load('Knight2.png')
         
        
    # Controls - Arrow Keys and Border Control (doesn't allow less than vel)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel

    #for border control on the right add below: and x < 800 - vel - width
    if keys[pygame.K_RIGHT] :  
        x += vel
        
    if isJump == False: 

        # Jump is active if space bar is pressed
        if keys[pygame.K_SPACE]:
            isJump = True
            
    # Code for decending.
    else:
        if jumpCount >= -10:
            #y -= (jumpCount*2)
            
            #Below lineof code is too high of a jump.
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 2
        else: 
            jumpCount = 10
            isJump = False
    
    
    if level_one == True:
        bg = pygame.image.load("level_1.png").convert()
        speech = pygame.image.load("speech3.png").convert()
        pygame.transform.scale(speech, (50, 50))
        
        if x > 800 - vel - width:
            x = 50
            level_two = True
            level_one = False
            
    if level_two == True:
        bg = pygame.image.load("level_2.png").convert()
        if x > 800 - vel - width:
            x = 50
            level_two = False
            level_three = True
    
    if level_three == True:
        bg = pygame.image.load("level_3.png").convert()
        if x > 800 - vel - width:
            x = 50
            level_three = False
            level_four = True
            
    if level_four == True:
        bg = pygame.image.load("level_4.png").convert()
        if x > 800 - vel - width:
            x = 50
            level_four = False
            level_five = True
        
        
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    screen.blit(bg, (0,0))
    
    
     
    screen.blit(player,(x,y))
    
    if level_one == True:
        screen.blit(speech,(600,50))
    
    # Uncomment below line for abstract rectangle jump.
    #pygame.draw.rect(screen, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()