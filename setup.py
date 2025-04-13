from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="prediction-metrics-backtester",
    version="0.1.0",
    author="Nathaniel William Huff",
    author_email="nathanielwilliam117@gmail.com",
    description="A flexible backtesting framework for evaluating trading strategies based on prediction metrics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nawihu/prediction-metrics-backtester",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial :: Investment",
        "Intended Audience :: Financial and Insurance Industry",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.20.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
    ],
    entry_points={
        "console_scripts": [
            "prediction-metrics-backtest=prediction_metrics_backtesting:main",
        ],
    },
)