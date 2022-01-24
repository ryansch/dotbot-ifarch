import platform
import dotbot
from dotbot.dispatcher import Dispatcher

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
                                exit_on_failure=self._context.options().exit_on_failure,
                                options=self._context.options())
        return dispatcher.dispatch(data)
