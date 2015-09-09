from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_hooks',
    description='rubocop pre commit hook.',
    url='https://github.com/jordant/rubocop-pre-commit-hook',
    version='0.1',

    author='Jordan Tardif',
    author_email='jordan.tardif@gmail.com',

    packages=find_packages('.', exclude=('tests*', 'testing*')),

    entry_points={
        'console_scripts': [
            'check-rubocop = pre_commit_hooks.check_rubocop:check_rubocop',
        ],
    },
)
