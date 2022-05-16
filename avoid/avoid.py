from random import *
import os
import pygame 
# 초기화 (반드시 필요)
pygame.init() 

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("avoid") # 게임 이름

# FPS
clock = pygame.time.Clock()
FPS = 30

########################################################################3

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트 등)
# current_path = os.path.dirname(os.path.realpath(__file__))
current_path = os.getcwd()
image_path = current_path + "/images/"

background = pygame.image.load(image_path + "background.png")

character = pygame.image.load(image_path + "character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width - (character_width / 2)
character_y_pos = screen_height - character_height

enemy = pygame.image.load(image_path + "enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 시작 시간
start_ticks = pygame.time.get_ticks()   # 현재 tick을 받아옴

to_x = 0
enemy_is_bottom = False

running = True
while running:
    dt = clock.tick(FPS)
    move = 0.5 * dt

    if enemy_is_bottom:
        enemy_x_pos = randint(0, screen_width - enemy_width)
        enemy_y_pos = 0
        enemy_is_bottom = False

    # 2. 이벤트 처리 (키보드 , 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= move
            if event.key == pygame.K_RIGHT:
                to_x += move

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    enemy_y_pos += move

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    if enemy_y_pos > screen_height - enemy_height:
        enemy_y_pos = screen_height - enemy_height
        enemy_is_bottom = True

    # 4. 충돌 처리

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
    

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(str(int(elapsed_time)), True, (50, 50, 0))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    pygame.display.update()


pygame.quit()