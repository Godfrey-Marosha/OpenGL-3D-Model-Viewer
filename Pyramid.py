from OpenGL.GL import *

vertices = (
    (0, 1, 0),
    (-1, -1, 1),
    (1, -1, 1),
    (1, -1, -1),
    (-1, -1, -1)
)

edges = (
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 1)
)

def Pyramid():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
