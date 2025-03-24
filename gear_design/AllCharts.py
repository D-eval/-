
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def bidirectional_interpolation(data):
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    x_to_y = interp1d(x, y, kind='linear', fill_value='extrapolate')
    y_to_x = interp1d(y, x, kind='linear', fill_value='extrapolate')
    return x_to_y, y_to_x


class Interpolation:
    def __init__(self, data):
        self.x_to_y, self.y_to_x = bidirectional_interpolation(data)
    def x2y(self, x):
        return self.x_to_y(x)
    def y2x(self, y):
        return self.y_to_x(y)


def interpolation(x1,y1,x2,y2,x):
    k = (y2-y1)/(x2-x1)
    dx = x - x1
    y = k*dx + y1
    return y


class MultiInterpolation:
    def __init__(self, z1, f1, z2, f2):
        self.z1 = z1
        self.f1 = f1
        self.z2 = z2
        self.f2 = f2
    def x2y(self, x, z):
        y1 = self.f1.x2y(x)
        y2 = self.f2.x2y(x)
        return interpolation(self.z1,y1,self.z2,y2,z)
    def y2x(self, y, z):
        x1 = self.f1.y2x(y)
        x2 = self.f2.y2x(y)
        return interpolation(self.z1,x1,self.z2,x2,z)


f_fig_10_8 = Interpolation([(0, 1), (5, 1.13), (20, 1.25), (40, 1.35)])
f_cha_10_4 = Interpolation([(40,1.201), (80,1.210), (120,1.219), (160,1.229), (200,1.238)])

f_cha_10_5 = {
    17:(2.97,1.52),
    18:(2.91,1.53),
    19:(2.85,1.54),
    20:(2.80,1.55),
    21:(2.76,1.56),
    22:(2.72,1.57),
    23:(2.69,1.575),
    24:(2.65,1.58),
    25:(2.62,1.59),
    26:(2.60,1.595),
    27:(2.57,1.60),
    28:(2.55,1.61),
    29:(2.53,1.62),
    30:(2.52,1.625),
    35:(2.45,1.65),
    40:(2.40,1.68),
    50:(2.32,1.70),
    60:(2.28,1.73),
    70:(2.24,1.75),
    80:(2.22,1.77),
    90:(2.20,1.78),
    100:(2.18,1.79),
    150:(2.14,1.83),
    200:(2.12,1.865),
}

f_cha_10_5_Fa = Interpolation([(i,f_cha_10_5[i][0]) for i in f_cha_10_5.keys()])
f_cha_10_5_Sa = Interpolation([(i,f_cha_10_5[i][1]) for i in f_cha_10_5.keys()])


# 弯曲疲劳寿命系数 K_FN
f_fig_10_18 = Interpolation([(2,1.1),(3,1.1),(np.log10(3e6),1), (10,0.9)])

# 接触疲劳寿命系数 K_HN
f_fig_10_19 = Interpolation([(4,1.6),(5,1.6),(np.log10(5e7),1), (10,0.85)])

sigma_Flim_small = 500 #MPa
sigma_Flim_big = 320 #MPa

sigma_Hlim_small = 600 #MPa
sigma_Hlim_big = 550 #MPa

f_fig_10_13_3 = Interpolation([(1.03,1.046),(1.04,1.065),(1.06,1.095),(1.08,1.14),(1.1,1.15),(1.2,1.3),(1.3,1.5),(1.5,1.9),(2,3),(3.2,6)])
f_fig_10_13_12 = Interpolation([(1.03,1.034),(1.04,1.042),(1.06,1.07),(1.08,1.09),(1.1,1.12),(1.2,1.22),(1.3,1.3),(1.5,1.65),(2,2.2),(3.2,3.2)])

f_fig_10_13 = MultiInterpolation(3,f_fig_10_13_3,12,f_fig_10_13_12)

