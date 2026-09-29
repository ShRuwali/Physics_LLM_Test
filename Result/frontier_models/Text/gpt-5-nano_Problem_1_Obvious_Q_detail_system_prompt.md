This problem as stated is not physically consistent. Two issues:
- The coefficient of kinetic friction cannot be negative; mu_k should be ≥ 0. A negative mu_k would imply friction acts in the same direction as motion, which is not physically possible for dry friction.
- The gravitational acceleration should act downward. Saying it is upward reverses the direction of the weight, which is also incorrect.

If we fix the physical signs and take a physically sensible mu_k, we can still compute the motion. The acceleration along the plane is
a = g (sin theta − mu_k cos theta)
where g = 10 m/s^2, theta = 30 degrees, sin 30 = 0.5, cos 30 ≈ 0.866.

Case A (physically sensible mu_k = 0.5):
- a = 10 [0.5 − 0.5 × 0.866] ≈ 10 × 0.066987 ≈ 0.6699 m/s^2
- starting from rest, s = 5 m, so s = 0.5 a t^2 → t = sqrt(2s / a) = sqrt(10 / 0.6699) ≈ sqrt(14.93) ≈ 3.86 s

Case B (using the problem’s given, but physically invalid, mu_k = −0.5):
- a = 10 [0.5 − (−0.5) × 0.866] ≈ 10 × 0.9330 ≈ 9.33 m/s^2
- t = sqrt(10 / 9.33) ≈ sqrt(1.07) ≈ 1.04 s
- Note: This result corresponds to friction that would accelerate the block, which is not physically possible.

Bottom line:
- The physically meaningful answer (with a nonnegative friction coefficient) is about 3.9 seconds.
- The given negative mu_k and the “upward g” are inconsistent with real physics; the problem as stated cannot be physically accurate. If you want, I can reframe the problem with mu_k ≥ 0 and g downward and redo the calculation, or explain how the numbers would change for other mu_k values.