# use modules that can be imported
# move required file into working directory

import sample
import sys

print(sample.a)

sys.path.insert(1, r"C:\Disk\python\programming_in_python\the_import_statement\workplace")
import trial
print(trial.b)