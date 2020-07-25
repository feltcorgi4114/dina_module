import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dina_modules",
    version="0.0.2",
    author="Dinanjanan Ravindran",
    author_email="dinaravi1414@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/feltcorgi4114/dina_module",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# pypi-AgENdGVzdC5weXBpLm9yZwIkMWVmMGI4YzItYjU4Mi00NTY1LWJmMjYtZDEyZTJhYjFiZTZmAAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiD-lLkiGbKSo6o5nIfc_UUYe-Ao3deZRkYEWt4OmoYaEQ