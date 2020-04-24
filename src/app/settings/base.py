BASE_SETTINGS = {
    'app': {
        'components': [
            'app.components.example',
        ]
    },
    'deploy': {
        'tasks': [
            'unv.deploy.components.vagrant:VagrantTasks',
            'unv.deploy.components.redis:RedisTasks',
            'unv.deploy.components.app:AppTasks'
        ],
    }
}
