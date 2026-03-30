+++
date = '2026-03-30T10:44:04+05:30'
title = 'Ml'
+++

> ##### !NOTE
>
> This is Slop

# CHAPTER 1

## 1. Why ML & When to Use It

Traditional programming requires hardcoding rules. ML dynamically learns them.

- **The Sweet Spot:** Problems with long lists of complex rules (e.g., spam filters), fluctuating environments (ML adapts to **concept drift**), and discovering hidden patterns in large datasets (**Data Mining**).
- **Skip ML If:** The problem can be solved with a few simple, static logic rules.

## 2. Classification of ML Systems

Géron categorizes systems across three distinct axes. A single system can be a combination of these (e.g., a supervised, online, model-based system).

### Axis A: Human Supervision

[Image of supervised vs unsupervised machine learning]

- **Supervised:** Training data includes desired solutions (**labels**).
  - _Tasks:_ Classification (discrete), Regression (continuous).
- **Unsupervised:** Training data is unlabeled. The system tries to learn without a teacher.
  - _Tasks:_ Clustering (grouping), Dimensionality Reduction (simplifying data without losing too much info), Anomaly Detection, Association Rule Learning.
- **Semi-supervised:** Partially labeled data (usually a lot of unlabeled, a little labeled). Often a combo of unsupervised + supervised (e.g., Google Photos grouping faces, then you label one).
- **Reinforcement Learning (RL):** An **Agent** observes an environment, acts, and gets **Rewards/Penalties**. It learns the best strategy (**Policy**) to maximize long-term reward.

### Axis B: Batch vs. Online Learning

How does the system handle incoming data?

| Feature        | Batch Learning (Offline)                             | Online Learning (Incremental)                                                                                      |
| :------------- | :--------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **Training**   | Trains on all available data at once.                | Trains incrementally in mini-batches.                                                                              |
| **Resources**  | High compute/time. Requires replacing the old model. | Fast, cheap, immediate.                                                                                            |
| **Use Case**   | Static environments, plenty of compute time.         | Rapidly changing data, limited compute, **Out-of-core learning** (datasets too large for main memory).             |
| **Key Metric** | N/A                                                  | **Learning Rate:** High rate = adapts fast but forgets old data. Low rate = high inertia, less sensitive to noise. |

### Axis C: Instance-based vs. Model-based Learning

How does the system generalize to new, unseen data?

| Type               | How it works                                                                                            | Example                     |
| :----------------- | :------------------------------------------------------------------------------------------------------ | :-------------------------- |
| **Instance-based** | Memorizes training data, then uses a **similarity measure** to compare new instances to memorized ones. | K-Nearest Neighbors (K-NN). |
| **Model-based**    | Detects patterns to build a mathematical model, then uses it to make predictions.                       | Linear Regression.          |

> **The Model-Based Workflow:** > 1. Define a model. 2. Define a **Utility Function** (measures how _good_ the model is) or a **Cost Function** (measures how _bad_ it is). 3. Train (optimize parameters to minimize cost). 4. Predict.

---

## 3. The Main Challenges of Machine Learning

Errors stem from either **Bad Data** or a **Bad Algorithm**.

### Problem A: Bad Data

1.  **Insufficient Quantity:** ML algorithms need _thousands_ to _millions_ of examples. (Recall the "Unreasonable Effectiveness of Data" concept—sometimes a dumb algorithm with massive data beats a smart algorithm with little data).
2.  **Nonrepresentative Data:** If training data doesn't perfectly mirror the production environment, the model won't generalize.
    - _Sampling Noise:_ Nonrepresentative data due to a sample being too small.
    - _Sampling Bias:_ The sample is large enough, but the collection method was flawed (e.g., Landon vs. Roosevelt poll).
3.  **Poor-Quality Data:** Riddled with errors, outliers, and noise. _Fix:_ Clean it up (discard outliers, fill missing features).
4.  **Irrelevant Features:** Garbage in, garbage out.
    - **Feature Engineering:** The most critical step. Involves _Feature Selection_ (choosing the most useful features) and _Feature Extraction_ (combining existing features to produce a more useful one, e.g., using dimensionality reduction).

### Problem B: Bad Algorithms

[Image of overfitting and underfitting in machine learning]

1.  **Overfitting:** The model performs perfectly on training data but bombs on new data. It has memorized the noise.
    - _Cause:_ Model is too complex relative to the amount/noisiness of the training data.
    - _Solutions:_ Simplify the model (fewer parameters), gather more data, clean the data, or **Constrain the model (Regularization)**.
      - _Note:_ The amount of regularization applied is controlled by a **Hyperparameter** (a parameter of the learning algorithm, not the model itself, set _prior_ to training).
2.  **Underfitting:** The model is too simple to learn the underlying structure of the data.
    - _Cause:_ Using a linear model for highly non-linear data.
    - _Solutions:_ Select a more powerful model, feed better features (feature engineering), reduce regularization constraints.

---

## 4. Testing, Validating, and Data Mismatch

You shouldn't train a model and blindly deploy it. You need a rigorous testing framework.

- **Train/Test Split:** Typically 80% train, 20% test. The error on the test set is the **Generalization Error (out-of-sample error)**.
- **The Hyperparameter Trap:** If you tweak your hyperparameters to perfectly fit the test set, you have _overfitted the test set_. The model will fail in production.
- **The Solution: The Validation Set:** 1. Train multiple models with various hyperparameters on the **Training Set**. 2. Select the model that performs best on the **Validation Set** (also called dev set/holdout set). 3. Run a final, single test on the **Test Set** to estimate the generalization error.
  - _Exam trick:_ If the validation set is too small, use **Cross-Validation** (train on multiple subsets, validate on the remaining parts).
- **Data Mismatch:** What if your training data (e.g., easy-to-scrape web images) is different from your target data (e.g., blurry mobile app photos)?
  - Géron introduces the **Train-Dev Set**: A subset carved out from the _training data_.
  - _How to use it:_ If the model performs well on the training set but poorly on the train-dev set = **Overfitting**. If it performs well on both the train set and train-dev set, but poorly on the validation set = **Data Mismatch**.

---

# Chapter 3: Classification

**Source:** _Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (A. Géron)_

## 1. The Starting Point: MNIST & Binary Classification

- **MNIST Dataset:** The "Hello World" of machine learning. 70,000 images of handwritten digits (0-9).
- **Training a Binary Classifier:** Before jumping to 10 digits, simplify. Build a "5-detector" (Output: _5_ or _Not-5_).
- **The Algorithm:** Géron uses `SGDClassifier` (Stochastic Gradient Descent) because it handles massive datasets efficiently by processing training instances independently.

---

## 2. Performance Measures (⚠️ High Exam Probability)

Evaluating a classifier is significantly trickier than evaluating a regressor. This section is the core of the chapter.

### A. Measuring Accuracy Using Cross-Validation

- **The Trap of Accuracy:** Accuracy is simply the ratio of correct predictions. For **skewed datasets** (imbalanced classes), accuracy is a terrible measure.
- _Intuition:_ If only 10% of your images are 5s, a "dumb" classifier that _always_ guesses "Not-5" will have 90% accuracy. It learned nothing, but looks great on paper.

### B. The Confusion Matrix

The ultimate tool for classification performance. It counts how many times instances of class `A` are classified as class `B`.

- **True Negatives (TN):** Correctly predicted _Not-5_.
- **False Positives (FP):** Predicted _5_, but it was _Not-5_ (Type I Error).
- **False Negatives (FN):** Predicted _Not-5_, but it was a _5_ (Type II Error).
- **True Positives (TP):** Correctly predicted _5_.

### C. Precision, Recall, and the `F_1` Score

Instead of looking at the whole matrix, we extract concise metrics.

1.  **Precision (Accuracy of the positive predictions):** Out of all the times the model yelled "It's a 5!", how often was it right?
    `Precision = .rac{TP}{TP + FP}`
2.  **Recall (Sensitivity / True Positive Rate):** Out of all the _actual_ 5s in the dataset, how many did the model find?
    `Recall = .rac{TP}{TP + FN}`
3.  **`F_1` Score:** The harmonic mean of precision and recall. It heavily punishes extreme values—you only get a high `F_1` score if _both_ recall and precision are high.
    `F_1 = .rac{2}{.rac{1}{Precision} + .rac{1}{Recall}} = 2 * .rac{Precision * Recall}{Precision + Recall}`

### D. The Precision/Recall Trade-off

> **Intuition Check:** You cannot have perfect precision and perfect recall. It is a slider.

- **High Precision, Low Recall:** "I only raise my hand if I am 100% sure it's a 5." (You miss a lot of messy 5s, but you never accidentally call a 3 a 5).
- **High Recall, Low Precision:** "I raise my hand if it even slightly looks like a 5." (You catch every single 5, but you also falsely flag a bunch of 8s and 3s).
- **How to adjust:** You change the **decision threshold**. `Scikit-Learn` doesn't let you set this directly, but you can access the decision scores using `decision_function()` and apply your own threshold.

### E. The ROC Curve (Receiver Operating Characteristic)

Plots the **True Positive Rate (Recall)** against the **False Positive Rate (FPR)**.

- **FPR:** The ratio of negative instances incorrectly classified as positive.
- **AUC (Area Under the Curve):** A perfect classifier has an ROC AUC equal to 1. A purely random classifier has an ROC AUC equal to 0.5.

| Metric        | When to use it? (Classic Exam Question)                                                                    |
| :------------ | :--------------------------------------------------------------------------------------------------------- |
| **PR Curve**  | Use when the positive class is **rare**, or when you care more about False Positives than False Negatives. |
| **ROC Curve** | Use strictly when you have roughly equal numbers of positive and negative classes.                         |

---

## 3. Beyond Binary: Multiclass Classification

Algorithms like Random Forest and Naive Bayes can handle multiple classes natively. Others (like SVM or Linear classifiers) are strictly binary. To do multiclass with binary algorithms, we use two strategies:

| Strategy                  | How it works                                                                                                           | Pros / Cons                                                                                                                |
| :------------------------ | :--------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **OvR (One-versus-Rest)** | Train 10 binary classifiers (one for 0, one for 1...). Keep the one with the highest decision score.                   | **Pro:** Default for most algorithms. Efficient. <br> **Con:** Classifiers are trained on the whole dataset.               |
| **OvO (One-versus-One)**  | Train a classifier for every pair of digits (0s vs 1s, 0s vs 2s). Requires `N * (N-1) / 2` classifiers (45 for MNIST). | **Pro:** Each classifier is only trained on a small subset of data. **Best for algorithms that scale poorly (like SVMs).** |

---

## 4. Error Analysis

Once you have a model, you analyze its mistakes to improve it.

1.  **Normalize the Confusion Matrix:** Divide each value by the number of images in the corresponding class. This prevents classes with lots of data from looking artificially bad.
2.  **Visualize:** Fill the diagonal with zeros to highlight the errors strictly.
3.  **Act:** If the model confuses 3s and 5s, you might preprocess the images to center them better, or add synthetic data of shifted 3s and 5s.

---

## 5. Advanced Output Types

Don't confuse these two—professors love testing the distinction.

- **Multilabel Classification:** Predicting multiple binary tags for a single instance.
  - _Example:_ A face recognition system sees a photo of Alice and Bob. It outputs `[1, 0, 1]` (Alice=Yes, Charlie=No, Bob=Yes).
  - _Evaluation:_ Compute the `F_1` score for each label, then average them.
- **Multioutput Classification (Multioutput-Multiclass):** A generalization of multilabel where each label can have _multiple classes_ (not just binary).
  - _Example:_ Removing noise from an image. The input is a noisy digit. The output is an array of 784 pixel intensities, where each pixel (label) can be any value from 0 to 255 (multiclass).

---

# Chapter 4: Training Models

> 💡 **The Core Theme:** You are opening the "black box" of Machine Learning. Instead of just calling `.fit()`, you are learning _how_ the algorithms actually find the best parameters.

## 1. Linear Regression

**Goal:** Predict a continuous value by fitting a straight line (or hyperplane) to your data.
**Model Prediction:** `.at{y} = .heta_0 + .heta_1 x_1 + ... + .heta_n x_n` (or vectorized: `.at{y} = .heta^T .athbf{x}`)
**Cost Function:** Mean Squared Error (MSE). We want to find the `.heta` (weights) that minimize this.

### The Normal Equation

Instead of iterating, we use a math formula to jump straight to the exact minimum.

- **Formula:** `.at{.heta} = (.athbf{X}^T .athbf{X})^{-1} .athbf{X}^T .athbf{y}`
- **Intuition:** It's like solving a puzzle instantly using a master key instead of trying every combination.
- **Computational Complexity:** Matrix inversion is slow. It is `O(n^{2.4})` to `O(n^3)` where `n` is the number of features.
  - _Exam Tip:_ **Great** for a small number of features (`n < 100,000`). **Terrible** if you have too many features. However, it handles large numbers of _instances_ (rows) very well!

---

## 2. Gradient Descent (GD)

> 💡 **Intuition:** Imagine you are blindfolded at the top of a mountain. To get to the bottom, you feel the slope of the ground with your feet and take a step in the steepest downward direction.

- **Learning Rate (`.ta`):** The size of your step. Too small = takes forever. Too big = you jump across the valley and diverge.
- **Requirement:** You **must** scale your features (e.g., StandardScaler) before using GD, or it will take a long, erratic path.
- **The Math:** `.heta^{.ext{next step}} = .heta - .ta .abla_{.heta} .ext{MSE}(.heta)`

### The 3 Flavors of Gradient Descent

| Feature                   | Batch GD                  | Stochastic GD (SGD)                     | Mini-batch GD                     |
| :------------------------ | :------------------------ | :-------------------------------------- | :-------------------------------- |
| **Data per step**         | The _entire_ dataset.     | One _single random_ instance.           | A small random subset (e.g., 32). |
| **Speed per step**        | Very slow.                | Very fast.                              | Fast (can use GPU optimization).  |
| **Path to minimum**       | Smooth and direct.        | Erratic, bounces around.                | Less erratic than SGD.            |
| **Escapes local minima?** | No.                       | Yes, because of its random bouncing.    | Yes, better than Batch.           |
| **Final accuracy**        | Stops exactly at minimum. | Never settles, needs learning schedule. | Close to minimum.                 |

---

## 3. Polynomial Regression

What if your data isn't a straight line? You can still use Linear Regression!

- **How it works:** You add powers of your original features as _new_ features. (e.g., if you have `x`, you add `x^2`, `x^3`, etc.).
- **Exam Trap:** Degree `d` polynomial expands features exponentially. A degree 3 polynomial on 10 features creates 286 features.

---

## 4. Learning Curves

Plots of the model's performance on the **training set** and **validation set** as a function of the training set size.

- **Underfitting:** Both curves plateau at a high error rate. They are close together.
  - _Fix:_ Adding more data won't help. You need a more complex model or better features.
- **Overfitting:** Training error is low, but validation error is high. There is a distinct **gap** between the two curves.
  - _Fix:_ Get more training data or add Regularization!

---

## 5. Regularized Linear Models

> 💡 **Intuition:** "Keep it simple, stupid." Regularization forces the learning algorithm to not only fit the data but also keep the model weights (`.heta`) as small as possible. This prevents overfitting.

_(Note: We generally do not regularize the bias term `.heta_0`)_

### Ridge Regression (L2 Regularization)

- **Mechanism:** Adds the squared value of the weights to the cost function: `.lpha .um_{i=1}^{n} .heta_i^2`
- **Effect:** Keeps weights small but rarely makes them exactly zero. Good default.

### Lasso Regression (L1 Regularization)

- **Mechanism:** Adds the absolute value of the weights to the cost function: `.lpha .um_{i=1}^{n} |.heta_i|`
- **Superpower (Exam Gold):** It automatically performs **feature selection**. It forces the weights of useless features to exactly `0`.

### Elastic Net

- A middle ground between Ridge and Lasso, controlled by a mix ratio `r`.
- **When to use what?**
  - Default `->` Ridge.
  - Suspect only a few features are useful? `->` Lasso or Elastic Net.
  - Features > Instances, or highly correlated features? `->` Elastic Net (Lasso acts erratically here).

### Early Stopping

- **Intuition:** The "beautiful free lunch." Just stop training the moment the validation error reaches its minimum and starts going back up.

---

## 6. Logistic Regression

[Image of Logistic Regression Sigmoid curve]

Despite the name, this is a **classification** algorithm.

- **Estimating Probabilities:** It computes a weighted sum of inputs (just like Linear Regression), but instead of outputting the result directly, it passes it through the **Sigmoid function (`.igma`)**.
- **Equation:** `.at{p} = .igma(.heta^T .athbf{x})`, where `.igma(t) = .rac{1}{1 + e^{-t}}`
  - Outputs a value between `0` and `1`.
  - Predicts class `1` if `.at{p} >= 0.5` (meaning `.heta^T .athbf{x} >= 0`).
- **Training and Cost Function:** It uses **Log Loss** (Binary Cross-Entropy).
  - _Exam Fact:_ There is **no Normal Equation** (closed-form solution) for Logistic Regression. You _must_ use Gradient Descent. Luckily, the cost function is convex (bowl-shaped), so GD is guaranteed to find the global minimum.
- **Decision Boundaries:** The line (or hyperplane) where the estimated probability is exactly 50%.

---

## 7. Softmax Regression (Multinomial Logistic Regression)

Logistic Regression is strictly binary (Yes/No). What if you have multiple classes (e.g., Red, Blue, Green)?

- **Intuition:** Instead of training multiple binary classifiers, Softmax does it all at once.
- **How it works:** 1. Computes a score `s_k(.athbf{x})` for every class `k`. 2. Applies the **Softmax function** to estimate the probability of each class (it takes the exponentials of the scores and normalizes them so they add up to 1).
- **Prediction:** Simply picks the class with the highest estimated probability.
- **Cost Function:** Uses **Cross-Entropy**. It penalizes models that estimate a low probability for the true target class.

---

## **Final Review Step:** Before the exam, make sure you can visualize the shape of the cost function (MSE vs Log Loss) and the difference between L1 (diamond shape) and L2 (circular shape) regularization penalties!
