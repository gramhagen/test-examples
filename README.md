# Installation

```bash
conda create -n test python=3.7 -y
conda activate test
pip install -e .
```

# Run tests

```bash
# run all tests
pytest tests

# run specific tests
pytest tests/bad -k "better"
```
