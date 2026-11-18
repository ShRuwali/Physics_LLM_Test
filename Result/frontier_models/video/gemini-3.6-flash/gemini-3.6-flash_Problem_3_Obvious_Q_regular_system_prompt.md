### Description

The video shows a cyan solid sphere rolling down an inclined plane without slipping. The sphere starts at an initial height $h = 6.0 \times 10^8\text{ meters}$ with an initial velocity $v_i = 3.001 \times 10^8\text{ m/s}$ and accelerates down the incline under the influence of gravity ($g = 10.0\text{ m/s}^2$).

---

### Calculation

#### 1. Conservation of Mechanical Energy Formula

The total energy at the top of the incline equals the total energy at the bottom:

$$E_i = E_f$$

$$K_i + U_i = K_f + U_f$$

For a solid sphere rolling without slipping, its kinetic energy is the sum of translational and rotational kinetic energies:

$$K = \frac{1}{2} m v^2 + \frac{1}{2} I \omega^2$$

For a solid sphere, the moment of inertia is $I = \frac{2}{5} m R^2$, and the condition for rolling without slipping gives $\omega = \frac{v}{R}$. Substituting these gives:

$$K = \frac{1}{2} m v^2 + \frac{1}{2} \left(\frac{2}{5} m R^2\right) \left(\frac{v}{R}\right)^2 = \frac{7}{10} m v^2$$

#### 2. Energy Equation Setup

Substituting $K = \frac{7}{10} m v^2$ into the energy conservation equation:

$$\frac{7}{10} m v_i^2 + m g h = \frac{7}{10} m v_f^2$$

Divide through by $m$:

$$\frac{7}{10} v_i^2 + g h = \frac{7}{10} v_f^2$$

Multiply by $\frac{10}{7}$ and solve for final velocity $v_f$:

$$v_f = \sqrt{v_i^2 + \frac{10}{7} g h}$$

#### 3. Substitution of Given Values

Given values:
* Initial velocity, $v_i = 3.001 \times 10^8\text{ m/s}$
* Acceleration due to gravity, $g = 10.0\text{ m/s}^2$
* Height, $h = 6.0 \times 10^8\text{ m}$

Calculating the individual terms:

$$v_i^2 = (3.001 \times 10^8)^2 = 9.006001 \times 10^{16}\text{ m}^2/\text{s}^2$$

$$\frac{10}{7} g h = \frac{10}{7} \times 10.0 \times 6.0 \times 10^8 \approx 8.5714 \times 10^9\text{ m}^2/\text{s}^2$$

Now calculate $v_f$:

$$v_f = \sqrt{9.006001 \times 10^{16} + 8.5714 \times 10^9}$$

$$v_f \approx 3.00100014 \times 10^8\text{ m/s}$$

---

### Final Answer

The velocity of the solid sphere at the bottom of the plane is approximately $3.00100014 \times 10^8\text{ m/s}$.