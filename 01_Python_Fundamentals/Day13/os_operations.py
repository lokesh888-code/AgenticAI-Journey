import os

print("Current directory:", os.getcwd())
os.chdir("Day11")
print("Current directory:", os.getcwd())

os.rename("../student.json", "student.json")

#print("File moved successfully.")

# print("Files in current directory:")
# for item in os.listdir():
#     print("-", item)

# folder_name = "sample_folder"
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
#     print(f"Created folder: {folder_name}")
# else:
#     print(f"Folder already exists: {folder_name}")