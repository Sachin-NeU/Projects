import os

file_list = os.listdir(r"C:\Users\Win10\Desktop\Axis bank loan application\Dad Docs")
print(file_list)
i = 1
svd_path = os.getcwd()
os.chdir(r"C:\Users\Win10\Desktop\Axis bank loan application\Dad Docs")
print(os.getcwd())
for file_name in file_list:
    dst_filename = str(i)+ "_" + file_name
    print("old file name: "+file_name+" and new file name: "+ dst_filename)
    i += 1
    os.rename(file_name,dst_filename)

os.chdir(svd_path)






