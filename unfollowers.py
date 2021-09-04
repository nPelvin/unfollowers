import json
import os
# import send2trash
import shutil


# Set Current Working Directory
cwd=os.getcwd()

followers = ''
following = ''
delete = ''
for dirpath, subdirs, files in os.walk(cwd):
    for x in files:
        if 'followers.json' in x:
            followers=os.path.join(dirpath, x)
        if 'following.json' in x:
            following=os.path.join(dirpath, x)
    for y in subdirs:
        if 'add-data-here' in y:
            delete=os.path.join(dirpath, y)

file = open(followers)
data=json.load(file)
followers=[]
file.close()
for i in data['relationships_followers']:
    followers.append(i['string_list_data'][0]['value'])
file = open(following)
data=json.load(file)
file.close()
following=[]
for i in data['relationships_following']:
    following.append(i['string_list_data'][0]['value'])

unfollowers=[]

for i in following:
    if i in followers:
        continue
    else:
        unfollowers.append(i)

# Create and write unfollowers.txt
file = open("unfollowers.txt","w")
for i in unfollowers:
    file.write(i+'\n')
file.close()

# send2trash.send2trash(delete)
shutil.rmtree(delete)

# Directory
directory = "add-data-here"
  
# Path
path = os.path.join(cwd, directory)
  
# Create the directory
os.mkdir(path)
