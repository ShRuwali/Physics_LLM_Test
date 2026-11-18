**Description:**

The video shows a diagram of a spherical pendulum consisting of a sphere of mass $m = 2.5\text{ nanograms}$ and diameter $D = 100\text{ nanometers}$ suspended from a support by a string of negligible mass. The distance from the point of support to the center of the sphere is given as $L = 50\text{ nanometers}$, and the acceleration due to gravity is $g = 10.0\text{ m/s}^2$.

---

### **Calculation of Time Period of Oscillation**

#### **1. Given Data:**
* Mass of the sphere, $m = 2.5\text{ nanograms} = 2.5 \times 10^{-12}\text{ kg}$
* Diameter of the sphere, $D = 100\text{ nm} \implies \text{Radius } R = \frac{D}{2} = 50\text{ nm} = 50 \times 10^{-9}\text{ m}$
* Distance between point of support and center of sphere, $L = 50\text{ nm} = 50 \times 10^{-9}\text{ m}$
* Acceleration due to gravity, $g = 10.0\text{ m/s}^2$

---

#### **2. Moment of Inertia:**
Since the size of the sphere is comparable to the length $L$, the system behaves as a physical pendulum. The moment of inertia $I$ about the point of support is calculated using the parallel axis theorem:

$$I = I_{\text{cm}} + m L^2$$

For a solid sphere, the moment of inertia about its center of mass is $I_{\text{cm}} = \frac{2}{5} m R^2$.

Since $R = L$:

$$I = \frac{2}{5} m L^2 + m L^2 = \frac{7}{5} m L^2$$

---

#### **3. Time Period Formula:**
The time period $T$ of a physical pendulum for small oscillations is given by:

$$T = 2\pi \sqrt{\frac{I}{m g L}}$$

Substituting $I = \frac{7}{5} m L^2$:

$$T = 2\pi \sqrt{\frac{\frac{7}{5} m L^2}{m g L}} = 2\pi \sqrt{\frac{7 L}{5 g}}$$

---

#### **4. Calculation:**
Substitute $L = 50 \times 10^{-9}\text{ m}$ and $g = 10.0\text{ m/s}^2$:

$$T = 2\pi \sqrt{\frac{7 \times (50 \times 10^{-9})}{5 \times 10.0}}$$

$$T = 2\pi \sqrt{7 \times 10^{-9}} = 2\pi \sqrt{70 \times 10^{-10}}$$

$$T = 2\pi \times \sqrt{70} \times 10^{-5}\text{ s}$$

$$T \approx 2 \times 3.14159 \times 8.3666 \times 10^{-5}\text{ s}$$

$$T \approx 5.26 \times 10^{-4}\text{ s}\quad (\text{or } 0.526\text{ ms})$$

---

**Final Answer:**
The time period of oscillation for small displacements is approximately $5.26 \times 10^{-4}\text{ s}$ (or $0.526\text{ ms}$).