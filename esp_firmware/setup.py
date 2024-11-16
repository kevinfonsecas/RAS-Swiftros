from setuptools import find_packages, setup

package_name = 'esp_firmware'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gabriel',
    maintainer_email='gabrieldiaz@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'wifi_transmitter = esp_firmware.wifi_transmitter:main',
            'wifi_receiver = esp_firmware.wifi_receiver:main',
        ],
    },
)
sor