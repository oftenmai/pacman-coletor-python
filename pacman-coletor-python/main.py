import pygame
import random
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def resource_path(relative_path):
    return os.path.join(BASE_DIR, relative_path)

# Inicializa o jogo
pygame.init()

# Configuração da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("TESTE DE JOGO")

# Cores
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Configuração do jogador
tamanho = 50
x = LARGURA // 2
y = ALTURA // 2
velocidade = 8

# Carregar a imagem do jogador
imagem_jogador = pygame.image.load(resource_path("assets/pacman.png"))# Usa o caminho correto
imagem_jogador = pygame.transform.scale(imagem_jogador, (tamanho, tamanho))

# Configuração dos pontos
ponto_x = random.randint(0, LARGURA - tamanho)
ponto_y = random.randint(0, ALTURA - tamanho)
pontos = 0

# Contador de pontos
pontos_necessarios = 15  # Agora são 15 pontos

# Tempo limite
tempo_limite = 30 * 1000  # 30 segundos em milissegundos
tempo_inicial = pygame.time.get_ticks()

# Fonte
fonte = pygame.font.Font(None, 36)

# Carregar e tocar a música
pygame.mixer.music.load(resource_path("assets/04 - Flying Battery Zone 1 MP3.mp3")) # Carregar o arquivo correto
pygame.mixer.music.play(-1, 0.0)  # A música vai tocar infinitamente, começando no início

# Exibir mensagem inicial
tela.fill(PRETO)
mensagem_inicial = fonte.render("COLETE 15 PONTOS", True, AZUL)
tela.blit(mensagem_inicial, (LARGURA // 2 - 120, ALTURA // 2 - 50))  # Posição da mensagem
pygame.display.update()

pygame.time.delay(2000)  # Exibe a mensagem por 2 segundos

# Loop do jogo
rodando = True
while rodando:
    pygame.time.delay(20)  # Controla a velocidade do jogo
    tela.fill(PRETO)  # Limpa a tela no início do loop

    # Calculando o tempo decorrido
    tempo_atual = pygame.time.get_ticks()
    tempo_restante = tempo_limite - (tempo_atual - tempo_inicial)
    segundos_restantes = max(0, tempo_restante // 1000)

    # Verifica se o tempo acabou ou se os pontos foram alcançados
    if segundos_restantes == 0 or pontos >= pontos_necessarios:
        rodando = False  # Encerra o jogo

    # Exibir tempo na tela
    texto_tempo = fonte.render(f"Tempo: {segundos_restantes}s", True, AZUL)
    tela.blit(texto_tempo, (20, 20))

    # Exibir mensagem de vitória se o jogador ganhar
    if pontos >= pontos_necessarios:
        tela.fill(PRETO)  # Limpa a tela
        mensagem = fonte.render("VOCÊ VENCEU!", True, AZUL)
        tela.blit(mensagem, (LARGURA // 2 - 100, ALTURA // 2))
        pygame.display.update()
        pygame.time.delay(3000)  # Exibe por 3 segundos antes de fechar

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Controles do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and x > 0:
        x -= velocidade
    if teclas[pygame.K_RIGHT] and x < LARGURA - tamanho:
        x += velocidade
    if teclas[pygame.K_UP] and y > 0:
        y -= velocidade
    if teclas[pygame.K_DOWN] and y < ALTURA - tamanho:
        y += velocidade

    # Verificar se pegou o ponto
    if abs(x - ponto_x) < tamanho and abs(y - ponto_y) < tamanho:
        pontos += 1
        ponto_x = random.randint(0, LARGURA - tamanho)
        ponto_y = random.randint(0, ALTURA - tamanho)

    # Desenha o jogador com a imagem
    tela.blit(imagem_jogador, (x, y))

    # Desenha o ponto
    ponto = pygame.draw.circle(tela, VERMELHO, (ponto_x, ponto_y), 10)

    # Exibe a pontuação
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, AMARELO)
    tela.blit(texto_pontos, (10, 50))

    # Atualiza a tela
    pygame.display.update()

# Finaliza o jogo
pygame.quit()
