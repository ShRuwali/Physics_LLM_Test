analysisWe have a pendulum. But it's a simple pendulum with a solid sphere bob (radius L/2 =1 m). Wait, the string length L is 2m, so the bob radius is L/2 = 1m. The string mass negligible. For small oscillations, the time period formula: T = 2π sqrt(L_eff / g). But we need moment of inertia of the sphere about the pivot. The center of mass is at distance L. Because the string attaches at the center of sphere? Or at a point on sphere? Clarify: "solid sphere of mass (m) 2kg and a string of negligible mass. The distance between the point of support and the center of the spherical mass is L = 2 meters, and the radius of the solid sphere is (L/2)=1 meter. The acceleration due to gravity is 10 m/s^2 at the location. Find the time period of this pendulum for small displacements."

Thus the bob is a solid sphere. The pivot is at a point a distance of L (2m) from its center, presumably the string is attached at the top of the sphere? Usually pendulum has string attached to the center? But they specify center of mass distance L from support. So pivot at distance L from center.

Question: For a physical pendulum (rigid body) with moment of inertia I about pivot at some distance from center. For small angles, period T = 2π sqrt( I / (m g d) ), where d is distance from pivot to center of mass.

But in case of simple pendulum with massless rod and point mass, the pendulum is treated like a simple pendulum with I= m L^2, giving T = 2π sqrt(L/g). But here we have a sphere with finite radius. But pivot is at distance L above its center. The moment of inertia around pivot is I = I_cm + m L^2. I_cm for a solid sphere rotating about an axis through its center perpendicular to the line from pivot is(2/5)mR^2 where R=1m. So I_cm = (2/5)*2*1^2 = (4/5) kg.m^2? Wait m=2 kg, so I_cm= (2/5)*m*R^2 = 0.4*2*1^2? Actually 2/5 * m * R^2 = (0.4)*2*1=0.8 kg.m^2? Let's compute: 0.4 * 2 = 0.8 kg.m^2.

Thus I_pivot = I_cm + mL^2 = 0.8 + 2*(2^2) = 0.8 + 8 = 8.8 kg.m^2.

But recall for simple pendulum (point mass) moment of inertia about pivot is m L^2. That would be 8 kg.m^2. So this is slightly bigger due to distributed mass.

Now use small-angle period for physical pendulum: T = 2π sqrt(I / (m d g)), with d = L? Actually the distance from pivot to center of mass is L. So d = L. So T = 2π sqrt( I / (m L g) ). Plug values: I = 8.8, m*L g = 2*2*10 = 40. So I/(mLg) = 8.8/40 = 0.22. sqrt = sqrt(0.22) ≈ 0.4690. Multiply by 2π ≈ 6.283 * 0.4690 = 2.948s? Wait 6.283*0.469 ≈ 2.948. So T ≈ 2.95 s.

Alternatively, we could compute simple pendulum with L=2, g=10, T=2π sqrt(2/10)=2π sqrt(0.2)=2π*0.4472=2.807. So difference is about ~5%.

Therefore answer ~2.95 seconds.

We need to present answer maybe 2.95 s.

We should explain steps. Provide calculations.

Let's produce final.assistantfinalFor a rigid body pendulum the small‑angle period is

\[
T = 2\pi \sqrt{\frac{I}{m\,d\,g}}
\]

where  

* \(I\) – moment of inertia of the body about the pivot,  
* \(m\) – mass of the body,  
* \(d\) – distance from the pivot to the centre of mass,  
* \(g\) – gravitational acceleration.

---

### 1.  Geometry and mass‑distribution

* Mass \(m = 2 \text{ kg}\).  
* Centre‑of‑mass distance to the pivot \(d = L = 2\ \text{m}\).  
* The sphere radius is \(R = L/2 = 1 \text{ m}\).

The moment of inertia of a solid sphere about an axis through its centre is

\[
I_{\text{cm}} = \frac{2}{5}\,m R^{2}.
\]

With \(m = 2\ \text{kg}\) and \(R = 1\ \text{m}\):

\[
I_{\text{cm}} = \frac{2}{5}\times 2 \times 1^{2}
               = 0.8 \ \text{kg}\,\text{m}^2.
\]

By the parallel‑axis theorem the moment of inertia about the pivot is

\[
I = I_{\text{cm}} + m d^{2}
  = 0.8 + 2 \times (2)^2
  = 0.8 + 8
  = 8.8 \ \text{kg}\,\text{m}^2.
\]

---

### 2.  Time‑period calculation

\[
T = 2\pi \sqrt{\frac{I}{m\,d\,g}}
   = 2\pi \sqrt{\frac{8.8}{2 \times 2 \times 10}}
   = 2\pi \sqrt{\frac{8.8}{40}}
   = 2\pi \sqrt{0.22}.
\]

\[
\sqrt{0.22}\approx 0.469,\qquad
T \approx 2\pi \times 0.469 \approx 2.95\ \text{s}.
\]

---

\[
\boxed{T \approx 3.0 \text{ seconds (for small oscillations).}}
\]