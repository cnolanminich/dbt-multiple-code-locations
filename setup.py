from setuptools import find_packages, setup

setup(
    name="dagster_multi_tenant_example",
    packages=find_packages(exclude=["dagster_multi_tenant_example_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-core"
        "dbt-duckdb"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
