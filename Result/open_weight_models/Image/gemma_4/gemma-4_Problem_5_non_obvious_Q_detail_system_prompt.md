### Description of the Problem

The problem describes a one-dimensional elastic collision between two blocks, Block A and Block B, moving towards each other on a frictionless surface. 

**Given Data:**
*   **Block A:**
    *   Mass $m_a = 100 \text{ nanograms}$
    *   Initial velocity $v_{a1} = 1.0 \text{ m/s}$
*   **Block B:**
    *   Mass $m_b = 200 \text{ nanograms}$
    *   Initial velocity $v_{b1} = -2.0 \text{ m/s}$
*   **After Collision:**
    *   Final velocity of Block B, $v_{b2} = 1.0 \text{ m/s}$
    *   Final velocity of Block A, $v_{a2} = ?$

### Calculation of Velocity $v_{a2}$

Since there is no friction and the collision is treated as a standard mechanics problem, we use the **Law of Conservation of Momentum**. The total momentum before the collision must equal the total momentum after the collision.

The formula for conservation of momentum is:
$$m_a v_{a1} + m_b v_{b1} = m_a v_{a2} + m_b v_{b2}$$

Substitute the given values into the equation:
$$(100 \text{ ng}) \cdot (1.0 \text{ m/s}) + (200 \text{ ng}) \cdot (-2.0 \text{ m/s}) = (100 \text{ ng}) \cdot v_{a2} + (200 \text{ ng}) \cdot (1.0 \text{ m/s})$$

Simplify the terms:
$$100 - 400 = 100 v_{a2} + 200$$
$$-300 = 100 v_{a2} + 200$$

Subtract 200 from both sides:
$$-500 = 100 v_{a2}$$

Divide by 100:
$$v_{a2} = -5.0 \text{ m/s}$$

**Final Answer:**
The velocity of Block A after the collision is $v_{a2} = -5.0 \text{ m/s}$.

---

### Physical Analysis and Justification

**1. Physical Model Consistency:**
The problem assumes a perfectly elastic collision (or at least one where momentum is conserved). Let's check the conservation of Kinetic Energy ($K$):
*   **Initial Kinetic Energy ($K_1$):**
    $$K_1 = \frac{1}{2} m_a v_{a1}^2 + \frac{1}{2} m_b v_{b1}^2 = \frac{1}{2}(100)(1)^2 + \frac{1}{2}(200)(-2)^2 = 50 + 400 = 450 \text{ units}$$
*   **Final Kinetic Energy ($K_2$):**
    $$K_2 = \frac{1}{2} m_a v_{a2}^2 + \frac{1}{2} m_b v_{b2}^2 = \frac{1}{2}(100)(-5)^2 + \frac{1}{2}(200)(1)^2 = 1250 + 100 = 1350 \text{ units}$$

**2. Conclusion on Physical Justifiability:**
The solution is **not physically justifiable** as a standard elastic or inelastic collision. 
*   **Reason:** The final kinetic energy ($1350$) is significantly higher than the initial kinetic energy ($450$). In a real-world collision without external work, kinetic energy cannot be created. This implies that the provided final velocity for Block B ($v_{b2} = 1.0 \text{ m/s}$) is inconsistent with the laws of physics given the initial conditions. For the collision to be physically possible, the final velocity of Block B would have to be much lower, or an external force would have to be acting on the system.