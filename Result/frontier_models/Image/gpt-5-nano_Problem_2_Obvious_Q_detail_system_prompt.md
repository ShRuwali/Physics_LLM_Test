Description:
- A tiny solid sphere (mass m = 2.5 ng) of diameter D = 100 nm is suspended by a massless string of length L = 50 nm from a fixed support.
- The center of mass of the sphere is at a distance L = 50 nm from the pivot. Gravity g = 10 m/s^2 acts downward.
- We consider small angular displacements (small-angle pendulum).

How to get the period (for a physical pendulum):
- For small θ, the equation of motion gives ω^2 = (m g d) / I_pivot, where d is the distance from pivot to CM (d = L) and I_pivot is the moment of inertia about the pivot.
- I_pivot = I_cm + m d^2, with I_cm the moment of inertia about the CM.
- For a solid sphere: I_cm = (2/5) m R^2, where R = D/2.

Numbers (from the figure):
- m = 2.5 ng = 2.5 × 10^-12 kg
- D = 100 nm ⇒ R = 50 nm = 5 × 10^-8 m
- L = d = 50 nm = 5 × 10^-8 m
- g = 10 m/s^2

Compute:
- I_cm = (2/5) m R^2 = 0.4 × (2.5 × 10^-12 kg) × (5 × 10^-8 m)^2
        = 2.5 × 10^-27 kg m^2
- I_pivot = I_cm + m L^2 = 2.5 × 10^-27 + (2.5 × 10^-12) × (5 × 10^-8)^2
          = 2.5 × 10^-27 + 6.25 × 10^-27
          = 8.75 × 10^-27 kg m^2
- m g d = m g L = (2.5 × 10^-12 kg) × (10 m/s^2) × (5 × 10^-8 m)
          = 1.25 × 10^-18 N·m

Period:
- T = 2π √( I_pivot / (m g d) )
    = 2π √( 8.75 × 10^-27 / 1.25 × 10^-18 )
    = 2π √(7.0 × 10^-9)
    ≈ 2π × 8.37 × 10^-5 s
    ≈ 5.3 × 10^-4 s

Thus the time period for small oscillations is about T ≈ 5.3 × 10^-4 seconds (≈ 0.53 ms). For comparison, the point-mass approximation T0 ≈ 2π √(L/g) gives ≈ 4.4 × 10^-4 s, so the finite size adds a modest correction.

Notes on physical validity:
- No fundamental laws are violated in the idealized model. We used the exact physical-pendulum formula with I_pivot = I_cm + m L^2 and the small-angle approximation.
- In a real nanoscale pendulum, non-ideal effects (air damping, Brownian motion, van der Waals/Casimir forces, string rigidity, etc.) would be significant and could invalidate the simple model. The problem, however, assumes an idealized, negligible-damping setup as given.