import os

from permamodel.components import bmi_Ku_component
print('Permamodel is installed.')

cfg_file = os.path.join('./inputs/', 'ku-hackathon-test.cfg')
x = bmi_Ku_component.BmiKuMethod()
print('Ku is configured.')

x.initialize(cfg_file)
print('Ku is initialized')

x.update()
x.finalize()
print('Ku successfully ran for 1 time step.')

print('All tests passed.')