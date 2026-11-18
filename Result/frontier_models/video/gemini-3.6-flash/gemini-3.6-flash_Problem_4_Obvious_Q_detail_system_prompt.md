### Description of the Video

 The video illustrates a object attached to a string executing vertical circular motion around a center point. The key parameters displayed on the screen are:

* Mass of the body, $m = 10 \text{ nanograms} = 1.0 \times 10^{-11} \text{ kg}$
* Radius of the body, $r = 100 \text{ nanometer} = 1.0 \times 10^{-7} \text{ m}$
* Radius of circular motion, $R = 5.0 \text{ meters}$
* Speed of the body, $v = 3.001 \times 10^8 \text{ m/s}$
* Acceleration due to gravity, $g = 10.0 \text{ m/s}^2$
* Highly elastic string

---

### Calculation of Tension at the Bottom

At the bottom of the vertical path, the tension force $T$ acts upward toward the center, while gravity $mg$ acts downward. The net inward force provides the centripetal acceleration:

$$T - mg = \frac{m v^2}{R}$$

Solving for the tension $T$:

$$T = m \left( g + \frac{v^2}{R} \right)$$

Substituting the given values using classical Newtonian mechanics:

$$v^2 = (3.001 \times 10^8 \text{ m/s})^2 = 9.006001 \times 10^{16} \text{ m}^2/\text{s}^2$$

$$\frac{v^2}{R} = \frac{9.006001 \times 10^{16}}{5.0} = 1.8012002 \times 10^{16} \text{ m/s}^2$$

Since $\frac{v^2}{R} \gg g$:

$$T \approx \frac{m v^2}{R} = (1.0 \times 10^{-11} \text{ kg}) \times (1.8012002 \times 10^{16} \text{ m/s}^2) \approx 1.8012 \times 10^5 \text{ N}$$

---

### Physical Justification and Violated Physical Laws

1. **Violation of Special Relativity:** The speed given for the body is $v = 3.001 \times 10^8 \text{ m/s}$, which exceeds the speed of light in vacuum ($c \approx 2.9979 \times 10^8 \text{ m/s}$). According to Einstein's theory of special relativity, no object with non-zero rest mass can reach or exceed the speed of light.
2. **Breakdown of Relativistic Mechanics:** At relativistic speeds, the Lorentz factor $\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$ must be applied. Because $v > c$, the term under the square root becomes negative, resulting in an imaginary Lorentz factor and rendering classical or standard relativistic force calculations mathematically undefined in real space.

**Conclusion:** The calculated solution of $T \approx 1.8012 \times 10^5 \text{ N}$ is **not physically justifiable** because the given parameter violates fundamental laws of physics.