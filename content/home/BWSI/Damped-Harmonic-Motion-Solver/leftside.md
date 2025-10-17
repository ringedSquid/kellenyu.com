# Damped Harmonic Motion Solver
An analog computer that models damped harmonic motion. 

<br>
## Overview
We want to solve the following differential equation, which describes how a damped harmonic oscillator behaves:
$$
m\frac{d^{2}x}{dt^2} = -c\frac{dx}{dt} - kx
$$
We can re-express this equation as follows:
$$
\frac{d^{2}x}{dt^2} = -\frac{1}{m}\left(c\int\frac{d^{2}x}{dt^2}\,dt + k\iint\frac{d^{2}x}{dt^2}\,dt\right)
$$
We can "implement" the relationship described here using a series of opamp integrators, summing amplifiers, and inverting amplifiers.

## The process
I first came up with a high level flowchart of the circuit before then simulating it in ltSPICE. It worked as expected so we then went to breadboarding. I used an LM358N as my Op-Amp coupled with a 12v dual rail supply. (I had to create a virtual ground, because I only have a single rail supply). <br>
Potentiometers were put on the inputs to the summing amplifiers to adjust the coefficients, and a simple voltage divider with a pushbutton acted as a way to initialize the system. <br>
What was cool was that by plugging the output of the last integrator right back into an input, we were "equating" the terms of the DE. It feels kind of weird to think about, how its all instantaneous. <br>


