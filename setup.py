from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='pyicloud_ipd',
    version='0.11.0',
    url='https://github.com/ndbroadbent/pyicloud',
    description=(
        'PyiCloud is a module which allows pythonistas to '
        'interact with iCloud webservices.'
    ),
    maintainer='The PyiCloud Authors',
    maintainer_email=' ',
    license='MIT',
    packages=find_packages(),
    install_requires=required,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'icloud = pyicloud_ipd.cmdline:main'
        ]
    },
)
