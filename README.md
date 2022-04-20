# converter-bot
To convert a file, drag and drop your files into the conversor folder
Then run this code:

    python main.py

and select the option you want
# Installation
## requirements
You need to install the requirements.txt file

    pip install -r requirements.txt

## PyAudio
You can do this if you have problems with PyAudio
First you need to uninstall the default version of PyAudio

    pip uninstall PyAudio

Then you need to install PyAudio with pipwin

    pip install pipwin

    pipwin install PyAudio

Finally if you want you can remove pipwin

    pip uninstall pipwin

## Tesseract-OCR
You need to install [Tesseract-OCR](https://github.com/tesseract-ocr/tessdoc#binaries)
- https://github.com/tesseract-ocr/tessdoc#binaries
## FFmpeg
You need to install [ffmpeg-git-full.7z](https://ffmpeg.org/download.html)
- https://ffmpeg.org/download.html

# Create executable
If you want to create an executable you need to do this:

1. Run this code:

    pyinstaller -F --icon=./logo.ico main.py

2. When the execution is complete, you need drag the 'main.exe' file into the dist folder and then drop it into the 'CONVERTER-BOT' folder

3. You can change the name of the 'main.exe' file if you want

4. You can delete the following folders: 'build', 'dist'

5. You can delete the 'main.spec' file
