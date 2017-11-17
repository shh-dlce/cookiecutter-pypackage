from setuptools import setup, find_packages


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.description }}',
    long_description=read("README.rst"),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
    ],
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}',
    keywords='{{ cookiecutter.keywords if cookiecutter.keywords != "-" else "" }}',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[{{ ', '.join('"{0}"'.format(p) for p in cooiecutter.requires.split()) if cookiecutter.requires != '' else '' }}],
    extras_require={
        'dev': ['flake8', 'wheel', 'twine'],
        'test': [
            'pytest>=3.1',
            'pytest-mock',
            'mock',
            'coverage>=4.2',
            'pytest-cov',
            {{ 'webtest' if cookiecutter.with_webtest != "-" else ''}}
        ],
    },
    license="Apache 2.0",
    {% if cookiecutter.cli_name != '-' %}
    entry_points={
        'console_scripts': [
            "{{ cookiecutter.cli_name }} = {{ cookiecutter.pkg_name }}.__main__:main",
        ]
    },
    {% endif %}
)

