from OpenGL.GL import *

vertices = (
    (-1, -1, -1),
    (1, -1, -1),
    (0, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (0, 1, 1)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 0),
    (3, 4),
    (4, 5),
    (5, 3),
    (0, 3),
    (1, 4),
    (2, 5)
)

def Prism():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
