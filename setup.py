from setuptools import setup

def readme():
	with open ('README.rst') as f:
		return f.read()

setup(name='rnainigo',
	version='0.1',
	description='Calculate read mapped percentage',
	url='https://github.com/kspham/rnainigo',
	author='ptdtan',
	author_email='ptdtan@gmail.com',
	license='MIT',
	scripts=['scripts/countmap','scripts/rnainigo'],
	packages=['rnainigo'],
	zip_safe=False)
	
