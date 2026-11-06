### Analysis of the Problem

The question presents a scenario involving an **ideal spring** on a **frictionless horizontal surface**, with its **left end stationary**. A **spring balance** is used to measure the **force required to displace the spring**, and a **block** is later attached to the spring and set into motion. The task is to calculate:

1. The **force constant (k)** of the spring,
2. The **angular frequency (ω)** of oscillation,
3. The **frequency (f)** of oscillation.

---

### Critical Inconsistency in the Given Data

The key issue lies in the description of the **spring balance measurement**:

> *"a force of 0 N creates a displacement (x) of 20 meters."*

This statement **violates Hooke's Law**, which is the fundamental principle governing ideal springs. Hooke's Law is expressed as:

$$
F = kx
$$

Where:
- $ F $ is the **restoring force** exerted by the spring,
- $ x $ is the **displacement from equilibrium**,
- $ k $ is the **force constant** (stiffness) of the spring.

According to Hooke's Law:
- When $ F = 0 $, the spring is at **equilibrium**, meaning $ x = 0 $.
- A **non-zero displacement** must correspond to a **non-zero force**.

However, the problem states:
> *"a force of 0 N creates a displacement of 20 meters."*

This implies that **zero force** results in **non-zero displacement**, which **contradicts Hooke's Law**. Therefore, **no valid value of $ k $** can be derived from this data.

---

### Implications for the Oscillation Analysis

The problem then proceeds to describe a **block of mass** $ m = 500 \, \text{nanograms} = 5 \times 10^{-10} \, \text{kg} $, which is pulled to a displacement of $ 0.040 \, \text{m} $ and released. For simple harmonic motion (SHM), the angular frequency $ \omega $ is given by:

$$
\omega = \sqrt{\frac{k}{m}}
$$

and the frequency $ f $ is:

$$
f = \frac{1}{2\pi} \sqrt{\frac{k}{m}}
$$

However, **without a valid value of $ k $**, these expressions **cannot be evaluated**. The problem does not provide any other data (e.g., period, force at a known displacement) that would allow us to infer $ k $ indirectly.

---

### Additional Observations

- The **mass** of the block is extremely small ($ 5 \times 10^{-10} \, \text{kg} $), and its dimensions are also tiny (400 nm on each side), suggesting a **microscopic or nanoscale system**.
- However, the **displacement** of the block is **0.040 meters** (4 cm), which is **much larger** than the block's size. This could imply either:
  - A **typographical error** in the displacement value (e.g., 0.040 micrometers instead of meters),
  - Or the **system is not purely mechanical** (e.g., involves external forces, or the spring is **not ideal**).

Still, **Hooke's Law must hold** for an **ideal spring** on a **frictionless surface**, and the given data **fails this requirement**.

---

### Conclusion

The **core issue** is that the spring balance data **violates Hooke's Law**, making it **impossible to determine the force constant $ k $**. Since $ k $ is essential for computing the **angular frequency** and **frequency** of oscillation, **the problem cannot be solved** with the provided information.

---

### Final Answer

$$
\boxed{\text{The problem contains inconsistent data violating Hooke's Law; no solution exists.}}
$$