import pygame
import sys
import json

pygame.init()

screen_width = 1280
bar_size = int(screen_width/45)
screen_height = bar_size*13

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

with open("ans/res.json") as file:
    answers = json.load(file)

current = 1

colors = [
    "#000000",
    "#9b5de5",
    "#f15bb5",
    "#fee440",
    "#00bbf9",
    "#00f5d4"
]

font_reg = pygame.font.Font("data/Pretendard-Regular.ttf", 25)
font_bold = pygame.font.Font("data/Pretendard-Bold.ttf", 80)

def draw_text(x, y, text, font):
    surface = font.render(text, True, colors[0])
    screen.blit(surface, (x, y))

def draw(current):
    screen.fill("#ffffff")

    for i in range(1, 5+1):
        count = answers[str(current)][str(i)]
        pygame.draw.rect(screen, colors[i], [bar_size*2, i*(bar_size+10), count*bar_size, bar_size])
        draw_text((count+2.5)*bar_size, i*(bar_size+10), f"{count}", font_reg)
        draw_text(bar_size, i*(bar_size+10), f"{i}", font_reg)

    draw_text(bar_size, bar_size*8, f"{current}번 문항", font_bold)

# for i in range(1, 45+1):
#     draw(i)
#     pygame.image.save(screen, f"ans/vis/num_{i}.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if current+1 <= 45:
                    current += 1
            if event.key == pygame.K_LEFT:
                if current-1 >= 1:
                    current -= 1
                
    dt = clock.tick(60)/(1000/60)

    draw(current)

    pygame.display.update()