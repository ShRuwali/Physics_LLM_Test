To find the time period of the pendulum, we must account for the fact that the mass is a solid sphere rather than a point mass. This requires using the **Moment of Inertia** and the **Parallel Axis Theorem**.

### 1. Identify the Given Data:
*   Mass of the sphere (m) = 2.0 kg
*   Distance from support to center of mass (L) = 2.0 m
*   Radius of the sphere (R) = 1.0 m
*   Acceleration due to gravity (g) = 10.0 m/s²

### 2. Calculate the Moment of Inertia (I):
The moment of inertia of a solid sphere about its center of mass is:
I_cm = (2/5) * m * R^2

Using the Parallel Axis Theorem, the moment of inertia (I) about the point of support (at distance L from the center) is:
I = I_cm + m * L^2
I = (2/5) * m * R^2 + m * L^2

Substitute the values:
I = (2/5) * (2.0 kg) * (1.0 m)^2 + (2.0 kg) * (2.0 m)^2
I = (0.4 * 2.0) + (2.0 * 4.0)
I = 0.8 + 8.0
I = 8.8 kg·m²

### 3. Determine the Formula for the Time Period (T):
For a physical pendulum (where the mass is distributed), the formula for the time period for small displacements is:
T = 2 * pi * sqrt(I / (m * g * h))

Where:
*   I = Moment of inertia about the pivot (8.8 kg·m²)
*   m = Mass (2.0 kg)
*   g = Gravity (10.0 m/s²)
*   h = Distance from the pivot to the center of mass (L = 2.0 m)

### 4. Calculate the Time Period:
T = 2 * pi * sqrt(8.8 / (2.0 * 10.0 * 2.0))
T = 2 * pi * sqrt(8.8 / 40.0)
T = 2 * pi * sqrt(0.22)

Calculate the square root:
sqrt(0.22) ≈ 0.469

Calculate the final value:
T = 2 * 3.14159 * 0.469
T ≈ 2.948

**Final Answer:**
The time period of the pendulum is approximately **2.95 seconds**.