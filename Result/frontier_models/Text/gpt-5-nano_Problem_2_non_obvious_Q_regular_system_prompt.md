Answer: about 2.8 seconds

Reasoning (for small oscillations):
- For a physical pendulum, the period is T = 2π sqrt(I / (m g d)), where:
  - I is the moment of inertia about the pivot,
  - m is the total mass,
  - g is gravity,
  - d is the distance from the pivot to the center of mass (here d = L = 2 m).

- The bob is a solid sphere of mass m = 2.5 ng = 2.5 × 10^-12 kg and radius r = diameter/2 = 0.5 nm = 0.5 × 10^-9 m.
  - Moment of inertia about its center: I_cm = (2/5) m r^2.
  - Moment of inertia about the pivot: I_pivot = I_cm + m d^2, with d = L = 2 m.

Compute:
- r^2 = (0.5 × 10^-9)^2 = 2.5 × 10^-19
- I_cm = (2/5) m r^2 = 0.4 × (2.5 × 10^-12) × (2.5 × 10^-19) ≈ 2.5 × 10^-31 kg·m^2
- m d^2 = (2.5 × 10^-12) × (2)^2 = 1.0 × 10^-11 kg·m^2
- I_pivot ≈ 1.0 × 10^-11 kg·m^2 (the I_cm term is negligible here)

- m g d = (2.5 × 10^-12) × 10 × 2 = 5.0 × 10^-11

- T = 2π√(I_pivot / (m g d)) ≈ 2π√(1.0 × 10^-11 / 5.0 × 10^-11) = 2π√(0.2) ≈ 2.81 s

Remark: This is essentially the same as a simple pendulum with length L = 2 m, since the sphere’s rotational inertia is tiny compared to m L^2.