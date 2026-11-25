### Description of the System

The image depicts a physical pendulum consisting of a sphere suspended from a fixed support by a string of negligible mass. The sphere has a diameter $D = 100 \text{ nm}$ and a mass $m = 2.5 \text{ nanograms}$. The distance from the point of support to the center of the sphere is $L = 50 \text{ nm}$. The acceleration due to gravity is given as $g = 10 \text{ m/s}^2$.

### Calculation of the Time Period

To find the time period of oscillation for small displacements, we use the formula for a physical pendulum:

$$T = 2\pi \sqrt{\frac{I}{mgL}}$$

Where:
*   $I$ is the moment of inertia of the sphere about the point of support.
*   $m$ is the mass of the sphere.
*   $g$ is the acceleration due to gravity.
*   $L$ is the distance from the pivot to the center of mass.

**1. Identify the Moment of Inertia ($I$):**
The moment of inertia of a solid sphere about its center is $I_{cm} = \frac{2}{5}mR^2$. Using the parallel axis theorem, the moment of inertia about the point of support is:
$$I = I_{cm} + mL^2$$
Given the diameter $D = 100 \text{ nm}$, the radius $R = 50 \text{ nm}$.
Note that $L = 50 \text{ nm}$, so $L = R$.

$$I = \frac{2}{5}mR^2 + mR^2 = \frac{7}{5}mR^2$$

**2. Substitute $I$ into the Time Period formula:**
$$T = 2\pi \sqrt{\frac{\frac{7}{5}mR^2}{mgL}}$$
Since $R = L$, the terms $m$, $R^2$, and $L$ simplify:
$$T = 2\pi \sqrt{\frac{\frac{7}{5}L^2}{gL}} = 2\pi \sqrt{\frac{7L}{5g}}$$

**3. Convert units to SI and calculate:**
*   $L = 50 \text{ nm} = 50 \times 10^{-9} \text{ m}$
*   $g = 10 \text{ m/s}^2$

$$T = 2\pi \sqrt{\frac{7 \times (50 \times 10^{-9})}{5 \times 10}}$$
$$T = 2\pi \sqrt{\frac{350 \times 10^{-9}}{50}}$$
$$T = 2\pi \sqrt{7 \times 10^{-9}}$$
$$T = 2\pi \sqrt{70 \times 10^{-10}}$$
$$T \approx 2 \times 3.14159 \times 8.366 \times 10^{-5}$$
$$T \approx 5.256 \times 10^{-4} \text{ seconds}$$

**Final Answer:**
The time period of oscillation for small displacements is approximately $5.26 \times 10^{-4} \text{ s}$ (or $0.526 \text{ ms}$).