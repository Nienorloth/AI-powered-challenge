import pygame
import sys
import math
import random

# Cargar el sprite sheet
SPRITE_SHEET = pygame.image.load("sprites.png")
SPRITE_WIDTH = 32  # Ancho de cada sprite individual
SPRITE_HEIGHT = 32  # Alto de cada sprite individual

# Cargar los sprites individuales
PLAYER_SPRITE_SHEET = pygame.image.load("human_8.png")
MOM_SPRITE_SHEET = pygame.image.load("human_4.png")
DAD_SPRITE_SHEET = pygame.image.load("human_1.png")
GOBLIN_KING_SPRITE_SHEET = pygame.image.load("human_7.png")

# Cargar sprites de enemigos goblins
GOBLIN_SPRITE_2 = pygame.image.load("enemy_2.png")
GOBLIN_SPRITE_4 = pygame.image.load("enemy_4.png")
GOBLIN_SPRITE_5 = pygame.image.load("enemy_5.png")

# Definir las posiciones de los sprites en el sprite sheet (fila, columna)
# Basado en la descripción: 8 filas x 10 columnas, cada sprite 32x32
# Fila 8 (última fila): Niña (esquina inferior derecha) - columna 10
GIRL_SPRITE_ROW = 7  # Fila 8 (índice 7)
GIRL_SPRITE_COL = 9   # Columna 10 (índice 9)

# Fila 7: Mamá (cabello rojo) - arriba de la niña
MOM_SPRITE_ROW = 6    # Fila 7 (índice 6) 
MOM_SPRITE_COL = 9    # Columna 10 (índice 9)

# Fila 8: Papá (capucha negra) - esquina inferior izquierda
DAD_SPRITE_ROW = 7    # Fila 8 (índice 7)
DAD_SPRITE_COL = 0    # Columna 1 (índice 0)

# Fila 8: Goblin King (cabello rubio) - izquierda de la niña
GOBLIN_SPRITE_ROW = 7 # Fila 8 (índice 7)
GOBLIN_SPRITE_COL = 8  # Columna 9 (índice 8)

# Direcciones de los sprites (0=down, 1=left, 2=right, 3=up)
class SpriteManager:
    def __init__(self):
        self.sprite_sheet = SPRITE_SHEET
        self.player_sprite_sheet = PLAYER_SPRITE_SHEET
        self.mom_sprite_sheet = MOM_SPRITE_SHEET
        self.dad_sprite_sheet = DAD_SPRITE_SHEET
        self.goblin_king_sprite_sheet = GOBLIN_KING_SPRITE_SHEET
        self.goblin_sprite_2 = GOBLIN_SPRITE_2
        self.goblin_sprite_4 = GOBLIN_SPRITE_4
        self.goblin_sprite_5 = GOBLIN_SPRITE_5
        
    def get_sprite(self, row, col, direction=0):
        """Obtiene un sprite específico del sprite sheet"""
        # Cada sprite tiene 4 direcciones: down (0), left (1), right (2), up (3)
        sprite_col = col * 4 + direction
        x = sprite_col * SPRITE_WIDTH
        y = row * SPRITE_HEIGHT
        
        # Verificar que las coordenadas estén dentro del sprite sheet
        sheet_width = self.sprite_sheet.get_width()
        sheet_height = self.sprite_sheet.get_height()
        
        if x + SPRITE_WIDTH > sheet_width or y + SPRITE_HEIGHT > sheet_height:
            # Usar el primer sprite como fallback
            return self.sprite_sheet.subsurface((0, 0, SPRITE_WIDTH, SPRITE_HEIGHT))
        
        return self.sprite_sheet.subsurface((x, y, SPRITE_WIDTH, SPRITE_HEIGHT))
    
    def get_girl_sprite(self, direction=0):
        return self.get_sprite(GIRL_SPRITE_ROW, GIRL_SPRITE_COL, direction)
    
    def get_mom_sprite(self, direction=0):
        return self.get_sprite(MOM_SPRITE_ROW, MOM_SPRITE_COL, direction)
    
    def get_dad_sprite(self, direction=0):
        return self.get_sprite(DAD_SPRITE_ROW, DAD_SPRITE_COL, direction)
    
    def get_goblin_sprite(self, direction=0):
        return self.get_sprite(GOBLIN_SPRITE_ROW, GOBLIN_SPRITE_COL, direction)
    
    def get_player_sprite(self, direction=0):
        """Obtiene el sprite del personaje principal desde human_8.png"""
        return self.get_individual_sprite(self.player_sprite_sheet, direction)
    
    def get_mom_sprite_new(self, direction=0):
        """Obtiene el sprite de la mamá desde human_4.png"""
        return self.get_individual_sprite(self.mom_sprite_sheet, direction)
    
    def get_dad_sprite_new(self, direction=0):
        """Obtiene el sprite del papá desde human_1.png"""
        return self.get_individual_sprite(self.dad_sprite_sheet, direction)
    
    def get_goblin_king_sprite(self, direction=0):
        """Obtiene el sprite del Goblin King desde human_7.png"""
        return self.get_individual_sprite(self.goblin_king_sprite_sheet, direction)
    
    def get_goblin_2_sprite(self, direction=0):
        """Obtiene el sprite del goblin desde enemy_2.png"""
        return self.get_individual_sprite(self.goblin_sprite_2, direction)
    
    def get_goblin_4_sprite(self, direction=0):
        """Obtiene el sprite del goblin desde enemy_4.png"""
        return self.get_individual_sprite(self.goblin_sprite_4, direction)
    
    def get_goblin_5_sprite(self, direction=0):
        """Obtiene el sprite del goblin desde enemy_5.png"""
        return self.get_individual_sprite(self.goblin_sprite_5, direction)
    
    def get_individual_sprite(self, sprite_sheet, direction=0):
        """Obtiene un sprite individual con 4 direcciones"""
        # Cada sprite individual tiene 4 direcciones: down (0), left (1), right (2), up (3)
        x = direction * SPRITE_WIDTH
        y = 0  # Solo hay una fila en estos sprite sheets
        
        # Verificar que las coordenadas estén dentro del sprite sheet
        sheet_width = sprite_sheet.get_width()
        sheet_height = sprite_sheet.get_height()
        
        if x + SPRITE_WIDTH > sheet_width or y + SPRITE_HEIGHT > sheet_height:
            # Usar el primer sprite como fallback
            return sprite_sheet.subsurface((0, 0, SPRITE_WIDTH, SPRITE_HEIGHT))
        
        return sprite_sheet.subsurface((x, y, SPRITE_WIDTH, SPRITE_HEIGHT))

# Instancia global del sprite manager
sprite_manager = SpriteManager()

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
PURPLE = (128, 0, 128)

# Velocidad del jugador
PLAYER_SPEED = 5

# Cargar y escalar el background de la casa
HOUSE_BACKGROUND = pygame.image.load("interior_casa.png")
HOUSE_BACKGROUND = pygame.transform.scale(HOUSE_BACKGROUND, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Clases de personaje
KARATEKA = "karateka"
MAGE = "mage"
PIRATE = "pirate"

# Estados del juego
NAME_INPUT = "name_input"
CLASS_SELECTION = "class_selection"
PLAYING = "playing"
CINEMATIC = "cinematic"

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

class Enemy:
    def __init__(self, x, y):
        """Inicializa el Goblin King"""
        self.x = x
        self.y = y
        self.width = 40  # Ajustar al tamaño estándar
        self.height = 50  # Ajustar al tamaño estándar
        self.animation_timer = 0
        self.animation_phase = 0  # 0: entrada, 1: caminar, 2: girar, 3: mirar frente, 4: diálogo
        self.target_x = 400  # Posición objetivo (mesa)
        self.target_y = 350
        self.angle = 0  # Ángulo de rotación
        self.visible = False
        self.dialogue_timer = 0
        self.dialogue_phase = 0  # 0: sin diálogo, 1: "vengo por estos dos", 2: padres gritan, 3: "me los llevaré a jugar", 4: batalla, 5: escape
        self.direction = 0  # 0=down, 1=left, 2=right, 3=up
        
    def update(self):
        """Actualiza la animación del enemigo"""
        self.animation_timer += 1
        
        if self.animation_phase == 0:  # Entrada desde el sótano
            if self.animation_timer < 60:  # 1 segundo
                self.y = 400 - (self.animation_timer * 2)  # Aparece desde abajo (sótano)
            else:
                self.animation_phase = 1
                self.animation_timer = 0
                
        elif self.animation_phase == 1:  # Caminar hacia la mesa donde están los padres
            if self.animation_timer < 90:  # 1.5 segundos
                # Movimiento suave hacia la mesa en la sala de estar
                progress = self.animation_timer / 90.0
                self.x = 100 + (490 - 100) * progress  # Se mueve hacia la mesa
                self.y = 400 - (200 - 400) * progress  # Se mueve hacia arriba
                # Determinar dirección basada en el movimiento
                self.direction = 2  # right (se mueve hacia la derecha)
            else:
                self.animation_phase = 2
                self.animation_timer = 0
                
        elif self.animation_phase == 2:  # Girar hacia el frente
            if self.animation_timer < 30:  # 0.5 segundos
                self.angle = (self.animation_timer / 30.0) * 90  # Gira 90 grados
            else:
                self.animation_phase = 3
                self.animation_timer = 0
                self.angle = 90  # Mirando hacia el frente
                self.direction = 0  # down (frente)
                
        elif self.animation_phase == 3:  # Mirar hacia el frente
            self.visible = True
            if self.animation_timer > 30:  # Esperar un poco antes del diálogo
                self.animation_phase = 4
                self.animation_timer = 0
                self.dialogue_phase = 1
                self.dialogue_timer = 0
                
        elif self.animation_phase == 4:  # Fase de diálogo
            self.dialogue_timer += 1
            
            if self.dialogue_phase == 1 and self.dialogue_timer > 120:  # 2 segundos
                self.dialogue_phase = 2
                self.dialogue_timer = 0
            elif self.dialogue_phase == 2 and self.dialogue_timer > 120:  # 2 segundos más
                self.dialogue_phase = 3
                self.dialogue_timer = 0
            elif self.dialogue_phase == 3 and self.dialogue_timer > 180:  # 3 segundos más
                self.dialogue_phase = 4
                self.dialogue_timer = 0
            elif self.dialogue_phase == 4 and self.dialogue_timer > 120:  # Batalla por 2 segundos
                self.dialogue_phase = 5
                self.dialogue_timer = 0
            elif self.dialogue_phase == 5 and self.dialogue_timer > 180:  # Escape por 3 segundos
                self.animation_phase = 6  # Terminar

class RandomGoblin:
    def __init__(self, x, y, sprite_type):
        """Inicializa un goblin aleatorio"""
        self.x = x
        self.y = y
        self.width = 30
        self.height = 40
        self.sprite_type = sprite_type  # 2, 4, o 5
        self.direction = random.randint(0, 3)  # Dirección aleatoria
        self.move_timer = 0
        self.change_direction_timer = 0
        self.speed = 2
        self.visible = True
        
        # Propiedades de combate
        self.health = 50
        self.max_health = 50
        self.attack_damage = 15
        self.attack_timer = 0
        self.attack_cooldown = 60  # 1 segundo
        self.in_combat = False
        self.target_player = False
        
    def update(self):
        """Actualiza el movimiento del goblin"""
        if not self.visible:
            return
            
        self.move_timer += 1
        self.change_direction_timer += 1
        
        # Cambiar dirección aleatoriamente cada 60 frames (1 segundo)
        if self.change_direction_timer >= 60:
            self.direction = random.randint(0, 3)
            self.change_direction_timer = 0
        
        # Moverse en la dirección actual
        old_x, old_y = self.x, self.y
        
        if self.direction == 0:  # down
            self.y += self.speed
        elif self.direction == 1:  # left
            self.x -= self.speed
        elif self.direction == 2:  # right
            self.x += self.speed
        elif self.direction == 3:  # up
            self.y -= self.speed
        
        # Mantener dentro de la pantalla
        self.x = max(50, min(self.x, WINDOW_WIDTH - self.width - 50))
        self.y = max(50, min(self.y, WINDOW_HEIGHT - self.height - 50))
        
        # Si se sale de la pantalla, cambiar dirección
        if self.x == 50 or self.x == WINDOW_WIDTH - self.width - 50:
            self.direction = random.choice([0, 3])  # up o down
        if self.y == 50 or self.y == WINDOW_HEIGHT - self.height - 50:
            self.direction = random.choice([1, 2])  # left o right
    
    def draw(self, screen):
        """Dibuja el goblin aleatorio"""
        if not self.visible:
            return
            
        # Obtener el sprite según el tipo
        if self.sprite_type == 2:
            sprite = sprite_manager.get_goblin_2_sprite(self.direction)
        elif self.sprite_type == 4:
            sprite = sprite_manager.get_goblin_4_sprite(self.direction)
        elif self.sprite_type == 5:
            sprite = sprite_manager.get_goblin_5_sprite(self.direction)
        else:
            sprite = sprite_manager.get_goblin_2_sprite(self.direction)  # fallback
        
        # Escalar el sprite
        scaled_sprite = pygame.transform.scale(sprite, (self.width, self.height))
        
        # Dibujar el sprite
        screen.blit(scaled_sprite, (self.x, self.y))
            
    def draw(self, screen):
        """Dibuja el Goblin King"""
        if not self.visible and self.animation_phase < 3:
            return
        
        # Obtener el sprite del Goblin King según la dirección
        sprite = sprite_manager.get_goblin_king_sprite(self.direction)
        
        # Escalar el sprite para que se vea más grande
        scaled_sprite = pygame.transform.scale(sprite, (self.width, self.height))
        
        # Dibujar el sprite
        screen.blit(scaled_sprite, (self.x, self.y))
        
        # Dibujar globo de diálogo si está en fase de diálogo
        if self.animation_phase == 4:
            self.draw_dialogue(screen)
    
    def draw_dialogue(self, screen):
        """Dibuja los globos de diálogo"""
        font = pygame.font.Font(None, 24)
        
        if self.dialogue_phase == 1:  # Goblin King habla
            # Globo de diálogo del Goblin King
            bubble_x = self.x - 50
            bubble_y = self.y - 40
            bubble_width = 200
            bubble_height = 60
            
            # Dibujar globo
            pygame.draw.ellipse(screen, WHITE, (bubble_x, bubble_y, bubble_width, bubble_height))
            pygame.draw.ellipse(screen, BLACK, (bubble_x, bubble_y, bubble_width, bubble_height), 3)
            
            # Cola del globo
            pygame.draw.polygon(screen, WHITE, [(bubble_x + 20, bubble_y + bubble_height), 
                                              (bubble_x + 30, bubble_y + bubble_height + 15),
                                              (bubble_x + 40, bubble_y + bubble_height)])
            pygame.draw.polygon(screen, BLACK, [(bubble_x + 20, bubble_y + bubble_height), 
                                              (bubble_x + 30, bubble_y + bubble_height + 15),
                                              (bubble_x + 40, bubble_y + bubble_height)], 3)
            
            # Texto
            text = font.render("¡Vengo por estos dos!", True, BLACK)
            text_rect = text.get_rect(center=(bubble_x + bubble_width//2, bubble_y + bubble_height//2))
            screen.blit(text, text_rect)
            
        elif self.dialogue_phase == 2:  # Padres gritan
            # Globos de diálogo de los padres
            # Padre (izquierda)
            father_bubble_x = 200
            father_bubble_y = 250
            father_bubble_width = 150
            father_bubble_height = 50
            
            pygame.draw.ellipse(screen, WHITE, (father_bubble_x, father_bubble_y, father_bubble_width, father_bubble_height))
            pygame.draw.ellipse(screen, BLACK, (father_bubble_x, father_bubble_y, father_bubble_width, father_bubble_height), 3)
            
            father_text = font.render("¡David Bowie!", True, BLACK)
            father_text_rect = father_text.get_rect(center=(father_bubble_x + father_bubble_width//2, father_bubble_y + father_bubble_height//2))
            screen.blit(father_text, father_text_rect)
            
            # Madre (derecha)
            mother_bubble_x = 450
            mother_bubble_y = 250
            mother_bubble_width = 150
            mother_bubble_height = 50
            
            pygame.draw.ellipse(screen, WHITE, (mother_bubble_x, mother_bubble_y, mother_bubble_width, mother_bubble_height))
            pygame.draw.ellipse(screen, BLACK, (mother_bubble_x, mother_bubble_y, mother_bubble_width, mother_bubble_height), 3)
            
            mother_text = font.render("¡David Bowie!", True, BLACK)
            mother_text_rect = mother_text.get_rect(center=(mother_bubble_x + mother_bubble_width//2, mother_bubble_y + mother_bubble_height//2))
            screen.blit(mother_text, mother_text_rect)
            
        elif self.dialogue_phase == 3:  # Goblin King continúa
            # Globo de diálogo del Goblin King (más grande)
            bubble_x = self.x - 80
            bubble_y = self.y - 60
            bubble_width = 300
            bubble_height = 80
            
            # Dibujar globo
            pygame.draw.ellipse(screen, WHITE, (bubble_x, bubble_y, bubble_width, bubble_height))
            pygame.draw.ellipse(screen, BLACK, (bubble_x, bubble_y, bubble_width, bubble_height), 3)
            
            # Cola del globo
            pygame.draw.polygon(screen, WHITE, [(bubble_x + 30, bubble_y + bubble_height), 
                                              (bubble_x + 40, bubble_y + bubble_height + 15),
                                              (bubble_x + 50, bubble_y + bubble_height)])
            pygame.draw.polygon(screen, BLACK, [(bubble_x + 30, bubble_y + bubble_height), 
                                              (bubble_x + 40, bubble_y + bubble_height + 15),
                                              (bubble_x + 50, bubble_y + bubble_height)], 3)
            
            # Texto en múltiples líneas
            text1 = font.render("¡Sí, estoy aburrido y me los llevaré", True, BLACK)
            text1_rect = text1.get_rect(center=(bubble_x + bubble_width//2, bubble_y + bubble_height//2 - 15))
            screen.blit(text1, text1_rect)
            
            text2 = font.render("a jugar juegos de mesa conmigo,", True, BLACK)
            text2_rect = text2.get_rect(center=(bubble_x + bubble_width//2, bubble_y + bubble_height//2 + 5))
            screen.blit(text2, text2_rect)
            
            text3 = font.render("el rey de los goblins!", True, BLACK)
            text3_rect = text3.get_rect(center=(bubble_x + bubble_width//2, bubble_y + bubble_height//2 + 25))
            screen.blit(text3, text3_rect)
            
        elif self.dialogue_phase == 4:  # Batalla
            # Efectos de batalla
            self.draw_battle_effects(screen)
            
        elif self.dialogue_phase == 5:  # Escape
            # Efectos de escape
            self.draw_escape_effects(screen)
    
    def draw_battle_effects(self, screen):
        """Dibuja los efectos de la batalla"""
        font = pygame.font.Font(None, 24)
        
        # Efectos de ataque del personaje
        if self.dialogue_timer < 60:  # Primer segundo
            # Efectos de ataque del personaje
            for i in range(10):
                x = self.x + (i * 5) + (self.dialogue_timer * 2)
                y = self.y + 20 + (i * 3)
                pygame.draw.circle(screen, YELLOW, (x, y), 3)
                pygame.draw.circle(screen, RED, (x, y), 2)
        
        # Texto de batalla
        battle_text = font.render("¡ATAQUE!", True, RED)
        battle_rect = battle_text.get_rect(center=(self.x + 50, self.y - 30))
        screen.blit(battle_text, battle_rect)
        
        # Efectos de contraataque del Goblin King
        if self.dialogue_timer > 30:
            # Rayos de poder del Goblin King
            for i in range(8):
                angle = (i * 45) + (self.dialogue_timer * 5)
                end_x = self.x + 25 + math.cos(math.radians(angle)) * 50
                end_y = self.y + 25 + math.sin(math.radians(angle)) * 50
                pygame.draw.line(screen, PURPLE, (self.x + 25, self.y + 25), (end_x, end_y), 3)
        
        # Texto de derrota
        if self.dialogue_timer > 60:
            defeat_text = font.render("¡El personaje es derrotado!", True, RED)
            defeat_rect = defeat_text.get_rect(center=(WINDOW_WIDTH//2, 100))
            screen.blit(defeat_text, defeat_rect)
    
    def draw_escape_effects(self, screen):
        """Dibuja los efectos del escape"""
        font = pygame.font.Font(None, 24)
        
        # Efectos de escape del Goblin King
        if self.dialogue_timer < 60:
            # Movimiento hacia arriba
            self.y -= 2
            
        # Efectos mágicos de escape
        for i in range(15):
            angle = (i * 24) + (self.dialogue_timer * 10)
            radius = 30 + (self.dialogue_timer * 2)
            x = self.x + 25 + math.cos(math.radians(angle)) * radius
            y = self.y + 25 + math.sin(math.radians(angle)) * radius
            pygame.draw.circle(screen, PURPLE, (int(x), int(y)), 2)
        
        # Texto de escape
        escape_text = font.render("¡El Goblin King escapa con los padres!", True, PURPLE)
        escape_rect = escape_text.get_rect(center=(WINDOW_WIDTH//2, 150))
        screen.blit(escape_text, escape_rect)

class NPC:
    def __init__(self, x, y, gender="male"):
        """Inicializa un NPC"""
        self.x = x
        self.y = y
        self.gender = gender
        self.width = 40
        self.height = 50
        self.dialogue_timer = 0
        self.show_dialogue = False
        self.dialogue_duration = 180  # 3 segundos
        self.visible = True
        self.direction = 0  # 0=down, 1=left, 2=right, 3=up
        
    def draw(self, screen):
        """Dibuja el NPC"""
        if not self.visible:
            return
        
        # Obtener el sprite correcto según el género y dirección
        if self.gender == "male":
            sprite = sprite_manager.get_dad_sprite_new(self.direction)
        else:
            sprite = sprite_manager.get_mom_sprite_new(self.direction)
        
        # Escalar el sprite para que se vea más grande
        scaled_sprite = pygame.transform.scale(sprite, (self.width, self.height))
        
        # Dibujar el sprite
        screen.blit(scaled_sprite, (self.x, self.y))
        
        # Dibujar globo de diálogo si está activo
        if self.show_dialogue:
            self.draw_dialogue(screen)
    
    def draw_dialogue(self, screen):
        """Dibuja el globo de diálogo del NPC"""
        font = pygame.font.Font(None, 20)
        
        # Globo de diálogo
        bubble_x = self.x - 30
        bubble_y = self.y - 50
        bubble_width = 200
        bubble_height = 40
        
        # Dibujar globo
        pygame.draw.ellipse(screen, WHITE, (bubble_x, bubble_y, bubble_width, bubble_height))
        pygame.draw.ellipse(screen, BLACK, (bubble_x, bubble_y, bubble_width, bubble_height), 2)
        
        # Cola del globo
        pygame.draw.polygon(screen, WHITE, [(bubble_x + 20, bubble_y + bubble_height), 
                                          (bubble_x + 30, bubble_y + bubble_height + 10),
                                          (bubble_x + 40, bubble_y + bubble_height)])
        pygame.draw.polygon(screen, BLACK, [(bubble_x + 20, bubble_y + bubble_height), 
                                          (bubble_x + 30, bubble_y + bubble_height + 10),
                                          (bubble_x + 40, bubble_y + bubble_height)], 2)
        
        # Texto
        text = font.render("Ya vete a dormir, nosotros", True, BLACK)
        text_rect = text.get_rect(center=(bubble_x + bubble_width//2, bubble_y + bubble_height//2 - 8))
        screen.blit(text, text_rect)
        
        text2 = font.render("vamos a quedarnos jugando", True, BLACK)
        text2_rect = text2.get_rect(center=(bubble_x + bubble_width//2, bubble_y + bubble_height//2 + 8))
        screen.blit(text2, text2_rect)
    
    def start_dialogue(self, player_x=None, player_y=None):
        """Inicia el diálogo del NPC y hace que mire al jugador"""
        self.show_dialogue = True
        self.dialogue_timer = 0
        
        # Hacer que el NPC mire hacia el jugador si se proporcionan coordenadas
        if player_x is not None and player_y is not None:
            self.face_player(player_x, player_y)
    
    def face_player(self, player_x, player_y):
        """Hace que el NPC mire hacia el jugador"""
        # Calcular la dirección hacia el jugador
        dx = player_x - (self.x + self.width // 2)
        dy = player_y - (self.y + self.height // 2)
        
        # Determinar la dirección basada en la diferencia mayor
        if abs(dx) > abs(dy):
            # Movimiento horizontal
            if dx > 0:
                self.direction = 2  # right
            else:
                self.direction = 1  # left
        else:
            # Movimiento vertical
            if dy > 0:
                self.direction = 0  # down
            else:
                self.direction = 3  # up
    
    def update_dialogue(self):
        """Actualiza el temporizador del diálogo"""
        if self.show_dialogue:
            self.dialogue_timer += 1
            if self.dialogue_timer >= self.dialogue_duration:
                self.show_dialogue = False
                self.dialogue_timer = 0

class Environment:
    def __init__(self):
        """Inicializa el ambiente de la casa"""
        self.obstacles = []
        self.background = HOUSE_BACKGROUND
        self.setup_obstacles()
        
    def setup_obstacles(self):
        """Configura todos los obstáculos de la casa basados en la nueva imagen"""
        self.obstacles = []
        
        # Paredes exteriores (ajustadas para la nueva imagen)
        self.obstacles.append(pygame.Rect(0, 0, WINDOW_WIDTH, 25))  # Pared superior
        self.obstacles.append(pygame.Rect(0, 0, 25, WINDOW_HEIGHT))  # Pared izquierda
        self.obstacles.append(pygame.Rect(WINDOW_WIDTH-25, 0, 25, WINDOW_HEIGHT))  # Pared derecha
        self.obstacles.append(pygame.Rect(0, WINDOW_HEIGHT-25, WINDOW_WIDTH, 25))  # Pared inferior
        
        # Paredes internas
        # Pared entre dormitorio y sala de estar
        self.obstacles.append(pygame.Rect(200, 0, 20, 250))  # Pared vertical izquierda
        # Pared entre sala de estar y cocina
        self.obstacles.append(pygame.Rect(450, 0, 20, 300))  # Pared vertical derecha
        # Pared horizontal entre habitaciones superiores e inferiores
        self.obstacles.append(pygame.Rect(200, 250, 250, 20))  # Pared horizontal
        
        # Muebles del dormitorio (superior izquierdo)
        self.obstacles.append(pygame.Rect(30, 50, 80, 120))  # Cama
        self.obstacles.append(pygame.Rect(120, 80, 60, 40))  # Estante con tetera
        
        # Muebles de la sala de estar (superior derecho)
        self.obstacles.append(pygame.Rect(480, 80, 80, 60))  # Chimenea
        self.obstacles.append(pygame.Rect(470, 160, 100, 60))  # Mesa con sillas
        self.obstacles.append(pygame.Rect(500, 40, 40, 30))  # Estante con plantas
        
        # Muebles del área central
        self.obstacles.append(pygame.Rect(220, 280, 40, 60))  # Perchero con canasta
        
        # Muebles del área de almacenamiento (inferior izquierdo)
        self.obstacles.append(pygame.Rect(30, 300, 120, 80))  # Estantes con jarras
        self.obstacles.append(pygame.Rect(80, 380, 40, 20))  # Escaleras al sótano
        
        # Muebles de la cocina (inferior derecho)
        self.obstacles.append(pygame.Rect(480, 320, 100, 40))  # Mostrador con fregadero
        self.obstacles.append(pygame.Rect(600, 320, 60, 40))  # Estufa
        self.obstacles.append(pygame.Rect(580, 360, 80, 60))  # Mesa de comedor
        self.obstacles.append(pygame.Rect(480, 380, 30, 40))  # Cubo blanco
        
    def draw(self, screen):
        """Dibuja el ambiente completo de la casa"""
        # Dibujar el background de la casa
        screen.blit(self.background, (0, 0))
        
    # Métodos de dibujo antiguos eliminados - ahora usamos background de imagen
    
    def draw_entrance(self, screen):
        """Dibuja la sala principal"""
        # Paredes
        pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, WINDOW_WIDTH, 20))  # Pared superior
        pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, 20, WINDOW_HEIGHT))  # Pared izquierda
        pygame.draw.rect(screen, LIGHT_GRAY, (WINDOW_WIDTH-20, 0, 20, WINDOW_HEIGHT))  # Pared derecha
        
        # Pared inferior con entrada
        pygame.draw.rect(screen, LIGHT_GRAY, (0, WINDOW_HEIGHT-20, 350, 20))  # Pared inferior izquierda
        pygame.draw.rect(screen, LIGHT_GRAY, (450, WINDOW_HEIGHT-20, 350, 20))  # Pared inferior derecha
        
        # Dibujar la entrada/puerta
        self.draw_entrance(screen)
        
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
    
    def draw_entrance(self, screen):
        """Dibuja la entrada al sótano donde aparece el Goblin King"""
        # Posición de la entrada al sótano (según la nueva imagen)
        entrance_x = 80
        entrance_y = 380
        entrance_width = 40
        entrance_height = 20
        
        # Dibujar indicador visual de la entrada
        pygame.draw.rect(screen, (100, 100, 100), (entrance_x, entrance_y, entrance_width, entrance_height))
        pygame.draw.rect(screen, BLACK, (entrance_x, entrance_y, entrance_width, entrance_height), 2)
        
        # Texto indicativo
        font = pygame.font.Font(None, 16)
        text = font.render("ENTRADA", True, WHITE)
        text_rect = text.get_rect(center=(entrance_x + entrance_width//2, entrance_y - 10))
        screen.blit(text, text_rect)

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
        self.direction = 0  # 0=down, 1=left, 2=right, 3=up
        self.last_movement = [0, 0, 0, 0]  # [down, left, right, up] para detectar última dirección
        
    def handle_input(self, keys, obstacles):
        """Maneja la entrada del teclado con detección de colisiones"""
        old_x, old_y = self.x, self.y
        
        # Detectar movimiento y actualizar dirección
        moved = False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = 1  # left
            self.last_movement = [0, 1, 0, 0]
            moved = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
            self.direction = 2  # right
            self.last_movement = [0, 0, 1, 0]
            moved = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = 3  # up
            self.last_movement = [0, 0, 0, 1]
            moved = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
            self.direction = 0  # down
            self.last_movement = [1, 0, 0, 0]
            moved = True
            
        # Si no se movió, mantener la última dirección
        if not moved:
            if self.last_movement[0]: self.direction = 0  # down
            elif self.last_movement[1]: self.direction = 1  # left
            elif self.last_movement[2]: self.direction = 2  # right
            elif self.last_movement[3]: self.direction = 3  # up
            
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
        """Dibuja el sprite de la niña"""
        # Obtener el sprite correcto según la dirección
        sprite = sprite_manager.get_player_sprite(self.direction)
        
        # Escalar el sprite para que se vea más grande
        scaled_sprite = pygame.transform.scale(sprite, (self.width, self.height))
        
        # Dibujar el sprite
        screen.blit(scaled_sprite, (self.x, self.y))
    

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
        self.enemy = None
        self.random_goblins = []  # Lista de goblins aleatorios
        
        # Variables de cinemática
        self.flash_timer = 0
        self.flash_duration = 30  # 0.5 segundos
        self.cinematic_triggered = False
        self.final_flash = False
        self.final_flash_timer = 0
        
        # Variables de acción
        self.action_pressed = False
        self.action_cooldown = 0
        
    def handle_events(self):
        """Maneja los eventos del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_RETURN and self.game_state == PLAYING:
                    # Botón de acción con ENTER
                    if self.action_cooldown == 0:
                        self.action_pressed = True
                        self.action_cooldown = 30  # 0.5 segundos de cooldown
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
        
        # Crear el jugador con nombre y clase (en el piso azul de la cocina)
        self.player = Player(550, 450, player_name, character_class)
        
        # Crear el ambiente
        self.environment = Environment()
        
        # Crear los NPCs (padres sentados en sillones junto a la mesita)
        self.father = NPC(480, 160, "male")  # Papá en sillón izquierdo
        self.mother = NPC(530, 160, "female")  # Mamá en sillón derecho
        
        # Crear el enemigo (inicialmente invisible) - aparece desde la entrada al sótano
        self.enemy = Enemy(100, 400)
        
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
            
            # Verificar colisión con NPCs para mostrar diálogos
            self.check_npc_collisions()
            
            # Actualizar diálogos de NPCs
            self.father.update_dialogue()
            self.mother.update_dialogue()
            
            # Actualizar cooldown del botón de acción
            if self.action_cooldown > 0:
                self.action_cooldown -= 1
            
            # Actualizar flash final
            if self.final_flash:
                self.final_flash_timer += 1
                if self.final_flash_timer > 60:  # 1 segundo
                    self.final_flash = False
            
            # Procesar acción si se presionó ENTER
            if self.action_pressed:
                self.process_action()
                self.action_pressed = False
            
            # Verificar si el jugador llegó a la zona de entrada para activar cinemática
            entrance_x = 350
            entrance_width = 100
            if (not self.cinematic_triggered and 
                self.player.y >= WINDOW_HEIGHT - self.player.height - 10 and
                entrance_x <= self.player.x + self.player.width//2 <= entrance_x + entrance_width):
                self.trigger_cinematic()
                
        elif self.game_state == CINEMATIC:
            # Actualizar la cinemática
            self.update_cinematic()
    
    def trigger_cinematic(self):
        """Activa la cinemática del enemigo"""
        self.cinematic_triggered = True
        self.game_state = CINEMATIC
        self.flash_timer = 0
        self.enemy.visible = True
        self.enemy.animation_phase = 0
        self.enemy.animation_timer = 0
        
        # Crear los goblins aleatorios
        self.random_goblins = []
        
        # Posiciones aleatorias para los goblins
        positions = [
            (100, 100),  # Esquina superior izquierda
            (400, 200),  # Centro
            (600, 400)   # Esquina inferior derecha
        ]
        
        sprite_types = [2, 4, 5]  # enemy_2, enemy_4, enemy_5
        
        for i, (x, y) in enumerate(positions):
            goblin = RandomGoblin(x, y, sprite_types[i])
            self.random_goblins.append(goblin)
        
    def update_cinematic(self):
        """Actualiza la animación de la cinemática"""
        # Actualizar el enemigo
        self.enemy.update()
        
        # Actualizar los goblins aleatorios
        for goblin in self.random_goblins:
            goblin.update()
        
        # Actualizar el flash
        if self.flash_timer < self.flash_duration:
            self.flash_timer += 1
        
        # Si la animación del enemigo terminó, volver al juego
        if self.enemy.animation_phase == 6:  # Fase final
            self.game_state = PLAYING
            # Los padres desaparecen (son llevados por el Goblin King)
            self.father.visible = False
            self.mother.visible = False
            # Activar flash final
            self.final_flash = True
            self.final_flash_timer = 0
    
    def check_npc_collisions(self):
        """Verifica colisiones con NPCs para mostrar diálogos"""
        player_rect = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)
        
        # Verificar colisión con el padre
        father_rect = pygame.Rect(self.father.x, self.father.y, self.father.width, self.father.height)
        if player_rect.colliderect(father_rect) and not self.father.show_dialogue:
            self.father.start_dialogue(self.player.x, self.player.y)
        
        # Verificar colisión con la madre
        mother_rect = pygame.Rect(self.mother.x, self.mother.y, self.mother.width, self.mother.height)
        if player_rect.colliderect(mother_rect) and not self.mother.show_dialogue:
            self.mother.start_dialogue(self.player.x, self.player.y)
    
    def process_action(self):
        """Procesa la acción del botón ENTER"""
        # Verificar si está cerca de algún NPC para forzar diálogo
        player_rect = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)
        
        # Verificar proximidad con el padre
        father_rect = pygame.Rect(self.father.x - 20, self.father.y - 20, self.father.width + 40, self.father.height + 40)
        if player_rect.colliderect(father_rect) and not self.father.show_dialogue:
            self.father.start_dialogue(self.player.x, self.player.y)
        
        # Verificar proximidad con la madre
        mother_rect = pygame.Rect(self.mother.x - 20, self.mother.y - 20, self.mother.width + 40, self.mother.height + 40)
        if player_rect.colliderect(mother_rect) and not self.mother.show_dialogue:
            self.mother.start_dialogue(self.player.x, self.player.y)
        
        # Verificar si está en alguna escalera o salida para activar cinemática
        if not self.cinematic_triggered:
            # Escalera hacia abajo (sótano) - izquierda
            if (self.player.x >= 75 and self.player.x <= 85 and 
                self.player.y >= 375 and self.player.y <= 385):
                self.trigger_cinematic()
            
            # Escalera hacia arriba - área central
            elif (self.player.x >= 300 and self.player.x <= 350 and 
                  self.player.y >= 240 and self.player.y <= 260):
                self.trigger_cinematic()
            
            # Salida derecha (puerta principal)
            elif (self.player.x >= 750 and self.player.x <= 800 and 
                  self.player.y >= 250 and self.player.y <= 350):
                self.trigger_cinematic()
            
            # Salida superior (ventana/puerta)
            elif (self.player.x >= 400 and self.player.x <= 500 and 
                  self.player.y >= 0 and self.player.y <= 30):
                self.trigger_cinematic()
        
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
            
            # Mostrar indicador de acción
            self.draw_action_indicator()
            
            # Mostrar flash final si está activo
            if self.final_flash:
                self.draw_final_flash()
            
            # Actualiza la pantalla
            pygame.display.flip()
            
        elif self.game_state == CINEMATIC:
            # Dibujar el ambiente primero (fondo)
            self.environment.draw(self.screen)
            
            # Dibujar los NPCs
            self.father.draw(self.screen)
            self.mother.draw(self.screen)
            
            # Dibujar el jugador
            self.player.draw(self.screen)
            
            # Dibujar el enemigo
            self.enemy.draw(self.screen)
            
            # Dibujar los goblins aleatorios
            for goblin in self.random_goblins:
                goblin.draw(self.screen)
            
            # Efecto de flash
            self.draw_flash_effect()
            
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
    
    def draw_flash_effect(self):
        """Dibuja el efecto de flash en pantalla completa"""
        if self.flash_timer < self.flash_duration:
            # Calcular la intensidad del flash (máximo al inicio, decrece con el tiempo)
            intensity = 255 - (self.flash_timer * 255 // self.flash_duration)
            
            # Crear una superficie semi-transparente blanca
            flash_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            flash_surface.set_alpha(intensity)
            flash_surface.fill(WHITE)
            
            # Dibujar el flash sobre toda la pantalla
            self.screen.blit(flash_surface, (0, 0))
    
    def draw_action_indicator(self):
        """Dibuja el indicador del botón de acción"""
        font = pygame.font.Font(None, 20)
        
        # Verificar si está cerca de algún NPC o la puerta
        player_rect = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)
        
        # Verificar proximidad con NPCs
        father_rect = pygame.Rect(self.father.x - 20, self.father.y - 20, self.father.width + 40, self.father.height + 40)
        mother_rect = pygame.Rect(self.mother.x - 20, self.mother.y - 20, self.mother.width + 40, self.mother.height + 40)
        
        # Verificar proximidad con la puerta
        entrance_x = 350
        entrance_width = 100
        entrance_rect = pygame.Rect(entrance_x, WINDOW_HEIGHT - 40, entrance_width, 40)
        
        show_indicator = False
        action_text = ""
        
        if player_rect.colliderect(father_rect) or player_rect.colliderect(mother_rect):
            show_indicator = True
            action_text = "ENTER - Hablar"
        elif player_rect.colliderect(entrance_rect) and not self.cinematic_triggered:
            show_indicator = True
            action_text = "ENTER - Salir"
        
        if show_indicator:
            # Dibujar fondo del indicador
            text_surface = font.render(action_text, True, WHITE)
            text_rect = text_surface.get_rect()
            
            # Fondo del texto
            bg_rect = pygame.Rect(self.player.x - 10, self.player.y - 30, text_rect.width + 20, text_rect.height + 10)
            pygame.draw.rect(self.screen, BLACK, bg_rect)
            pygame.draw.rect(self.screen, WHITE, bg_rect, 2)
            
            # Texto
            text_rect.center = bg_rect.center
            self.screen.blit(text_surface, text_rect)
            
            # Indicador visual de cooldown
            if self.action_cooldown > 0:
                cooldown_text = font.render(f"({self.action_cooldown//10 + 1})", True, YELLOW)
                cooldown_rect = cooldown_text.get_rect()
                cooldown_rect.center = (bg_rect.centerx, bg_rect.centery + 20)
                self.screen.blit(cooldown_text, cooldown_rect)
    
    def draw_final_flash(self):
        """Dibuja el flash final cuando el Goblin King se lleva a los padres"""
        # Calcular la intensidad del flash (máximo al inicio, decrece con el tiempo)
        intensity = 255 - (self.final_flash_timer * 255 // 60)
        
        # Crear una superficie semi-transparente púrpura
        flash_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        flash_surface.set_alpha(intensity)
        flash_surface.fill(PURPLE)
        
        # Dibujar el flash sobre toda la pantalla
        self.screen.blit(flash_surface, (0, 0))
        
        # Texto dramático
        font = pygame.font.Font(None, 36)
        text = font.render("¡Los padres han sido secuestrados!", True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        self.screen.blit(text, text_rect)
        
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

