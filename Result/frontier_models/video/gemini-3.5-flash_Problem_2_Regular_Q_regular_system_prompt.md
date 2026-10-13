Based on the details provided in the video, here is the description of the setup and the step-by-step calculation of the time period of oscillation for small displacements.

---

### **Description of the System**
The video shows a **physical pendulum** consisting of a uniform solid sphere of mass $m = 2\text{ kg}$ and radius $R = 1\text{ m}$ suspended by a massless string. The distance from the point of support (pivot) to the center of the sphere (which is also the center of mass of the system) is $L = 2\text{ m}$.

---

### **Calculation of the Time Period of Oscillation**

Because the radius of the sphere is significant compared to the suspension length ($R$ is not negligible compared to $L$), we must treat this as a **physical pendulum** rather than a simple pendulum.

The time period ($T$) for small-angle oscillations of a physical pendulum is given by:
$$T = 2\pi \sqrt{\frac{I}{mgd}}$$

Where:
* $I$ = Moment of inertia of the system about the point of support
* $m = 2\text{ kg}$ (mass of the sphere)
* $g = 10\text{ m/s}^2$ (acceleration due to gravity)
* $d = L = 2\text{ m}$ (distance from the support to the center of mass)

---

#### **Step 1: Calculate the Moment of Inertia ($I$)**
Using the parallel axis theorem, the moment of inertia about the suspension point is:
$$I = I_{\text{cm}} + md^2$$

For a solid sphere, the moment of inertia about its center of mass ($I_{\text{cm}}$) is:
$$I_{\text{cm}} = \frac{2}{5}mR^2$$

Substituting $d = L$:
$$I = \frac{2}{5}mR^2 + mL^2$$

Substitute the given values ($m = 2\text{ kg}$, $R = 1\text{ m}$, $L = 2\text{ m}$):
$$I = \frac{2}{5}(2)(1)^2 + (2)(2)^2$$
$$I = 0.8 + 8 = 8.8\text{ kg}\cdot\text{m}^2$$

---

#### **Step 2: Calculate the Time Period ($T$)**
Now, substitute $I$, $m$, $g$, and $d$ into the time period formula:
$$T = 2\pi \sqrt{\frac{8.8}{2 \times 10 \times 2}}$$
$$T = 2\pi \sqrt{\frac{8.8}{40}}$$
$$T = 2\pi \sqrt{0.22}$$

Using $\sqrt{0.22} \approx 0.469$:
$$T \approx 2 \times 3.1416 \times 0.469$$
$$T \approx 2.95\text{ seconds}$$

---

### **Conclusion**
The time period of oscillation for small displacements is approximately **$2.95\text{ seconds}$** (or exactly $2\pi\sqrt{0.22}\text{ s}$).