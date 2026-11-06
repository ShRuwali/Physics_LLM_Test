To determine the **tension in the string** at the **bottom of the vertical circular path**, we analyze the forces acting on the object at that specific point.

---

### **Given:**

- Mass of the object:  
  $ m = 10 \text{ nanograms} = 10 \times 10^{-12} \text{ kg} = 1.0 \times 10^{-11} \text{ kg} $

- Radius of the circular path:  
  $ R = 5.0 \text{ meters} $

- Speed of the object:  
  $ v = 3.001 \times 10^8 \text{ m/s} $

- Acceleration due to gravity:  
  $ g = 10.0 \text{ m/s}^2 $

- The motion is **uniform circular motion** in a **vertical circle**, so the **speed is constant** (as per the problem statement).

---

### **Conceptual Setup:**

At the **bottom of the vertical circle**, the **tension** in the string must provide **two components** of force:

1. The **centripetal force** required to maintain circular motion:
   $$
   F_{\text{centripetal}} = \frac{mv^2}{R}
   $$

2. The **weight** of the object (which acts **downward**, opposite to the direction of the centripetal force):
   $$
   F_{\text{gravity}} = mg
   $$

Since the **tension** is the **net upward force**, the tension at the bottom is:
$$
T = \frac{mv^2}{R} + mg
$$

However, given the **very small mass** and **extremely high speed**, the **gravitational term** is **negligible** compared to the **centripetal force**. Let's verify this.

---

### **Step-by-Step Calculation:**

#### **1. Centripetal Force:**
$$
\frac{mv^2}{R} = \frac{(1.0 \times 10^{-11}) \times (3.001 \times 10^8)^2}{5.0}
$$

First, calculate $ v^2 $:
$$
(3.001 \times 10^8)^2 = 9.006001 \times 10^{16}
$$

Now:
$$
\frac{mv^2}{R} = \frac{1.0 \times 10^{-11} \times 9.006001 \times 10^{16}}{5.0} = \frac{9.006001 \times 10^5}{5.0} = 1.8012002 \times 10^5 \text{ N}
$$

#### **2. Gravitational Force:**
$$
mg = (1.0 \times 10^{-11}) \times 10.0 = 1.0 \times 10^{-10} \text{ N}
$$

#### **3. Total Tension:**
$$
T = 1.8012002 \times 10^5 + 1.0 \times 10^{-10} \approx 1.8012 \times 10^5 \text{ N}
$$

The gravitational component is **100 million times smaller** than the centripetal force, so it can be **safely ignored**.

---

### **Significant Figures Consideration:**

- The **mass** is given as **10 nanograms**, which is **two significant figures** (if written as "10. nanograms").
- The **radius** is **5.0 meters**, also **two significant figures**.
- The **speed** is given as **3.001 × 10⁸ m/s**, which is **four significant figures**.
- **g** is given as **10.0 m/s²**, which is **three significant figures**.

The **least precise value** (mass or radius) has **two significant figures**, so the final answer should be **rounded to two significant figures**.

$$
T = \boxed{1.8 \times 10^5} \text{ N}
$$

---

### **Additional Notes:**

- The **speed given** (3.001 × 10⁸ m/s) is **slightly greater than the speed of light** (c ≈ 3.0 × 10⁸ m/s), which is **physically impossible** under classical mechanics. This suggests the problem may be **intended to test classical physics assumptions**, or it's a **theoretical scenario** where the speed is close to, but not exceeding, c.
- However, even if we **did** consider relativistic effects, the **Lorentz factor** would be **imaginary** due to $ v > c $, which is not physically meaningful. Therefore, **relativistic corrections are not applicable here**.

---

### **Final Answer:**

$$
\boxed{1.8 \times 10^5} \text{ N}
$$