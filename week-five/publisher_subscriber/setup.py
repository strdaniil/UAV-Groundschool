maintainer='Daniil',
maintainer_email='test@email.com',
description='Examples of minimal publisher/subscriber using rclpy',
license='Apache-2.0',

entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
                'listener = py_pubsub.subscriber_member_function:main',
        ],
},