import os, sys

sys.path.append('../permamodel/')
print('Permamodel added to system path.')

from permamodel.components import bmi_Ku_component
print('Permamodel is installed.')

cfg_file = os.path.join('./inputs/', 'ku-hackathon-test.cfg')
x = bmi_Ku_component.BmiKuMethod()
print('Ku is configured.')

print('All tests passed.')