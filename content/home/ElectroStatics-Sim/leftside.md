# ElectroStatics-Sim
A fairly limited electrostatics simulator I made for Mr.K's APCS final project (2024). The simulator runs in processing. 
<br>
### [link to simulator](https://github.com/ringedSquid/Electrostatics-Sim-APCS-final)
<br>
## Quick overview:
This program simulates electrostatics by approximating solutions to the Poisson equation for electrostatics ($\nabla^2 = \frac{\rho}{\epsilon}$) in a 3D space.
Via a desription language, the initial conditions for the simulation can be set. Currently the simulation supports simple 3D geometries, charged materials, and conductive materials.

<br>The operations involved are computationally expensive, and the size of the space is practically limited at 30x30x30 units. (This takes about a minute to be solved)

<br>Due to limitations in the original project guidelines, the 3D space is not rendered. Rather, a single 2D slice of the space can be rendered at a time. 
<br>
## The theory behind this simulation
The entire simulation relies on one very important relationship between the electric field and the potential field:
$$\nabla V = -E$$ using the fact that $\nabla E = \frac{\rho}{\epsilon}$ we can show:

$$
\nabla V = -E \\\
\nabla \cdot (\nabla V) = -\nabla E = -\frac{\rho}{\epsilon} \\\
\nabla^2 V = -\frac{\rho}{\epsilon}
$$ which can also be expressed as:

$$
\frac{\partial^2{V}}{\partial{x^2}} + \frac{\partial^2{V}}{\partial{y^2}} + \frac{\partial^2{V}}{\partial{z^2}} = -\frac{\rho}{\epsilon}
$$

we now have this partial differential equation. We can approximate a solution using the Finite Difference Method. We must now discretize our equation.

<br>
### What is discretization?
Discretization in this context means to go from using an infinitesimally small change $dx$ to a discrete small change $\Delta x$. Using the definition of a derivative:
$$
\frac{d}{dx}f(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}
$$
when h is small:
$$
\frac{f(x+h)-f(x)}{h} \approx \frac{d}{dx}f(x)
$$
we can do the same thing for second derivatives:
$$
\frac{f(x+h)-2f(x)+f(x-h)}{h^2} \approx \frac{d^2 f}{dx^2}
$$
lets now discretize our PDE:
$$
\nabla^2 V = \frac{\partial^2{V}}{\partial{x^2}} + \frac{\partial^2{V}}{\partial{y^2}} + \frac{\partial^2{V}}{\partial{z^2}} \\\
\nabla^2 V \approx \frac{V\_{i+h, j, k}-2V\_{i,j,k}+V\_{i-h, j, k}}{h^2} + \frac{V\_{i, j+h, k}-2V\_{i,j,k}+V\_{i, j-h, k}}{h^2} + \frac{V\_{i, j, k+h}-2V\_{i,j,k}+V\_{i, j, k-h}}{h^2} \\\
\nabla^2 V \approx \frac{V\_{i+h, j, k}+V\_{i-h, j, k}+V\_{i, j+h, k}+V\_{i, j-h, k}+V\_{i, j, k+h}+V\_{i, j, k-h}-6V\_{i,j,k}}{h^2}
$$
### Now how do we solve it?
Lets say our space is some nxnxn units in dimension. If we know the charge density of every region of our space (which will be broken up in a discrete grid of cubes) we can solve for the potential of each region and then the electric field. $V_\{i, j, k}$ is our unknown, with coefficients of either $\frac{1}{h^2}$ or $-6$.
<br>Lets look at our equation with the context of a space in mind. Because we are only looking at the region designated by $(i, j, k)$ and it's "neighbors", the coefficients of every other region is zero. Thinking about this like this, we can create a system of linear equations to find the potential field. 
<br>We can solve this system of linear equations and therefore approximate the solutions to our PDE! (My understanding of the reasoning and processes behind solving a system of linear equations in a 3D space like this is limited and my explanation sucks, look at this [youtube video](https://youtu.be/8MP9rDxfpDI?t=376))
<br>
### Wait but what if we don't know the charge density and only potential? How do we find the charge density?
This is something that needs to be done when trying to find the charge density of the surface of a conductor. The solution is to just rearrange the equation to find the charge distribution.
<br>idfk I forgot how I did this...
<br>
## Using the description language
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

