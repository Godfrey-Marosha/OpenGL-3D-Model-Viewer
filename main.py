# main.py
import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Cube import Cube
from Prism import Prism
from Pyramid import Pyramid
from Display import handle_events, draw_shape, translate_obj, rotate_obj, scale_obj

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    shapes = [Cube, Prism, Pyramid]
    current_shape_index = 0

    while True:
        current_shape_index, _ = handle_events(shapes, current_shape_index, False)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            translate_obj(-0.1, 0, 0)
        elif keys[pygame.K_RIGHT]:
            translate_obj(0.1, 0, 0)
        elif keys[pygame.K_UP]:
            translate_obj(0, 0.1, 0)
        elif keys[pygame.K_DOWN]:
            translate_obj(0, -0.1, 0)
        elif keys[pygame.K_w]:
            translate_obj(0, 0, 0.1)
        elif keys[pygame.K_s]:
            translate_obj(0, 0, -0.1)
        elif keys[pygame.K_q]:
            rotate_obj(1, (1, 0, 0))  # Rotate around x-axis positively
        elif keys[pygame.K_e]:
            rotate_obj(-1, (1, 0, 0))  # Rotate around x-axis negatively
        elif keys[pygame.K_a]:
            rotate_obj(1, (0, 1, 0))  # Rotate around y-axis positively
        elif keys[pygame.K_d]:
            rotate_obj(-1, (0, 1, 0))  # Rotate around y-axis negatively
        elif keys[pygame.K_z]:
            rotate_obj(1, (0, 0, 1))  # Rotate around z-axis positively
        elif keys[pygame.K_c]:
            rotate_obj(-1, (0, 0, 1))  # Rotate around z-axis negatively
        elif keys[pygame.K_l]:
            scale_obj(1.1, 1, 1)  # Scale up on x-axis
        elif keys[pygame.K_j]:
            scale_obj(0.9, 1, 1)  # Scale down on x-axis
        elif keys[pygame.K_i]:
            scale_obj(1, 1.1, 1)  # Scale up on y-axis
        elif keys[pygame.K_k]:
            scale_obj(1, 0.9, 1)  # Scale down on y-axis
        elif keys[pygame.K_u]:
            scale_obj(1, 1, 1.1)  # Scale up on z-axis
        elif keys[pygame.K_m]:
            scale_obj(1, 1, 0.9)  # Scale down on z-axis

        glRotatef(1, 3, 1, 1)  # Continuous rotation for display purposes

        draw_shape(shapes, current_shape_index)

        pygame.time.wait(10)

if __name__ == "__main__":
    main()
