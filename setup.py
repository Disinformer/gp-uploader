from setuptools import find_packages, setup

setup(
    name='gp-uploader-custom',
    version='0.0.1',
    description='Script to monitor a directory and upload any existing files to google photo using adb connected android device',
    author='Disinformer',
    url='https://github.com/Disinformer/gp-uploader',
    packages=find_packages(),
    install_requires=[
        'rich',
        'lxml',
    ],
    entry_points={
        'console_scripts': ['gp-uploader-custom = gp_uploader.watch_dir:main']
    },
)
