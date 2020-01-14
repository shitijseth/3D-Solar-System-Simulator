##All the libraries##
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter import *
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import imread


##GUI using Tkinter##
window = Tk()

window.title("Solar System 3D Simulator")

window.geometry('500x500')


lbl4 = Label(window, text='Enter a start date')
lbl4.grid(row=0, column=0)
start_date_value = IntVar()
start_date = Entry()

lbl1 = Label(window, text="Click here to start the simulation -> ")
lbl1.grid(row=2, column=0)

lbl3 = Label(window, text = "Enter a value for General Relativity ->")
lbl3.grid(row=1, column=0)
username = IntVar()
name = Entry(textvariable=username)
name.grid(row=1, column=1, pady=10)


def clicked():
    lbl = Label(window, text="The Simulation is loading...", bg = 'lightgreen')
    lbl.grid(row=4, column=1, pady=10)
##Constant
    GMs = 4*(math.pi**2)
#    G = 6.67e
##Bulk and Orbital Parameters, Initial Positions for all the Planets and the Sun
 #Sun
    m_sun = 1.989e50
    x_sun = 0.00000001
    y_sun = 0.00000001
    z_sun = 0.00000001

 #Earth
    ecc_earth = 0.0167
    semimajor_earth = 1.00000011
    a_earth = semimajor_earth
    perihelion_earth = a_earth*(1-ecc_earth)
    m_earth = 9.72e24
    vp_earth = math.sqrt(GMs) * math.sqrt((1+ecc_earth) / (a_earth*(1-ecc_earth)) * (1+(m_earth/m_sun)))
    vx_earth = 0
    vy_earth = vp_earth
    vz_earth = 0
    x_earth = -perihelion_earth
    y_earth = 0
    z_earth = 0

 #Mercury
    ecc_mercury = 0.205630
    semimajor_mercury = 0.387098 #AU
    a = semimajor_mercury
    perihelion_mercury = a*(1-ecc_mercury)
    m_mercury = 3.3011e23 #kg
    vp_mercury = math.sqrt(GMs) * math.sqrt((1+ecc_mercury) / (a*(1-ecc_mercury)) * (1+(m_mercury/m_sun)))
    vx_mercury = 0
    vy_mercury = vp_mercury
    vz_mercury = 0
    x_mercury = -perihelion_mercury
    y_mercury = 0
    z_mercury = semimajor_mercury * math.cos(1.44862)

    #Venus
    ecc_venus = 0.006772
    semimajor_venus = 0.723332 #AU
    a = semimajor_venus
    perihelion_venus = a*(1-ecc_venus)
    m_venus = 4.8675e24 #kg
    vp_venus = math.sqrt(GMs) * math.sqrt((1+ecc_venus) / (a*(1-ecc_venus)) * (1+(m_venus/m_sun)))
    vx_venus = 0
    vy_venus = vp_venus
    vz_venus = 0
    x_venus = -perihelion_venus
    y_venus = 0
    z_venus = semimajor_venus * math.cos(1.511455)

    #Mars
    ecc_mars = 0.0935
    semimajor_mars = 1.5235511 #AU
    a = semimajor_mars
    perihelion_mars = a*(1-ecc_mars)
    m_mars = 0.64171e24 #kg
    vp_mars = math.sqrt(GMs) * math.sqrt((1+ecc_mars) / (a*(1-ecc_mars)) * (1+(m_mars/m_sun)))
    vx_mars = 0
    vy_mars = vp_mars
    vz_mars = 0
    x_mars = -perihelion_mars
    y_mars = 0
    z_mars = semimajor_mars * math.cos(1.537635)

    #Jupiter
    ecc_jupiter = 0.0489
    semimajor_jupiter = 5.204418 #AU
    a = semimajor_jupiter
    perihelion_jupiter = a*(1-ecc_jupiter)
    m_jupiter = 1898.19e24 #kg
    vp_jupiter = math.sqrt(GMs) * math.sqrt((1+ecc_jupiter) / (a*(1-ecc_jupiter)) * (1+(m_jupiter/m_sun)))
    vx_jupiter = 0
    vy_jupiter = vp_jupiter
    vz_jupiter = 0
    x_jupiter = -perihelion_jupiter
    y_jupiter = 0
    z_jupiter = semimajor_jupiter * math.cos(1.548107)

    #Saturn
    ecc_saturn = 0.0565
    semimajor_saturn = 9.582556177385 #AU
    a = semimajor_saturn
    perihelion_saturn = a*(1-ecc_saturn)
    m_saturn = 568.34e24 #kg
    vp_saturn = math.sqrt(GMs) * math.sqrt((1+ecc_saturn) / (a*(1-ecc_saturn)) * (1+(m_saturn/m_sun)))
    vx_saturn = 0
    vy_saturn = vp_saturn
    vz_saturn = 0
    x_saturn = -perihelion_saturn
    y_saturn = 0
    z_saturn = semimajor_jupiter * math.cos(1.527163)

    #Uranus
    ecc_uranus = 0.0457
    semimajor_uranus = 19.201209125 #AU
    a = semimajor_uranus
    perihelion_uranus = a*(1-ecc_uranus)
    m_uranus = 86.813e24 #kg
    vp_uranus = math.sqrt(GMs) * math.sqrt((1+ecc_uranus) / (a*(1-ecc_uranus)) * (1+(m_uranus/m_sun)))
    vx_uranus = 0
    vy_uranus = vp_uranus
    vz_uranus = 0
    x_uranus = -perihelion_uranus
    y_uranus = 0
    z_uranus = semimajor_uranus * math.cos(1.556834)

    #Neptune
    ecc_neptune = 0.0113
    semimajor_neptune = 30.047620189 #AU
    a = semimajor_neptune
    perihelion_neptune = a*(1-ecc_neptune)
    m_neptune = 102.413e24 #kg
    vp_neptune = math.sqrt(GMs) * math.sqrt((1+ecc_neptune) / (a*(1-ecc_neptune)) * (1+(m_neptune/m_sun)))
    vx_neptune = 0
    vy_neptune = vp_neptune
    vz_neptune = 0
    x_neptune = -perihelion_neptune
    y_neptune = 0
    z_neptune = semimajor_neptune * math.cos(1.53938)

    #Pluto
    ecc_pluto = 0.2488
    semimajor_pluto = 39.481711687 #AU
    a = semimajor_pluto
    perihelion_pluto = a*(1-ecc_pluto)
    m_pluto = 0.01303e24 #kg
    vp_pluto = math.sqrt(GMs) * math.sqrt((1+ecc_pluto) / (a*(1-ecc_pluto)) * (1+(m_pluto/m_sun)))
    vx_pluto = 0
    vy_pluto = vp_pluto
    vz_pluto = 0
    x_pluto = -perihelion_pluto
    y_pluto = 0
    z_pluto = semimajor_pluto * math.cos(1.2706)


##Creating arrays to store positions, calculating intial radii and velocities
    xarr_sun = np.array([])
    yarr_sun = np.array([])
    zarr_sun = np.array([])
    xarr_sun = np.append(xarr_sun, x_sun)
    yarr_sun = np.append(yarr_sun, y_sun)
    zarr_sun = np.append(zarr_sun, z_sun)

    xarr_mercury = np.array([])
    yarr_mercury = np.array([])
    zarr_mercury = np.array([])
    xarr_mercury = np.append(xarr_mercury, x_mercury)
    yarr_mercury = np.append(yarr_mercury, y_mercury)
    zarr_mercury = np.append(zarr_mercury, z_mercury)
    r_mercury = math.sqrt(x_mercury**2 + y_mercury**2 + z_mercury**2)
    v_mercury = math.sqrt(vx_mercury**2 + vy_mercury**2 + vz_mercury**2)

    xarr_venus = np.array([])
    yarr_venus = np.array([])
    zarr_venus = np.array([])
    xarr_venus = np.append(xarr_venus, x_venus)
    yarr_venus = np.append(yarr_venus, y_venus)
    zarr_venus = np.append(zarr_venus, z_venus)
    r_venus = math.sqrt(x_venus**2 + y_venus**2 + z_venus**2)
    v_venus = math.sqrt(vx_venus**2 + vy_venus**2 + vz_venus**2)

    xarr_earth = np.array([])
    yarr_earth = np.array([])
    zarr_earth = np.array([])
    xarr_earth = np.append(xarr_earth, x_earth)
    yarr_earth = np.append(yarr_earth, y_earth)
    zarr_earth = np.append(zarr_earth, z_earth)
    r_earth = math.sqrt(x_earth**2 + y_earth**2 + z_earth**2)
    v_earth = math.sqrt(vx_earth**2 + vy_earth**2 + vz_earth**2)

    xarr_mars = np.array([])
    yarr_mars = np.array([])
    zarr_mars = np.array([])
    xarr_mars = np.append(xarr_mars, x_mars)
    yarr_mars = np.append(yarr_mars, y_mars)
    zarr_mars = np.append(zarr_mars, z_mars)
    r_mars = math.sqrt(x_mars**2 + y_mars**2 + z_mars**2)
    v_mars = math.sqrt(vx_mars**2 + vy_mars**2 + vz_mars**2)

    xarr_jupiter = np.array([])
    yarr_jupiter = np.array([])
    zarr_jupiter = np.array([])
    xarr_jupiter = np.append(xarr_jupiter, x_jupiter)
    yarr_jupiter = np.append(yarr_jupiter, y_jupiter)
    zarr_jupiter = np.append(zarr_jupiter, z_jupiter)
    r_jupiter = math.sqrt(x_jupiter**2 + y_jupiter**2 + z_jupiter**2)
    v_jupiter = math.sqrt(vx_jupiter**2 + vy_jupiter**2 + vz_jupiter**2)

    xarr_saturn = np.array([])
    yarr_saturn = np.array([])
    zarr_saturn = np.array([])
    xarr_saturn = np.append(xarr_saturn, x_saturn)
    yarr_saturn = np.append(yarr_saturn, y_saturn)
    zarr_saturn = np.append(zarr_saturn, z_saturn)
    r_saturn = math.sqrt(x_saturn**2 + y_saturn**2 + z_saturn**2)
    v_saturn = math.sqrt(vx_saturn**2 + vy_saturn**2 + vz_saturn**2)

    xarr_uranus = np.array([])
    yarr_uranus = np.array([])
    zarr_uranus = np.array([])
    xarr_uranus = np.append(xarr_uranus, x_uranus)
    yarr_uranus = np.append(yarr_uranus, y_uranus)
    zarr_uranus = np.append(zarr_uranus, z_uranus)
    r_uranus = math.sqrt(x_uranus**2 + y_uranus**2 + z_uranus**2)
    v_uranus = math.sqrt(vx_uranus**2 + vy_uranus**2 + vz_uranus**2)

    xarr_neptune = np.array([])
    yarr_neptune = np.array([])
    zarr_neptune = np.array([])
    xarr_neptune = np.append(xarr_neptune, x_neptune)
    yarr_neptune = np.append(yarr_neptune, y_neptune)
    zarr_neptune = np.append(zarr_neptune, z_neptune)
    r_neptune = math.sqrt(x_neptune**2 + y_neptune**2 + z_neptune**2)
    v_neptune = math.sqrt(vx_neptune**2 + vy_neptune**2 + vz_neptune**2)

    xarr_pluto = np.array([])
    yarr_pluto = np.array([])
    zarr_pluto = np.array([])
    xarr_pluto = np.append(xarr_pluto, x_pluto)
    yarr_pluto = np.append(yarr_pluto, y_pluto)
    zarr_pluto = np.append(zarr_pluto, z_pluto)
    r_pluto = math.sqrt(x_pluto**2 + y_pluto**2 + z_pluto**2)
    v_pluto = math.sqrt(vx_pluto**2 + vy_pluto**2 + vz_pluto**2)

##Timestep
    h = 1e-3
##Runtime in years
    t_final = 5
    t_initial = 0
    t = t_initial
##To store values for General Relativity
    count = 0
    alpha = int(name.get())

    while (t < t_final):

##Calculating relative radius from Jupiter
        rrel_mercury = math.sqrt((x_mercury - x_jupiter)**2 + (y_mercury - y_jupiter)**2 + (z_mercury - z_jupiter)**2)
        rrel_venus = math.sqrt((x_venus - x_jupiter)**2 + (y_venus - y_jupiter)**2 + (z_venus - z_jupiter)**2)
        rrel_earth = math.sqrt((x_earth - x_jupiter)**2 + (y_earth - y_jupiter)**2 + (z_earth - z_jupiter)**2)
        rrel_mars = math.sqrt((x_mars - x_jupiter)**2 + (y_mars - y_jupiter)**2 + (z_mars - z_jupiter)**2)
        rrel_saturn = math.sqrt((x_saturn - x_jupiter)**2 + (y_saturn - y_jupiter)**2 + (z_saturn - z_jupiter)**2)
        rrel_uranus = math.sqrt((x_uranus - x_jupiter)**2 + (y_uranus - y_jupiter)**2 + (z_uranus - z_jupiter)**2)
        rrel_neptune = math.sqrt((x_neptune - x_jupiter)**2 + (y_neptune - y_jupiter)**2 + (z_neptune - z_jupiter)**2)
        rrel_pluto = math.sqrt((x_pluto - x_jupiter)**2 + (y_pluto - y_jupiter)**2 + (z_pluto - z_jupiter)**2)

##Velocity Verlet method to calculate new positions (Sun is stationary for now, so just adding 0)
        #Sun
        x_sun = x_sun + 0
        y_sun = y_sun + 0
        z_sun = z_sun + 0

        #Mercury
        ax_mercury  = (-((GMs * x_mercury * math.sqrt(x_mercury**2 + y_mercury**2)) / (r_mercury**4)) - ((GMs * 0.001 * (x_mercury - x_jupiter) * math.sqrt((x_mercury - x_jupiter)**2 + (y_mercury - y_jupiter)**2) / rrel_mercury**4)) * (1 + (alpha / r_mercury**2)))
        ay_mercury  = (-((GMs * y_mercury * math.sqrt(x_mercury**2 + y_mercury**2)) / (r_mercury**4)) - ((GMs * 0.001 * (y_mercury - y_jupiter) * math.sqrt((x_mercury - x_jupiter)**2 + (y_mercury - y_jupiter)**2) / rrel_mercury**4)) * (1 + (alpha / r_mercury**2)))
        az_mercury  = (-((GMs * z_mercury) / (r_mercury**3)) - ((GMs * 0.001 * (z_mercury - z_jupiter) / rrel_mercury**3)) * (1 + (alpha / r_mercury**2)))
        x_mercury   = x_mercury+ vx_mercury * h + ((1 / 2) * ax_mercury * (h**2))
        y_mercury   = y_mercury+ vy_mercury * h + ((1 / 2) * ay_mercury * (h**2))
        z_mercury   = z_mercury+ vz_mercury * h + ((1 / 2) * az_mercury * (h**2))
        r_mercury   = math.sqrt(x_mercury**2 + y_mercury**2 + z_mercury**2)
        ax1_mercury = (-((GMs * x_mercury * math.sqrt(x_mercury**2 + y_mercury**2)) / (r_mercury**4)) - ((GMs * 0.001 * (x_mercury - x_jupiter) * math.sqrt((x_mercury - x_jupiter)**2 + (y_mercury - y_jupiter)**2) / rrel_mercury**4)) * (1 + (alpha / r_mercury**2)))
        ay1_mercury = (-((GMs * y_mercury * math.sqrt(x_mercury**2 + y_mercury**2)) / (r_mercury**4)) - ((GMs * 0.001 * (y_mercury - y_jupiter) * math.sqrt((x_mercury - x_jupiter)**2 + (y_mercury - y_jupiter)**2) / rrel_mercury**4)) * (1 + (alpha / r_mercury**2)))
        az1_mercury = (-((GMs * z_mercury) / (r_mercury**3)) - ((GMs * 0.001 * (z_mercury - z_jupiter) / rrel_mercury**3)) * (1 + (alpha / r_mercury**2)))
        vx_mercury  = vx_mercury + ((h / 2) * (ax1_mercury + ax_mercury))
        vy_mercury  = vy_mercury + ((h / 2) * (ay1_mercury + ay_mercury))
        vz_mercury  = vz_mercury + ((h / 2) * (az1_mercury + az_mercury))
        v_mercury   = math.sqrt(vx_mercury**2 + vy_mercury**2 + vz_mercury**2)

        #Venus
        ax_venus  = (-((GMs * x_venus * math.sqrt(x_venus**2 + y_venus**2)) / (r_venus**4)) - ((GMs * 0.001 * (x_venus - x_jupiter) * math.sqrt((x_venus - x_jupiter)**2 + (y_venus - y_jupiter)**2) / rrel_venus**4)) * (1 + (alpha / r_venus**2)))
        ay_venus  = (-((GMs * y_venus * math.sqrt(x_venus**2 + y_venus**2)) / (r_venus**4)) - ((GMs * 0.001 * (y_venus - y_jupiter) * math.sqrt((x_venus - x_jupiter)**2 + (y_venus - y_jupiter)**2) / rrel_venus**4)) * (1 + (alpha / r_venus**2)))
        az_venus  = (-((GMs * z_venus) / (r_venus**3)) - ((GMs * 0.001 * (z_venus - z_jupiter) / rrel_venus**3)) * (1 + (alpha / r_venus**2)))
        x_venus   = x_venus+ vx_venus * h + ((1 / 2) * ax_venus * (h**2))
        y_venus   = y_venus+ vy_venus * h + ((1 / 2) * ay_venus * (h**2))
        z_venus   = z_venus+ vz_venus * h + ((1 / 2) * az_venus * (h**2))
        r_venus   = math.sqrt(x_venus**2 + y_venus**2 + z_venus**2)
        ax1_venus = (-((GMs * x_venus * math.sqrt(x_venus**2 + y_venus**2)) / (r_venus**4)) - ((GMs * 0.001 * (x_venus - x_jupiter) * math.sqrt((x_venus - x_jupiter)**2 + (y_venus - y_jupiter)**2) / rrel_venus**4)) * (1 + (alpha / r_venus**2)))
        ay1_venus = (-((GMs * y_venus * math.sqrt(x_venus**2 + y_venus**2)) / (r_venus**4)) - ((GMs * 0.001 * (y_venus - y_jupiter) * math.sqrt((x_venus - x_jupiter)**2 + (y_venus - y_jupiter)**2) / rrel_venus**4)) * (1 + (alpha / r_venus**2)))
        az1_venus = (-((GMs * z_venus) / (r_venus**3)) - ((GMs * 0.001 * (z_venus - z_jupiter) / rrel_venus**3)) * (1 + (alpha / r_venus**2)))
        vx_venus  = vx_venus + ((h / 2) * (ax1_venus + ax_venus))
        vy_venus  = vy_venus + ((h / 2) * (ay1_venus + ay_venus))
        vz_venus  = vz_venus + ((h / 2) * (az1_venus + az_venus))
        v_venus   = math.sqrt(vx_venus**2 + vy_venus**2 + vz_venus**2)


        ax_earth  = (-((GMs * x_earth * math.sqrt(x_earth**2 + y_earth**2)) / (r_earth**4)) - ((GMs * 0.001 * (x_earth - x_jupiter) * math.sqrt((x_earth - x_jupiter)**2 + (y_earth - y_jupiter)**2) / rrel_earth**4)) * (1 + (alpha / r_earth**2)))
        ay_earth  = (-((GMs * y_earth * math.sqrt(x_earth**2 + y_earth**2)) / (r_earth**4)) - ((GMs * 0.001 * (y_earth - y_jupiter) * math.sqrt((x_earth - x_jupiter)**2 + (y_earth - y_jupiter)**2) / rrel_earth**4)) * (1 + (alpha / r_earth**2)))
        az_earth  = (-((GMs * z_earth) / (r_earth**3)) - ((GMs * 0.001 * (z_earth - z_jupiter) / rrel_earth**3)) * (1 + (alpha / r_earth**2)))
        x_earth   = x_earth+ vx_earth * h + ((1 / 2) * ax_earth * (h**2))
        y_earth   = y_earth+ vy_earth * h + ((1 / 2) * ay_earth * (h**2))
        z_earth   = z_earth+ vz_earth * h + ((1 / 2) * az_earth * (h**2))
        r_earth   = math.sqrt(x_earth**2 + y_earth**2 + z_earth**2)
        ax1_earth = (-((GMs * x_earth * math.sqrt(x_earth**2 + y_earth**2)) / (r_earth**4)) - ((GMs * 0.001 * (x_earth - x_jupiter) * math.sqrt((x_earth - x_jupiter)**2 + (y_earth - y_jupiter)**2) / rrel_earth**4)) * (1 + (alpha / r_earth**2)))
        ay1_earth = (-((GMs * y_earth * math.sqrt(x_earth**2 + y_earth**2)) / (r_earth**4)) - ((GMs * 0.001 * (y_earth - y_jupiter) * math.sqrt((x_earth - x_jupiter)**2 + (y_earth - y_jupiter)**2) / rrel_earth**4)) * (1 + (alpha / r_earth**2)))
        az1_earth = (-((GMs * z_earth) / (r_earth**3)) - ((GMs * 0.001 * (z_earth - z_jupiter) / rrel_earth**3)) * (1 + (alpha / r_earth**2)))
        vx_earth  = vx_earth + ((h / 2) * (ax1_earth + ax_earth))
        vy_earth  = vy_earth + ((h / 2) * (ay1_earth + ay_earth))
        vz_earth  = vz_earth + ((h / 2) * (az1_earth + az_earth))
        v_earth   = math.sqrt(vx_earth**2 + vy_earth**2 + vz_earth**2)


        ax_mars  = (-((GMs * x_mars * math.sqrt(x_mars**2 + y_mars**2)) / (r_mars**4)) - ((GMs * 0.001 * (x_mars - x_jupiter) * math.sqrt((x_mars - x_jupiter)**2 + (y_mars - y_jupiter)**2) / rrel_mars**4)) * (1 + (alpha / r_mars**2)))
        ay_mars  = (-((GMs * y_mars * math.sqrt(x_mars**2 + y_mars**2)) / (r_mars**4)) - ((GMs * 0.001 * (y_mars - y_jupiter) * math.sqrt((x_mars - x_jupiter)**2 + (y_mars - y_jupiter)**2) / rrel_mars**4)) * (1 + (alpha / r_mars**2)))
        az_mars  = (-((GMs * z_mars) / (r_mars**3)) - ((GMs * 0.001 * (z_mars - z_jupiter) / rrel_mars**3)) * (1 + (alpha / r_mars**2)))
        x_mars   = x_mars+ vx_mars * h + ((1 / 2) * ax_mars * (h**2))
        y_mars   = y_mars+ vy_mars * h + ((1 / 2) * ay_mars * (h**2))
        z_mars   = z_mars+ vz_mars * h + ((1 / 2) * az_mars * (h**2))
        r_mars   = math.sqrt(x_mars**2 + y_mars**2 + z_mars**2)
        ax1_mars = (-((GMs * x_mars * math.sqrt(x_mars**2 + y_mars**2)) / (r_mars**4)) - ((GMs * 0.001 * (x_mars - x_jupiter) * math.sqrt((x_mars - x_jupiter)**2 + (y_mars - y_jupiter)**2) / rrel_mars**4)) * (1 + (alpha / r_mars**2)))
        ay1_mars = (-((GMs * y_mars * math.sqrt(x_mars**2 + y_mars**2)) / (r_mars**4)) - ((GMs * 0.001 * (y_mars - y_jupiter) * math.sqrt((x_mars - x_jupiter)**2 + (y_mars - y_jupiter)**2) / rrel_mars**4)) * (1 + (alpha / r_mars**2)))
        az1_mars = (-((GMs * z_mars) / (r_mars**3)) - ((GMs * 0.001 * (z_mars - z_jupiter) / rrel_mars**3)) * (1 + (alpha / r_mars**2)))
        vx_mars  = vx_mars + ((h / 2) * (ax1_mars + ax_mars))
        vy_mars  = vy_mars + ((h / 2) * (ay1_mars + ay_mars))
        vz_mars  = vz_mars + ((h / 2) * (az1_mars + az_mars))
        v_mars   = math.sqrt(vx_mars**2 + vy_mars**2 + vz_mars**2)


        ax_jupiter  = (-((GMs * x_jupiter * math.sqrt(x_jupiter**2 + y_jupiter**2)) / (r_jupiter**4)) * (1 + (alpha / r_jupiter**2)))
        ay_jupiter  = (-((GMs * y_jupiter * math.sqrt(x_jupiter**2 + y_jupiter**2)) / (r_jupiter**4)) * (1 + (alpha / r_jupiter**2)))
        az_jupiter  = (-((GMs * z_jupiter) / (r_jupiter**3)) * (1 + (alpha / r_jupiter**2)))
        x_jupiter   = x_jupiter+ vx_jupiter * h + ((1 / 2) * ax_jupiter * (h**2))
        y_jupiter   = y_jupiter+ vy_jupiter * h + ((1 / 2) * ay_jupiter * (h**2))
        z_jupiter   = z_jupiter+ vz_jupiter * h + ((1 / 2) * az_jupiter * (h**2))
        r_jupiter   = math.sqrt(x_jupiter**2 + y_jupiter**2 + z_jupiter**2)
        ax1_jupiter = (-((GMs * x_jupiter * math.sqrt(x_jupiter**2 + y_jupiter**2)) / (r_jupiter**4)) * (1 + (alpha / r_jupiter**2)))
        ay1_jupiter = (-((GMs * y_jupiter * math.sqrt(x_jupiter**2 + y_jupiter**2)) / (r_jupiter**4)) * (1 + (alpha / r_jupiter**2)))
        az1_jupiter = (-((GMs * z_jupiter) / (r_jupiter**3)) * (1 + (alpha / r_jupiter**2)))
        vx_jupiter  = vx_jupiter + ((h / 2) * (ax1_jupiter + ax_jupiter))
        vy_jupiter  = vy_jupiter + ((h / 2) * (ay1_jupiter + ay_jupiter))
        vz_jupiter  = vz_jupiter + ((h / 2) * (az1_jupiter + az_jupiter))
        v_jupiter   = math.sqrt(vx_jupiter**2 + vy_jupiter**2 + vz_jupiter**2)


        ax_saturn  = (-((GMs * x_saturn * math.sqrt(x_saturn**2 + y_saturn**2)) / (r_saturn**4)) + ((GMs * 0.001 * (x_saturn - x_jupiter) * math.sqrt((x_saturn - x_jupiter)**2 + (y_saturn - y_jupiter)**2) / rrel_saturn**4)) * (1 + (alpha / r_saturn**2)))
        ay_saturn  = (-((GMs * y_saturn * math.sqrt(x_saturn**2 + y_saturn**2)) / (r_saturn**4)) + ((GMs * 0.001 * (y_saturn - y_jupiter) * math.sqrt((x_saturn - x_jupiter)**2 + (y_saturn - y_jupiter)**2) / rrel_saturn**4)) * (1 + (alpha / r_saturn**2)))
        az_saturn  = (-((GMs * z_saturn) / (r_saturn**3)) + ((GMs * 0.001 * (z_saturn - z_jupiter) / rrel_saturn**3)) * (1 + (alpha / r_saturn**2)))
        x_saturn   = x_saturn+ vx_saturn * h + ((1 / 2) * ax_saturn * (h**2))
        y_saturn   = y_saturn+ vy_saturn * h + ((1 / 2) * ay_saturn * (h**2))
        z_saturn   = z_saturn+ vz_saturn * h + ((1 / 2) * az_saturn * (h**2))
        r_saturn   = math.sqrt(x_saturn**2 + y_saturn**2 + z_saturn**2)
        ax1_saturn = (-((GMs * x_saturn * math.sqrt(x_saturn**2 + y_saturn**2)) / (r_saturn**4)) + ((GMs * 0.001 * (x_saturn - x_jupiter) * math.sqrt((x_saturn - x_jupiter)**2 + (y_saturn - y_jupiter)**2) / rrel_saturn**4)) * (1 + (alpha / r_saturn**2)))
        ay1_saturn = (-((GMs * y_saturn * math.sqrt(x_saturn**2 + y_saturn**2)) / (r_saturn**4)) + ((GMs * 0.001 * (y_saturn - y_jupiter) * math.sqrt((x_saturn - x_jupiter)**2 + (y_saturn - y_jupiter)**2) / rrel_saturn**4)) * (1 + (alpha / r_saturn**2)))
        az1_saturn = (-((GMs * z_saturn) / (r_saturn**3)) + ((GMs * 0.001 * (z_saturn - z_jupiter) / rrel_saturn**3)) * (1 + (alpha / r_saturn**2)))
        vx_saturn  = vx_saturn + ((h / 2) * (ax1_saturn + ax_saturn))
        vy_saturn  = vy_saturn + ((h / 2) * (ay1_saturn + ay_saturn))
        vz_saturn  = vz_saturn + ((h / 2) * (az1_saturn + az_saturn))
        v_saturn   = math.sqrt(vx_saturn**2 + vy_saturn**2 + vz_saturn**2)


        ax_uranus  = (-((GMs * x_uranus * math.sqrt(x_uranus**2 + y_uranus**2)) / (r_uranus**4)) + ((GMs * 0.001 * (x_uranus - x_jupiter) * math.sqrt((x_uranus - x_jupiter)**2 + (y_uranus - y_jupiter)**2) / rrel_uranus**4)) * (1 + (alpha / r_uranus**2)))
        ay_uranus  = (-((GMs * y_uranus * math.sqrt(x_uranus**2 + y_uranus**2)) / (r_uranus**4)) + ((GMs * 0.001 * (y_uranus - y_jupiter) * math.sqrt((x_uranus - x_jupiter)**2 + (y_uranus - y_jupiter)**2) / rrel_uranus**4)) * (1 + (alpha / r_uranus**2)))
        az_uranus  = (-((GMs * z_uranus) / (r_uranus**3)) + ((GMs * 0.001 * (z_uranus - z_jupiter) / rrel_uranus**3)) * (1 + (alpha / r_uranus**2)))
        x_uranus   = x_uranus+ vx_uranus * h + ((1 / 2) * ax_uranus * (h**2))
        y_uranus   = y_uranus+ vy_uranus * h + ((1 / 2) * ay_uranus * (h**2))
        z_uranus   = z_uranus+ vz_uranus * h + ((1 / 2) * az_uranus * (h**2))
        r_uranus   = math.sqrt(x_uranus**2 + y_uranus**2 + z_uranus**2)
        ax1_uranus = (-((GMs * x_uranus * math.sqrt(x_uranus**2 + y_uranus**2)) / (r_uranus**4)) + ((GMs * 0.001 * (x_uranus - x_jupiter) * math.sqrt((x_uranus - x_jupiter)**2 + (y_uranus - y_jupiter)**2) / rrel_uranus**4)) * (1 + (alpha / r_uranus**2)))
        ay1_uranus = (-((GMs * y_uranus * math.sqrt(x_uranus**2 + y_uranus**2)) / (r_uranus**4)) + ((GMs * 0.001 * (y_uranus - y_jupiter) * math.sqrt((x_uranus - x_jupiter)**2 + (y_uranus - y_jupiter)**2) / rrel_uranus**4)) * (1 + (alpha / r_uranus**2)))
        az1_uranus = (-((GMs * z_uranus) / (r_uranus**3)) + ((GMs * 0.001 * (z_uranus - z_jupiter) / rrel_uranus**3)) * (1 + (alpha / r_uranus**2)))
        vx_uranus  = vx_uranus + ((h / 2) * (ax1_uranus + ax_uranus))
        vy_uranus  = vy_uranus + ((h / 2) * (ay1_uranus + ay_uranus))
        vz_uranus  = vz_uranus + ((h / 2) * (az1_uranus + az_uranus))
        v_uranus   = math.sqrt(vx_uranus**2 + vy_uranus**2 + vz_uranus**2)


        ax_neptune  = (-((GMs * x_neptune * math.sqrt(x_neptune**2 + y_neptune**2)) / (r_neptune**4)) + ((GMs * 0.001 * (x_neptune - x_jupiter) * math.sqrt((x_neptune - x_jupiter)**2 + (y_neptune - y_jupiter)**2) / rrel_neptune**4)) * (1 + (alpha / r_neptune**2)))
        ay_neptune  = (-((GMs * y_neptune * math.sqrt(x_neptune**2 + y_neptune**2)) / (r_neptune**4)) + ((GMs * 0.001 * (y_neptune - y_jupiter) * math.sqrt((x_neptune - x_jupiter)**2 + (y_neptune - y_jupiter)**2) / rrel_neptune**4)) * (1 + (alpha / r_neptune**2)))
        az_neptune  = (-((GMs * z_neptune) / (r_neptune**3)) + ((GMs * 0.001 * (z_neptune - z_jupiter) / rrel_neptune**3)) * (1 + (alpha / r_neptune**2)))
        x_neptune   = x_neptune+ vx_neptune * h + ((1 / 2) * ax_neptune * (h**2))
        y_neptune   = y_neptune+ vy_neptune * h + ((1 / 2) * ay_neptune * (h**2))
        z_neptune   = z_neptune+ vz_neptune * h + ((1 / 2) * az_neptune * (h**2))
        r_neptune   = math.sqrt(x_neptune**2 + y_neptune**2 + z_neptune**2)
        ax1_neptune = (-((GMs * x_neptune * math.sqrt(x_neptune**2 + y_neptune**2)) / (r_neptune**4)) + ((GMs * 0.001 * (x_neptune - x_jupiter) * math.sqrt((x_neptune - x_jupiter)**2 + (y_neptune - y_jupiter)**2) / rrel_neptune**4)) * (1 + (alpha / r_neptune**2)))
        ay1_neptune = (-((GMs * y_neptune * math.sqrt(x_neptune**2 + y_neptune**2)) / (r_neptune**4)) + ((GMs * 0.001 * (y_neptune - y_jupiter) * math.sqrt((x_neptune - x_jupiter)**2 + (y_neptune - y_jupiter)**2) / rrel_neptune**4)) * (1 + (alpha / r_neptune**2)))
        az1_neptune = (-((GMs * z_neptune) / (r_neptune**3)) + ((GMs * 0.001 * (z_neptune - z_jupiter) / rrel_neptune**3)) * (1 + (alpha / r_neptune**2)))
        vx_neptune  = vx_neptune + ((h / 2) * (ax1_neptune + ax_neptune))
        vy_neptune  = vy_neptune + ((h / 2) * (ay1_neptune + ay_neptune))
        vz_neptune  = vz_neptune + ((h / 2) * (az1_neptune + az_neptune))
        v_neptune   = math.sqrt(vx_neptune**2 + vy_neptune**2 + vz_neptune**2)


        ax_pluto  = (-((GMs * x_pluto * math.sqrt(x_pluto**2 + y_pluto**2)) / (r_pluto**4)) + ((GMs * 0.001 * (x_pluto - x_jupiter) * math.sqrt((x_pluto - x_jupiter)**2 + (y_pluto - y_jupiter)**2) / rrel_pluto**4)) * (1 + (alpha / r_pluto**2)))
        ay_pluto  = (-((GMs * y_pluto * math.sqrt(x_pluto**2 + y_pluto**2)) / (r_pluto**4)) + ((GMs * 0.001 * (y_pluto - y_jupiter) * math.sqrt((x_pluto - x_jupiter)**2 + (y_pluto - y_jupiter)**2) / rrel_pluto**4)) * (1 + (alpha / r_pluto**2)))
        az_pluto  = (-((GMs * z_pluto) / (r_pluto**3)) + ((GMs * 0.001 * (z_pluto - z_jupiter) / rrel_pluto**3)) * (1 + (alpha / r_pluto**2)))
        x_pluto   = x_pluto+ vx_pluto * h + ((1 / 2) * ax_pluto * (h**2))
        y_pluto   = y_pluto+ vy_pluto * h + ((1 / 2) * ay_pluto * (h**2))
        z_pluto   = z_pluto+ vz_pluto * h + ((1 / 2) * az_pluto * (h**2))
        r_pluto   = math.sqrt(x_pluto**2 + y_pluto**2 + z_pluto**2)
        ax1_pluto = (-((GMs * x_pluto * math.sqrt(x_pluto**2 + y_pluto**2)) / (r_pluto**4)) + ((GMs * 0.001 * (x_pluto - x_jupiter) * math.sqrt((x_pluto - x_jupiter)**2 + (y_pluto - y_jupiter)**2) / rrel_pluto**4)) * (1 + (alpha / r_pluto**2)))
        ay1_pluto = (-((GMs * y_pluto * math.sqrt(x_pluto**2 + y_pluto**2)) / (r_pluto**4)) + ((GMs * 0.001 * (y_pluto - y_jupiter) * math.sqrt((x_pluto - x_jupiter)**2 + (y_pluto - y_jupiter)**2) / rrel_pluto**4)) * (1 + (alpha / r_pluto**2)))
        az1_pluto = (-((GMs * z_pluto) / (r_pluto**3)) + ((GMs * 0.001 * (z_pluto - z_jupiter) / rrel_pluto**3)) * (1 + (alpha / r_pluto**2)))
        vx_pluto  = vx_pluto + ((h / 2) * (ax1_pluto + ax_pluto))
        vy_pluto  = vy_pluto + ((h / 2) * (ay1_pluto + ay_pluto))
        vz_pluto  = vz_pluto + ((h / 2) * (az1_pluto + az_pluto))
        v_pluto   = math.sqrt(vx_pluto**2 + vy_pluto**2 + vz_pluto**2)


##Storing new positions
        xarr_sun = np.append(xarr_sun, x_sun)
        yarr_sun = np.append(yarr_sun, y_sun)
        zarr_sun = np.append(zarr_sun, z_sun)

        xarr_mercury = np.append(xarr_mercury, x_mercury)
        yarr_mercury = np.append(yarr_mercury, y_mercury)
        zarr_mercury = np.append(zarr_mercury, z_mercury)

        xarr_venus = np.append(xarr_venus, x_venus)
        yarr_venus = np.append(yarr_venus, y_venus)
        zarr_venus = np.append(zarr_venus, z_venus)

        xarr_earth = np.append(xarr_earth, x_earth)
        yarr_earth = np.append(yarr_earth, y_earth)
        zarr_earth = np.append(zarr_earth, z_earth)

        xarr_mars = np.append(xarr_mars, x_mars)
        yarr_mars = np.append(yarr_mars, y_mars)
        zarr_mars = np.append(zarr_mars, z_mars)

        xarr_jupiter = np.append(xarr_jupiter, x_jupiter)
        yarr_jupiter = np.append(yarr_jupiter, y_jupiter)
        zarr_jupiter = np.append(zarr_jupiter, z_jupiter)

        xarr_saturn = np.append(xarr_saturn, x_saturn)
        yarr_saturn = np.append(yarr_saturn, y_saturn)
        zarr_saturn = np.append(zarr_saturn, z_saturn)

        xarr_uranus = np.append(xarr_uranus, x_uranus)
        yarr_uranus = np.append(yarr_uranus, y_uranus)
        zarr_uranus = np.append(zarr_uranus, z_uranus)

        xarr_neptune = np.append(xarr_neptune, x_neptune)
        yarr_neptune = np.append(yarr_neptune, y_neptune)
        zarr_neptune = np.append(zarr_neptune, z_neptune)

        xarr_pluto = np.append(xarr_pluto, x_pluto)
        yarr_pluto = np.append(yarr_pluto, y_pluto)
        zarr_pluto = np.append(zarr_pluto, z_pluto)

##Updating count
        count += 1

##Increasing time
        t = t+h


##3D plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

##Removing axes display
    ax.set_axis_off()

##Creating lists for frame updates
    #Sun
    xdata, ydata, zdata  = [], [], []
    xdata2, ydata2, zdata2 = [], [], []
    # #Mercury
    xdata3, ydata3, zdata3 = [], [], []
    xdata4, ydata4, zdata4 = [], [], []
    # #Venus
    xdata5, ydata5, zdata5 = [], [], []
    xdata6, ydata6, zdata6 = [], [], []
    # #Earth
    xdata7, ydata7, zdata7 = [], [], []
    xdata8, ydata8, zdata8 = [], [], []
    # #Mars
    xdata9, ydata9, zdata9 = [], [], []
    xdata10, ydata10, zdata10 = [], [], []
    # #Jupiter
    xdata11, ydata11, zdata11 = [], [], []
    xdata12, ydata12, zdata12 = [], [], []
    # #Saturn
    xdata13, ydata13, zdata13 = [], [], []
    xdata14, ydata14, zdata14 = [], [], []
    # #Uranus
    xdata15, ydata15, zdata15 = [], [], []
    xdata16, ydata16, zdata16 = [], [], []
    # #Neptune
    xdata17, ydata17, zdata17 = [], [], []
    xdata18, ydata18, zdata18 = [], [], []
    # #Pluto
    xdata19, ydata19, zdata19 = [], [], []
    xdata20, ydata20, zdata20 = [], [], []
    #

##Creating line objects
    #Mercury
    ln3, = plt.plot([], [],  marker='o', markerfacecolor='#A9A9A9', markersize=3.78, markeredgewidth=0, animated=True, label='Mercury')
    ln4, = plt.plot([], [],  marker='.', markerfacecolor='#C0C0C0', markersize=0.0, animated=True)
    #Venus
    ln5, = plt.plot([], [], marker='o', markerfacecolor='xkcd:reddish brown', markersize=4.17, markeredgewidth=0, animated=True, label='Venus')
    ln6, = plt.plot([], [], marker='.', markerfacecolor='xkcd:reddish brown', markersize=0.0, animated=True)
    #Earth
    ln7, = plt.plot([], [], marker='o', markerfacecolor='xkcd:cloudy blue', markersize=4.19, markeredgewidth=0, animated=True, label='Earth')
    ln8, = plt.plot([], [], marker='.', markerfacecolor='xkcd:dark blue', markersize=0.0, animated=True)
    #Mars
    ln9, = plt.plot([], [], marker='o', markerfacecolor='xkcd:brownish red', markersize=3.92, markeredgewidth=0, animated=True, label='Mars')
    ln10, = plt.plot([], [], marker='.', markerfacecolor='xkcd:brownish red', markersize=0.0, animated=True)
    #Jupiter
    ln11, = plt.plot([], [], marker='o', markerfacecolor='xkcd:brownish orange', markersize=5.23, markeredgewidth=0, animated=True, label='Jupiter')
    ln12, = plt.plot([], [], marker='.', markerfacecolor='xkcd:brownish orange', markersize=0.0, animated=True)
    #Saturn
    ln13, = plt.plot([], [], marker='o', markerfacecolor='xkcd:brownish yellow', markersize=5.16, markeredgewidth=0, animated=True, label='Saturn')
    ln14, = plt.plot([], [], marker='.', markerfacecolor='xkcd:brownish yellow', markersize=0.0, animated=True)
    #Uranus
    ln15, = plt.plot([], [], marker='o', markerfacecolor='xkcd:really light blue', markersize=4.8, markeredgewidth=0, animated=True, label='Uranus')
    ln16, = plt.plot([], [], marker='.', markerfacecolor='xkcd:really light blue', markersize=0.0, animated=True)
    #Neptune
    ln17, = plt.plot([], [], marker='o', markerfacecolor='xkcd:blue with a hint of purple', markersize=4.78, markeredgewidth=0, animated=True, label='Neptune')
    ln18, = plt.plot([], [], marker='.', markerfacecolor='xkcd:blue with a hint of purple', markersize=0.0, animated=True)
    #Pluto
    ln19, = plt.plot([], [],  marker='o', markerfacecolor='xkcd:dust', markersize=3.46, markeredgewidth=0, animated=True, label='Pluto')
    ln20, = plt.plot([], [],  marker='.', markerfacecolor='xkcd:dust', markersize=0.0, animated=True)
    #Sun
    ln1, = plt.plot([], [],  marker='o', markerfacecolor='xkcd:yellow', markersize=15, markeredgewidth=0, animated=True, label='Sun')
    ln2, = plt.plot([], [],  markerfacecolor='xkcd:yellow', animated=True)

    def init():
##Setting intial field of view
        ax.set_xlim(-1.55, 1.55)
        ax.set_ylim(-1.55, 1.55)
        ax.set_zlim(-1.55, 1.55)
        return ln1, ln2, ln3, ln4, ln5, ln6, ln7, ln8, ln9, ln10, ln11, ln12, ln13, ln14, ln15, ln16, ln17, ln18, ln19, ln20,

    def update(frame):
##Updating frames
        xdata2.append(xarr_sun[frame])
        ydata2.append(yarr_sun[frame])
        zdata2.append(zarr_sun[frame])
        xdata = xarr_sun[frame]
        ydata = yarr_sun[frame]
        zdata = zarr_sun[frame]
        #
        xdata4.append(xarr_mercury[frame])
        ydata4.append(yarr_mercury[frame])
        zdata4.append(zarr_mercury[frame])
        xdata3 = xarr_mercury[frame]
        ydata3 = yarr_mercury[frame]
        zdata3 = zarr_mercury[frame]
        #
        xdata6.append(xarr_venus[frame])
        ydata6.append(yarr_venus[frame])
        zdata6.append(zarr_venus[frame])
        xdata5 = xarr_venus[frame]
        ydata5 = yarr_venus[frame]
        zdata5 = zarr_venus[frame]
        #
        xdata8.append(xarr_earth[frame])
        ydata8.append(yarr_earth[frame])
        zdata8.append(zarr_earth[frame])
        xdata7 = xarr_earth[frame]
        ydata7 = yarr_earth[frame]
        zdata7 = zarr_earth[frame]
        #
        xdata10.append(xarr_mars[frame])
        ydata10.append(yarr_mars[frame])
        zdata10.append(zarr_mars[frame])
        xdata9 = xarr_mars[frame]
        ydata9 = yarr_mars[frame]
        zdata9 = zarr_mars[frame]

        xdata12.append(xarr_jupiter[frame])
        ydata12.append(yarr_jupiter[frame])
        zdata12.append(zarr_jupiter[frame])
        xdata11 = xarr_jupiter[frame]
        ydata11 = yarr_jupiter[frame]
        zdata11 = zarr_jupiter[frame]

        xdata14.append(xarr_saturn[frame])
        ydata14.append(yarr_saturn[frame])
        zdata14.append(zarr_saturn[frame])
        xdata13 = xarr_saturn[frame]
        ydata13 = yarr_saturn[frame]
        zdata13 = zarr_saturn[frame]

        xdata16.append(xarr_uranus[frame])
        ydata16.append(yarr_uranus[frame])
        zdata16.append(zarr_uranus[frame])
        xdata15 = xarr_uranus[frame]
        ydata15 = yarr_uranus[frame]
        zdata15 = zarr_uranus[frame]

        xdata18.append(xarr_neptune[frame])
        ydata18.append(yarr_neptune[frame])
        zdata18.append(zarr_neptune[frame])
        xdata17 = xarr_neptune[frame]
        ydata17 = yarr_neptune[frame]
        zdata17 = zarr_neptune[frame]

        xdata20.append(xarr_pluto[frame])
        ydata20.append(yarr_pluto[frame])
        zdata20.append(zarr_pluto[frame])
        xdata19 = xarr_pluto[frame]
        ydata19 = yarr_pluto[frame]
        zdata19 = zarr_pluto[frame]
        #
##Giving 2D properties to line objects
        ln1.set_data(xdata, ydata)
        ln2.set_data(xdata2, ydata2)
        ln3.set_data(xdata3, ydata3)
        ln4.set_data(xdata4, ydata4)
        ln5.set_data(xdata5, ydata5)
        ln6.set_data(xdata6, ydata6)
        ln7.set_data(xdata7, ydata7)
        ln8.set_data(xdata8, ydata8)
        ln9.set_data(xdata9, ydata9)
        ln10.set_data(xdata10, ydata10)
        ln11.set_data(xdata11, ydata11)
        ln12.set_data(xdata12, ydata12)
        ln13.set_data(xdata13, ydata13)
        ln14.set_data(xdata14, ydata14)
        ln15.set_data(xdata15, ydata15)
        ln16.set_data(xdata16, ydata16)
        ln17.set_data(xdata17, ydata17)
        ln18.set_data(xdata18, ydata18)
        ln19.set_data(xdata19, ydata19)
        ln20.set_data(xdata20, ydata20)

##Giving 3D properties to line objects
        ln1.set_3d_properties(zdata)
        ln2.set_3d_properties(zdata2)
        ln3.set_3d_properties(zdata3)
        ln4.set_3d_properties(zdata4)
        ln5.set_3d_properties(zdata5)
        ln6.set_3d_properties(zdata6)
        ln7.set_3d_properties(zdata7)
        ln8.set_3d_properties(zdata8)
        ln9.set_3d_properties(zdata9)
        ln10.set_3d_properties(zdata10)
        ln11.set_3d_properties(zdata11)
        ln12.set_3d_properties(zdata12)
        ln13.set_3d_properties(zdata13)
        ln14.set_3d_properties(zdata14)
        ln15.set_3d_properties(zdata15)
        ln16.set_3d_properties(zdata16)
        ln17.set_3d_properties(zdata17)
        ln18.set_3d_properties(zdata18)
        ln19.set_3d_properties(zdata19)
        ln20.set_3d_properties(zdata20)

        return ln1, ln2, ln3, ln4, ln5, ln6, ln7, ln8, ln9, ln10, ln11, ln12, ln13, ln14, ln15, ln16, ln17, ln18, ln19, ln20,

##For making the legend
    plt.legend(loc=3, ncol=10, bbox_to_anchor=(-0.12,1.0,1.20,1.1), mode="expand", handletextpad=0.1, fontsize='small', handles=[ln1, ln2, ln3, ln4, ln5, ln6, ln7, ln8, ln9, ln10, ln11, ln12, ln13, ln14, ln15, ln16, ln17, ln18, ln19, ln20])
##For the black background
    ax.set_facecolor('xkcd:black')
    fig.patch.set_facecolor('xkcd:black')
##Main animation call
    ani = FuncAnimation(fig, update, frames=int(xarr_earth.size), interval=0.00000000000000000000000000001, init_func=init, blit=True)
##Background Picture
    #img = imread("stars.jpeg")
    #plt.imshow(img)
    plt.show()

##Tkinter stuff
btn = Button(window, text="Hit Me", command=clicked, bg = 'lightblue')
btn.grid(row=2, column=1, pady=10)
#p = Progressbar(btn, orient=HORIZONTAL, length=200, mode='determinate')
#p.grid(row=2, column=2, pady=10)


window.mainloop()
