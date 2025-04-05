# ElectroStatics-Sim
An FDM electrostatics simulator I made for Mr.K's APCS final project (2024). Made in Processing.
<br>
### [Github Repo](https://github.com/ringedSquid/Electrostatics-Sim-APCS-final)
<br>
## Quick overview:
This program simulates electrostatics by solving the Poisson equation for electrostatics ($\nabla^2 V = -\frac{\rho}{\epsilon}$). 
Via a desription language, the initial conditions for the simulation can be set. Currently the simulation supports simple 3D geometries, charged materials, and conductive materials.

<br>The operations involved are computationally expensive, and the size of the space is practically limited at 30x30x30 units. (This takes about a minute to be solved)

<br>Due to limitations in the original project guidelines, the 3D space is not rendered. Rather, a single 2D slice of the space can be rendered at a time. 
<br>
## Theory
The laplacian of potential is equal to the negative charge density divided by the permittivity of space:
\begin{align}
\nabla \cdot V &= -\vec{E} \\\
\nabla \cdot (\nabla \cdot V) &= -\nabla \cdot \vec{E} = -\frac{\rho}{\epsilon} \\\
\nabla^2 V &= -\frac{\rho}{\epsilon}
\end{align}
This can also be expressed as:
\begin{align}
    \frac{\partial^2{V}}{\partial{x^2}} + \frac{\partial^2{V}}{\partial{y^2}} + \frac{\partial^2{V}}{\partial{z^2}} = -\frac{\rho}{\epsilon}
\end{align}
Now given some space, we can approximate solutions to this equation using the finite difference method. This involves first discretizing our space before then solving a system of linear equations.
<br>
### Setting up our FDM (Finite Difference Method) scheme
#### Discretization
Recall the definition of the derivative of $f(x)$:
\begin{align}
    \frac{df}{dx} = \lim_{h \to 0}\frac{f(x+h) - f(x)}{h}
\end{align}
Now for some small h (call it $\Delta h$):
\begin{align}
    \frac{df}{dx} \approx \frac{f(x+\Delta h)-f(x)}{\Delta h}
\end{align}
We can approximate second derivatives in a similar manner:
\begin{align}
     \frac{d^2 f}{dx^2} \approx \frac{f(x+\Delta h)-2f(x)+f(x-\Delta h)}{(\Delta h)^2}
\end{align}
We can discretize space, essentially breaking it up into a grid of small regions of space, 
to approximate a solution for $\nabla^2 V = -\frac{\rho}{\epsilon}$
\begin{align}
    \nabla^2 V &= \frac{\partial^2{V}}{\partial{x^2}} + \frac{\partial^2{V}}{\partial{y^2}} + \frac{\partial^2{V}}{\partial{z^2}} \\\
    \nabla^2 V &\approx 
    \frac{V\_{i+\Delta h, j, k}-2V\_{i,j,k}+V\_{i-\Delta h, j, k}}{(\Delta h)^2} + 
    \frac{V\_{i, j+\Delta h, k}-2V\_{i,j,k}+V\_{i, j-\Delta h, k}}{(\Delta h)^2} + 
    \frac{V\_{i, j, k+\Delta h}-2V\_{i,j,k}+V\_{i, j, k-\Delta h}}{(\Delta h)^2} \\\
    \nabla^2 V &\approx \frac{V\_{i+\Delta h, j, k}+V\_{i-\Delta h, j, k}+V\_{i, j+\Delta h, k}+V\_{i, j-\Delta h, k}+V\_{i, j, k+\Delta h}+V\_{i, j, k-\Delta h}-6V\_{i,j,k}}{(\Delta h)^2}
\end{align}
#### Boundary conditions
In this simulation, the potential at the boundaries of our space are set to zero. $V_{x, y, z} = 0$ for $(x, y, z) \in \partial\Omega$
<br>
#### Setting up a system of linear equations
Assuming that the charge density of every region within our discretized space is defined, we'll set up a system of linear equations:
\begin{align}
    \frac{1}{(\Delta h)^2}V\_{1, 0, 0} + \frac{1}{(\Delta h)^2}V\_{0, 1, 0} + \frac{1}{(\Delta h)^2}V\_{0, 0, 1} + -\frac{6}{(\Delta h)^2}V\_{0, 0, 0} &= -\frac{\rho\_{0, 0, 0}}{\epsilon}\\\
    \frac{1}{(\Delta h)^2}V\_{2, 0, 0} +  \frac{1}{(\Delta h)^2}V\_{0, 0, 0} + \frac{1}{(\Delta h)^2}V\_{0, 1, 0} + \frac{1}{(\Delta h)^2}V\_{0, 0, 1} + -\frac{6}{(\Delta h)^2}V\_{1, 0, 0} &= -\frac{\rho\_{1, 0, 0}}{\epsilon}\\\
    &\vdots \\\
    \frac{1}{(\Delta h)^2}V\_{\hat{X}-1, \hat{Y}, \hat{Z}} + \frac{1}{(\Delta h)^2}V\_{\hat{X}, \hat{Y}-1, \hat{Z}} + \frac{1}{(\Delta h)^2}V\_{\hat{X}, \hat{Y}, \hat{Z}-1} + -\frac{6}{(\Delta h)^2}V\_{\hat{X}, \hat{Y}, \hat{Z}} &= -\frac{\rho\_{\hat{X}, \hat{Y}, \hat{Z}}}{\epsilon}
\end{align}

Before we represent our system of equations as a matrix equation, we have to first index each point in our discretized space of dimensions $\hat{X} \times \hat{Y} \times \hat{Z}$. The index $i$ of the region associated with coordinates $(x, y, z)$ is defined as:
\begin{align}
    i = x + \hat{Y}y + (\hat{X}\hat{Y})z
\end{align}

Our system as a matrix equation in the form $\mathrm{M}\vec{x} = \vec{b}$:
\begin{align}
    \underbrace{
    \begin{bmatrix}
    -\frac{6}{(\Delta h)^2} & \frac{1}{(\Delta h)^2} & 0 & \dots \\\
    \frac{1}{(\Delta h)^2} & -\frac{6}{(\Delta h)^2} & \frac{1}{(\Delta h)^2} & \dots \\\
    0 & \frac{1}{(\Delta h)^2} & -\frac{6}{(\Delta h)^2} & \dots \\\
    0 & 0 & \frac{1}{(\Delta h)^2} & \ddots \\\
    \vdots & \vdots & \vdots & \vdots \\\
    0 & 0 & 0 & \dots \\\
    \end{bmatrix}
    }\_{\mathrm{M}}
    \underbrace{
    \begin{bmatrix}
    V\_{0, 0, 0} \\\
    V\_{1, 0, 0} \\\
    V\_{2, 0, 0} \\\
    \vdots \\\
    V\_{\hat{X}, \hat{Y}, \hat{Z}}
    \end{bmatrix}
    }\_{\vec{x}}
    &=
    \underbrace{
    \begin{bmatrix}
    -\frac{\rho\_{0, 0, 0}}{\epsilon} \\\
    -\frac{\rho\_{1, 0, 0}}{\epsilon} \\\
    -\frac{\rho\_{2, 0, 0}}{\epsilon} \\\
    \vdots \\\
    -\frac{\rho{\_{\hat{X}, \hat{Y}, \hat{Z}}}}{\epsilon}
    \end{bmatrix}
    }\_{\vec{b}} \\\
    \mathrm{M}\vec{x} &= \vec{b}
\end{align}
If the potential at some region is known but the charge density is not, a simple re-arrangement of terms lets us solve for it.
\begin{align}
    \frac{V\_{i+\Delta h, j, k}+V\_{i-\Delta h, j, k}+V\_{i, j+\Delta h, k}+V\_{i, j-\Delta h, k}+V\_{i, j, k+\Delta h}+V\_{i, j, k-\Delta h}-6V\_{i,j,k}}{(\Delta h)^2} &= -\frac{\rho\_{i, j, k}}{\epsilon} \\\
    V\_{i+\Delta h, j, k}+V\_{i-\Delta h, j, k}+V\_{i, j+\Delta h, k}+V\_{i, j-\Delta h, k}+V\_{i, j, k+\Delta h}+V\_{i, j, k-\Delta h}-6V\_{i,j,k} &= -\frac{\rho\_{i, j, k}(\Delta h)^2}{\epsilon} \\\
    V\_{i+\Delta h, j, k}+V\_{i-\Delta h, j, k}+V\_{i, j+\Delta h, k}+V\_{i, j-\Delta h, k}+V\_{i, j, k+\Delta h}+V\_{i, j, k-\Delta h}+\frac{\rho\_{i, j, k}(\Delta h)^2}{\epsilon} &= 6V\_{i,j,k}\\\
    \frac{V\_{i+\Delta h, j, k}+V\_{i-\Delta h, j, k}+V\_{i, j+\Delta h, k}+V\_{i, j-\Delta h, k}+V\_{i, j, k+\Delta h}+V\_{i, j, k-\Delta h}}{6} +  \frac{\rho\_{i, j, k}(\Delta h)^2}{6\epsilon} &= V\_{i,j,k}
\end{align}
Once the charge density at that region is solved for, the values can be swapped from their respective places in vectors $\vec{x}$ and $\vec{b}$.
<br>
### Implementation Notes
The implementation of this FDM scheme is fairly straightforward. But I want to note that I used sparse matricies to reduce the memory complexity of this program. This simulation is computationaly expensive, with the rendered examples taking around a minute to be solved.
<br>
## Simulation Description Language
This program interprets a custom description language that describes a scenario for the simulation to run. The syntax is very simple. 
<br>
#### Every program must start with this line:

```
BEGIN X Y Z GRIDSIZE PIXELS_PER_GRID SHOW_KEY 
```

- X, Y, Z (int) describe the size of the grid in cells. 
- GRIDSIZE (float) describes the sidelength of each cell in the grid in real life units.
- PIXELS\_PER\_GRID (int) describes how many pixels on each side are used to render one cell.
- SHOW\_KEY (boolean) toggles if the key (scale) for the simulation will show.

<br>
#### Now that you have set up your grid, its time to add materials:
```
MAT MAT_NAME R G B PERM TYPE VAL
```
- MAT\_NAME (String, single word) is the name of the material.
- R, G, B (int) describe the color of the material. 
- PERM (float) is the permittivity of the material. 
- TYPE (char) is the type of material. 'c' is for conductors, 'd' is for charged objects. 
- VAL (float) can describe either: the potential of a conductor (TYPE = 'c') or the charge of an object (TYPE = 'd'). 

<br>
#### Lets now add a geometry:
```
BOX MAT pX pY pZ sX sY sZ
HBOX MAT pX pY pZ sX sY sZ T
DISC MAT pX pY pZ ORIENT R
WASHER MAT pX pY pZ ORIENT R1 R2
SPHERE MAT pX pY pZ R
HSPHERE MAT pX pY pZ R1 R2
ELLIPSOID MAT pX pY pZ A B C R
HELLIPSOID MAT pX pY pZ A B C R1 R2
POINT MAT pX pY pZ
```
- MAT (String) is the name of a predefined material. 
- pX, pY, pZ (float) is the center positon of the geometry.
- sX, sY, sZ (float) is the size of a geometry. 
- ORIENT (char) is the orientation of a disc/washer. 'x' - faces the x direction, 'y' - faces the y direction, 'z'- faces the z direction. 
- T (float) is the thickness of a hollow box's walls. 
- A, B, C (float) is the coefficients for an ellipse (you have to know what this is first). 
- R (float) is the radius of a sphere/ellipse. 
- R1 (float) is the inner radius of a hollow sphere/ellipse. 
- R2 (float) is the outer radius of a hollow sphere/ellipse.
<br>

Once you add your geometries, you must put SOLVE at the end of the program if you want it to run properly. 
<br>
#### Here is a quick example (NOTE THAT THE ACTUAL SIM DOES NOT SUPPORT COMMENTS): 
```
//Begin grid with size 50x5x50, set the size of each cell to .001m. 10 pixels per cell, show key.
BEGIN 50 5 50 .001 10 true 
//Define materials, both charged substances
MAT posCharge 240 240 0 8.85418782E-12 d 10
MAT negCharge 120 0 120 8.85418782E-12 d -10
//Place two spheres next to each other
SPHERE posCharge -7 0 0 4
SPHERE negCharge  7 0 0 4
SOLVE
```

