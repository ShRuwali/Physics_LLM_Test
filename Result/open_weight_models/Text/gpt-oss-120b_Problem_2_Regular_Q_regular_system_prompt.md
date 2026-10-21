**Solution Outline**

The pendulum is a **physical pendulum**: the bob is not a point mass but a solid sphere that can rotate about its own centre while its centre of mass describes a circular arc of radius  

\[
d = L = 2\;\text{m}
\]

from the point of support.

For a physical pendulum the small‑angle period is  

\[
T = 2\pi \sqrt{\frac{I_{\text{pivot}}}{m g d}}
\]

where  

* \(m\) – mass of the bob,  
* \(g\) – acceleration of gravity,  
* \(d\) – distance from the pivot to the centre of mass,  
* \(I_{\text{pivot}}\) – moment of inertia of the bob about the pivot point.

---

### 1. Moment of inertia about the centre of the sphere  

A solid sphere of mass \(m\) and radius \(r\) has  

\[
I_{\text{cm}} = \frac{2}{5} m r^{2}
\]

Given  

* \(m = 2\;\text{kg}\)  
* \(r = \dfrac{L}{2}=1\;\text{m}\)

\[
I_{\text{cm}} = \frac{2}{5}\,(2)\,(1)^{2}=0.8\;\text{kg·m}^{2}
\]

---

### 2. Moment of inertia about the pivot (parallel‑axis theorem)

\[
I_{\text{pivot}} = I_{\text{cm}} + m d^{2}
\]

with \(d = L = 2\;\text{m}\):

\[
I_{\text{pivot}} = 0.8 + (2)(2)^{2}=0.8 + 8 = 8.8\;\text{kg·m}^{2}
\]

---

### 3. Period of small oscillations

\[
T = 2\pi \sqrt{\frac{I_{\text{pivot}}}{m g d}}
     = 2\pi \sqrt{\frac{8.8}{(2)(10)(2)}}
     = 2\pi \sqrt{\frac{8.8}{40}}
\]

\[
\frac{8.8}{40}=0.22 \qquad\Rightarrow\qquad \sqrt{0.22}\approx 0.469
\]

\[
T \approx 2\pi \times 0.469 \approx 2.95\;\text{s}
\]

---

### 4. Comparison with an ideal simple pendulum

If the bob were a point mass the period would be  

\[
T_{0}=2\pi\sqrt{\frac{L}{g}} = 2\pi\sqrt{\frac{2}{10}} \approx 2.81\;\text{s}
\]

The rotational inertia of the solid sphere makes the actual period slightly longer (about 5 % increase).

---

**Answer:** The period of the pendulum for small displacements is approximately **\(T \approx 3.0\ \text{s}\)** (more precisely, \(2.95\ \text{s}\)).