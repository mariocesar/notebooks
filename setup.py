from setuptools import setup, find_packages

setup(
    name='binder',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development :: Build Tools"
    ],
    author='Mario César Señoranis Ayala',
    license='GPL2',
    include_package_data=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False
)
