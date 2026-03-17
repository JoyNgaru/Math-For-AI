import numpy as np
import matplotlib.pyplot as plt

def perform_svd(A):
    # Perform SVD
    U, S, VT = np.linalg.svd(A)
    return U, S, VT

def plot_singular_values(S):
    plt.figure()
    plt.plot(range(1, len(S) + 1), S, 'o-', label="Singular Values")
    plt.xlabel("Index")
    plt.ylabel("Singular Value")
    plt.title("Singular Values of the Matrix")
    plt.grid()
    plt.legend()
    plt.show()

def reconstruct_with_truncation(U, S, VT, k):
    # Build rectangular Sigma with top k singular values
    Sigma_k = np.zeros((U.shape[0], VT.shape[0]))
    np.fill_diagonal(Sigma_k, S[:k])
    return U @ Sigma_k @ VT

def visualize_approximations(A, U, S, VT):
    ranks = [1, 2]  # Different values of k to test
    plt.figure(figsize=(10, 5))
    for i, k in enumerate(ranks, start=1):
        A_approx = reconstruct_with_truncation(U, S, VT, k)
        plt.subplot(1, len(ranks), i)
        plt.imshow(A_approx, cmap='viridis', aspect='auto')
        plt.colorbar()
        plt.title(f"Approximation with k={k}")
    plt.tight_layout()
    plt.show()

# Test the implementation
if __name__ == "__main__":
    # Define the matrix A
    A = np.array([[3, 2, 2],
                  [2, 3, -2]])

    # Perform SVD
    U, S, VT = perform_svd(A)

    # Build full rectangular Sigma
    Sigma = np.zeros((U.shape[0], VT.shape[0]))
    np.fill_diagonal(Sigma, S)

    # Reconstruct A using all singular values
    A_reconstructed = U @ Sigma @ VT

    # Print results
    print("Original Matrix A:")
    print(A)
    print("\nMatrix U:")
    print(U)
    print("\nSingular Values Σ:")
    print(S)
    print("\nMatrix VT:")
    print(VT)
    print("\nReconstructed Matrix A:")
    print(A_reconstructed)
    print("\nCheck reconstruction:", np.allclose(A, A_reconstructed))

    # Visualize singular values
    plot_singular_values(S)

    # Visualize approximations with truncated SVD
    visualize_approximations(A, U, S, VT)
