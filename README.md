# ncapimg
Downloads zoomify tiles and creates image. Mainly created for service at: http://ncap.org.uk/  
  
Requirements :  
- Python >= 3.2 (http://www.python.org)
- montage - from ImageMagic package (http://www.imagemagick.org)  
  
Program must be run with image number i.e. NCAP UNI number seen in lower right of image we page.  
I think default number of columns and rows (9) to check is enough. Don't worry if you see "404"s -
it usually means that particular column or row dosen't exists.  
Based on given image number, program creates directory and downloads all tiles into that folder. Then
it creates results image in same folder as tiles. Name of result image is: final_image.jpg  
  
Example usage:  
python3 ncapimg.py NCAP-000-000-302-950
