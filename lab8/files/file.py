import shutil, magic, os

JPEG = "JPEG"
PNG = "PNG"
ASCIITXT = "ASCII"
MP3 = "Audio"

os.mkdir('jpegFolder')
os.mkdir('pngFolder')
os.mkdir('txtFolder')
os.mkdir('mp3Folder')

for i in range (10,150):

	contentType = magic.from_file("file" + str(i))
	
	if JPEG in contentType:
		shutil.move("file" + str(i), "jpegFolder/")

	elif PNG in contentType:
		shutil.move("file" + str(i), "pngFolder/")

	elif ASCIITXT in contentType:
		shutil.move("file" + str(i), "txtFolder/")

	elif MP3 in contentType:
		shutil.move("file" + str(i), "mp3Folder/")

print ("All files separated by type")
