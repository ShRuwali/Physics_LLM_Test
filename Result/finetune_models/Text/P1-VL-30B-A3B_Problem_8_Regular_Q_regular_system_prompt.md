To calculate the gravitational force between Planet A and its moon at the given closest distance, we apply **Newton's Law of Universal Gravitation**, which states:

$$
F = G \cdot \frac{M \cdot m}{d^2}
$$

Where:
- $ F $ is the gravitational force (in newtons),
- $ G $ is the gravitational constant: $ 6.674 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2} $,
- $ M $ is the mass of Planet A,
- $ m $ is the mass of the moon,
- $ d $ is the center-to-center distance between the two bodies.

---

### Step 1: Convert All Units to Standard SI

**Planet A's mass (M):**
- Given: $ 6000 \, \text{nanograms} $
- Since $ 1 \, \text{nanogram} = 10^{-12} \, \text{kg} $,  
  $$
  M = 6000 \times 10^{-12} = 6.0 \times 10^{-9} \, \text{kg}
  $$

**Moon's mass (m):**
- Given: $ 2.0 \times 10^{22} \, \text{kg} $  
  → Already in SI units.

**Distance (d):**
- Given: $ 3.0 \times 10^9 \, \text{m} $  
  → Already in SI units.

---

### Step 2: Plug Values into the Formula

$$
F = (6.674 \times 10^{-11}) \cdot \frac{(6.0 \times 10^{-9}) \cdot (2.0 \times 10^{22})}{(3.0 \times 10^9)^2}
$$

#### Step 2.1: Multiply $ M \cdot m $

$$
M \cdot m = (6.0 \times 10^{-9}) \cdot (2.0 \times 10^{22}) = 12.0 \times 10^{13} = 1.2 \times 10^{14} \, \text{kg}^2
$$

#### Step 2.2: Compute $ d^2 $

$$
d^2 = (3.0 \times 10^9)^2 = 9.0 \times 10^{18} \, \text{m}^2
$$

#### Step 2.3: Multiply by $ G $

$$
G \cdot (M \cdot m) = (6.674 \times 10^{-11}) \cdot (1.2 \times 10^{14}) = 8.0088 \times 10^3 \, \text{m}^3 \text{kg} \cdot \text{s}^{-2}
$$

#### Step 2.4: Divide by $ d^2 $

$$
F = \frac{8.0088 \times 10^3}{9.0 \times 10^{18}} = 0.88986 \times 10^{-15} = 8.8986 \times 10^{-16} \, \text{N}
$$

---

### Step 3: Apply Significant Figures

The given data has:
- Planet A's mass: 6000 nanograms → **2 significant figures** (as written),
- Moon's mass: $ 2.0 \times 10^{22} $ → **2 significant figures**,
- Distance: $ 3.0 \times 10^9 $ → **2 significant figures**.

Thus, the final result should be rounded to **2 significant figures**.

$$
F \approx 8.9 \times 10^{-16} \, \text{N}
$$

---

### Final Answer

$$
\boxed{8.9 \times 10^{-16}} \, \text{newtons}
$$