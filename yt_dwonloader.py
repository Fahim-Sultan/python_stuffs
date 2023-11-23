from pytube import YouTube


link = input("Enter the link : ")
yt = YouTube(link)

print("Title : ", yt.title)

print("Views :", yt.views)

down = yt.streams.get_highest_resolution()


def downloads(down):
    
    try:
        down.download('Desktop')
        
    except:
        print("Error in the link") 
   
print("Succesfully downloaded")

downloads(down)