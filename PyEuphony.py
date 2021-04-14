import pygame
import pygame_gui
from pygame_gui.windows.ui_file_dialog import UIFileDialog
from pygame_gui.elements.ui_button import UIButton
from pygame.rect import Rect
import datetime
import math
import random
import time
def layout(board,left,right,sound,dif,angle,stride,speed):
    #pygame.draw.rect(board,(255,23,25),(390,0,410,350),1)
    #Bottom rect
    if(dif<int(sound.get_length())):
        y = ((dif/int(sound.get_length()))*600)
        

    else:
        y=100
    pygame.draw.rect(board,(255,255,255),(0,550,800,50))
    pygame.draw.line(board,(20,20,200),(100,575),(700,575),6)
    pygame.draw.circle(board,(255,255,25),(y+100,575),12,10)
    #8D Start
    pygame.draw.line(board,(20,20,200),(570,400),(700,400),6)#Distance
    y = stride*100
    y+=600
    pygame.draw.circle(board,(255,255,25),(y,400),10)
    pygame.draw.line(board,(20,20,200),(570,510),(700,510),6)#Speed
    y = 570
    if(speed>1):
        speed=1
    y+=speed*130
    pygame.draw.circle(board,(255,255,25),(y,510),10)
    #8D stop

    #Media Controller
    pygame.draw.rect(board,(20,20,200),(40,400,40,40))#Play Button
    
    pygame.draw.rect(board,(20,20,200),(240,400,40,40))#Pause Button
    
    pygame.draw.rect(board,(20,20,200),(40,480,40,40))#Mute Button
    
    pygame.draw.rect(board,(20,20,200),(240,480,40,40))#UnMuteButton
    #Line
    #Animation
    x,y=590,160
    theta = math.radians(angle)
    x += 130*math.cos(theta)
    y+=130*math.sin(theta)
    pygame.draw.circle(board, (255,255,255), (x,y),15)
    dx,dy= left-0.5,right-0.5
    x,y=590,160
    pygame.draw.rect(board,(10,255,10),(x+dx*150,330,15,15))
    pygame.draw.rect(board,(50,55,255),(x-dx*150,0,15,15))
    pygame.draw.rect(board,(255,160,89),(790,y+dx*150,15,15))    
    pygame.draw.rect(board,(70,200,189),(390,y-dx*150,15,15))
    pygame.draw.rect(board,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(600,180,50,50))
    pygame.draw.rect(board,(random.randint(0,255),random.randint(0,255),150),(550,180,50,50))
    pygame.draw.rect(board,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(550,130,50,50))
    pygame.draw.rect(board,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(600,130,50,50))

    
def text_printer(board,file,total,sod):
    myfont = pygame.font.SysFont('Comic Sans MS', 17)
    textsurface = myfont.render('Song:', False, (255,255,255))
    board.blit(textsurface,(0,70))
    textsurface = myfont.render(file, False, (255,255,255))
    board.blit(textsurface,(0,100))
    mins,sec=0,0
    total = int(total)
    mins = total//60
    sec = total-mins*60
    if(mins<10):
        mins='0'+str(mins)
    if(sec<10):
        sec='0'+str(sec)

    textsurface = myfont.render(str(mins)+':'+str(sec), False, (255,0,0))
    board.blit(textsurface,(20,560))
    mins,sec=0,0
    total = sod
    mins = total//60
    sec = total-mins*60
    if(mins<10):
        mins='0'+str(mins)
    if(sec<10):
        sec='0'+str(sec)

    textsurface = myfont.render(str(mins)+':'+str(sec), False, (255,0,0))
    board.blit(textsurface,(720,560))
    textsurface = myfont.render('8D Controller', False, (255,255,255))
    board.blit(textsurface,(570,440))
    textsurface = myfont.render('Stride:', False, (255,255,255))
    board.blit(textsurface,(500,390))
    textsurface = myfont.render('Speed:', False, (255,255,255))
    board.blit(textsurface,(500,500))

    pygame.draw.polygon(board,(255,255,25),((50,405),(50,435),(70,420)))#Play Triangle
    pygame.draw.rect(board,(255,255,25),(253,405,7,30))#Pause Rect 1
    pygame.draw.rect(board,(255,255,25),(263,405,7,30))#Pause Rect 2
    pygame.draw.rect(board,(255,255,25),(45,496,9,9))
    pygame.draw.polygon(board,(255,255,25),((63,490),(63,510),(47,500)))#Play Triangle
    pygame.draw.line(board,(255,255,25),(70,490),(45,510),4)#VErtical -

    pygame.draw.rect(board,(255,255,25),(250,496,9,9))
    pygame.draw.polygon(board,(255,255,25),((263,490),(263,510),(250,500)))#Play Triangle
    
    textsurface = myfont.render('Media Controller', False, (255,255,255))
    board.blit(textsurface,(100,440))
    
pygame.init()
pygame.font.init()
print("\n\n\tHello There! Welcome to PyEuphony...\n-By Default a Song is kept so you can listen to it.\n-Stride: It is the distance the sound travel in the imaginary circle",
      "\n-Speed:It is the speed of the Stride\n-As the Beat of the each song is different so you can adjust them to your comfort\n***ShortCuts***\n-p:Play;\t-k:Pause",
      "\n\tq-Quit;\n-m:Mute;\t-l:Unmute\n\n-You can change the song using the 'File'(Top-Left)\n\t***No Need TO Click,Hover Is Considered as Click***\n\t\t**Cannot Change Seek**")
print("\n\n\t\tJust a Moment...")
time.sleep(5)
window_surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyEuphony")
gameIcon = pygame.image.load('1.jpg')
pygame.display.set_icon(gameIcon)
board = pygame.Surface((800, 600))
board.fill((25,0,0))
manager = pygame_gui.UIManager((800, 600))
clock = pygame.time.Clock()
file_selection_button = UIButton(relative_rect=Rect(0, 0, 50, 50),manager=manager, text='File')
a,b=1.0,0.0
temp=[-1,1]
rodda1 ='Sample.mp3' 
sound = pygame.mixer.Sound(rodda1)
paused = 0
channel = pygame.mixer.find_channel()
channel.set_volume(1.0,0.0)
count =0
current=0
channel.play(sound)
channel.set_volume(0.5)
x= datetime.datetime.now()
wes = z=x
cx,cy = 151,170
angle=0
paused = False
elapsed =0
stride,speed =.19,0.3#Stride - Step taken by sound;Speed-At what spped\
pu,pk=0,0
muted=False
while True:
    time_delta = clock.tick(5) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == file_selection_button:
                    file_selection = UIFileDialog(rect=Rect(0, 0, 300, 300), manager=manager, allow_picking_directories=True)

                if event.ui_element == file_selection.ok_button:
                    rodda = str(file_selection.current_file_path)
                    rodda1=rodda
                    sega = rodda.split('.')[-1]
                    if('mp3' in sega):
                        sound = pygame.mixer.Sound(rodda1)
                        channel.play(sound)
                        z=datetime.datetime.now()
                        wes = datetime.datetime.now()
                        elapsed=0
                    else:
                        print("Kindly Give Mp3 Format!!!!")
                        pygame.quit()
                        exit()

                    x= datetime.datetime.now()
        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(board, (0, 0))
    manager.draw_ui(window_surface)
    y= datetime.datetime.now()
    
    if((y-x).total_seconds()>speed):
        a+=temp[0]*stride
        b+=(temp[1]*stride)
        if(a<0.01 and b>0.9):
            a,b=0,1
            temp[0],temp[1] = temp[1],temp[0]
        if(b<0.01 and a>0.9):        
            a,b=1,0
            temp[0],temp[1] = temp[1],temp[0]
        if(not paused):
            if(not muted):
                channel.set_volume(abs(a),b)
        x= datetime.datetime.now()
    angle-=5
    angle=angle%360
    post = pygame.mouse.get_pos()
    
    if((40<post[0]<80 and 400<post[1]<440) or pygame.key.get_pressed()[pygame.K_p]):
        print("Playing...")
        pygame.mixer.unpause()
        paused = False
        
    if((40<post[0]<80 and 480<post[1]<520) or pygame.key.get_pressed()[pygame.K_m]):
        print("Muted...")
        channel.set_volume(0.0,0.0)
        muted = True
    if((240<post[0]<280 and 400<post[1]<440) or  pygame.key.get_pressed()[pygame.K_k]):
        print("Paused...")
        paused=True
        channel.pause()
        
    if((240<post[0]<280 and 480<post[1]<520) or pygame.key.get_pressed()[pygame.K_l]):
        muted= False
        print("Unmuted..")
    if(pygame.key.get_pressed()[pygame.K_q]):
        pygame.quit()
        exit()
    if(390<post[1]<405 and 570<post[0]<700):
        temp2 = post[0]
        temp2-=600
        temp2/=100
        stride = temp2
    if(500<post[1]<515 and 570<post[0]<700):
        temp2 = post[0]
        temp2-=600
        temp2/=100
        speed = temp2+.29
    if(paused and muted==False):
        y=datetime.datetime.now()
        wes=datetime.datetime.now()
        
    if(int((y-wes).total_seconds())==1):
        wes = datetime.datetime.now()
        elapsed+=1
    layout(window_surface,a,b,sound,elapsed,angle,stride,speed)#Board,left,Right,timediff,cirlcex,circley
    text_printer(window_surface,rodda1,elapsed,int(sound.get_length()))
    pygame.display.flip()
    pygame.display.update()
