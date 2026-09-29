Use the physical pendulum formula for the period:
T = 2π sqrt( I_pivot / (m g d) ),
where d is the distance from the pivot to the center of mass, and I_pivot is the moment of inertia about the pivot.

For a solid sphere of radius r, I_cm = (2/5) m r^2. By the parallel axis theorem,
I_pivot = I_cm + m d^2 = m(d^2 + (2/5) r^2).

Here:
- d = L = 2 m
- r = diameter/2 = 0.5 nm = 5e-10 m
- g = 10 m/s^2
- m cancels in the final expression.

Thus,
T = 2π sqrt( (d^2 + (2/5) r^2) / (g d) )
  = 2π sqrt( (4 + (2/5)*(5e-10)^2) / (10*2) )
  ≈ 2π sqrt(4/20)
  = 2π sqrt(0.2)
  ≈ 2.81 seconds.

Note: the tiny mass (2.5 nanograms) and the sphere’s small size have negligible effect; the result is essentially the same as a point mass at distance 2 m.