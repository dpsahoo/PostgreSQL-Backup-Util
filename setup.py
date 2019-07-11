from setuptools import find_packages, setup

with open('README.md', 'r') as f:
	long_description = f.read()

##Call setup() function by passing in the required parameters
setup(
	name='pgbackup',
	version='0.1.0',
	author='Durga Sahoo',
	author_email='dpsahoo@gmail.com',
	description='A utility for backing up PostgreSQL databases - built in Python3.7',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/dpsahoo/pgbackup',
	packages=find_packages('src'),
	package_dir={'': 'src'},
	install_requires=['boto3'],
	python_requires='>=3.6',
	entry_points={
		'console_scripts': [
			'pgbackup=pgbackup.cli:main',
		],
	}
	)
