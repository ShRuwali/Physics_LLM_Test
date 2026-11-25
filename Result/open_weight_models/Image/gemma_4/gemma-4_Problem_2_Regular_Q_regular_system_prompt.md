### Description of the System

The image depicts a physical pendulum consisting of a sphere of mass $m$ suspended from a fixed point by a string of negligible mass. The distance from the point of support to the center of the sphere is $L$. The sphere has a radius $R$, where $R = L/2$. 

In this system, the sphere acts as a rigid body undergoing rotational motion about the pivot point. For small angular displacements, the system behaves like a simple harmonic oscillator.

### Given Data
*   Mass of the sphere ($m$) = $2.0 \text{ kg}$
*   Distance from support to center of mass ($L$) = $2.0 \text{ m}$
*   Radius of the sphere ($R$) = $1.0 \text{ m}$
*   Acceleration due to gravity ($g$) = $10.0 \text{ m/s}^2$

### Calculation of Time Period

The time period $T$ for a physical pendulum for small oscillations is given by the formula:
$$T = 2\pi \sqrt{\frac{I}{mgL}}$$
where $I$ is the moment of inertia of the body about the pivot point.

**1. Moment of Inertia ($I$):**
Using the parallel axis theorem, the moment of inertia about the pivot point is:
$$I = I_{cm} + mL^2$$
For a solid sphere, the moment of inertia about its center of mass is $I_{cm} = \frac{2}{5}mR^2$. Substituting this into the equation:
$$I = \frac{2}{5}mR^2 + mL^2$$

**2. Substituting the values:**
Since $R = 1.0 \text{ m}$ and $L = 2.0 \text{ m}$:
$$I = \frac{2}{5}(2.0)(1.0)^2 + (2.0)(2.0)^2$$
$$I = 0.8 + 8.0 = 8.8 \text{ kg}\cdot\text{m}^2$$

**3. Calculating the Time Period ($T$):**
Now, substitute $I$, $m$, $g$, and $L$ into the time period formula:
$$T = 2\pi \sqrt{\frac{8.8}{(2.0)(10.0)(2.0)}}$$
$$T = 2\pi \sqrt{\frac{8.8}{40.0}}$$
$$T = 2\pi \sqrt{0.22}$$
$$T \approx 2 \times 3.14159 \times 0.469$$
$$T \approx 2.947 \text{ seconds}$$

**Final Answer:**
The time period of oscillation for small displacements is approximately $2.95 \text{ s}$.