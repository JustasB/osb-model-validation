import os
import subprocess as sp

from ..common.inout import inform, trim_path, check_output
from engine import OMVEngine, EngineExecutionError


class Brian2Engine(OMVEngine):
    
    name = "Brian2"

    @staticmethod
    def is_installed(version):
        ret = True
        try:
            import brian2
            print brian2.__file__
            inform("Brian2 version %s is correctly installed..." % brian2.__version__, indent=2)
            
        except Exception as err:
            inform("Couldn't import Brian2 into Python: ", err, indent=1)
            ret = False
        return ret
        
    @staticmethod
    def install(version):
        from getbrian2 import install_brian2
        home = os.environ['HOME']
        inform('Will fetch and install the latest Brian (version 2.x)', indent=2)
        install_brian2()
        inform('Done...', indent=2)
        
    def run(self):
        try:
            inform("Running file %s with %s" % (trim_path(self.modelpath), self.name), indent=1)
            self.stdout = check_output(['python', self.modelpath, '-nogui'],
                                          cwd=os.path.dirname(self.modelpath))
            self.returncode = 0
        except sp.CalledProcessError as err:
            self.returncode = err.returncode
            self.stdout = err.output
            raise EngineExecutionError
        except Exception as err:
            inform("Another error with running %s: "%self.name, err, indent=1)
            self.returncode = -1
            self.stdout = "???"


















