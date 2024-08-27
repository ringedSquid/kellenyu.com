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

## How can we solve this DE?
Say we wanted to know the displacement $x$ at some time $t$. How would we do this? The straightforward approach is to take a double integral of our DE to find $x$ with respect to $t$. However this is not easy. What if instead of trying to solve this DE we just create an analog to this system? <br>
With this analog we can plug in initial paramters $x$, $v$, and $a$, let the system run, then measure it at some time $t$. Turns out we can in fact do this! Using the magic of operational amplifiers, we can set up an analog to this system that will behave the exact same way! (except voltages vary instead of displacement).<br>
We can set up a few integrators and summing amplifiers in a way that "mimics" our DE and put a scope probe at certain points of the circuit to get the information we want. <br>

## The process
My group and I first came up with a high level flowchart of the circuit before then simulating it in ltSPICE. It worked as expected so we then went to breadboarding. I used an LM358N as my Op-Amp coupled with a 12v dual rail supply. (I had to create a virtual ground, because I only have a single rail supply). <br>
Potentiometers were put on the inputs to the summing amplifiers to adjust the coefficients, and a simple voltage divider with a pushbutton acted as a way to initialize the system. <br>
What was cool was that by plugging the output of the last integrator right back into an input, we were "equating" the terms of the DE. It feels kind of weird to think about, how its all instantaneous. <br>
One really important thing to do is slap a buffer on the virtual ground connection as without it, things don't work quite well. 
Also that some settings would make the Op-Amps saturate real fast, or just kind of break things (something to do with the frequency being too high). Measuring things was kind of painful as I had to set my scope to the longest capture window, and updates would take like 10 seconds to be shown.
