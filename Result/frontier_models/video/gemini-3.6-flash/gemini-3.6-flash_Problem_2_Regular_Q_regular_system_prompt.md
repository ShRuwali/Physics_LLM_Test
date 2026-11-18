### Description

The image shows a physical pendulum consisting of a uniform solid sphere suspended from a fixed horizontal support by a string of negligible mass. The key parameters given are:

* Mass of the sphere, $m = 2.0\text{ kg}$
* Distance between point of support and center of sphere, $L = 2.0\text{ m}$
* Radius of the sphere, $R = \frac{L}{2} = 1.0\text{ m}$
* Acceleration due to gravity, $g = 10.0\text{ m/s}^2$

---

### Calculation of Time Period

The sphere acts as a **physical pendulum**. 

1. **Moment of Inertia about the Center of Mass:**
   For a uniform solid sphere, the moment of inertia about its center of mass is:
   $$I_{\text{cm}} = \frac{2}{5} m R^2$$

2. **Moment of Inertia about the Pivot Point:**
   Using the parallel axis theorem, the moment of inertia about the point of support is:
   $$I = I_{\text{cm}} + m L^2 = \frac{2}{5} m R^2 + m L^2$$

3. **Time Period of Oscillation:**
   The formula for the time period $T$ of a physical pendulum for small displacement angles is:
   $$T = 2\pi \sqrt{\frac{I}{m g L}}$$

   Substituting $I = \frac{2}{5} m R^2 + m L^2$ into the formula:
   $$T = 2\pi \sqrt{\frac{\frac{2}{5} m R^2 + m L^2}{m g L}} = 2\pi \sqrt{\frac{\frac{2}{5} R^2 + L^2}{g L}}$$

4. **Substituting the Given Values:**
   * $R = 1.0\text{ m}$
   * $L = 2.0\text{ m}$
   * $g = 10.0\text{ m/s}^2$

   $$T = 2\pi \sqrt{\frac{\frac{2}{5} (1.0)^2 + (2.0)^2}{10.0 \times 2.0}}$$

   $$T = 2\pi \sqrt{\frac{0.4 + 4.0}{20.0}} = 2\pi \sqrt{\frac{4.4}{20.0}} = 2\pi \sqrt{0.22}$$

   $$T \approx 2\pi \times 0.469 = 0.938 \pi \approx 2.95\text{ seconds}$$

### Final Answer
The time period of oscillation for small displacements is approximately **$2.95\text{ s}$** (or $2\pi\sqrt{0.22}\text{ s}$).