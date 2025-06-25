from setuptools import find_packages, setup

package_name = 'homework'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', []),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/homework_launch.py', 'launch/homework_all_nodes_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jaewon',
    maintainer_email='jaewon@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = homework.publisher_node:main',
            'subscriber_node = homework.subscriber_node:main',
            'node1 = homework.node1:main',
            'node2 = homework.node2:main',
            'node3 = homework.node3:main',
        ],
    },
)
