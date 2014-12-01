import os
import subprocess as sp

from ..common.inout import inform, trim_path, check_output
from backend import OMVBackend, BackendExecutionError


class Brian1Backend(OMVBackend):
    
    name = "Brian"

    @staticmethod
    def is_installed(version):
        ret = True
        try:
            import brian
            inform("Brian version %s is correctly installed..." % brian.__version__, indent=2)
            
        except Exception as err:
            inform("Couldn't import Brian into Python: ", err, indent=1)
            ret = False
        return ret
        
    @staticmethod
    def install(version):
        from getbrian1 import install_brian
        home = os.environ['HOME']
        inform('Will fetch and install the latest Brian (version 1.x)', indent=2)
        install_brian()
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
            raise BackendExecutionError
        except Exception as err:
            inform("Another error with running %s: "%self.name, err, indent=1)
            self.returncode = -1
            self.stdout = "???"


















