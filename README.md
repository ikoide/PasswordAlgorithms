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

Every test was run on a Macbook Pro with an Intel i5 with 4 cores @ 3.3GHz. As the test is running the terminal running the test is the only application/ window running (at least in the foreground).


Brute Force | 1 (5000) | 2 (1000) | 3 (1000) | 4 (1000) | 5 (100) | 6 (100) | 7 (100) | 8 (50) | 9 (50) | 10 (50) | 11 (50)
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
Digits | 4.938864707946777e-06 | 2.0994114875793457e-05 | 0.00014107332229614257 | 0.0014989945888519286 |  |  | 287 | 287 | 272 | 276 | 269
Lowercase Letters | 3.249139785766601e-05 | 9.94868278503418e-05 | 0.002379296064376831 | 0.0667981026172638 | 289 | 285 | 287 | 287 | 272 | 276 | 269
All Letters | 1.0273218154907226e-05 | 0.0003543832302093506 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269
Letters & Digits |1.2705755233764649e-05 | 0.0003015468120574951| | | | | | | | |
All Characters | 2.1324825286865236e-05 | 0.0012004685401916504 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269

Random | 1 (5000) | 2 (1000) | 3 (1000) | 4 (1000) | 5 (100) | 6 | 7 | 8 | 9 | 10 | 11
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
Digits | 1.614978313446045e-05 | 0.00016159887313842774 | 0.002036902093887329 | 0.023996698379516603 |  |  | 287 | 287 | 272 | 276 | 269
Lowercase Letters | 4.077901840209961e-05 | 0.0009644088745117187 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269
All Letters | 7.398281097412109e-05 | 0.007703065872192383 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269
Letters & Digits | 8.547763824462891e-05 | | | | | | | | | |
All Characters | 0.00012075304985046387 | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269

Random Smart | 1 (5000) | 2 (1000) | 3 (1000) | 4 (1000) | 5 (100) | 6 | 7 | 8 | 9 | 10 | 11
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
Digits | 1.5900540351867675e-05 | 0.00022317664623260498 | 0.007019866704940796 | 0.4214940881729126 |  |  | 287 | 287 | 272 | 276 | 269
Lowercase Letters | 3.981060981750488e-05 | 0.0031957836151123046 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269
All Letters | 8.148808479309082e-05 | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269
Letters & Digits | 0.0001033487319946289 | | | | | | | | | |
All Characters | 0.0001887138843536377 | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269

Dictionary | 1 (20) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
Digits | 1.94845534324646 |  |  |  |  |  | 287 | 287 | 272 | 276 | 269
Lowercase Letters |  | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269
All Letters |  | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269
Letters & Digits | | | | | | | | | | |
All Characters |  | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269
