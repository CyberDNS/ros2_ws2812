from setuptools import find_packages, setup

package_name = 'ws2812_driver'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='David Ney',
    maintainer_email='david.ney@live.com',
    description='Driver for WS2812 LED strips',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ws2812_node = ws2812_driver.ws2812_node:main',
        ],
    },
)
