To solve this problem, we will proceed step-by-step using the principles of Hooke's Law and Simple Harmonic Motion (SHM).

### 1. Calculation of the Force Constant (k)
According to Hooke's Law, the force (F) exerted by a spring is directly proportional to its displacement (x):
F = k * x

Given:
Force (F) = 5.0 N
Displacement (x) = 0.020 m

k = F / x
k = 5.0 N / 0.020 m
**k = 250 N/m**

### 2. Calculation of the Mass (m)
The mass of the block is given in nanograms. We must convert this to the standard SI unit (kilograms).
1 nanogram (ng) = 10^-9 grams
1 gram (g) = 10^-3 kilograms (kg)
Therefore, 1 nanogram = 10^-12 kg.

Given:
m = 500 ng
m = 500 * 10^-12 kg
**m = 5.0 * 10^-10 kg**

### 3. Calculation of Angular Frequency (ω)
The angular frequency for a mass-spring system is given by the formula:
ω = sqrt(k / m)

Substituting the values:
ω = sqrt(250 / (5.0 * 10^-10))
ω = sqrt(50 * 10^10)
ω = sqrt(5 * 10^11)
ω = sqrt(50 * 10^10) ≈ 7.07 * 10^5 rad/s
**ω ≈ 707,107 rad/s**

### 4. Calculation of Frequency (f)
The frequency is related to the angular frequency by the formula:
f = ω / (2 * π)

Substituting the values:
f = 707,107 / (2 * 3.14159)
**f ≈ 112,540 Hz (or 112.54 kHz)**

---

### Physical Analysis and Justification

**Physical Laws and Parameters Check:**
1.  **Scale Discrepancy:** There is a massive discrepancy between the scale of the spring and the scale of the object. The spring constant (k = 250 N/m) is typical for a macroscopic spring (like one used in a laboratory). However, the mass (500 ng) and dimensions (400 nm) are on the **nanoscale**.
2.  **Inertia vs. Spring Stiffness:** A mass of 500 nanograms is incredibly small. When attached to a spring with a stiffness of 250 N/m, the "restoring force" is overwhelmingly dominant. This results in an extremely high frequency of oscillation (over 112 kHz).
3.  **Damping and Air Resistance:** While the problem specifies a "frictionless surface," in a real-world scenario at this scale, air resistance (viscosity) would be the dominant force. At 112 kHz, the motion would likely be "overdamped" or "critically damped" by the surrounding air molecules, meaning the block would not oscillate freely as predicted by the ideal model.
4.  **Material Limits:** A spring capable of maintaining a constant k of 250 N/m while interacting with a 400 nm object is physically difficult to manufacture. At the nanoscale, the "spring" would likely behave more like a molecular bond or a cantilever beam, where the physics of elasticity changes.

**Conclusion on Physical Justifiability:**
The solution is **mathematically correct** based on the provided parameters, but it is **physically questionable**. The model assumes an "ideal spring" can behave identically at the macro scale (where it was calibrated) and the nano scale (where the mass is placed). In reality, the spring's properties would change, and environmental factors like air viscosity would prevent the observed oscillation.