import os
import pygame 

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height =640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game") # 게임 이름

# 이미지 위치 지정
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 이미지 불러오기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 이벤트 루프
running = True # 게임이 진행 중
while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트
            running = False

    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))

    pygame.display.update()

# pygame 종료
pygame.quit()