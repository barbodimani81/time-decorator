# Decorators Example Project

Welcome to the **Decorators Example Project** – a simple yet powerful demonstration of how to use decorators in Python to add logging and execution time measurement to functions.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Code Explanation](#code-explanation)
6. [Contributing](#contributing)
7. [License](#license)

## Overview

This project showcases the use of two decorators in Python:

1. **Time Decorator**: Measures and prints the execution time of a function.
2. **Logger Decorator**: Logs the start and end of function execution.

These decorators are then applied to a simple function `say_hi` to demonstrate their usage.

## Features

- **Execution Time Measurement**: Prints the time taken for a function to execute.
- **Logging**: Logs messages indicating when a function starts and finishes.

## Installation

To get started with the **Decorators Example Project**, follow these steps:

1. **Clone the Repository** (if applicable):

    ```bash
    git clone https://github.com/yourusername/decorators-example.git
    cd decorators-example
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    This project does not require any external libraries other than the standard Python library.

## Usage

1. **Run the Script**:

    ```bash
    python main.py
    ```

    The script will execute the `say_hi` function, and you will see the execution time and log messages in the console.

## Code Explanation

### Decorators

#### Time Decorator

The `time_decorator` measures the execution time of a function:

```python
def time_decorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        stop = time.time()
        print(f"It took {stop - start} seconds")
        return result

    return wrapper

