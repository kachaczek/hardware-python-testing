# Hardware Integration Testing (Python + Pytest)

This project provides a simple but extensible **hardware validation test suite** written in Python using **pytest**.  
It demonstrates how to perform *integration-level hardware checks* — verifying that system components such as CPU, RAM, storage, GPU, and battery respond correctly.

The project is designed just for learning purposes and it contains:
- usage of **fixtures** and **pytest markers** (`@pytest.mark.hardware`, `@pytest.mark.integration`)
- meaningful **assertions and messages**
- **graceful handling** of missing hardware (using `pytest.skip`)
- clear **docstrings** and consistent structure (ready for CI/CD reporting)

## Installation & Setup

### Clone the repository
git clone https://github.com/kachaczek/hardware-python-testing

### Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

### Install dependencies
cd ~/hardware-python-testing
pip install -r requirements.txt

### Running tests
pytest -v

### Run all hardware tests
pytest -v -s

### Run all integration tests
pytest -v -s -m integration



