from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="webarena",
        packages=find_packages(
            where=".",
            include=["agent", "browser_env", "evaluation_harness", "llms"],
        )
    )
