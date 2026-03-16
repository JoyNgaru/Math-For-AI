import numpy as np
import matplotlib.pyplot as plt

# Define the matrix
A = np.array([[1, 2],
              [5, 4]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# --- Plot 1: Heatmap of the matrix ---
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(A, cmap='viridis', interpolation='nearest')
plt.colorbar(label="Value")
plt.title("Matrix A Heatmap")
for (i, j), val in np.ndenumerate(A):
    plt.text(j, i, f"{val}", ha='center', va='center', color='white')

# --- Plot 2: Eigenvectors scaled by eigenvalues ---
plt.subplot(1, 2, 2)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Plot each eigenvector
for i in range(len(eigenvalues)):
    vec = eigenvectors[:, i]
    val = eigenvalues[i]
    plt.quiver(0, 0, vec[0]*val, vec[1]*val,
               angles='xy', scale_units='xy', scale=1,
               color=['red','blue'][i],
               label=f"Eigenvalue {val:.2f}")

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Eigenvectors scaled by Eigenvalues")
plt.legend()

plt.tight_layout()
plt.show()
