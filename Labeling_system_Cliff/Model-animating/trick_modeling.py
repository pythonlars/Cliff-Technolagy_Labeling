import pygame
import sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Correct file paths: using raw strings and adding the extension
vertextxt = r"C:\Users\User\OneDrive\Desktop\txtFiles\vertices.txt"
facestxt = r"C:\Users\User\OneDrive\Desktop\txtFiles\faces.txt"

paints = [     # Colors for our faces (RGB format)
    (0, 1, 0),       # green (using normalized values for OpenGL)
    (1, 0, 0),       # red
    (1, 1, 0),       # yellow
    (0, 1, 1),       # cyan
    (0, 0, 1),       # blue
    (1, 1, 1)        # white
]

def get_list(txtname):
    listname = []
    with open(txtname) as f:
        for line in f:
            # Remove extra characters and split the line by commas
            line = line.rstrip(",\r\n").replace("(", "").replace(")", "").replace(" ", '')
            row = list(line.split(","))
            listname.append(row)
    # Convert all values to float
    listname = [[float(j) for j in i] for i in listname]
    return listname

modelVerts = get_list(vertextxt)  # list of vertices
modelFaces = get_list(facestxt)    # list of faces

def drawfaces():
    # Use the bitwise OR operator | to clear the buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)  # We're drawing triangles
    for face in modelFaces:
        color_index = 0
        for vert_index in face:
            # Cycle through paints for each vertex in the face
            glColor3fv(paints[color_index])
            glVertex3fv(modelVerts[int(vert_index)])
            color_index = (color_index + 1) % len(paints)
    glEnd()

def main():
    pygame.init()
    display = (800, 800)  # Set window size
    pygame.display.set_caption("RENDERING OBJECT")
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)  # Enable depth testing for correct 3D rendering
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)  # Translate the object
    glRotatef(-90, 1, 0, 0) # Rotate the object

    Left = False
    Right = False

    def moveOBJ():
        # Rotate the object based on key flags
        if Left:
            glRotatef(-1, 0, 0, 1)
        if Right:
            glRotatef(1, 0, 0, 1)

    clock = pygame.time.Clock()  # For frame rate control

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_a:
                    Left = True
                if event.key == K_d:
                    Right = True
            if event.type == KEYUP:
                if event.key == K_a:
                    Left = False
                if event.key == K_d:
                    Right = False

        drawfaces()
        moveOBJ()
        pygame.display.flip()
        clock.tick(60)

main()
