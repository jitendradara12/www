+++
date = '2026-05-18T16:04:21+05:30'
title = 'Ml'
+++

# **SVM**:

Capable of...

- linear
- nonlinear
- regression
- outlier detection

SVM = fitting the widest possible street (large margin classification)

# Linear SVM

### 1. Hard margin

- only works if the data is linearly separable
- sensitive to outliers

### 2. Soft margin

```python
svm_clf = Pipeline([
  ("scaler", StandardScaler()),
  ("linear_svc", LinearSVC(C=1, loss="hinge")),
])
svm_clf.fit(X, y)
```

# Nonlinear SVM (polynomial)

Add more features to make data linearly separable.

```python
X, y = make_moons(n_samples=100, noise=0.15) polynomial_svm_clf = Pipeline([
  ("poly_features", PolynomialFeatures(degree=3)),# <--- add this line
  ("scaler", StandardScaler()),
  ("svm_clf", LinearSVC(C=10, loss="hinge"))
]) polynomial_svm_clf.fit(X, y)
```

**Disadvantage**: too slow  
**Solution**: kernel trick (Polynomial kernel,RBF kernel)

# Polynomial kernel

("svm_clf", SVC(`kernel="poly"`, degree=3, coef0=1, C=5))

# Similarity features

> Gaussian Radial Basis Function

$$\phi_{\gamma}(\mathbf{x}, \ell) = \exp\left(-\gamma\|\mathbf{x} - \ell\|^2\right)$$

but we don't know the landmarks so we have to take every instance as one means `m features for m instances`

# Gaussian RBF kernel

("svm_clf", SVC(`kernel="rbf"`, gamma=5, C=0.001))
