---
name: ermes runner
about: Describe this issue template's purpose here.
title: '[run] - @date.now() - ${{ github.actor }}'
labels: ' ermes'
assignees: ' ${{ github.actor }}'

---

## Ermes Pipeline

### backend

- [ ] Tensorflow Data Validation
- [ ] Tensorflow Model Analysis
- [ ] MLFlow Metrics

### variables

DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'chicago_taxi_output')
TRAIN_DATA = os.path.join(DATA_DIR, 'train', 'data.csv')
EVAL_DATA = os.path.join(DATA_DIR, 'eval', 'data.csv')
SERVING_DATA = os.path.join(DATA_DIR, 'serving', 'data.csv')
