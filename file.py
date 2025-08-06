import os 
import shutil

image_extension =['.jpg', '.jpeg', '.png', '.gif']
video_extension =['.mp4', '.mkv', '.avi', '.mov']
music_extension =['.mp3', '.wav', '.flac']
document_extension =['.pdf', '.docx', '.txt', '.xlsx']

files=[]

for f in os.listdir():
    if os.path.isfile(f):
        files.append(f)

        
        for file in files:
            extension =file.split(".") [-1].lower()

            if extension in image_extension:
                catagory ="image"
            elif extension in document_extension:
                catagory ="document"
            elif extension in music_extension:
                catagory ="music"
            elif extension in video_extension:
                catagory ="video"
            else 
                catagory ="others"

            if not os.path.exists(catagory):
                os.makedirs(catagory)
                print(f"Created directory: {catagory}")

                shutil.move(file, od.path.join(catagory,file))
                print (f"Move {file} to {catagory} directory.")    
             
            
