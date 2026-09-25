# Physical Pendulum Solution

Since the sphere's radius (1 m) is not small compared to the string length, we cannot treat this as a simple point-mass pendulum. We must use the **physical pendulum** formula.

## Setting Up

**Time period formula:** T = 2π √(I / mgd)

where:
- I = moment of inertia about the pivot point
- d = distance from pivot to center of mass = L = 2 m
- m = 2 kg, g = 10 m/s², sphere radius R = L/2 = 1 m

## Moment of Inertia (Parallel Axis Theorem)

I = (2/5)mR² + md²

I = (2/5)(2)(1)² + (2)(2)²

I = 0.8 + 8 = 8.8 kg·m²

## Calculating the Period

T = 2π √(I / mgd)

T = 2π √(8.8 / (2 × 10 × 2))

T = 2π √(8.8 / 40)

T = 2π √(0.22)

T = 2π × 0.469

**T ≈ 2.95 seconds**

## Note

If we had (incorrectly) treated this as a simple pendulum, we would get T = 2π√(2/10) ≈ 2.81 s. The finite size of the sphere increases the period slightly because of its rotational inertia about its own center.