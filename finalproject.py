from tkinter import *
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

window = Tk()

window.title("Solar System 3D Simulaor")

window.geometry('700x400')

lbl = Label(window, text="Click here to start simulation -> ")

lbl.grid(column=50, row=0)

lbl = Label(window, text="3D Solar System Simulator by Shitij Seth")

lbl.grid(column=550, row=250)

def clicked():

    GMs = 4*(math.pi**2)
    m_sun = 1.989e30

    ecc_earth = 0.0167
    semimajor_earth = 1.00000011
    a_earth = semimajor_earth
    perihelion_earth = a_earth*(1-ecc_earth)
    m_earth = 9.72e24

    ecc_jup = 0.0489
    semimajor_jup = 5.2044
    a_jup = semimajor_jup
    perihelion_jup = a_jup*(1-ecc_jup)
    m_jup = 1.8982e27



    vp_earth = math.sqrt(GMs) * math.sqrt((1+ecc_earth) / (a_earth*(1-ecc_earth)) * (1+(m_earth/m_sun)))
    vx = 0
    vy = vp_earth
    x = -perihelion_earth
    y = 0

    vp_jup = math.sqrt(GMs) * math.sqrt((1+ecc_jup) / (a_jup*(1-ecc_jup)) * (1+(m_jup/m_sun)))
    vx2 = 0
    vy2 = vp_jup
    x2 = -perihelion_jup
    y2 = 0

    x3 = 0.000001
    y3 = 0.000001

    # years
    h = 1e-3
    t_final = 50
    t_initial = 0
    t = t_initial
    count = 0

    xarr = np.array([])
    yarr = np.array([])
    xarr = np.append(xarr,x)
    yarr = np.append(yarr,y)
    r = math.sqrt(x**2 + y**2)
    v = math.sqrt(vx**2 + vy**2)

    xarr2 = np.array([])
    yarr2 = np.array([])
    xarr2 = np.append(xarr2,x2)
    yarr2 = np.append(yarr2,y2)
    r2 = math.sqrt(x2**2 + y2**2)
    v2 = math.sqrt(vx2**2 + vy2**2)

    xarr3 = np.array([])
    yarr3 = np.array([])

    while (t < t_final):

          r = math.sqrt(x**2 + y**2)
          r2 = math.sqrt(x2**2 + y2**2)
          rrel = math.sqrt( (x-x2)**2 + (y-y2)**2)

          # complete the next four lines of code
          # vx, vy is jupiter
          # vx2, vy2 is earth
          vx = vx - ((GMs * x) / (r**3) + (GMs * 0.001 * (x - x2) / rrel**3)) * h
          vy = vy -  ((GMs * y) / (r**3) + (GMs * 0.001 * (y - y2) / rrel**3)) * h
          vx2 = vx2 - ((GMs * x2) / (r2**3) + (GMs * (m_earth / m_sun) * (x2 - x) / (rrel**3))) * h
          vy2 = vy2 - ((GMs * y2) / (r2**3) + (GMs * (m_earth / m_sun) * (y2 - y) / (rrel**3))) * h

          x = x + vx*h
          y = y + vy*h
          x2 = x2 + vx2*h
          y2 = y2 + vy2*h
          x3 = x3 + 0
          y3 = y3 + 0

          #if (count%200 == 0 ):
          xarr = np.append(xarr,x)
          yarr = np.append(yarr,y)
          xarr2 = np.append(xarr2,x2)
          yarr2 = np.append(yarr2,y2)
          xarr3 = np.append(xarr3,x3)
          yarr3 = np.append(yarr3,y3)
          count += 1

          t = t+h

    print (xarr.size)

    fig, ax = plt.subplots()
    xdata, ydata = [], []
    xdata2, ydata2 = [], []
    xdata3, ydata3 = [], []
    xdata4, ydata4 = [], []
    xdata5, ydata5 = [], []
    xdata6, ydata6 = [], []

    ln1, = plt.plot([], [], 'ro', animated=True)
    ln2, = plt.plot([], [], 'b', animated=True)
    ln3, = plt.plot([], [], 'ro', animated=True)
    ln4, = plt.plot([], [], 'g', animated=True)
    ln5, = plt.plot([], [], 'yo',markersize=20, animated=True)
    ln6, = plt.plot([], [], 'y', animated=True)
    print (type(xdata))

    def init():
        ax.set_xlim(-5.5, 5.5)
        ax.set_ylim(-5.5, 5.5)
        return ln1, ln2, ln3, ln4, ln5, ln6

    def update(frame):
        #print (type(frame))
        xdata2.append(xarr[frame])
        ydata2.append(yarr[frame])
        xdata = xarr[frame]
        ydata = yarr[frame]

        xdata4.append(xarr2[frame])
        ydata4.append(yarr2[frame])
        xdata3 = xarr2[frame]
        ydata3 = yarr2[frame]

        xdata6.append(xarr3[frame])
        ydata6.append(yarr3[frame])
        xdata5 = xarr3[frame]
        ydata5 = yarr3[frame]
        #ydata = yarr(frame)
        #xdata.append(frame)
        #ydata.append(np.sin(frame))
        ln1.set_data(xdata, ydata)
        ln2.set_data(xdata2, ydata2)
        ln3.set_data(xdata3, ydata3)
        ln4.set_data(xdata4, ydata4)
        ln5.set_data(xdata5, ydata5)
        ln6.set_data(xdata6, ydata6)
        return ln1, ln2, ln3, ln4, ln5, ln6

    ani = FuncAnimation(fig, update, frames=xarr.size, interval=0.01, init_func=init, blit=True)
    plt.show()

# #Universal constants
#         G = 6.67e-11
#         GMs = 4*(math.pi**2)
#         alpha = 0.00
#         m_sun =  1.989e30 #kg
#
# #Values fo Mercury
#         ecc_mercury = 0.205630
#         semimajor_mercury = 0.387098 #AU
#         a = semimajor_mercury
#         perihelion_mercury = a*(1-ecc_mercury)
#         m_mercury = 3.3011e23 #kg
#         vp_mercury = math.sqrt(GMs) * math.sqrt((1+ecc_mercury) / (a*(1-ecc_mercury)) * (1+(m_mercury/m_sun)))
#         vx_mercury = 0
#         vy_mercury = vp_mercury
#         x_mercury = -perihelion_mercury
#         y_mercury = 0
#
# #Values for Earth
#         ecc_earth = 0.0167
#         semimajor_earth = 1.00000011 #AU
#         a_earth = semimajor_earth
#         perihelion_earth = a_earth*(1-ecc_earth)
#         m_earth = 9.72e24 #kg
#         vp_earth = math.sqrt(GMs) * math.sqrt((1+ecc_earth) / (a_earth*(1-ecc_earth)) * (1+(m_earth/m_sun)))
#         vx = 0
#         vy = vp_earth
#         x = -perihelion_earth
#         y = 0
#
# #Values for Jupiter
#         ecc_jup = 0.0489
#         semimajor_jup = 5.2044
#         a_jup = semimajor_jup
#         perihelion_jup = a_jup*(1-ecc_jup)
#         m_jup = 1.8982e27
#         vp_jup = math.sqrt(GMs) * math.sqrt((1+ecc_jup) / (a_jup*(1-ecc_jup)) * (1+(m_jup/m_sun)))
#         vx2 = 0
#         vy2 = vp_jup
#         x2 = -perihelion_jup
#         y2 = 0
#
# #Values for Sun
#         m_sun = 1.989e30 #kg
#         x3 = 0.000001
#         y3 = 0.000001
#
# #Times for the simulation (years)
#         h = 1e-3
#         t_final = 50
#         t_initial = 0
#         t = t_initial
#         count = 0
#
#         xarr_mercury = np.array([])
#         yarr_mercury = np.array([])
#         xarr_mercury = np.append(xarr_mercury,x_mercury)
#         yarr_mercury = np.append(yarr_mercury,y_mercury)
#         r_mercury = math.sqrt(x_mercury**2 + y_mercury**2)
#         v_mercury = math.sqrt(vx_mercury**2 + vy_mercury**2)
#
#         while (t < t_final):
#
#             ax_mercury= (-(GMs * x_mercury) / (r_mercury**3)) * (1 + (alpha / r_mercury**2))
#             ay_mercury = (-(GMs * y_mercury) / (r_mercury**3)) * (1 + (alpha / r_mercury**2))
#             x_mercury= x_mercury+ vx_mercury* h + ((1 / 2) * ax_mercury* (h**2))
#             y_mercury= y_mercury+ vy_mercury* h + ((1 / 2) * ay_mercury* (h**2))
#             r_mercury = math.sqrt(x_mercury**2 + y_mercury**2)
#             ax_mercury_1 = (-(GMs * x_mercury) / (r_mercury**3)) * (1 + (alpha / r_mercury**2))
#             ay_mercury_1 = (-(GMs * y_mercury) / (r_mercury**3)) * (1 + (alpha / r_mercury**2))
#             vx_mercury= vx_mercury+ (h / 2) *  (ax_mercury_1 + ax_mercury)
#             vy_mercury= vy_mercury+ (h / 2) * (ay_mercury_1 + ay_mercury)
#             r_mercury = math.sqrt(x_mercury**2 + y_mercury**2)
#             v_mercury = math.sqrt(vx_mercury**2 + vy_mercury**2)
#             xarr_mercury = np.append(xarr_mercury,x_mercury)
#             yarr_mercury = np.append(yarr_mercury,y_mercury)
#             count += 1
#
#             t = t+h
#
#         print (xarr_mercury.size)
#     #stuff put in for animation
#         fig, ax = plt.subplots()
#         xdata, ydata = [], []
#         x2data, y2data = [], []
#         ln1, = plt.plot([], [], 'ro', animated=True)
#         ln2, = plt.plot([], [], 'b', animated=True)
#         print (type(xdata))
#
#         def init():
#             ax.set_xlim(-0.5, 0.5)
#             ax.set_ylim(-0.5, 0.5)
#             return ln1,ln2
#
#          def update(frame):
#             x2data.append(xarr_mercury[frame])
#             y2data.append(yarr_mercury[frame])
#             xdata = xarr_mercury[frame]
#             ydata = yarr_mercury[frame]
#
#             ln1.set_data(xdata, ydata)
#             ln2.set_data(x2data, y2data)
#             return ln1, ln2
#     #main line for animation
#     #interval size so small to speed up the animation process
#         ani = FuncAnimation(fig, update, frames=xarr_mercury.size, interval=0.0000000000000000000000000000000000000000000000000000000000001, init_func=init, blit=True)
#
#         plt.show()

    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Hit Me", command=clicked)

btn.grid(column=100, row=0)

window.mainloop()
