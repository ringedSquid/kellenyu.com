# Damped Harmonic Motion Solver
A simple analog computer constructed from Op-Amps that models damped harmonic motion through solving a 2nd order differential equation.
<br>

### [link to repo](https://github.com/ringedSquid/BWSI-ASICS-24-BoingBoing)
<br>
## Quick overview of the physics:
We first start with Hooke's Law, which describes the relationship between the force a spring exerts and its displacement from the equilibrium position:
$$
F = -kx
$$

Since $F = ma$, we can rewrite this as:
$$
ma = -kx
$$

This describes simple harmonic motion, and to make it damped harmonic motion, we need to model the system losing energy due to friction/air resistance:
$$
ma = -kx - cv
$$

And since $a = \frac{d^{2}x}{dt^2}$ and $v = \frac{dx}{dt}$, we can rewrite this as:
$$
m\frac{d^{2}x}{dt^2} = -c\frac{dx}{dt} - kx
$$

## How do we solve this DE?




