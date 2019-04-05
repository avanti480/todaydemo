from setuptools import setup


setup(
	name= 'todaydemo',
	version= '0.1',
	description= 'Assorted personal functions and tools.',
	url= '',
	author='Avanti Gogate',
	author_email='avanti@astro.rug.nl',
	license='',
	packages=['todaydemo'],
	install_requires=['numpy', 'astropy','matplotlib'],
	include_package_data=True,
	zip_safe=False
)
