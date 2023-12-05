import pygame
import random
from explicacao import iniciar_explicacao

pygame.init()

# variaveis de configuração
largura, altura = 400, 450
tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('Rumo ao NP!')
timer = pygame.time.Clock()
fps = 60
fonte = pygame.font.Font('freesansbold.ttf', 24)

# cores do jogo 2048
cores = { 0 : (204, 192, 179),
          2 : (238, 228, 218),
          4 : (237, 224, 200),
          8 : (242, 177, 121),
          16 : (245, 149, 99),
          32 : (246, 124, 95),
          64 : (246, 94, 59),
          128 : (237, 207, 114),
          256 : (237, 204, 97),
          512 : (237, 200, 80),
          1024 : (237, 197, 63),
          2048 : (237, 194, 46),
          'light text' : (249, 246, 242),
          'dark text' : (119, 110, 101),
          'maior' : (0, 0, 0),
          'fundo_tela' : (187, 173, 160)}

# variaveis iniciais do jogo
valores_iniciais_celulas = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
game_over = False
gerar_nova_celula = True
init_count = 0
direcao = ''
pontuacao = 0
tamanho_tabuleiro = 4

# reseta textos e tabuleiro també
def gerar_tela_game_over():
    pygame.draw.rect(tela, 'gray', [50, 50, 300, 100], 0, 10)
    
    game_over_text1 = fonte.render('Game Over!', True, 'black')
    tela.blit(game_over_text1, (130, 65))
    

def realizar_jogada(direcao, tabuleiro):
    global pontuacao
    merged = [ [False for i in range(tamanho_tabuleiro)] for j in range(tamanho_tabuleiro) ]
    match direcao:
        case 'UP':
            for i in range(tamanho_tabuleiro):
                for j in range(tamanho_tabuleiro):
                    nova_posicao = 0
                    if i > 0:
                        for q in range(i):
                            if tabuleiro[q][j] == 0: nova_posicao += 1
                        if nova_posicao > 0:
                            tabuleiro[i - nova_posicao][j] = tabuleiro[i][j]
                            tabuleiro[i][j] = 0
                        if tabuleiro[i - nova_posicao - 1][j] == tabuleiro[i - nova_posicao][j] and not merged[i - nova_posicao][j] \
                                and not merged[i - nova_posicao - 1][j]:
                            tabuleiro[i - nova_posicao - 1][j] *= 2
                            pontuacao += tabuleiro[i - nova_posicao - 1][j]
                            tabuleiro[i - nova_posicao][j] = 0
                            merged[i - nova_posicao - 1][j] = True

        case 'DOWN':
            for i in range(3):
                for j in range(tamanho_tabuleiro):
                    nova_posicao = 0
                    for q in range(i + 1):
                        if tabuleiro[3 - q][j] == 0: nova_posicao += 1
                    if nova_posicao > 0:
                        tabuleiro[2 - i + nova_posicao][j] = tabuleiro[2 - i][j]
                        tabuleiro[2 - i][j] = 0
                    if 3 - i + nova_posicao <= 3:
                        if tabuleiro[2 - i + nova_posicao][j] == tabuleiro[3 - i + nova_posicao][j] and not merged[3 - i + nova_posicao][j] \
                                and not merged[2 - i + nova_posicao][j]:
                            tabuleiro[3 - i + nova_posicao][j] *= 2
                            pontuacao += tabuleiro[3 - i + nova_posicao][j]
                            tabuleiro[2 - i + nova_posicao][j] = 0
                            merged[3 - i + nova_posicao][j] = True

        case 'LEFT':
            for i in range(tamanho_tabuleiro):
                for j in range(tamanho_tabuleiro):
                    nova_posicao = 0
                    for q in range(j):
                        if tabuleiro[i][q] == 0:
                            nova_posicao += 1
                    if nova_posicao > 0:
                        tabuleiro[i][j - nova_posicao] = tabuleiro[i][j]
                        tabuleiro[i][j] = 0
                    if tabuleiro[i][j - nova_posicao] == tabuleiro[i][j - nova_posicao - 1] and not merged[i][j - nova_posicao - 1] \
                            and not merged[i][j - nova_posicao]:
                        tabuleiro[i][j - nova_posicao - 1] *= 2
                        pontuacao += tabuleiro[i][j - nova_posicao - 1]
                        tabuleiro[i][j - nova_posicao] = 0
                        merged[i][j - nova_posicao - 1] = True

        case 'RIGHT':
            for i in range(tamanho_tabuleiro):
                for j in range(tamanho_tabuleiro):
                    nova_posicao = 0
                    for q in range(j):
                        if tabuleiro[i][3 - q] == 0:
                            nova_posicao += 1
                    if nova_posicao > 0:
                        tabuleiro[i][3 - j + nova_posicao] = tabuleiro[i][3 - j]
                        tabuleiro[i][3 - j] = 0
                    if tamanho_tabuleiro - j + nova_posicao <= 3:
                        if tabuleiro[i][tamanho_tabuleiro - j + nova_posicao] == tabuleiro[i][3 - j + nova_posicao] and not merged[i][4 - j + nova_posicao] \
                                and not merged[i][3 - j + nova_posicao]:
                            tabuleiro[i][tamanho_tabuleiro - j + nova_posicao] *= 2
                            pontuacao += tabuleiro[i][4 - j + nova_posicao]
                            tabuleiro[i][3 - j + nova_posicao] = 0
                            merged[i][tamanho_tabuleiro - j + nova_posicao] = True
    return tabuleiro

def add_celulas_inicais(tabuleiro):
    count = 0
    tabuleiro_cheio = False
    while any(0 in row for row in tabuleiro) and count < 1: # adicionando aleatoriamente
        linhas = random.randint(0, 3)
        colunas = random.randint(0, 3)
        if tabuleiro[linhas][colunas] == 0:
            count += 1
            if random.randint(1, 10) == 10:
                tabuleiro[linhas][colunas] = tamanho_tabuleiro
            else:
                tabuleiro[linhas][colunas] = 2
    if count < 1:
        tabuleiro_cheio = True
    return tabuleiro, tabuleiro_cheio

# desenhando o tabuleiro
def gerar_tabuleiro():
    pygame.draw.rect(tela, cores['fundo_tela'], [0, 0, 400, 400], 0, 10)
    score_text = fonte.render(f'Pontuação: {pontuacao}', True, 'black')
    tela.blit(score_text, (10, 410))

def gerar_celulas(board):
    global complexidades
    # valores brutos, depois vou refatorar
    for i in range(tamanho_tabuleiro):
        for j in range(tamanho_tabuleiro):
            celula = board[i][j]
            if celula > 256 and celula < 128:
                vc_color = cores['light text']
            else: 
                vc_color = cores['dark text']
            if celula <= 128: color = cores[celula]
            else: color = cores['maior']
            pygame.draw.rect(tela, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
            if celula > 0:
                comprimento_valor = len(complexidades[celula])
                tamanho = 48 - (4 * comprimento_valor)
                fonte = pygame.font.Font('freesansbold.ttf', tamanho)
                value_text = fonte.render(complexidades[celula], True, vc_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))
                tela.blit(value_text, text_rect)
                pygame.draw.rect(tela, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5)


complexidades: dict[int, str] = {
    2 : "1",
    4 : "log n",
    8 : "n",
    16 : "n*log n",
    32 : "n^2",
    64 : "n^3",
    128 : "B^n",
    256 : "NP",
    512 : "NPH",
    1024 : "NPC",
}
# main game loop
continuar_rodando = True
while continuar_rodando:
    timer.tick(fps)
    tela.fill('gray')
    gerar_tabuleiro()
    gerar_celulas(valores_iniciais_celulas)
    if gerar_nova_celula or init_count < 2:
        valores_iniciais_celulas, game_over = add_celulas_inicais(valores_iniciais_celulas)
        gerar_nova_celula = False
        init_count += 1
    if direcao != '':
        valores_iniciais_celulas = realizar_jogada(direcao, valores_iniciais_celulas)
        direcao = ''
        gerar_nova_celula = True
    if game_over:
        gerar_tela_game_over()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuar_rodando = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direcao = 'UP'
            elif event.key == pygame.K_DOWN:
                direcao = 'DOWN'
            elif event.key == pygame.K_LEFT:
                direcao = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                direcao = 'RIGHT'

            if game_over:
                iniciar_explicacao()
                if event.key == pygame.K_RETURN:
                    valores_iniciais_celulas = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
                    gerar_nova_celula = True
                    init_count = 0
                    pontuacao = 0
                    direcao = ''
                    game_over = False
                    
    pygame.display.flip()

pygame.quit()
