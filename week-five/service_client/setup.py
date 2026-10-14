maintainer='Daniil',
maintainer_email='test@email.com',
description='Python client server tutorial',
license='Apache-2.0',
entry_points={
    'console_scripts': [
        'service = py_srvcli.service_member_function:main',
        'client = py_srvcli.client_member_function:main',
    ],
},