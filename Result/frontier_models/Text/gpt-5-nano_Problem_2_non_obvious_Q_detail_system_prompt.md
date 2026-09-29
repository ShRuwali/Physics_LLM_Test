Yes, this is solvable and no physical laws are broken. The system is a physical pendulum (solid sphere on a massless string).

Key formulas (no latex in the answer):
- Moment of inertia about the pivot: I = I_cm + m L^2
- For a solid sphere of mass m and radius a: I_cm = (2/5) m a^2
- Small-angle period for a physical pendulum: T = 2π sqrt(I / (m g L))

Given:
- m = 2.5 nanograms = 2.5 x 10^-12 kg
- diameter = 1 nanometer, so radius a = 0.5 nm = 5 x 10^-10 m
- L = 2 m
- g = 10 m/s^2

Compute I_cm:
- a^2 = (5 x 10^-10)^2 = 2.5 x 10^-19
- I_cm = (2/5) m a^2 = 0.4 x (2.5 x 10^-12) x (2.5 x 10^-19) ≈ 2.5 x 10^-31 kg m^2

Compute I about the pivot:
- m L^2 = (2.5 x 10^-12) x (2)^2 = 1.0 x 10^-11 kg m^2
- I ≈ I_cm + m L^2 ≈ 1.0 x 10^-11 kg m^2 (the I_cm term is negligible)

Compute m g L:
- m g L = (2.5 x 10^-12) x 10 x 2 = 5.0 x 10^-11

Thus the period:
- T = 2π sqrt(I / (m g L)) ≈ 2π sqrt( (1.0 x 10^-11) / (5.0 x 10^-11) ) = 2π sqrt(0.2)
- sqrt(0.2) ≈ 0.4472, so T ≈ 2π x 0.4472 ≈ 2.81 seconds

Conclusion:
- The pendulum’s period is about 2.8 seconds.
- The sphere’s finite size has an utterly negligible effect; the motion is essentially that of a point mass at distance L.