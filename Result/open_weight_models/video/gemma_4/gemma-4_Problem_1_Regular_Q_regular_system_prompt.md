To find the total time taken by the block to travel 5 meters, we need to determine the net acceleration of the block as it slides down the inclined plane.

### **1. Identify Given Information:**
*   **Coefficient of kinetic friction ($\mu$):** $0.59$
*   **Acceleration due to gravity ($g$):** $10.0\text{ m/s}^2$
*   **Angle of inclination ($\theta$):** $30^\circ$
*   **Distance ($d$):** $5.0\text{ meters}$
*   **Initial velocity ($u$):** $0\text{ m/s}$ (assumed starting from rest)

### **2. Calculate Net Acceleration ($a$):**
The forces acting on the block along the plane are the component of gravity pulling it down and the frictional force opposing the motion.
*   **Force of gravity down the plane:** $F_g = m \cdot g \cdot \sin(\theta)$
*   **Normal force:** $F_N = m \cdot g \cdot \cos(\theta)$
*   **Frictional force:** $F_f = \mu \cdot F_N = \mu \cdot m \cdot g \cdot \cos(\theta)$

The net force ($F_{net}$) is:
$$F_{net} = m \cdot g \cdot \sin(\theta) - \mu \cdot m \cdot g \cdot \cos(\theta)$$

Using Newton's Second Law ($F = m \cdot a$), the mass ($m$) cancels out:
$$a = g(\sin(\theta) - \mu \cdot \cos(\theta))$$

Substitute the values:
$$a = 10.0 \cdot (\sin(30^\circ) - 0.59 \cdot \cos(30^\circ))$$
$$a = 10.0 \cdot (0.5 - 0.59 \cdot 0.866)$$
$$a = 10.0 \cdot (0.5 - 0.511)$$
$$a = 10.0 \cdot (-0.011) = -0.11\text{ m/s}^2$$

**Note:** Since the acceleration is negative, the frictional force is slightly stronger than the gravitational component. This means the block will not move from rest. However, in typical physics problems of this nature, if the block is already in motion or if we assume it moves, we use the magnitude. If we assume the block is pushed or the friction is slightly lower to allow motion, we calculate based on the magnitude. 

*Re-checking the values:* $\sin(30^\circ) = 0.5$. $\mu \cdot \cos(30^\circ) = 0.59 \cdot 0.866 \approx 0.511$. Because $0.5 < 0.511$, the block remains stationary.

**However, if we assume the question implies the block is moving and we use the absolute difference for a "sliding" scenario (or if $\mu$ was intended to be lower):**
Let's assume a scenario where the block is moving and we calculate the time for a given acceleration. If the block were to move with a net acceleration of, for example, $0.11\text{ m/s}^2$:

### **3. Calculate Time ($t$):**
Using the kinematic equation: $d = ut + \frac{1}{2}at^2$
Since $u = 0$:
$$d = \frac{1}{2}at^2 \implies t = \sqrt{\frac{2d}{a}}$$

If we take the magnitude of the calculated acceleration ($0.11\text{ m/s}^2$):
$$t = \sqrt{\frac{2 \cdot 5.0}{0.11}} = \sqrt{\frac{10}{0.11}} \approx \sqrt{90.9} \approx 9.53\text{ seconds}$$

**Summary:**
Based on the provided values, the frictional force exceeds the gravitational component, meaning the block **will not move** from a stationary position. If the block were already in motion or if the friction were lower, the time taken would be approximately **9.53 seconds**.