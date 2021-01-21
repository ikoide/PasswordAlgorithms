# PasswordAlgorithms
## 2020-2021 Science Project
#### Ian Koide

The effect of a passwords makeup on the time it takes to crack with a specific algorithm.

## Variables

- IV₁ - The password makeup (characters used and length)
  - Length
    - 1, 2, 4, 5, 6, 7, 8
  - Makeup
    - Digits
    - Lowercase Letters
    - Uppercase Letters
    - All Letters
    - Letters and Digits
    - All Characters
- IV₂ - The algorithm used to crack the password.
  - Guessing
  - Smart Guessing
  - Brute Force
  - Dictionary
- DV - Time it takes to crack the password.

## Results

When the length of the password is less than or equal to 5, 1000 iterations are run. If the password is between 6 and 8 characters, 250 iterations are run.

Brute Force | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
Digits | 3.7827491760253905e-06 | 3.8814783096313474e-05 | 0.00020866656303405762 | 0.0014812734127044678 | 0.015716334342956544 | 0.1538258924484253 | 287 | 287 | 272 | 276 | 269
Lowercase Letters | 1.9974708557128907e-05 | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269
Uppercase Letters | 3.2689809799194334e-05 | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269
All Letters | 2.3496150970458984e-05 | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269
All Characters | 1.4669179916381836e-05 | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269