### **Description of the Video**
The video displays a schematic diagram of a pendulum system consisting of:
*   A sphere of mass ($m$) = $2.5\text{ nanograms} = 2.5 \times 10^{-12}\text{ kg}$
*   Diameter of the sphere ($D$) = $100\text{ nanometers} \implies$ Radius ($R$) = $50\text{ nanometers} = 50 \times 10^{-9}\text{ m}$
*   Distance from the point of support (pivot) to the center of the sphere ($L$) = $50\text{ nanometers} = 50 \times 10^{-9}\text{ m}$
*   Acceleration due to gravity ($g$) = $10\text{ m/s}^2$
*   A suspension string of negligible mass.

---

### **Calculation of the Time Period of Oscillation**

Because the radius of the sphere ($R = 50\text{ nm}$) is equal to the distance from the pivot to its center ($L = 50\text{ nm}$), the size of the sphere is not negligible compared to the length of the pendulum. Thus, the system must be analyzed as a **physical pendulum** rather than a simple pendulum.

#### **1. Physical Pendulum Calculation (Solid Sphere)**
The time period $T$ for small-angle oscillations of a physical pendulum is given by:
$$T = 2\pi \sqrt{\frac{I}{mgd}}$$

Where:
*   $d = L = 50\text{ nm}$ (distance from pivot to center of mass)
*   $I$ is the moment of inertia about the pivot point.

Using the **parallel axis theorem** for a solid sphere:
$$I = I_{\text{cm}} + mL^2 = \frac{2}{5}mR^2 + mL^2$$

Since $R = L$:
$$I = \frac{2}{5}mL^2 + mL^2 = \frac{7}{5}mL^2$$

Substitute $I$ into the time period equation:
$$T = 2\pi \sqrt{\frac{\frac{7}{5}mL^2}{mgL}} = 2\pi \sqrt{\frac{7L}{5g}}$$

Substitute the given values ($L = 50 \times 10^{-9}\text{ m}$, $g = 10\text{ m/s}^2$):
$$T = 2\pi \sqrt{\frac{7 \times (50 \times 10^{-9})}{5 \times 10}}$$
$$T = 2\pi \sqrt{7 \times 10^{-9}}\text{ s}$$
$$T \approx 2\pi \times (8.367 \times 10^{-5})\text{ s} \approx \mathbf{5.26 \times 10^{-4}\text{ s}} \quad (0.526\text{ ms})$$

---

#### **2. Simple Pendulum Approximation (Point Mass)**
If the sphere is approximated as a simple point mass concentrated at its center of mass:
$$T \approx 2\pi \sqrt{\frac{L}{g}}$$
$$T \approx 2\pi \sqrt{\frac{50 \times 10^{-9}}{10}} = 2\pi \sqrt{5 \times 10^{-9}}\text{ s}$$
$$T \approx 2\pi \times (7.071 \times 10^{-5})\text{ s} \approx \mathbf{4.44 \times 10^{-4}\text{ s}} \quad (0.444\text{ ms})$$