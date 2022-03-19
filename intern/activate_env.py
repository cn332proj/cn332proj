import os
from pathlib import Path
print("\n###   activate venv!   ###")
pp = os.getcwd()+"\\..\\.venv_project\\Scripts\\activate";
qq = "source  " + os.getcwd()+"/../.venv_project/Scripts/activate";
print(qq)
os.system('cmd /k ' + pp)
os.system(qq)



#print('getcwd:      ', os.getcwd())
#print('__file__:    ', __file__)
#os.system('cmd /k "C:\\Users\\Administrator\\Desktop\\cn331_project_mechatopia\\.venv_project\\Scripts\\activate"' tesdewettt ttt tt)