# Architecture — PulseTwin AI

```text
User adjusts fictional profile in Streamlit sidebar
                      |
                      v
              Patient feature vector
                      |
                      v
Synthetic generator --> Random Forest training (cached)
(2,400 records)       |         |
        |             |         +--> Feature importance chart
        +--> formula-based labels |
                      v         v
                Illustrative model score
                      |
                      v
             Streamlit dashboard
              /       |       \
       Rule flags  7-day timeline  CSV export
```

## Data flow
1. NumPy generates reproducible synthetic records; an arbitrary formula creates labels.
2. scikit-learn splits records into train/test sets and trains Random Forest.
3. User inputs are evaluated by the trained model, with an illustrative score displayed.
4. An independent deterministic random generator creates fictional seven-day measurements.
5. Streamlit displays charts, demo observations, and a downloadable CSV.

No real patient records, live devices, external APIs, persistent database, or clinical validation.
