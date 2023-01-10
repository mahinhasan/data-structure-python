import os
import time

sourc = ['/home/mahin/ডেস্কটপ/h.zip'] # Dictories from datastructure
target_dir = '/home/mahin/ডেস্কটপ/Backup'
target = target_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
zip_command = 'zip -r {0} {1}'.format(target,' '.join(sourc))
print('zip command is : ')
print(zip_command)
print("Running")
if os.system(zip_command)==0:
    print("Succesful backup to ",target)
else:
    print("Backup failed")