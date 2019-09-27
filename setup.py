from setuptools import setup

with open('README.md', 'r') as fp:
    long_desc = fp.read()

setup(
    name='discord_msg_lite',
    version='1',
    author='Tom YU Choe',
    author_email='yonguk.choe@gmail.com',
    description='A simple and lightweight Python PyPI module to send messages easily using Discord Webhooks.',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    py_modules=['discord_msg_lite'],
    package_dir={'': 'src'},
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.6"
        "Operating System :: OS Independent",
    ],
)