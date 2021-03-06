import os
import subprocess as sp

from ..common.inout import inform, trim_path, check_output
from engine import OMVEngine, EngineExecutionError

from nestsli import NestEngine


class PyNestEngine(OMVEngine):
    
    name = "PyNEST"
    

    @staticmethod
    def is_installed(version):
        ret = True
        try:
            import nest
            inform("NEST version %s is correctly installed with Python support..." % "???", indent=2)
            inform("Env vars: %s" % PyNestEngine.environment_vars, indent=2)
            
        except Exception as err:
            inform("Couldn't import NEST into Python: ", err, indent=1)
            ret = False
        return ret
        
    @staticmethod
    def install(version):
        NestEngine.install(version)
        PyNestEngine.path = NestEngine.path
        PyNestEngine.environment_vars = NestEngine.environment_vars
        
    def run(self):
        
        nestpath2 = os.path.join(os.environ['HOME'],'nest/nest')
        
        self.environment_vars = {'NEST_HOME': nestpath2,
                                 'PYTHONPATH': nestpath2+'/lib/python2.7/site-packages/'}
                            
        self.set_environment()
                                        
        inform("Env vars: %s" % self.environment_vars, indent=2)
        
        try:
            inform("Running file %s with %s" % (trim_path(self.modelpath), self.name), indent=1)
            self.stdout = check_output(['python', self.modelpath],
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


















