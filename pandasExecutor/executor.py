import sys
from io import StringIO
import contextlib
from codeProcessor.reader import CodeReader


class PandaExecutor():

    @contextlib.contextmanager
    def stdoutIO(self, stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

    def runCode(self, code, filePath):
        with self.stdoutIO() as s:
            code = CodeReader().readCode(code)
            exec(code + """\n""")
            result = locals()['studioResults']
            return result
