from setuptools import setup, find_packages
import os

ROOT_DIR='redvypr_device_skeleton'
with open(os.path.join(ROOT_DIR, 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(name='redvypr_device_skeleton',
      version=version,
      description='redvypr device',
      long_description='redvypr device',
      url='https://github.com/redvypr/redvypr_device_skeleton',
      author='Peter Holtermann',
      author_email='peter.holtermann@systemausfall.org',
      license='GPLv03',
      packages=find_packages(),
      scripts = [],
      entry_points={},
      package_data = {'':['VERSION']},
      install_requires=[ 'redvypr'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering',          
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
      ],
      python_requires='>=3.5',
      zip_safe=False)
