# Author: Sun Hao
# Contact: sunhaonuaa@outlook.com
# Copyright (c) 2022 Sun Hao, All rights reserved.

import numpy as np
from geomdl import BSpline, operations
from geomdl import utilities
from geomdl import exchange
from geomdl.visualization import VisMPL
from matplotlib import pyplot as plt

# Create a curve instance
curve = BSpline.Curve()

# Set degree
curve.degree = 4

# Set control points
curve.ctrlpts = [
    [1.000000, 0.000400]
    , [0.980000, 0.001800]
    , [0.950000, 0.005400]
    , [0.890000, 0.015000]
    , [0.850000, 0.022600]
    , [0.810000, 0.030900]
    , [0.770000, 0.039400]
    , [0.730000, 0.047300]
    , [0.680000, 0.056700]
    , [0.630000, 0.065900]
    , [0.580000, 0.074300]
    , [0.530000, 0.081400]
    , [0.480000, 0.087600]
    , [0.430000, 0.092000]
    , [0.350000, 0.094000]
    , [0.310000, 0.093000]
    , [0.270000, 0.090300]
    , [0.210000, 0.084000]
    , [0.160000, 0.076000]
    , [0.120000, 0.066400]
    , [0.085000, 0.056300]
    , [0.060000, 0.047200]
    , [0.040000, 0.038600]
    , [0.022500, 0.029100]
    , [0.011000, 0.020900]
    , [0.007000, 0.017200]
    , [0.003500, 0.013400]
    , [0.000000, 0.000000]
    , [0.003500, -0.004600]
    , [0.007000, -0.006800]
    , [0.011000, -0.008630]
    , [0.022500, -0.011350]
    , [0.040000, -0.013400]
    , [0.060000, -0.015200]
    , [0.085000, -0.016700]
    , [0.120000, -0.018100]
    , [0.160000, -0.019600]
    , [0.210000, -0.022000]
    , [0.270000, -0.024400]
    , [0.310000, -0.025800]
    , [0.350000, -0.026000]
    , [0.430000, -0.026200]
    , [0.480000, -0.026000]
    , [0.530000, -0.024400]
    , [0.580000, -0.022000]
    , [0.630000, -0.019000]
    , [0.680000, -0.015800]
    , [0.730000, -0.012600]
    , [0.770000, -0.009800]
    , [0.810000, -0.007200]
    , [0.850000, -0.005000]
    , [0.890000, -0.002900]
    , [0.950000, -0.000450]
    , [0.980000, -0.000400]
    , [1.000000, -0.000400]
]

# Set knot vector
curve.knotvector = np.linspace(0, 1, 60)

# Set visualization component
curve.vis = VisMPL.VisCurve2D()

# Refine knot vector
operations.refine_knotvector(curve, [3])

# Visualize
curve.render()

evalpts = np.array(curve.evalpts)

plt.plot(evalpts[:, 0], evalpts[:, 1])
# plt.scatter(pts[:, 0], pts[:, 1], color="red")
plt.show()

x = evalpts[:, 0]
y = evalpts[:, 1]
file = open("vr5.dat", 'w+')
file.write("BOEING-VERTOL VR-5 AIRFOIL" + '\n')
for i in range(len(x)):
    file.write(str(x[i]) + '\t')
    file.write(str(y[i]) + '\n')
file.close()
