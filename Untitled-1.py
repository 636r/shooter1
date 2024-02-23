from pygame import *  
from pygame.sprite import Group 
from random import randint  

 
 
class GameSprite(sprite.Sprite):  
  
    def __init__(self, player_image , player_x , player_y, size_x, syze_y, player_speed):  
        sprite.Sprite.__init__(self)  
        self.image = transform.scale(image.load(player_image),(50 , 50))   
        self.speed = player_speed  
        self.rect = self.image.get_rect()  
        self.rect.x = player_x  
        self.rect.y = player_y  
    def reset (self):  
        window.blit(self.image,(self.rect.x , self.rect.y))  
class Bullet(GameSprite): 
    def update(self): 
        self.rect.y += self.speed  
        #зникає дійдучи до краю екрану 
        if self.rect.y < 0: 
            self.kill()  
class Player(GameSprite):  
    def update(self):  
        keys_pressed = key.get_pressed()  
        if keys_pressed [K_LEFT] and self.rect.x > 5 :  
            self.rect.x -= self.speed    
  
            keys_pressed = key.get_pressed()  
        if keys_pressed [K_RIGHT] and self.rect.x < win_width - 80 :  
            self.rect.x += self.speed  
  
  
    def fire(self):  
        pass 
         
        bullet = Bullet(ammo, self.rect.x, self.rect.y, 15, 20, -15) 
        bullets.add(bullet) 
#лічильник збитих і пропущених кораблів  
 
score = 0  
lost = 0  
class Enemy(GameSprite):  
    def update(self):  
        self.rect.y += self.speed  
        global lost   
  
        if self.rect.y > win_height:  
            self.rect.x = randint(80, win_width - 80)  
            self.rect.y = 0  
            lost = lost + 1  
         
 
#ігрова сцена  
win_width = 700  
win_height = 500  
window = display.set_mode((win_width, win_height))  
display.set_caption("Shooter Game")  
background = transform.scale(image.load("hex_grass_2.jpg"), (win_width, win_height))  
#шрифти ы написи  
font.init()  
font2 = font.Font(None, 36)  
font1 = font.Font(None,100) 
#зображення  
asteroid_img = 'asteroid.png'  
ammo = 'bullet.png'  
rocket = 'rocket.png'  
  
 
#спайти  
rocket = Player(rocket, 5, win_height - 100, 80, 100, 20)  
asteroids = sprite.Group() 
for i in range(1, 2): 
    asteroid = Enemy( asteroid_img, randint(80, win_height - 80), -30,  80, 50, randint(1, 5)) 
    asteroids.add(asteroid) 
#змінна гра закінчилась  
bullets = sprite.Group() 
 
finish = False  
 
 
#Основний цикл гри  
run = True  
lose = font1.render("YOU lose", True, (182,21,21)) 
win = font1.render("YOU win", True, (34,139,34)) 
while run:  
  
    #подія натискання на кнопку закрити  
      
    for e in event.get():  
        if e.type == QUIT:  
            run = False  
        elif e.type == KEYDOWN: 
            if e.key == K_SPACE: 
                rocket.fire() 
                 
    if not finish:  
        
        window.blit(background, (0, 0))  
        rocket.update()  
 
         
        asteroids.update() 
        asteroids.draw(window) 
        bullets.update() 
        bullets.draw(window) 
        rocket.reset()  
        
        if lost >= 5: 
            finish = True 
            window.blit(lose, (200, 200)) 
        if score >= 10: 
            finish = True 
            window.blit(win, (200, 200))  
        if sprite.spritecollide(rocket,asteroids, False): 
            window.blit(lose, (200, 200)) 
            finish = True 
 
        collides = sprite.groupcollide(bullets,asteroids, True, True) 
         
      
        collidesds = sprite.groupcollide(asteroids,bullets, True, True) 
        for s in collidesds: 
            asteroid = Enemy( asteroid_img, randint(80, win_height - 80), -30,580, 50, randint(1, 5)) 
            asteroids.add(asteroid) 
            score = score + 5
 
         #пишемо текст на екрані  
  
        text = font2.render("Рахунок:" + str(score), 1, (255, 255, 255))  
        window.blit(text, (10, 20))  
  
        text_lose = font2.render("Пропущено:" + str(lost), 1, (255, 255, 255))  
        window.blit(text_lose, (10, 50))  
  
        #рухи спрайтів  
   
       
        
        
       
    else: 
        score = 0 
        lost = 0 
        for m in monsters: 
            m.kill() 
             
        for m in bullets: 
            m.kill() 
        for m in asteroids: 
            m.kill() 
        time.delay(3000) 
        finish = False 
        monsters = sprite.Group()  
        for i in range(1, 5):  
            monster = Enemy( randint(80, win_width - 80), -40, 80, 50, randint(1, 5))  
            monsters.add(monster)   
        asteroids = sprite.Group() 
        for i in range(1, 2): 
            asteroid = Enemy( asteroid_img, randint(80, win_height - 80), -30,  80, 50, randint(1, 5)) 
            asteroids.add(asteroid) 
    display.update()  
  
    time.delay(50)
