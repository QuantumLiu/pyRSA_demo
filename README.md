# pyRSA_demo
A Python demo implemention of encrypt software
#  Important  
I have never design or spread any malicious software.This is for study purpose only.You must comply with your local laws!  
# Functions  
Batch encrypting specific fomats files(defualt.txt,.png,.doc) with RSA.  
# Versions  
`_re*` means release version,rewrite files.  
`_test` test version ,compute only,don't  rewrite files.  
`*_c` background model,no console and STD I/O.  
# Platform and Dependencies  
Win10  
Ananconda3  
Python3.5.2
pyinstaller3.2.1  
# Compile  
background model:  
`pyinstaller -F -n pyRSA_single_re_c --clean --uac-admin -w RSA_single_re_c.py`
else:  
`pyinstaller -F -n pyRSA_single_re --clean --uac-admin -c RSA_single_re.py`  
