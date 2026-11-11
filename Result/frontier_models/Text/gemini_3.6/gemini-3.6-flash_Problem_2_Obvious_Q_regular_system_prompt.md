To find the time period of the pendulum for small displacements, we can evaluate it using two perspectives: taking into account the finite size (rotational inertia) of the sphere (the physical pendulum model), and treating the mass as a point mass (the ideal simple pendulum model).

---

### Method 1: Considering the Sphere's Finite Size (Physical Pendulum - Most Accurate)

When the size of the sphere is comparable to the length $L$, the rotational moment of inertia of the sphere about its center of mass must be taken into account.

**1. Given Data:**
* Mass of sphere, $m = 2.5\text{ ng} = 2.5 \times 10^{-15}\text{ kg}$
* Radius of sphere, $R = \text{Diameter} / 2 = 100\text{ nm} / 2 = 50\text{ nm} = 5 \times 10^{-8}\text{ m}$
* Distance from point of support to center of mass, $L = 50\text{ nm} = 5 \times 10^{-8}\text{ m}$
* Acceleration due to gravity, $g = 10.0\text{ m/s}^2$

**2. Moment of Inertia ($I$):**
Using the parallel axis theorem:
* $I_{\text{cm}} = (2/5) \times m \times R^2$
* $I = I_{\text{cm}} + m \times L^2$

Since $L = R$:
* $I = (2/5) \times m \times R^2 + m \times R^2 = (7/5) \times m \times R^2$

**3. Time Period ($T$):**
The time period for a physical pendulum is given by:
* $T = 2 \times \pi \times \text{sqrt}(I / (m \times g \times L))$

Substitute $I$ and $L = R$:
* $T = 2 \times \pi \times \text{sqrt}( ((7/5) \times m \times R^2) / (m \times g \times R) )$
* $T = 2 \times \pi \times \text{sqrt}( 7 \times R / (5 \times g) )$

**4. Calculation:**
* $7 \times R / (5 \times g) = 7 \times (5 \times 10^{-8}) / (5 \times 10.0) = 7 \times 10^{-9}\text{ s}^2$
* $\text{sqrt}(7 \times 10^{-9}) \approx 8.3666 \times 10^{-5}\text{ s}$
* $T \approx 2 \times \pi \times 8.3666 \times 10^{-5} \approx 5.257 \times 10^{-4}\text{ seconds}$

---

### Method 2: Point-Mass Approximation (Ideal Simple Pendulum)

If the sphere is approximated as a point mass concentrated at its center:

* $T = 2 \times \pi \times \text{sqrt}(L / g)$
* $L / g = (5 \times 10^{-8}) / 10.0 = 5 \times 10^{-9}\text{ s}^2$
* $\text{sqrt}(5 \times 10^{-9}) \approx 7.071 \times 10^{-5}\text{ s}$
* $T \approx 2 \times \pi \times 7.071 \times 10^{-5} \approx 4.443 \times 10^{-4}\text{ seconds}$

---

### Final Answer:
* **Accounting for the sphere's size (Physical Pendulum):** **5.26 × 10⁻⁴ seconds** (or 0.526 milliseconds)
* **Point-mass simple pendulum approximation:** **4.44 × 10⁻⁴ seconds** (or 0.444 milliseconds)