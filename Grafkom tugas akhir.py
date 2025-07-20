from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

window_width, window_height = 800, 600
mode = 'point'
color = (1.0, 0.0, 0.0)
points = []
line_thickness = 2

translate = [0.0, 0.0]
rotation = 0
scale = 1.0

mode3D = False
angle3D = 0

window_defined = False
clip_window = []  # [(x_min, y_min), (x_max, y_max)]

#A1 A2 - Gambar objek dasar 2D dan input koordinat dengan mouse
def draw_2d_objects():
    glColor3f(*color)
    glLineWidth(line_thickness)
    glPushMatrix()
    glTranslatef(*translate, 0.0)  #C4 - Translasi
    glRotatef(rotation, 0.0, 0.0, 1.0)  #C4 - Rotasi
    glScalef(scale, scale, 1.0)  #C4 - Scaling

    if mode == 'point' and points:
        glBegin(GL_POINTS)
        for p in points:
            glVertex2f(*p)
        glEnd()
    elif mode == 'line' and len(points) >= 2:
        p1, p2 = points[-2], points[-1]
        if window_defined:
            clipped = cohen_sutherland_clip(p1[0], p1[1], p2[0], p2[1])
            if clipped:
                glColor3f(0.0, 1.0, 0.0)  #D7 - objek dalam window jadi hijau
                glBegin(GL_LINES)
                glVertex2f(clipped[0], clipped[1])
                glVertex2f(clipped[2], clipped[3])
                glEnd()
        else:
            glBegin(GL_LINES)
            glVertex2f(*p1)
            glVertex2f(*p2)
            glEnd()
    elif mode == 'square' and len(points) >= 1:
        x, y = points[-1]
        size = 50
        glBegin(GL_LINE_LOOP)
        glVertex2f(x, y)
        glVertex2f(x + size, y)
        glVertex2f(x + size, y + size)
        glVertex2f(x, y + size)
        glEnd()
    elif mode == 'ellipse' and len(points) >= 1:
        x, y = points[-1]
        glBegin(GL_LINE_LOOP)
        for i in range(360):
            theta = math.radians(i)
            glVertex2f(x + 40 * math.cos(theta), y + 20 * math.sin(theta))
        glEnd()

    glPopMatrix()

    if window_defined:
        glColor3f(0.2, 0.2, 1.0)
        x1, y1 = clip_window[0]
        x2, y2 = clip_window[1]
        glBegin(GL_LINE_LOOP)
        glVertex2f(x1, y1)
        glVertex2f(x2, y1)
        glVertex2f(x2, y2)
        glVertex2f(x1, y2)
        glEnd()

#B1 - Visualisasi objek 3D
#B3 - Shading & Pencahayaan
def draw_3d_object():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    ambient = [0.2, 0.2, 0.2, 1.0]
    diffuse = [0.8, 0.8, 0.8, 1.0]
    specular = [1.0, 1.0, 1.0, 1.0]
    position = [4.0, 4.0, 4.0, 1.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular)
    glLightfv(GL_LIGHT0, GL_POSITION, position)

    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMateriali(GL_FRONT, GL_SHININESS, 50)

    glColor3f(*color)
    glRotatef(angle3D, 1, 1, 0)  #B2 - Rotasi objek 3D
    glutSolidCube(2)
    glDisable(GL_LIGHTING)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    if mode3D:
        gluLookAt(4, 4, 4, 0, 0, 0, 0, 1, 0)  #B4 - Kamera dan perspektif
        draw_3d_object()
    else:
        draw_2d_objects()

    glutSwapBuffers()

def reshape(w, h):
    global window_width, window_height
    window_width, window_height = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if mode3D:
        gluPerspective(45, w / h, 1, 100)  #B4 - Proyeksi perspektif
    else:
        gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)

#B2, C5 - Keyboard kontrol untuk transformasi objek
#B3, C5 - Warna, ketebalan, mode, clipping
def keyboard(key, x, y):
    global mode, color, line_thickness, translate, rotation, scale, mode3D, clip_window, window_defined
    key = key.decode("utf-8")
    if key == 'q': sys.exit()
    elif key == '1': mode = 'point'  #A1
    elif key == '2': mode = 'line'   #A1
    elif key == '3': mode = 'square' #A1
    elif key == '4': mode = 'ellipse' #A1
    elif key == 'r': color = (1.0, 0.0, 0.0)  #B3
    elif key == 'g': color = (0.0, 1.0, 0.0)
    elif key == 'b': color = (0.0, 0.0, 1.0)
    elif key == '+': line_thickness += 1  #B3
    elif key == '-': line_thickness = max(1, line_thickness - 1)
    elif key == 'w': translate[1] += 10  #C5
    elif key == 's': translate[1] -= 10
    elif key == 'a': translate[0] -= 10
    elif key == 'd': translate[0] += 10
    elif key == 'z': scale += 0.1
    elif key == 'x': scale = max(0.1, scale - 0.1)
    elif key == 'e': rotation += 10
    elif key == 'm': mode3D = not mode3D  #B1
    elif key == 'c':
        if len(points) >= 2:
            clip_window = [points[-2], points[-1]]  #D6
            window_defined = True
    reshape(window_width, window_height)
    glutPostRedisplay()

#A2 - Input titik dengan klik mouse
def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and not mode3D:
        y = window_height - y
        points.append((x, y))
        glutPostRedisplay()

def idle():
    global angle3D
    if mode3D:
        angle3D += 0.2
        glutPostRedisplay()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glPointSize(5.0)

#D7 D8 - Algoritma Clipping Cohen-Sutherland
INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def compute_out_code(x, y, xmin, xmax, ymin, ymax):
    code = INSIDE
    if x < xmin: code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin: code |= BOTTOM
    elif y > ymax: code |= TOP
    return code

def cohen_sutherland_clip(x1, y1, x2, y2):
    if not window_defined: return None
    xmin, ymin = clip_window[0]
    xmax, ymax = clip_window[1]

    outcode1 = compute_out_code(x1, y1, xmin, xmax, ymin, ymax)
    outcode2 = compute_out_code(x2, y2, xmin, xmax, ymin, ymax)
    accept = False

    while True:
        if not (outcode1 | outcode2):
            accept = True
            break
        elif outcode1 & outcode2:
            break
        else:
            outcode_out = outcode1 if outcode1 else outcode2
            if outcode_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif outcode_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif outcode_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif outcode_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin
            if outcode_out == outcode1:
                x1, y1 = x, y
                outcode1 = compute_out_code(x1, y1, xmin, xmax, ymin, ymax)
            else:
                x2, y2 = x, y
                outcode2 = compute_out_code(x2, y2, xmin, xmax, ymin, ymax)

    if accept:
        return (x1, y1, x2, y2)
    else:
        return None

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"UAS Grafkom 2025 - 2D & 3D Viewer")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutIdleFunc(idle)
    glutMainLoop()


if __name__ == '__main__':
    main()