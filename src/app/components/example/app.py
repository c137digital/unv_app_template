from unv.app.base import Application

from . import base


def setup(app: Application):
    app.register_run_task(base.main)
