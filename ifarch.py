import platform
import glob
import os

import dotbot
from dotbot.dispatcher import Dispatcher
from dotbot.util import module
from dotbot.plugins import Clean, Create, Link, Shell

class IfArch(dotbot.Plugin):
    _archs = [
        'aarch64',
        'arm64',
        'armv7l',
        'x86_64',
    ]

    def __init__(self, context):
        super(IfArch, self).__init__(context)
        self._directives = ['if'+a for a in self._archs]

    def _load_plugins(self):
        plugin_paths = self._context.options().plugins
        plugins = []
        for dir in self._context.options().plugin_dirs:
            for path in glob.glob(os.path.join(dir, '*.py')):
                plugin_paths.append(path)
        for path in plugin_paths:
            abspath = os.path.abspath(path)
            plugins.extend(module.load(abspath))
        if not self._context.options().disable_built_in_plugins:
            plugins.extend([Clean, Create, Link, Shell])
        return plugins

    def can_handle(self, directive):
        return directive in self._directives

    def handle(self, directive, data):
        if directive not in self._directives:
            raise ValueError('Cannot handle this directive %s' % directive)

        arch = platform.machine()
        if directive == 'if'+arch:
            self._log.debug('Matched arch %s' % arch)
            return self._run_internal(data)
        else:
            return True

    def _run_internal(self, data):
        dispatcher = Dispatcher(self._context.base_directory(),
                                only=self._context.options().only,
                                skip=self._context.options().skip,
                                options=self._context.options(),
                                plugins=self._load_plugins())
        return dispatcher.dispatch(data)