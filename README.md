# ncapimg
Downloads zoomify tiles and creates one image. Mainly created to download aerial photos from service at: http://ncap.org.uk/  
  
Requirements :  
- Python >= 3.2 (http://www.python.org)
- montage - from ImageMagic package (http://www.imagemagick.org)  
**Windows users note:** when installing Python 3.x. select "Add Python to PATH". When installing ImageMagic package 
select  "Install legacy utilities (e.g. convert)"
  
Program must be run with image number i.e. NCAP UNI number seen in lower right of image we page.  
I think default number of columns and rows (9) is enough. Don't worry if you see "404"s -
it usually means that particular column or row dosen't exists.  
Based on given image number, program creates directory and downloads all tiles into that folder. Then
it creates results image in same folder as tiles. Name of result image is always: final_image.jpg  
  
Example usage:  
```
python3 ncapimg.py NCAP-000-000-302-950
```
