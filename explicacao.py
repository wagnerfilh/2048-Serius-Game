import pygame

def iniciar_explicacao():
    pygame.init()
    largura, altura = 1090, 290
    tela = pygame.display.set_mode([largura, altura])
    pygame.display.set_caption('Extras')
    timer = pygame.time.Clock()
    fps = 60
    tela.fill('gray')
    fonte = pygame.font.SysFont('Verdana', 20)
    rodar = True

    textos = [
    "(1) constante - algoritmos que executam na mesma velocidade ex: stack.push()",
    "(log n) logarítimo iterado - executam uma fração do comprimento dos dados ex: binary search",
    "(n) linear -  linear search, max(n1, n2)",
    "(n * log n) logarítmica - algoritmos eficientes em dados ordenados ex: merge sort",
    "(n^2) quadrática - algoritmos ineficientes para grandes conjuntos de dados ex: selection sort, bubble sort",
    "(n^3) cúbica - multiplicação de matrizes",
    "(B^n) exponencial - algoritmos com crescimento exponencial em relação ao tamanho dos dados",
    "NP Not Only Polynomial - Algoritmos que ainda não têm solução polinomial conhecida",
    "NP Hard - problemas que são pelo menos tão difíceis quanto os mais difíceis em NP",
    "NP Complete - problemas que são tanto NP quanto NP Hard",
    ]
    
    while rodar:
        timer.tick(fps)
        for i in range(0, len(textos)):
            escrever = fonte.render(textos[i], True, 'black')
            altura_1 = 24 * (i + 1)
            tela.blit(escrever, (10, altura_1))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False
        pygame.display.flip()
    pygame.quit()

iniciar_explicacao()
        