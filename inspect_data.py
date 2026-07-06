import numpy as np

data = np.load("data/processed/burnout_processed.npz", allow_pickle=True)

print("Arrays inside:", data.files)

X_train = data["X_train"]
print("X_train shape:", X_train.shape, X_train.dtype)
print(X_train[:5])

y_train = data["y_train"]
print("\ny_train shape:", y_train.shape, y_train.dtype)
print(y_train[:20])