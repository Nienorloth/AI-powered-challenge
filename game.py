import pygame
import sys
import math

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Mi Juego 2D"

# Colores (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
PINK = (255, 192, 203)
YELLOW = (255, 255, 0)
SKIN = (255, 220, 177)
GRAY = (128, 128, 128)
DARK_BROWN = (101, 67, 33)
LIGHT_BROWN = (160, 82, 45)
CREAM = (255, 253, 208)
DARK_GRAY = (64, 64, 64)
LIGHT_GRAY = (192, 192, 192)
DARK_BLUE = (0, 0, 139)
LIGHT_PINK = (255, 182, 193)

# Velocidad del jugador
PLAYER_SPEED = 5

# Clases de personaje
KARATEKA = "karateka"
MAGE = "mage"
PIRATE = "pirate"

# Estados del juego
NAME_INPUT = "name_input"
CLASS_SELECTION = "class_selection"
PLAYING = "playing"

# Dimensiones de las habitaciones
ROOM_WIDTH = 800
ROOM_HEIGHT = 600
KITCHEN_WIDTH = 200
KITCHEN_HEIGHT = 300
LOBBY_WIDTH = 200
LOBBY_HEIGHT = 300

class ClassSelection:
    def __init__(self, screen):
        """Inicializa la pantalla de selección de clases"""
        self.screen = screen
        self.selected_class = None
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        
    def draw(self):
        """Dibuja la pantalla de selección de clases"""
        self.screen.fill(BLACK)
        
        # Título
        title = self.font_large.render("¡Elige tu Clase!", True, WHITE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 80))
        self.screen.blit(title, title_rect)
        
        # Instrucciones
        instruction = self.font_medium.render("Presiona 1, 2 o 3 para seleccionar", True, WHITE)
        instruction_rect = instruction.get_rect(center=(WINDOW_WIDTH//2, 120))
        self.screen.blit(instruction, instruction_rect)
        
        # Clase 1: Karateka
        self.draw_class_option(150, 200, "1", "KARATEKA", 
                              "Artes Marciales", "Puños, Patadas, Defensa", 
                              "Velocidad alta, Ataques cuerpo a cuerpo")
        
        # Clase 2: Mago
        self.draw_class_option(400, 200, "2", "MAGO", 
                              "Magia Arcana", "Hechizos, Poción, Escudo", 
                              "Poder mágico, Ataques a distancia")
        
        # Clase 3: Pirata
        self.draw_class_option(650, 200, "3", "PIRATA", 
                              "Aventura Marina", "Espada, Cañón, Gancho", 
                              "Fuerza bruta, Ataques poderosos")
        
        # Información adicional
        info = self.font_small.render("Presiona ENTER para confirmar tu elección", True, YELLOW)
        info_rect = info.get_rect(center=(WINDOW_WIDTH//2, 550))
        self.screen.blit(info, info_rect)
        
        pygame.display.flip()
    
    def draw_class_option(self, x, y, key, name, weapon, abilities, description):
        """Dibuja una opción de clase"""
        # Marco de la clase
        pygame.draw.rect(self.screen, WHITE, (x-10, y-10, 200, 300), 3)
        pygame.draw.rect(self.screen, DARK_GRAY, (x-5, y-5, 190, 290))
        
        # Tecla
        key_text = self.font_large.render(key, True, YELLOW)
        key_rect = key_text.get_rect(center=(x+90, y+20))
        self.screen.blit(key_text, key_rect)
        
        # Nombre de la clase
        name_text = self.font_medium.render(name, True, WHITE)
        name_rect = name_text.get_rect(center=(x+90, y+50))
        self.screen.blit(name_text, name_rect)
        
        # Arma
        weapon_text = self.font_small.render(f"Arma: {weapon}", True, GREEN)
        weapon_rect = weapon_text.get_rect(center=(x+90, y+80))
        self.screen.blit(weapon_text, weapon_rect)
        
        # Habilidades
        abilities_text = self.font_small.render(f"Habilidades:", True, BLUE)
        abilities_rect = abilities_text.get_rect(center=(x+90, y+110))
        self.screen.blit(abilities_text, abilities_rect)
        
        abilities_list = abilities.split(", ")
        for i, ability in enumerate(abilities_list):
            ability_text = self.font_small.render(f"• {ability}", True, WHITE)
            ability_rect = ability_text.get_rect(center=(x+90, y+130+i*20))
            self.screen.blit(ability_text, ability_rect)
        
        # Descripción
        desc_text = self.font_small.render(description, True, PINK)
        desc_rect = desc_text.get_rect(center=(x+90, y+220))
        self.screen.blit(desc_text, desc_rect)
    
    def handle_input(self, keys):
        """Maneja la entrada para selección de clase"""
        if keys[pygame.K_1]:
            self.selected_class = KARATEKA
        elif keys[pygame.K_2]:
            self.selected_class = MAGE
        elif keys[pygame.K_3]:
            self.selected_class = PIRATE
        
        return keys[pygame.K_RETURN] and self.selected_class is not None

class NameInput:
    def __init__(self, screen):
        """Inicializa la pantalla de entrada de nombre"""
        self.screen = screen
        self.player_name = ""
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        self.input_active = True
        
    def draw(self):
        """Dibuja la pantalla de entrada de nombre"""
        self.screen.fill(BLACK)
        
        # Título
        title = self.font_large.render("¡Bienvenida!", True, WHITE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 150))
        self.screen.blit(title, title_rect)
        
        # Instrucción
        instruction = self.font_medium.render("Ingresa tu nombre:", True, WHITE)
        instruction_rect = instruction.get_rect(center=(WINDOW_WIDTH//2, 220))
        self.screen.blit(instruction, instruction_rect)
        
        # Campo de entrada
        input_rect = pygame.Rect(WINDOW_WIDTH//2 - 200, 280, 400, 50)
        pygame.draw.rect(self.screen, WHITE, input_rect, 3)
        pygame.draw.rect(self.screen, DARK_GRAY, input_rect)
        
        # Texto del nombre
        if self.player_name:
            name_text = self.font_medium.render(self.player_name, True, WHITE)
            name_rect = name_text.get_rect(center=input_rect.center)
            self.screen.blit(name_text, name_rect)
        else:
            placeholder = self.font_medium.render("Escribe tu nombre aquí...", True, GRAY)
            placeholder_rect = placeholder.get_rect(center=input_rect.center)
            self.screen.blit(placeholder, placeholder_rect)
        
        # Instrucciones de teclado
        instructions = [
            "• Escribe tu nombre usando el teclado",
            "• Presiona BACKSPACE para borrar",
            "• Presiona ENTER cuando termines"
        ]
        
        for i, instruction in enumerate(instructions):
            inst_text = self.font_small.render(instruction, True, YELLOW)
            inst_rect = inst_text.get_rect(center=(WINDOW_WIDTH//2, 380 + i*30))
            self.screen.blit(inst_text, inst_rect)
        
        # Botón de continuar
        if self.player_name.strip():
            continue_text = self.font_medium.render("Presiona ENTER para continuar", True, GREEN)
            continue_rect = continue_text.get_rect(center=(WINDOW_WIDTH//2, 500))
            self.screen.blit(continue_text, continue_rect)
        
        pygame.display.flip()
    
    def handle_input(self, event):
        """Maneja la entrada de texto"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.player_name.strip():
                return True
            elif event.key == pygame.K_BACKSPACE:
                self.player_name = self.player_name[:-1]
            elif event.unicode.isprintable() and len(self.player_name) < 20:
                self.player_name += event.unicode
        return False

class NPC:
    def __init__(self, x, y, gender="male"):
        """Inicializa un NPC"""
        self.x = x
        self.y = y
        self.gender = gender
        self.width = 40
        self.height = 50
        
    def draw(self, screen):
        """Dibuja el NPC"""
        if self.gender == "male":
            # Papá
            # Cuerpo (camisa azul)
            pygame.draw.rect(screen, DARK_BLUE, (self.x + 10, self.y + 25, 20, 25))
            # Cabeza
            pygame.draw.circle(screen, SKIN, (self.x + 20, self.y + 20), 12)
            # Cabello castaño oscuro
            pygame.draw.circle(screen, DARK_BROWN, (self.x + 20, self.y + 15), 15)
            pygame.draw.circle(screen, SKIN, (self.x + 20, self.y + 20), 12)
            # Ojos
            pygame.draw.circle(screen, BLACK, (self.x + 16, self.y + 17), 2)
            pygame.draw.circle(screen, BLACK, (self.x + 24, self.y + 17), 2)
            # Bigote
            pygame.draw.arc(screen, DARK_BROWN, (self.x + 15, self.y + 22, 10, 4), 0, math.pi, 3)
            # Piernas (pantalones)
            pygame.draw.line(screen, GRAY, (self.x + 15, self.y + 50), (self.x + 15, self.y + 60), 4)
            pygame.draw.line(screen, GRAY, (self.x + 25, self.y + 50), (self.x + 25, self.y + 60), 4)
        else:
            # Mamá
            # Cuerpo (vestido rosa claro)
            pygame.draw.rect(screen, LIGHT_PINK, (self.x + 10, self.y + 25, 20, 25))
            # Cabeza
            pygame.draw.circle(screen, SKIN, (self.x + 20, self.y + 20), 12)
            # Cabello rubio
            pygame.draw.circle(screen, YELLOW, (self.x + 20, self.y + 15), 15)
            pygame.draw.circle(screen, SKIN, (self.x + 20, self.y + 20), 12)
            # Ojos
            pygame.draw.circle(screen, BLACK, (self.x + 16, self.y + 17), 2)
            pygame.draw.circle(screen, BLACK, (self.x + 24, self.y + 17), 2)
            # Boca sonriente
            pygame.draw.arc(screen, BLACK, (self.x + 16, self.y + 20, 8, 6), 0, math.pi, 2)
            # Piernas
            pygame.draw.line(screen, BLACK, (self.x + 15, self.y + 50), (self.x + 15, self.y + 60), 4)
            pygame.draw.line(screen, BLACK, (self.x + 25, self.y + 50), (self.x + 25, self.y + 60), 4)

class Environment:
    def __init__(self):
        """Inicializa el ambiente de la casa"""
        self.obstacles = []
        self.setup_obstacles()
        
    def setup_obstacles(self):
        """Configura todos los obstáculos de la casa"""
        self.obstacles = []
        
        # Paredes exteriores
        self.obstacles.append(pygame.Rect(0, 0, WINDOW_WIDTH, 20))  # Pared superior
        self.obstacles.append(pygame.Rect(0, 0, 20, WINDOW_HEIGHT))  # Pared izquierda
        self.obstacles.append(pygame.Rect(WINDOW_WIDTH-20, 0, 20, WINDOW_HEIGHT))  # Pared derecha
        self.obstacles.append(pygame.Rect(0, WINDOW_HEIGHT-20, WINDOW_WIDTH, 20))  # Pared inferior
        
        # Paredes internas
        self.obstacles.append(pygame.Rect(200, 0, 20, 300))  # Pared entre sala y cocina
        self.obstacles.append(pygame.Rect(580, 0, 20, 300))  # Pared entre sala y lobby
        self.obstacles.append(pygame.Rect(200, 280, 400, 20))  # Pared horizontal entre habitaciones
        
        # Libreros
        self.obstacles.append(pygame.Rect(50, 100, 120, 200))  # Librero izquierdo
        self.obstacles.append(pygame.Rect(630, 100, 120, 200))  # Librero derecho
        
        # Mesa del comedor
        self.obstacles.append(pygame.Rect(300, 300, 200, 100))
        
        # Sillas del comedor
        self.obstacles.append(pygame.Rect(280, 320, 20, 30))  # Silla izquierda
        self.obstacles.append(pygame.Rect(500, 320, 20, 30))  # Silla derecha
        
        # Muebles de cocina
        self.obstacles.append(pygame.Rect(20, 320, 60, 40))  # Refrigerador
        self.obstacles.append(pygame.Rect(100, 320, 80, 40))  # Estufa
        self.obstacles.append(pygame.Rect(20, 380, 160, 40))  # Mesada
        
        # Muebles del lobby
        self.obstacles.append(pygame.Rect(600, 320, 60, 40))  # Mesa de entrada
        self.obstacles.append(pygame.Rect(600, 380, 60, 40))  # Banco
        self.obstacles.append(pygame.Rect(680, 320, 100, 100))  # Sofá
        
    def draw(self, screen):
        """Dibuja el ambiente completo de la casa"""
        # Piso principal
        pygame.draw.rect(screen, CREAM, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        
        # Dibujar todas las habitaciones
        self.draw_main_room(screen)
        self.draw_kitchen(screen)
        self.draw_lobby(screen)
        
    def draw_main_room(self, screen):
        """Dibuja la sala principal"""
        # Paredes
        pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, WINDOW_WIDTH, 20))  # Pared superior
        pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, 20, WINDOW_HEIGHT))  # Pared izquierda
        pygame.draw.rect(screen, LIGHT_GRAY, (WINDOW_WIDTH-20, 0, 20, WINDOW_HEIGHT))  # Pared derecha
        pygame.draw.rect(screen, LIGHT_GRAY, (0, WINDOW_HEIGHT-20, WINDOW_WIDTH, 20))  # Pared inferior
        
        # Paredes internas
        pygame.draw.rect(screen, LIGHT_GRAY, (200, 0, 20, 300))  # Pared a cocina
        pygame.draw.rect(screen, LIGHT_GRAY, (580, 0, 20, 300))  # Pared a lobby
        pygame.draw.rect(screen, LIGHT_GRAY, (200, 280, 400, 20))  # Pared horizontal
        
        # Librero izquierdo
        self.draw_bookshelf(screen, 50, 100, 120, 200)
        
        # Librero derecho
        self.draw_bookshelf(screen, 630, 100, 120, 200)
        
        # Mesa del comedor
        pygame.draw.rect(screen, DARK_BROWN, (300, 300, 200, 100))
        pygame.draw.rect(screen, BROWN, (300, 300, 200, 10))  # Mesa superior
        
        # Sillas del comedor
        self.draw_chair(screen, 280, 320)  # Silla izquierda
        self.draw_chair(screen, 500, 320)  # Silla derecha
        
        # Ventana
        pygame.draw.rect(screen, DARK_BLUE, (350, 50, 100, 80))
        pygame.draw.rect(screen, WHITE, (350, 50, 100, 80), 3)
        pygame.draw.line(screen, WHITE, (400, 50), (400, 130), 2)
        pygame.draw.line(screen, WHITE, (350, 90), (450, 90), 2)
        
        # Lámpara de mesa
        pygame.draw.rect(screen, DARK_BROWN, (320, 280, 10, 20))
        pygame.draw.circle(screen, YELLOW, (325, 270), 15)
        
        # Cuadros en las paredes
        pygame.draw.rect(screen, BROWN, (250, 50, 60, 40))  # Cuadro 1
        pygame.draw.rect(screen, WHITE, (250, 50, 60, 40), 2)
        pygame.draw.rect(screen, BROWN, (500, 50, 60, 40))  # Cuadro 2
        pygame.draw.rect(screen, WHITE, (500, 50, 60, 40), 2)
        
        # Planta
        pygame.draw.circle(screen, GREEN, (100, 400), 20)
        pygame.draw.rect(screen, BROWN, (95, 420, 10, 30))  # Maceta
        
    def draw_kitchen(self, screen):
        """Dibuja la cocina"""
        # Paredes de la cocina
        pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, 20, 300))  # Pared izquierda
        pygame.draw.rect(screen, LIGHT_GRAY, (0, 280, 200, 20))  # Pared inferior
        
        # Refrigerador
        pygame.draw.rect(screen, WHITE, (20, 320, 60, 40))
        pygame.draw.rect(screen, GRAY, (20, 320, 60, 40), 2)
        pygame.draw.rect(screen, GRAY, (25, 325, 50, 10))  # Puerta del refrigerador
        
        # Estufa
        pygame.draw.rect(screen, BLACK, (100, 320, 80, 40))
        pygame.draw.circle(screen, GRAY, (120, 340), 8)  # Quemador 1
        pygame.draw.circle(screen, GRAY, (160, 340), 8)  # Quemador 2
        
        # Mesada
        pygame.draw.rect(screen, LIGHT_GRAY, (20, 380, 160, 40))
        pygame.draw.rect(screen, DARK_GRAY, (20, 380, 160, 5))  # Borde superior
        
        # Fregadero
        pygame.draw.rect(screen, DARK_BLUE, (40, 390, 30, 20))
        pygame.draw.circle(screen, GRAY, (55, 400), 3)  # Grifo
        
        # Microondas
        pygame.draw.rect(screen, WHITE, (90, 390, 30, 20))
        pygame.draw.rect(screen, GRAY, (90, 390, 30, 20), 2)
        
        # Horno
        pygame.draw.rect(screen, DARK_GRAY, (130, 390, 30, 20))
        pygame.draw.rect(screen, BLACK, (135, 395, 20, 10))  # Puerta del horno
        
        # Ventilador
        pygame.draw.circle(screen, GRAY, (180, 400), 15)
        pygame.draw.line(screen, BLACK, (180, 385), (180, 415), 2)
        pygame.draw.line(screen, BLACK, (165, 400), (195, 400), 2)
        
        # Pasillo a la cocina
        pygame.draw.rect(screen, CREAM, (20, 280, 180, 20))  # Piso del pasillo
        
    def draw_lobby(self, screen):
        """Dibuja el lobby y entrada"""
        # Paredes del lobby
        pygame.draw.rect(screen, LIGHT_GRAY, (580, 0, 20, 300))  # Pared izquierda
        pygame.draw.rect(screen, LIGHT_GRAY, (580, 280, 220, 20))  # Pared inferior
        
        # Mesa de entrada
        pygame.draw.rect(screen, DARK_BROWN, (600, 320, 60, 40))
        pygame.draw.rect(screen, BROWN, (600, 320, 60, 5))  # Mesa superior
        
        # Florero en la mesa
        pygame.draw.rect(screen, BROWN, (625, 315, 10, 10))
        pygame.draw.circle(screen, RED, (630, 310), 8)
        
        # Banco
        pygame.draw.rect(screen, BROWN, (600, 380, 60, 40))
        pygame.draw.rect(screen, DARK_BROWN, (600, 380, 60, 10))  # Respaldo
        
        # Sofá
        pygame.draw.rect(screen, DARK_BLUE, (680, 320, 100, 100))
        pygame.draw.rect(screen, BLUE, (680, 320, 100, 20))  # Respaldo del sofá
        pygame.draw.rect(screen, DARK_BLUE, (680, 340, 100, 80))  # Asiento
        
        # Perchero
        pygame.draw.rect(screen, BROWN, (750, 200, 5, 80))
        pygame.draw.circle(screen, BROWN, (750, 200), 8)  # Base del perchero
        pygame.draw.line(screen, BROWN, (740, 220), (760, 220), 3)  # Gancho 1
        pygame.draw.line(screen, BROWN, (740, 240), (760, 240), 3)  # Gancho 2
        
        # Espejo
        pygame.draw.rect(screen, WHITE, (620, 200, 40, 60))
        pygame.draw.rect(screen, GRAY, (620, 200, 40, 60), 3)
        
        # Pasillo al lobby
        pygame.draw.rect(screen, CREAM, (580, 280, 220, 20))  # Piso del pasillo
        
        # Alfombra de entrada
        pygame.draw.rect(screen, RED, (650, 400, 80, 40))
        pygame.draw.rect(screen, BLACK, (650, 400, 80, 40), 2)
        
    def draw_bookshelf(self, screen, x, y, width, height):
        """Dibuja un librero con juegos de mesa y libros"""
        # Estructura del librero
        pygame.draw.rect(screen, DARK_BROWN, (x, y, width, height))
        
        # Estantes horizontales
        for i in range(4):
            shelf_y = y + 40 + i * 40
            pygame.draw.rect(screen, BROWN, (x, shelf_y, width, 5))
        
        # Libros de colores
        book_colors = [RED, BLUE, GREEN, YELLOW, PINK]
        for shelf in range(4):
            for book in range(6):
                book_x = x + 10 + book * 15
                book_y = y + 45 + shelf * 40
                color = book_colors[book % len(book_colors)]
                pygame.draw.rect(screen, color, (book_x, book_y, 12, 25))
                pygame.draw.rect(screen, BLACK, (book_x, book_y, 12, 25), 1)
        
        # Juegos de mesa en la parte superior
        # Monopoly
        pygame.draw.rect(screen, GREEN, (x + 10, y + 10, 30, 20))
        pygame.draw.rect(screen, BLACK, (x + 10, y + 10, 30, 20), 2)
        
        # Ajedrez
        pygame.draw.rect(screen, WHITE, (x + 50, y + 10, 30, 20))
        pygame.draw.rect(screen, BLACK, (x + 50, y + 10, 30, 20), 2)
        
        # Scrabble
        pygame.draw.rect(screen, BLUE, (x + 90, y + 10, 30, 20))
        pygame.draw.rect(screen, BLACK, (x + 90, y + 10, 30, 20), 2)
    
    def draw_chair(self, screen, x, y):
        """Dibuja una silla"""
        # Respaldo
        pygame.draw.rect(screen, DARK_BROWN, (x, y, 20, 30))
        # Asiento
        pygame.draw.rect(screen, BROWN, (x, y + 30, 20, 10))
        # Patas
        pygame.draw.rect(screen, DARK_BROWN, (x + 2, y + 40, 3, 20))
        pygame.draw.rect(screen, DARK_BROWN, (x + 15, y + 40, 3, 20))

class Player:
    def __init__(self, x, y, name="", character_class=KARATEKA):
        """Inicializa el jugador"""
        self.x = x
        self.y = y
        self.width = 40
        self.height = 50
        self.speed = PLAYER_SPEED
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.max_health = 100
        self.mana = 100 if character_class == MAGE else 0
        self.max_mana = 100 if character_class == MAGE else 0
        
    def handle_input(self, keys, obstacles):
        """Maneja la entrada del teclado con detección de colisiones"""
        old_x, old_y = self.x, self.y
        
        # Movimiento con flechas
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
            
        # Verificar colisiones con obstáculos
        if self.check_collision(obstacles):
            self.x, self.y = old_x, old_y
            
        # Mantener al jugador dentro de la pantalla
        self.x = max(0, min(self.x, WINDOW_WIDTH - self.width))
        self.y = max(0, min(self.y, WINDOW_HEIGHT - self.height))
    
    def check_collision(self, obstacles):
        """Verifica colisiones con obstáculos"""
        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                return True
        return False
    
    def draw(self, screen):
        """Dibuja el sprite de la niña según su clase"""
        if self.character_class == KARATEKA:
            self.draw_karateka(screen)
        elif self.character_class == MAGE:
            self.draw_mage(screen)
        elif self.character_class == PIRATE:
            self.draw_pirate(screen)
    
    def draw_karateka(self, screen):
        """Dibuja el sprite de karateka"""
        # Cuerpo (kimono blanco)
        pygame.draw.rect(screen, WHITE, (self.x + 10, self.y + 25, 20, 25))
        pygame.draw.rect(screen, BLACK, (self.x + 10, self.y + 25, 20, 25), 2)
        
        # Cabeza
        pygame.draw.circle(screen, SKIN, (self.x + 20, self.y + 20), 12)
        
        # Cabello castaño más largo
        pygame.draw.circle(screen, BROWN, (self.x + 20, self.y + 15), 15)
        pygame.draw.ellipse(screen, BROWN, (self.x + 5, self.y + 10, 20, 25))
        pygame.draw.ellipse(screen, BROWN, (self.x + 15, self.y + 10, 20, 25))
        pygame.draw.ellipse(screen, BROWN, (self.x + 12, self.y + 5, 16, 20))
        pygame.draw.ellipse(screen, BROWN, (self.x + 18, self.y + 25, 12, 30))
        pygame.draw.ellipse(screen, BROWN, (self.x + 10, self.y + 25, 12, 30))
        
        # Cabeza encima del cabello
        pygame.draw.circle(screen, SKIN, (self.x + 20, self.y + 20), 12)
        
        # Ojos
        pygame.draw.circle(screen, BLACK, (self.x + 16, self.y + 17), 2)
        pygame.draw.circle(screen, BLACK, (self.x + 24, self.y + 17), 2)
        
        # Boca
        pygame.draw.arc(screen, BLACK, (self.x + 16, self.y + 20, 8, 6), 0, math.pi, 2)
        
        # Brazos (en posición de karate)
        pygame.draw.line(screen, SKIN, (self.x + 8, self.y + 30), (self.x + 3, self.y + 40), 4)
        pygame.draw.line(screen, SKIN, (self.x + 32, self.y + 30), (self.x + 37, self.y + 40), 4)
        
        # Piernas (pantalones de karate)
        pygame.draw.line(screen, WHITE, (self.x + 15, self.y + 50), (self.x + 15, self.y + 60), 4)
        pygame.draw.line(screen, WHITE, (self.x + 25, self.y + 50), (self.x + 25, self.y + 60), 4)
        pygame.draw.line(screen, BLACK, (self.x + 15, self.y + 50), (self.x + 15, self.y + 60), 2)
        pygame.draw.line(screen, BLACK, (self.x + 25, self.y + 50), (self.x + 25, self.y + 60), 2)
    
    def draw_mage(self, screen):
        """Dibuja el sprite de mago"""
        # Cuerpo (túnica morada)
        pygame.draw.rect(screen, (128, 0, 128), (self.x + 10, self.y + 25, 20, 25))
        
        # Cabeza
        pygame.draw.circle(screen, SKIN, (self.x + 20, self.y + 20), 12)
        
        # Cabello castaño más largo
        pygame.draw.circle(screen, BROWN, (self.x + 20, self.y + 15), 15)
        pygame.draw.ellipse(screen, BROWN, (self.x + 5, self.y + 10, 20, 25))
        pygame.draw.ellipse(screen, BROWN, (self.x + 15, self.y + 10, 20, 25))
        pygame.draw.ellipse(screen, BROWN, (self.x + 12, self.y + 5, 16, 20))
        pygame.draw.ellipse(screen, BROWN, (self.x + 18, self.y + 25, 12, 30))
        pygame.draw.ellipse(screen, BROWN, (self.x + 10, self.y + 25, 12, 30))
        
        # Cabeza encima del cabello
        pygame.draw.circle(screen, SKIN, (self.x + 20, self.y + 20), 12)
        
        # Ojos
        pygame.draw.circle(screen, BLACK, (self.x + 16, self.y + 17), 2)
        pygame.draw.circle(screen, BLACK, (self.x + 24, self.y + 17), 2)
        
        # Boca
        pygame.draw.arc(screen, BLACK, (self.x + 16, self.y + 20, 8, 6), 0, math.pi, 2)
        
        # Brazos
        pygame.draw.line(screen, SKIN, (self.x + 10, self.y + 30), (self.x + 5, self.y + 40), 4)
        pygame.draw.line(screen, SKIN, (self.x + 30, self.y + 30), (self.x + 35, self.y + 40), 4)
        
        # Piernas (pantalones morados)
        pygame.draw.line(screen, (128, 0, 128), (self.x + 15, self.y + 50), (self.x + 15, self.y + 60), 4)
        pygame.draw.line(screen, (128, 0, 128), (self.x + 25, self.y + 50), (self.x + 25, self.y + 60), 4)
        
        # Sombrero de mago
        pygame.draw.circle(screen, (64, 0, 64), (self.x + 20, self.y + 8), 8)
        pygame.draw.circle(screen, (64, 0, 64), (self.x + 20, self.y + 12), 10)
    
    def draw_pirate(self, screen):
        """Dibuja el sprite de pirata"""
        # Cuerpo (chaqueta de pirata)
        pygame.draw.rect(screen, DARK_BLUE, (self.x + 10, self.y + 25, 20, 25))
        
        # Cabeza
        pygame.draw.circle(screen, SKIN, (self.x + 20, self.y + 20), 12)
        
        # Cabello castaño más largo
        pygame.draw.circle(screen, BROWN, (self.x + 20, self.y + 15), 15)
        pygame.draw.ellipse(screen, BROWN, (self.x + 5, self.y + 10, 20, 25))
        pygame.draw.ellipse(screen, BROWN, (self.x + 15, self.y + 10, 20, 25))
        pygame.draw.ellipse(screen, BROWN, (self.x + 12, self.y + 5, 16, 20))
        pygame.draw.ellipse(screen, BROWN, (self.x + 18, self.y + 25, 12, 30))
        pygame.draw.ellipse(screen, BROWN, (self.x + 10, self.y + 25, 12, 30))
        
        # Cabeza encima del cabello
        pygame.draw.circle(screen, SKIN, (self.x + 20, self.y + 20), 12)
        
        # Ojos
        pygame.draw.circle(screen, BLACK, (self.x + 16, self.y + 17), 2)
        pygame.draw.circle(screen, BLACK, (self.x + 24, self.y + 17), 2)
        
        # Boca
        pygame.draw.arc(screen, BLACK, (self.x + 16, self.y + 20, 8, 6), 0, math.pi, 2)
        
        # Brazos
        pygame.draw.line(screen, SKIN, (self.x + 10, self.y + 30), (self.x + 5, self.y + 40), 4)
        pygame.draw.line(screen, SKIN, (self.x + 30, self.y + 30), (self.x + 35, self.y + 40), 4)
        
        # Piernas (pantalones de pirata)
        pygame.draw.line(screen, BROWN, (self.x + 15, self.y + 50), (self.x + 15, self.y + 60), 4)
        pygame.draw.line(screen, BROWN, (self.x + 25, self.y + 50), (self.x + 25, self.y + 60), 4)
        
        # Parche en el ojo
        pygame.draw.circle(screen, BLACK, (self.x + 16, self.y + 17), 4)
        pygame.draw.line(screen, BLACK, (self.x + 12, self.y + 13), (self.x + 20, self.y + 21), 2)
        
        # Sombrero de pirata
        pygame.draw.ellipse(screen, BLACK, (self.x + 8, self.y + 5, 24, 12))
        pygame.draw.ellipse(screen, WHITE, (self.x + 8, self.y + 5, 24, 12), 2)

class Game:
    def __init__(self):
        """Inicializa el juego"""
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Estado del juego
        self.game_state = NAME_INPUT
        
        # Pantallas de inicio
        self.name_input = NameInput(self.screen)
        self.class_selection = ClassSelection(self.screen)
        
        # Variables del jugador (se inicializarán después de la selección)
        self.player = None
        self.environment = None
        self.father = None
        self.mother = None
        
    def handle_events(self):
        """Maneja los eventos del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif self.game_state == NAME_INPUT:
                    if self.name_input.handle_input(event):
                        self.game_state = CLASS_SELECTION
                elif self.game_state == CLASS_SELECTION:
                    keys = pygame.key.get_pressed()
                    if self.class_selection.handle_input(keys):
                        self.start_game()
                        
    def start_game(self):
        """Inicializa el juego con la información del jugador"""
        player_name = self.name_input.player_name
        character_class = self.class_selection.selected_class
        
        # Crear el jugador con nombre y clase
        self.player = Player(400, 450, player_name, character_class)
        
        # Crear el ambiente
        self.environment = Environment()
        
        # Crear los NPCs (padres en el comedor)
        self.father = NPC(280, 320, "male")  # Papá en la silla izquierda
        self.mother = NPC(500, 320, "female")  # Mamá en la silla derecha
        
        # Cambiar al estado de juego
        self.game_state = PLAYING
                    
    def update(self):
        """Actualiza la lógica del juego"""
        if self.game_state == PLAYING:
            # Obtener el estado de las teclas
            keys = pygame.key.get_pressed()
            
            # Crear lista de obstáculos incluyendo NPCs
            all_obstacles = self.environment.obstacles.copy()
            all_obstacles.append(pygame.Rect(self.father.x, self.father.y, self.father.width, self.father.height))
            all_obstacles.append(pygame.Rect(self.mother.x, self.mother.y, self.mother.width, self.mother.height))
            
            # Actualizar el jugador con detección de colisiones
            self.player.handle_input(keys, all_obstacles)
        
    def draw(self):
        """Dibuja todos los elementos en pantalla"""
        if self.game_state == NAME_INPUT:
            self.name_input.draw()
        elif self.game_state == CLASS_SELECTION:
            self.class_selection.draw()
        elif self.game_state == PLAYING:
            # Dibujar el ambiente primero (fondo)
            self.environment.draw(self.screen)
            
            # Dibujar los NPCs
            self.father.draw(self.screen)
            self.mother.draw(self.screen)
            
            # Dibujar el jugador encima de todo
            self.player.draw(self.screen)
            
            # Mostrar información del jugador
            self.draw_player_info()
            
            # Actualiza la pantalla
            pygame.display.flip()
    
    def draw_player_info(self):
        """Dibuja la información del jugador en pantalla"""
        font = pygame.font.Font(None, 24)
        
        # Nombre del jugador
        name_text = font.render(f"Nombre: {self.player.name}", True, WHITE)
        self.screen.blit(name_text, (10, 10))
        
        # Clase del jugador
        class_text = font.render(f"Clase: {self.player.character_class.upper()}", True, WHITE)
        self.screen.blit(class_text, (10, 35))
        
        # Salud
        health_text = font.render(f"Salud: {self.player.health}/{self.player.max_health}", True, RED)
        self.screen.blit(health_text, (10, 60))
        
        # Mana (solo para mago)
        if self.player.character_class == MAGE:
            mana_text = font.render(f"Maná: {self.player.mana}/{self.player.max_mana}", True, BLUE)
            self.screen.blit(mana_text, (10, 85))
        
    def run(self):
        """Bucle principal del juego"""
        while self.running:
            # Maneja eventos
            self.handle_events()
            
            # Actualiza la lógica del juego
            self.update()
            
            # Dibuja todo en pantalla
            self.draw()
            
            # Controla la velocidad del juego (60 FPS)
            self.clock.tick(60)
            
        # Limpia y cierra Pygame
        pygame.quit()
        sys.exit()

def main():
    """Función principal"""
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
