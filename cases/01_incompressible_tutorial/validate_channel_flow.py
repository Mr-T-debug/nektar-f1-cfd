# ==========================================================
# Nektar++ CFD Project
# Case 01: Incompressible Channel Flow
#
# Objective:
# Compare the numerical velocity profile against the
# analytical solution for fully developed channel flow.
# ==========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ----------------------------------------------------------
# 1. Import numerical results
# ----------------------------------------------------------

data = pd.read_csv("channel_velocity_profile.csv")

# Extract the vertical coordinates and horizontal velocity
y = data["Points:1"].to_numpy()
u_numerical = data["u"].to_numpy()


# ----------------------------------------------------------
# 2. Calculate analytical solution
# ----------------------------------------------------------

# Fully developed channel flow:
# u(y) = y(1-y)

u_analytical = y * (1 - y)


# ----------------------------------------------------------
# 3. Calculate numerical errors
# ----------------------------------------------------------

error = u_numerical - u_analytical

RMSE = np.sqrt(np.mean(error**2))
max_error = np.max(np.abs(error))

print("======================================")
print("NEKTAR++ CHANNEL FLOW VALIDATION")
print("======================================")
print(f"Number of sampling points: {len(y)}")
print(f"RMSE: {RMSE:.6e}")
print(f"Maximum absolute error: {max_error:.6e}")


# ----------------------------------------------------------
# 4. Plot numerical vs analytical solution
# ----------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    u_numerical,
    y,
    label="Nektar++ CFD",
    linewidth=2
)

plt.plot(
    u_analytical,
    y,
    "--",
    label="Analytical solution",
    linewidth=2
)

plt.xlabel("Streamwise velocity, u")
plt.ylabel("Vertical position, y")
plt.title("Incompressible Channel Flow: CFD Validation")

plt.legend()
plt.grid(True)
plt.tight_layout()

# Save figure
plt.savefig("channel_flow_validation.png", dpi=300)

plt.show()


# ----------------------------------------------------------
# 5. Plot numerical error
# ----------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(y, error, linewidth=2)

plt.xlabel("Vertical position, y")
plt.ylabel("Numerical error")
plt.title("Channel Flow: Numerical Error")

plt.grid(True)
plt.tight_layout()

plt.savefig("channel_flow_error.png", dpi=300)

plt.show()