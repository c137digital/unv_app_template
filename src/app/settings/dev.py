from unv.app.settings import ComponentSettings

from .base import BASE_SETTINGS

# NOTE: add check you don't import nothing with settings inside

SETTINGS = ComponentSettings.create({
    'app': {
        'env': 'dev'
    },
    'deploy': {
        'hosts': {
            'vagrant': {
                'public_ip': '10.50.25.32',
                'private_ip': '10.50.25.32',
                'components': ['app', 'redis'],
            }
        },
        'components': {
            'app': {
                'settings': 'app.settings.dev'
            }
        }
    }
}, BASE_SETTINGS)
