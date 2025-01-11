from setuptools import setup, find_packages

setup(
    name="TASK-TRACKER-CLI",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['typing','rich'],
    entry_points={"console_scripts": ["taskr=task_tracker.main:main"]},
)
