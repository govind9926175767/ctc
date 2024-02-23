from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ctc_custom/__init__.py
from ctc_custom import __version__ as version

setup(
	name="ctc_custom",
	version=version,
	description="for demo pratice",
	author="Yes",
	author_email="yes@123gamil.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
