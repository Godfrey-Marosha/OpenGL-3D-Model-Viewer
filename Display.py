# Display.py
import pygame
from pygame.locals import *
from OpenGL.GL import *

def handle_events(shapes, current_shape_index, draw_all_shapes):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_shape_index = (current_shape_index + 1) % len(shapes)
                draw_all_shapes = False
    return current_shape_index, draw_all_shapes

def draw_shape(shapes, index):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    shapes[index]()
    pygame.display.flip()

def translate_obj(dx, dy, dz):
    glTranslatef(dx, dy, dz)

def rotate_obj(angle, axis):
    glRotatef(angle, *axis)

def scale_obj(sx, sy, sz):
    glScalef(sx, sy, sz)
