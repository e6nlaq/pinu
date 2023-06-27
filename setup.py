from setuptools import setup

setup(
    name="Pinu",
    version="0.0.1",
    license="MIT",
    description="Python is not unix.",
    author="e6nlaq",
    packages=["pinu"],
    requires=["argparse", "deep_translator"],
    entry_points={
        "console_scripts": [
            "prand=pinu.prand:prand_run",
            "ptrans=pinu.ptrans:ptrans_run",
        ]
    },
)
