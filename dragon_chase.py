import pygame
import math
import sys
import os
# Estas librerías son para interactuar con la ventana de Windows
import win32gui
import win32con
import win32api

# --- Configuración (Basada en tu Especificación) ---
# Intenta usar la resolución de tu monitor
pygame.init()
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
# SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080 # Descomenta si quieres un tamaño fijo

DRAGON_IMAGE_FILE = "dragon_uhd.png" # Nombre de tu imagen Ultra HD
DRAGON_SCALE = 0.5   # 1.0 es tamaño original. 0.5 es la mitad. Ajusta según la resolución de tu imagen.
DRAGON_SPEED = 5      # Velocidad de persecución
ROTATION_OFFSET = 0  # Ajusta esto (0, 90, 180, 270) si el dragón mira para otro lado

# Colores (Para el fuego, aunque el dragón será a color desde la imagen)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)

# --- Configuración de la Ventana Transparente ---
# Esto es crucial para que solo veas al dragón sobre tu escritorio
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
# pygame.display.set_caption("Dragon Desktop Pet")

# Crear una clave de color para la transparencia
# Todo lo que sea de este color exacto será invisible
fuchsia = (255, 0, 255)

# Hacer la ventana transparente e interactuable (layered window)
hwnd = pygame.display.get_wm_info()['window']
styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
# Establecer el color fucsia como la clave de transparencia
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

# Hacer que la ventana esté siempre encima de todo
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


# --- Clase del Fuego (Partículas) ---
# Para que "escupa fuego", necesitamos un sistema de partículas simple
class FireParticle:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle + (pygame.time.get_ticks() % 20 - 10) / 10.0 # Un poco de aleatoriedad
        self.speed = 10
        self.radius = 15
        self.life = 1.0 # 1.0 es vida completa
        self.decay = 0.05 # Cuánto pierde de vida por frame

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.life -= self.decay
        self.radius -= 0.5 # Se encoge
        if self.radius < 1: self.radius = 1

    def draw(self, surf):
        if self.life > 0:
            # Color basado en la vida (empieza amarillo/rojo, termina transparente/negro)
            if self.life > 0.6:
                color = (255, int(255 * self.life), 0)
            else:
                color = (int(255 * self.life * 1.5), 0, 0)
            
            # Dibujar la partícula (con una pequeña variación de color)
            # Nota: El renderizado de Pygame no maneja alfa por canal de forma eficiente en ventanas transparentes
            # así que simulamos el fuego con círculos de colores sólidos
            pygame.draw.circle(surf, color, (int(self.x), int(self.y)), int(self.radius))


# --- Cargar y Preparar la Imagen (UHD) ---
if not os.path.exists(DRAGON_IMAGE_FILE):
    print(f"ERROR: No se encontró el archivo {DRAGON_IMAGE_FILE}.")
    print("Por favor, asegúrate de tener una imagen PNG con fondo transparente en esta carpeta.")
    sys.exit()

# Cargar imagen con canal alfa (transparencia)
dragon_original = pygame.image.load(DRAGON_IMAGE_FILE).convert_alpha()

# Escalar la imagen si es demasiado grande para Ultra HD directo
w, h = dragon_original.get_size()
dragon_scaled = pygame.transform.scale(dragon_original, (int(w * DRAGON_SCALE), int(h * DRAGON_SCALE)))

# Coordenadas iniciales del dragón (centro de la pantalla)
dragon_x = SCREEN_WIDTH // 2
dragon_y = SCREEN_HEIGHT // 2
dragon_rect = dragon_scaled.get_rect(center=(dragon_x, dragon_y))

# Sistema de partículas para el fuego
fire_particles = []

# --- Bucle Principal del Juego ---
clock = pygame.time.Clock()
running = True
spitting_fire = False

while running:
    # 1. Gestión de Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Salir con ESC
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Clic izquierdo para escupir fuego
                spitting_fire = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                spitting_fire = False

    # 2. Lógica de Persecución (Ubicación del Mouse)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Calcular ángulo hacia el mouse
    dx = mouse_x - dragon_x
    dy = mouse_y - dragon_y
    angle_rad = math.atan2(dy, dx)
    angle_deg = math.degrees(angle_rad) + ROTATION_OFFSET # Añadir offset si es necesario
    
    # Mover el dragón hacia el mouse (suavemente)
    dist = math.hypot(dx, dy)
    if dist > 5: # No mover si está muy cerca para evitar parpadeos
        dragon_x += (dx / dist) * DRAGON_SPEED
        dragon_y += (dy / dist) * DRAGON_SPEED

    # Rotar la imagen del dragón (Pygame rotar es lento con UHD, pero es necesario)
    # Nota: Rotar imágenes grandes cada frame puede reducir el rendimiento
    dragon_rotated = pygame.transform.rotate(dragon_scaled, -angle_deg) # Negativo porque Pygame rota anti-horario
    new_rect = dragon_rotated.get_rect(center=(dragon_x, dragon_y))

    # 3. Lógica del Fuego (Upa Fuego)
    if spitting_fire:
        # Escupir desde la "boca". Calculamos la posición de la boca basada en la rotación.
        # Asumimos que la boca está en el centro-derecha de la imagen original.
        mouth_offset_x = (w * DRAGON_SCALE) / 2
        fire_x = dragon_x + mouth_offset_x * math.cos(angle_rad)
        fire_y = dragon_y + mouth_offset_x * math.sin(angle_rad)
        
        # Crear nuevas partículas
        for _ in range(3): # Crear 3 partículas por frame
            fire_particles.append(FireParticle(fire_x, fire_y, angle_rad))

    # Actualizar partículas existentes
    for p in fire_particles[:]:
        p.update()
        if p.life <= 0:
            fire_particles.remove(p)

    # 4. Renderizado (Dibujar todo)
    # Llenar el fondo con la clave de transparencia
    screen.fill(fuchsia)

    # Dibujar fuego (detrás del dragón)
    for p in fire_particles:
        p.draw(screen)

    # Dibujar al Dragón
    screen.blit(dragon_rotated, new_rect)

    # Actualizar la pantalla
    pygame.display.flip()
    
    # Limitar a 60 FPS para no sobrecargar la CPU/GPU
    clock.tick(60)

pygame.quit()
sys.exit()