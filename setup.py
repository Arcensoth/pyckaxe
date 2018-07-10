from setuptools import find_packages, setup

with open('VERSION.txt') as fp:
    version = fp.read().strip()

with open('README.md') as fp:
    readme = fp.read()

with open('requirements.txt') as fp:
    requirements = fp.read().splitlines()

setup(
    name='pyckaxe',
    version=version,
    author='Arcensoth',
    author_email='arcensoth@gmail.com',
    url='https://github.com/Arcensoth/pyckaxe',
    license='MIT',
    description='An expressive Minecraft utility library revolving around data manipulation and generation.',
    long_description_content_type='text/markdown',
    long_description=readme,
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
    keywords='minecraft commands library utility datapack data',
    classifiers=(
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
    )
)
