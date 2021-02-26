import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
from pygame.locals import *

pygame.init()
pygame.font.init()

vec = pygame.math.Vector2 #Para crear vectores de dos dimensiones (x,y)

#Funciones

def  account_limit(x): #Texto cuando hay limite de cuentas
    fuente = pygame.font.SysFont("Comic Sans MS",30)
    texto = fuente.render("Se le devolverá al menú en:", True, blanco)
    conteo = fuente.render(x, True , blanco)
    caption = pygame.image.load('account_limit.png')
    cajon.fill(negro)
    cajon.blit(caption,(100,200))
    cajon.blit(texto, (200, 400))
    cajon.blit(conteo,(600,400))
    pygame.display.flip()

def account_del(x): #Texto cuando se elimina una cuenta
    fuente = pygame.font.SysFont("Comic Sans MS",30)
    texto = fuente.render("Se le devolverá al menú en:", True, blanco)
    conteo = fuente.render(x, True , blanco)
    caption = pygame.image.load('account_deleted.png')
    cajon.fill(negro)
    cajon.blit(caption,(150,150))
    cajon.blit(texto,(200,400))
    cajon.blit(conteo,(600,400))
    pygame.display.flip()

def no_account(x): #Texto cuando no hay cuentas elegibles
    fuente = pygame.font.SysFont("Comic Sans MS",30)
    texto = fuente.render("Se le devolverá al menú en:", True, blanco)
    conteo = fuente.render(x, True, blanco)
    caption = pygame.image.load('noaccount.png')
    cajon.fill(negro)
    cajon.blit(caption,(150,150))
    cajon.blit(texto,(200,400))
    cajon.blit(conteo,(600,400))
    pygame.display.flip()

def selector(x,y): #Función del cuadrado blanco usado para elegir
    pygame.draw.rect(cajon,blanco,(x,y,20,20))

def menu_return(): #Texto que indica que se le devolverá al menú
    fuente = pygame.font.SysFont("Comic Sans MS",30)
    texto = fuente.render("Se le devolverá al menú", True, blanco)
    cajon.fill(negro)
    cajon.blit(texto,(200,200))
    pygame.display.flip()

def text(w,x,y,z): #Función para crear texto con parametros de ubicación y tamaño
    fuente = pygame.font.SysFont("Comic Sans MS",30 + w)
    texto = fuente.render(z, True, blanco)
    cajon.blit(texto,(x,y))

def account_text(x,y): #Texto de la esquina superior derecha que indica el estado de cuenta
    fuente = pygame.font.SysFont("Comic Sans MS",20)
    texto1 = fuente.render("Usted ha iniciado sesión como:", True, blanco)
    if y:
        texto2 = fuente.render(x, True, blanco)
    else:
        texto2 = fuente.render("Invitado", True, blanco)
    cajon.blit(texto1,(0,0))
    cajon.blit(texto2,(290,0))

def get_save(): #Función para guardar los datos de un archivo txt en una variable
    save = open("data.txt","r")
    data = save.readlines()
    save.close()
    return data

def write_save(x): #Función para guardar los datos de una variable a un archivo txt
    save = open("data.txt","w")
    save.writelines(x)
    save.close()

def count(x): #Función que cuenta el número de cuentas en el archivo de guardado
    if len(x) == 2:
        return 1
    elif len(x) == 4:
        return 2
    elif len(x) == 6:
        return 3
    else:
        return 0
    
def delete_onespace(x): #Función que borra el ultimo espacio de un string
    x = x[:len(x) - 1]
    return x


    x = x[:len(x) - 2]
    return x
    

# Tamaño de la consola del juego
HEIGHT = 500    #Altura
WIDTH = 800     #Ancho
ACC = 0.5       #Variable de la aceleración
FRIC = -0.12    #Variable de la fricción
FPS = 60        #La velocidad a la que ejecuta el programa
FramePerSec = pygame.time.Clock()
cajon = pygame.display.set_mode((WIDTH, HEIGHT))

#Imagenes
title = pygame.image.load('titulo.png')
play = pygame.image.load('jugar.png')
account = pygame.image.load('cuenta.png')
create = pygame.image.load('crear_cuenta.png')
choose = pygame.image.load('elegir_cuenta.png')
choose1 = pygame.image.load('account_choose.png')
select = pygame.image.load('account_select.png')
exitp = pygame.image.load('salir.png')
delete = pygame.image.load('account_delete.png')
keys = pygame.image.load('teclas.png')
enter = pygame.image.load('enter.png')
esc = pygame.image.load('esc.png')
tec = pygame.image.load('tec.png')
fondo = pygame.image.load('image01.jpeg')

#Sonido
salto = pygame.mixer.Sound('jump.wav')
principal = pygame.mixer.Sound('on.mp3')

#Titulo e icono de la ventana
pygame.display.set_caption("ObstaClimb")
icon = pygame.image.load('icono.png')
pygame.display.set_icon(icon)

#Estados del Juego
ex = False              #Indicador para actualizar el display antes del ciclo
title_state = True      #Estado del título
account1_state = False  #Estado del menú de cuentas
account2_state = False  #Estado del menú de creación de cuentas
account3_state = False  #Estado del menú de selección de cuentas
account4_state = False  #Estado del menú de eliminación de cuentas
play_state = False      #Estado del juego
running = True          #Estado para el bucle general
account_choosen = False #Estado para saber si se ha escogido cuenta
highscore = False       #Estado de la existencia del highscore
score_written = False   #Estado para la confirmación del guardado del highscore
rules = True            #Estado para monitorear si es pertinente mostrar las reglas
up_key = False          #Estado para que el sonido de salto se escuche adecuadamente

#Variables
fle_pos = 0             #Ubicación de la selección en los menús
data = get_save()       #Variable que almacena los datos locales
acc_count = count(data) #Variable que almacena el número de cuentas disponibles
acc_id = 0              #Variable que almacena el numero de posición del Highscore
acc = ""                #Variable para el guardado del string de nombre de cuenta
acc1 = ""               #Variable para el guardado del string de nombre de cuenta

#Colores RGB
blanco =  (255,255,255)
azul =    (  0,  0,255)
rojo =    (255,  0,  0)
verde =   (  0,255,  0)
negro =   (  0,  0,  0)
amarillo =(255,255,  0)

#Personaje y plataformas
class Player(pygame.sprite.Sprite):
    def __init__(self):     #Valores que adquiere el objeto jugador cuando es llamado
        super().__init__() 
        self.pos = vec((WIDTH/2, HEIGHT - 40))
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((amarillo))
        self.rect = self.surf.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT - 40)

        
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
        self.score = 0
 
    def move(self):         #Función que se encarga del movimiento del jugador
        self.acc = vec(0,0.5)
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc            
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        
        self.rect.midbottom = self.pos
       
 
    def jump(self):         #Función que se encarga del salto del jugador
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -15

    def cancel_jump(self):  #Función que se encarga de que el jugador no siga saltando
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
 
    def update(self):       #Función que actualiza la ubicación del jugador
        hits = pygame.sprite.spritecollide(self ,platforms, False)
        if self.vel.y > 0:        
            if hits:
                if self.rect.bottom - 5 < hits[0].rect.bottom:
                    if hits[0].point == True:   
                        hits[0].point = False   
                        self.score += 1         
                    self.pos.y = hits[0].rect.top + 1
                    self.vel.y = 0
                    self.jumping = False
                    for xd in platforms:
                        if P1.rect.bottom < xd.rect.top:
                            xd.point = False

class platform(pygame.sprite.Sprite):
    def __init__(self):     #Valores que obtienen las plataformas cuando son creadas (Al azar)
        super().__init__()
        self.surf = pygame.Surface((random.randint(150,200), 12))
        self.surf.fill((blanco))
        self.moving = True
        self.point = True   
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH - 10),
                                                 random.randint(0, HEIGHT - 30)))
        self.speed = random.randint(-1,1)


    def move(self):         #Función para el movimiento de las plataformas
        if self.moving == True:  
            self.rect.move_ip(self.speed * 4,0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = WIDTH
    
def check(platform, groupies): #Función que checkea el espacio disponible para la generación de plataformas
    if pygame.sprite.spritecollideany(platform,groupies):
        return True
    else:
        for entity in groupies:
            if ( abs(platform.rect.top - entity.rect.bottom) < 50) and (abs(platform.rect.bottom - entity.rect.top) < 50):
                return True

        return False

def plat_gen_start():       #Generación de las primeras plataformas
    while len(platforms) < 7:
        width = random.randint(130,150)
        C = True
        while C:
            p = platform()
            p.moving = False
            p.rect.center = (random.randrange(0 + width, WIDTH - width),
                                random.randrange(0 , HEIGHT))
            C = check(p, platforms)
        platforms.add(p)
        all_sprites.add(p)

def plat_gen_easy():        #Generación de las plataformas hasta los 50 puntos
    while len(platforms) < 8:
        width = random.randint(130,150)
        C = True
        while C:
            p = platform()
            p.moving = False
            p.rect.center = (random.randrange(0 + width, WIDTH - width),
                                random.randrange(-150, 0))
            C = check(p, platforms)
        platforms.add(p)
        all_sprites.add(p)

def plat_gen_medium():      #Generación de las plataformas desde los 50 puntos
    while len(platforms) < 8:
        C = True
        while C:
            p = platform()
            p.rect.center = (random.randrange(0, WIDTH),
                                random.randrange(-150, 0))
            C = check(p, platforms)
        platforms.add(p)
        all_sprites.add(p)

#Soundtrack Principal
principal.play()

#Loop general
while running:
    #Loop Título
    while title_state:
        if ex:
            cajon.blit(fondo,(0,0))
            account_text(acc,account_choosen)
            cajon.blit(title, (25,50))
            cajon.blit(play, (280,160))
            cajon.blit(account, (280,240))
            cajon.blit(exitp, (280,320))
            cajon.blit(keys,(15, HEIGHT - 80))
            cajon.blit(enter,(WIDTH - 190, HEIGHT - 75))
            cajon.blit(esc,(WIDTH / 2 - 110, HEIGHT - 75))
            text(-10 , 50, HEIGHT - 60,": Mover")
            text(-10 , WIDTH / 2 - 40, HEIGHT - 60,": Atrás")
            text(-10 , WIDTH - 130, HEIGHT - 60,": Seleccionar")
            fle_pos = 0
            selector(250,200)
            pygame.display.flip()
            ex = False
        cajon.blit(fondo,(0,0))
        account_text(acc,account_choosen)

        for event in pygame.event.get():
       
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if fle_pos == 1:
                        fle_pos = 0
                    elif fle_pos == 2:
                        fle_pos = 1
                if event.key == pygame.K_DOWN:
                    if fle_pos == 0:
                        fle_pos = 1
                    elif fle_pos == 1:
                        fle_pos = 2
                if event.key == pygame.K_RETURN:
                    if fle_pos == 1:
                        account1_state = True
                        title_state = False
                    elif fle_pos == 0:
                        play_state = True
                        title_state = False
                    else:
                        pygame.quit()
                        sys.exit()

            if fle_pos == 0:
               selector(250,200)
            elif fle_pos == 1:
               selector(250,280)
            else:
               selector(250,360) 


            cajon.blit(title, (25,50))
            cajon.blit(play, (280,160))
            cajon.blit(account, (280,240))
            cajon.blit(exitp, (280,320))
            cajon.blit(keys,(15, HEIGHT - 80))
            cajon.blit(enter,(WIDTH - 190, HEIGHT - 75))
            cajon.blit(esc,(WIDTH / 2 - 110, HEIGHT - 75))
            text(-10 , 50, HEIGHT - 60,": Mover")
            text(-10 , WIDTH / 2 - 40, HEIGHT - 60,": Atrás")
            text(-10 , WIDTH - 130, HEIGHT - 60,": Seleccionar")
            
            pygame.display.flip()
    #Preparaciones Loop Juego
    if play_state:
        PT1 = platform()  # Plataforma Roja Inicial
        PT2 = platform()  # Plataforma Central Inicial
        P1 = Player()
        score_written = False

        PT1.surf = pygame.Surface((WIDTH, 20))
        PT1.surf.fill((255, 0, 0))
        PT1.rect = PT1.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))
        PT2.surf = pygame.Surface((random.randint(100, 200), 12))
        PT2.surf.fill((blanco))
        PT2.moving = False
        PT2.point = True
        PT2.rect = PT2.surf.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))

        all_sprites = pygame.sprite.Group()
        all_sprites.add(PT1)
        all_sprites.add(P1)
        PT1.moving = False
        PT1.point = False
        platforms = pygame.sprite.Group()
        platforms.add(PT1)
        all_sprites.add(PT2)
        platforms.add(PT2)

        #Generación de 7 plataformas extra
        plat_gen_start()

        if acc_id > 0:
            highscore = True
        else:
            highscore = False

        if rules and not account_choosen:
            cajon.fill(negro)
            key = True
            text(20, WIDTH - 480, 10, "Reglas")
            text(-10, 10, 100, "1.)  Consigues puntos saltando plataformas, solo te cuenta el punto si la plataforma-")
            text(-10, 45, 124, "está más alta que la anterior plataforma en la que estabas.")
            text(-10, 10, 170, "2.)  Puedes moverte fuera de la pantalla para aparecer en el otro lado.")
            text(-10, 10, 216, "3.)  Ten cuidado al abandonar el juego, no se guardará tu progreso")
            text(-10, 10, 262, "4.)  Te mueves con las flechas y puedes pausar con Escape:")
            text(-10, 10, 410, "5.)  Diviértete!!!!111!!!!!1!")
            text(-10, WIDTH /2 - 190, HEIGHT - 50, "Presiona cualquier botón para continuar.")
            cajon.blit(tec,(WIDTH/2 - 180, 310))
            cajon.blit(esc,(WIDTH/2 + 80, 325))





            pygame.display.flip()
            while key:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        key = False
            rules = False
    #Loop juego
    while play_state:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #Salto del personaje
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_UP:
                P1.jump()
                if up_key == False:
                    salto.play()
                    up_key = True
            #Menú Pausa
            if event.key == pygame.K_ESCAPE:
                option = False
                fle_pos = 0
                while option == False:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        cajon.fill(negro)
                        for entity in all_sprites:
                            cajon.blit(entity.surf, entity.rect)

                        text(-10, 75, 0, str(P1.score))
                        text(-10, 10, 0, "Score:")
                        if highscore:
                            text(-10, 10, 30, "Highscore:")
                            text(-10, 115, 30, delete_onespace(data[acc_id]))

                        image = pygame.Surface((WIDTH,HEIGHT))
                        image.fill(negro)
                        image.set_alpha(200)
                        cajon.blit(image,(0,0))
                        text(20,WIDTH/2 - 80,HEIGHT/2 - 180, "PAUSA")
                        text(0,WIDTH/2 - 75,HEIGHT/2 - 15, "Reanudar")
                        text(0,WIDTH/2 - 75,HEIGHT/2 + 65, "Abandonar")

                        if event.type == pygame.KEYDOWN:
                            if event.key == K_RETURN:
                                if fle_pos == 0:
                                    option = True
                                    break
                                else:
                                    option = True
                                    play_state = False
                                    title_state = True
                                    break
                            if event.key == K_UP:
                                if fle_pos == 1:
                                    fle_pos = 0
                            elif event.key == K_DOWN:
                                if fle_pos == 0:
                                    fle_pos = 1
                                
                                    
                        
                        if fle_pos == 0:
                            selector(WIDTH/2 - 115,HEIGHT/2)
                        else:
                            selector(WIDTH/2 - 115,HEIGHT/2 + 80)
        


                        

    
                        pygame.display.flip()
        if fle_pos == 1:
            break
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                P1.cancel_jump()
                up_key = False
        
        #Pantalla GameOver
        if P1.rect.top > HEIGHT:

            option = False
            fle_pos = 0
            cajon.fill(negro)
            for entity in all_sprites:
                cajon.blit(entity.surf, entity.rect)

            image = pygame.Surface((WIDTH, HEIGHT))
            image.fill(negro)
            image.set_alpha(200)
            cajon.blit(image, (0, 0))

            if highscore:
                if int(delete_onespace(data[acc_id])) < P1.score or score_written:
                    score_written = True
                    data[acc_id] = (str(P1.score) + "\n")
                    write_save(data)
                    text(-10, 10, 0, "Su nuevo Highscore es:")
                    text(-10, 240, 0, str(P1.score))
                else:
                    text(-10, 10, 0, "Su puntaje fue:")
                    text(-10, 160, 0, str(P1.score))
            else:
                text(-10, 10, 0, "Su puntaje fue:")
                text(-10, 160, 0, str(P1.score))


            text(20, WIDTH / 2 - 130, HEIGHT / 2 - 180, "Has perdido")
            text(0, WIDTH / 2 - 75, HEIGHT / 2 - 15, "Reintentar")
            text(0, WIDTH / 2 - 75, HEIGHT / 2 + 65, "Abandonar")
            if fle_pos == 0:
                selector(WIDTH / 2 - 115, HEIGHT / 2)
            else:
                selector(WIDTH / 2 - 115, HEIGHT / 2 + 80)

            pygame.display.flip()
            while option == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    cajon.fill(negro)
                    for entity in all_sprites:
                        cajon.blit(entity.surf, entity.rect)

                    image = pygame.Surface((WIDTH, HEIGHT))
                    image.fill(negro)
                    image.set_alpha(200)
                    cajon.blit(image, (0, 0))

                    if highscore:
                        if int(delete_onespace(data[acc_id])) < P1.score or score_written:
                            score_written = True
                            data[acc_id] = (str(P1.score) + "\n")
                            write_save(data)
                            text(-10, 10, 0, "Su nuevo Highscore es:")
                            text(-10, 240, 0, str(P1.score))
                        else:
                            text(-10, 10, 0, "Su puntaje fue:")
                            text(-10, 160, 0, str(P1.score))
                    else:
                        text(-10, 10, 0, "Su puntaje fue:")
                        text(-10, 160, 0, str(P1.score))

                    text(20, WIDTH / 2 - 130, HEIGHT / 2 - 180, "Has perdido")
                    text(0, WIDTH / 2 - 75, HEIGHT / 2 - 15, "Reintentar")
                    text(0, WIDTH / 2 - 75, HEIGHT / 2 + 65, "Abandonar")


                    if event.type == pygame.KEYDOWN:
                        if event.key == K_RETURN:
                            if fle_pos == 0:
                                option = True
                                break
                            else:
                                option = True
                                play_state = False
                                title_state = True
                                break
                        if event.key == K_UP:
                            if fle_pos == 1:
                                fle_pos = 0
                        elif event.key == K_DOWN:
                            if fle_pos == 0:
                                fle_pos = 1

                    if fle_pos == 0:
                        selector(WIDTH / 2 - 115, HEIGHT / 2)
                    else:
                        selector(WIDTH / 2 - 115, HEIGHT / 2 + 80)

                    pygame.display.flip()
            break

          
        #Desplazamiento de pantalla
        if P1.rect.top < HEIGHT / 3:
            P1.pos.y += abs(P1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P1.vel.y)
                if plat.rect.top > HEIGHT:
                    plat.kill()
                    if P1.score < 50:
                        plat_gen_easy()
                    else:
                        plat_gen_medium()   
                     
        #Mostrar el Score
        cajon.fill((0,0,0))
        text(-10,75,0,str(P1.score))
        text(-10,10,0, "Score:")
        if highscore:
            text(-10,10,30,"Highscore:")
            text(-10,115,30,delete_onespace(data[acc_id]))

        P1.update()

        #Movimiento de los objetos y su display
        for entity in all_sprites:
            cajon.blit(entity.surf, entity.rect)
            entity.move()
        
        

        pygame.display.update()
        FramePerSec.tick(60)
    #Loop Cuenta
    fle_pos = 0
    #Menú Cuenta
    while account1_state:
        cajon.fill(negro)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    account1_state = False
                    title_state = True
                    fle_pos = 0
                    break
                if event.key == pygame.K_UP:
                    if fle_pos == 1:
                        fle_pos = 0

                    elif fle_pos == 2:
                        fle_pos = 1

                    
                if event.key == pygame.K_DOWN:
                    if fle_pos == 0:
                        fle_pos = 1
                    elif fle_pos == 1:
                        fle_pos = 2

                    
                if event.key == pygame.K_RETURN:
                    if fle_pos == 0:
                        account1_state = False
                        account2_state = True
                        can_write = True   
                    elif fle_pos == 1:
                        account1_state = False
                        account3_state = True
                    else: 
                        account1_state = False
                        account4_state = True
        
            if fle_pos == 0:
                selector(180,120)
            elif fle_pos == 1:
                selector(180,220)
            else:
                selector(180,320)

            cajon.blit(create,(200,80))
            cajon.blit(choose,(200,180))
            cajon.blit(delete,(200,280))
            cajon.blit(keys,(15, HEIGHT - 80))
            cajon.blit(enter,(WIDTH - 190, HEIGHT - 75))
            cajon.blit(esc,(WIDTH / 2 - 110, HEIGHT - 75))
            text(-10 , 50, HEIGHT - 60,": Mover")
            text(-10 , WIDTH / 2 - 40, HEIGHT - 60,": Atrás")
            text(-10 , WIDTH - 130, HEIGHT - 60,": Seleccionar")
            pygame.display.flip()
    #Menú Creación de cuenta
    while account2_state:
        if ex:
            break
        cajon.fill(negro)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #Pantalla generada al haber suficientes cuentas creadas
            if acc_count == 3:
                account_limit("3")
                pygame.time.delay(1000)
                account_limit("2")
                pygame.time.delay(1000)
                account_limit("1")
                pygame.time.delay(1000)
                fle_pos = 0
                ex = True
                account2_state = False
                title_state = True
                break


            
            cajon.blit(choose1,(0,100))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    account2_state = False
                    account1_state = True
                    fle_pos = 0
                    break
                #Mostrar en pantalla las teclas presionadas
                key = pygame.key.name(event.key)  
                if len(key) == 1:  
                    acc1 += key.upper() 
                elif key == "backspace":
                    acc1 = acc1[:len(acc1) - 1]
                elif event.key == pygame.K_SPACE:
                    acc1 += " "
                elif event.key == pygame.K_RETURN:
                    acc = acc1
                    acc1 = ""
                    account2_state = False
                    title_state = True
                    account_choosen = True
                    acc_count += 1
                    if acc_count == 1:
                        acc_id = 1
                    elif acc_count == 2:
                        acc_id = 3
                    else:
                        acc_id = 5
                    
                    data.append(acc +"\n")
                    data.append("0\n")
                    write_save(data)
                    

                    break   
            text(0,200,200,acc1)
            cajon.blit(enter,(WIDTH - 190, HEIGHT - 75))
            cajon.blit(esc,(10, HEIGHT - 75))
            text(-10 , 80, HEIGHT - 60,": Atrás")
            text(-10 , WIDTH - 130, HEIGHT - 60,": Seleccionar")
            pygame.display.flip()
    fle_pos = 0
    #Menú Selección de cuenta
    while account3_state:
        cajon.fill(negro)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #Generación de la ubicación de los usuarios y los scores
            if acc_count == 3:
                for x in range(0,6):
                    if x % 2 == 0:
                        text(0,280,120 + (50 * x),"Usuario: ")
                        text(0,400,120 + (50 * x), delete_onespace(data[x]))
                    else:
                        text(0,300,110 + (50 * x),"Highscore: ")
                        text(0,460,110 + (50 * x), delete_onespace(data[x]))
                   
            elif acc_count == 2:
                for x in range(0,4):
                    if x % 2 == 0:
                        text(0,280,120 + (50 * x),"Usuario: ")
                        text(0,400,120 + (50 * x), delete_onespace(data[x]))
                    else:
                        text(0,300,110 + (50 * x),"Highscore: ")
                        text(0,460,110 + (50 * x), delete_onespace(data[x]))
            elif acc_count == 1:
                for x in range(0,2):
                    if x % 2 == 0:
                        text(0,280,120 + (50 * x),"Usuario: ")
                        text(0,400,120 + (50 * x), delete_onespace(data[x]))
                    else:
                        text(0,300,110 + (50 * x),"Highscore: ")
                        text(0,460,110 + (50 * x), delete_onespace(data[x]))

                   
            else: #Pantalla generada al no haber cuentas para elegir
                
                no_account("3")
                pygame.time.delay(1000)
                no_account("2")
                pygame.time.delay(1000)
                no_account("1")
                pygame.time.delay(1000)
                account3_state = False
                title_state = True
                ex = True
                fle_pos = 0
                break
            
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    account3_state = False
                    account1_state = True
                    fle_pos = 0
                    break
                if event.key == pygame.K_UP and acc_count == 3:
                    if fle_pos == 1:
                        fle_pos = 0

                    elif fle_pos == 2:
                        fle_pos = 1


                elif event.key == pygame.K_UP and acc_count == 2:
                    if fle_pos == 1:
                        fle_pos = 0

                if event.key == pygame.K_DOWN and acc_count == 3:
                    if fle_pos == 0:
                        fle_pos = 1

                    elif fle_pos == 1:
                        fle_pos = 2

                elif event.key == pygame.K_DOWN and acc_count == 2:
                    if fle_pos == 0:
                        fle_pos = 1

                #Asignación al seleccionar una cuenta
                if event.key == pygame.K_RETURN:
                        if fle_pos == 0:
                            acc = delete_onespace(data[0])
                            acc_id = 1
                            account3_state = False
                            account_choosen = True
                            title_state = True
                            ex = True
                            fle_pos = 0
                            break
                            
                        elif fle_pos == 1:
                            acc = delete_onespace(data[2])
                            acc_id = 3
                            account3_state = False
                            account_choosen = True
                            title_state = True
                            ex = True
                            fle_pos = 0
                            break
                        elif fle_pos == 2:
                            acc = delete_onespace(data[4])
                            acc_id = 5
                            account3_state = False
                            account_choosen = True
                            title_state = True
                            ex = True
                            fle_pos = 0
                            break
            if fle_pos == 0:
                selector(180,140)
            elif fle_pos == 1:
                selector(180,240)
            else:
                selector(180,340)
            



            cajon.blit(keys,(15, HEIGHT - 80))
            cajon.blit(enter,(WIDTH - 190, HEIGHT - 75))
            cajon.blit(esc,(WIDTH / 2 - 110, HEIGHT - 75))
            text(-10 , 50, HEIGHT - 60,": Mover")
            text(-10 , WIDTH / 2 - 40, HEIGHT - 60,": Atrás")
            text(-10 , WIDTH - 130, HEIGHT - 60,": Seleccionar")
            cajon.blit(select,(70,0))
            pygame.display.flip()
    fle_pos = 0
    #Menú Eliminación de cuenta
    while account4_state:
        cajon.fill(negro)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            #Generación ubicación de las cuentas y los puntajes
            if acc_count == 3:
                for x in range(0,6):
                    if x % 2 == 0:
                        text(0,280,120 + (50 * x),"Usuario: ")
                        text(0,400,120 + (50 * x), delete_onespace(data[x]))
                    else:
                        text(0,300,110 + (50 * x),"Highscore: ")
                        text(0,460,110 + (50 * x), delete_onespace(data[x]))
                   
            elif acc_count == 2:
                for x in range(0,4):
                    if x % 2 == 0:
                        text(0,280,120 + (50 * x),"Usuario: ")
                        text(0,400,120 + (50 * x), delete_onespace(data[x]))
                    else:
                        text(0,300,110 + (50 * x),"Highscore: ")
                        text(0,460,110 + (50 * x), delete_onespace(data[x]))
            elif acc_count == 1:
                for x in range(0,2):
                    if x % 2 == 0:
                        text(0,280,120 + (50 * x),"Usuario: ")
                        text(0,400,120 + (50 * x), delete_onespace(data[x]))
                    else:
                        text(0,300,110 + (50 * x),"Highscore: ")
                        text(0,460,110 + (50 * x), delete_onespace(data[x]))
                   
            else: #Pantalla generada al no haber cuentas para eliminar
                no_account("3")
                pygame.time.delay(1000)
                no_account("2")
                pygame.time.delay(1000)
                no_account("1")
                pygame.time.delay(1000)
                account4_state = False
                title_state = True
                ex = True
                fle_pos = 0
                break
            
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        account4_state = False
                        account1_state = True
                        fle_pos = 0
                        break
                    if event.key == pygame.K_UP and acc_count == 3:
                        if fle_pos == 1:
                            fle_pos = 0

                        elif fle_pos == 2:
                            fle_pos = 1


                    elif event.key == pygame.K_UP and acc_count == 2:
                        if fle_pos == 1:
                            fle_pos = 0

                        

                    if event.key == pygame.K_DOWN and acc_count == 3:
                        if fle_pos == 0:
                            fle_pos = 1

                        elif fle_pos == 1:
                            fle_pos = 2


                    elif event.key == pygame.K_DOWN and acc_count == 2:
                        if fle_pos == 0:
                            fle_pos = 1


                    #Pantalla generada al eliminar una cuenta
                    if event.key == pygame.K_RETURN:
                        acc_id = 0
                        if fle_pos == 0:
                            data.pop(0)
                            data.pop(0)
                            write_save(data)
                            acc_count -= 1
                            account_del("3")
                            pygame.time.delay(1000)
                            account_del("2")
                            pygame.time.delay(1000)
                            account_del("1")
                            pygame.time.delay(1000)
                            account4_state = False
                            account_choosen = False
                            title_state = True
                            ex = True
                            fle_pos = 0
                            break
                            
                        elif fle_pos == 1:
                            data.pop(2)
                            data.pop(2)
                            write_save(data)
                            acc_count -= 1
                            account_del("3")
                            pygame.time.delay(1000)
                            account_del("2")
                            pygame.time.delay(1000)
                            account_del("1")
                            pygame.time.delay(1000)
                            account4_state = False
                            account_choosen = False
                            title_state = True
                            ex = True
                            fle_pos = 0
                            break
                        elif fle_pos == 2:
                            data.pop(4)
                            data.pop(4)
                            write_save(data)
                            acc_count -= 1
                            account_del("3")
                            pygame.time.delay(1000)
                            account_del("2")
                            pygame.time.delay(1000)
                            account_del("1")
                            pygame.time.delay(1000)
                            account4_state = False
                            account_choosen = False
                            title_state = True
                            ex = True
                            fle_pos = 0
                            break

            if fle_pos == 0:
                selector(180,140)
            elif fle_pos == 1:
                selector(180,240)
            elif fle_pos == 2:
                selector(180,340)
            
            cajon.blit(keys,(15, HEIGHT - 80))
            cajon.blit(enter,(WIDTH - 190, HEIGHT - 75))
            cajon.blit(esc,(WIDTH / 2 - 110, HEIGHT - 75))
            text(-10 , 50, HEIGHT - 60,": Mover")
            text(-10 , WIDTH / 2 - 40, HEIGHT - 60,": Atrás")
            text(-10 , WIDTH - 130, HEIGHT - 60,": Seleccionar")
            cajon.blit(select,(70,0))
            pygame.display.flip()


