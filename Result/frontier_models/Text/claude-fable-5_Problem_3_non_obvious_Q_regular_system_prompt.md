# Setting Up the Problem

For a solid sphere rolling down an incline (without slipping), conservation of energy gives:

**Initial KE + Potential Energy = Final KE**

(1/2)mv₀² + (1/2)Iω₀² + mgh = (1/2)mv² + (1/2)Iω²

For a solid sphere, I = (2/5)mr², and with rolling condition ω = v/r, the total kinetic energy becomes (7/10)mv². So:

(7/10)v₀² + gh = (7/10)v²

Solving for the final velocity:

**v = √[v₀² + (10/7)gh]**

# Plugging in Numbers

- v₀ = 3.001 × 10⁸ m/s, so v₀² = 9.006 × 10¹⁶ m²/s²
- (10/7)gh = (10/7)(10)(6 × 10⁸) = 8.571 × 10⁹ m²/s²

Then:

v = √(9.006 × 10¹⁶ + 0.0000008571 × 10¹⁶) ≈ √(9.006 × 10¹⁶)

**v ≈ 3.001 × 10⁸ m/s**

The gravitational term is about seven orders of magnitude smaller than v₀², so the velocity gain is utterly negligible (an increase of only about 10⁻⁸ m/s). Note also that the mass and diameter of the sphere never actually matter — mass cancels out, and the radius cancels in the moment of inertia term.

# Important Physical Caveat

This problem is unphysical: the given initial speed of 3.001 × 10⁸ m/s **exceeds the speed of light** (c ≈ 2.998 × 10⁸ m/s), which no massive object can reach. Additionally, a height of 6 × 10⁸ m is nearly 100 times Earth's radius, so g would not remain 10 m/s² over that distance. Treating it purely as a classical energy-conservation exercise, however, the answer is essentially unchanged from the initial value: **about 3.001 × 10⁸ m/s**.