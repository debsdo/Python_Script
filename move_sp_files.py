#import required libraries
import shutil, os

#file names you want to move
file = ["20161207-111327-0.jpg",
"20170718-095159-2.jpg",
"20170811-133439-1.jpg",
"20170811-133752-1.jpg",
"20170217-114015-0.jpg",
"20170811-123145-2.jpg",
"20170811-131023-1.jpg",
"20170405-155147-0.jpg",
"20161207-111246-0.jpg",
"20170718-102020-2.jpg",
"20170217-103427-0.jpg",
"20170811-134228-1.jpg",
"20170217-151259-0.jpg",
"20170811-112723-2.jpg",
"20170210-131822-0.jpg",
"20170718-095128-2.jpg",
"20170811-125149-2.jpg"]
	
#source folder
dir_src = 'D:\\deepweedsx\\DeepWeeds_Images_256'

#destination folder
dir_dst = 'D:\\project\\train' 

#dir_dst = 'D:\\project\\test'

#code to move files
for f in file:
    	print file  # testing
   	src_file = os.path.join(dir_src, f)
	dst_file = os.path.join(dir_dst, f)
    	shutil.move(src_file, dst_file)
