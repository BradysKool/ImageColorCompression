# ImageComprestion

In this project, I created a clustering algorithm by scratch in Python that I used to group similar colors in a picture together. So I only have to store what color each pixel is linked to and that color. I started with an 871 by 1284 image and for each of those pixels I stored 3 integers for the RGB value but this script allows me to store one int for each of the pixels pointing to a separate list of what color it will use. The result is that I only have to store a third of the information which is a pretty big compression. 

Here is the Original Photo:
![murphy](https://github.com/BradysKool/ImageColorCompression/assets/101609721/33089524-5d23-42b9-8203-f6220e807cbb)

Compressed to 20 colors:


![murphy 20](https://github.com/BradysKool/ImageColorCompression/assets/101609721/502a1930-9d8a-4751-8e97-5a000d10af6f)


Compressed to 10 colors:


![murphy10](https://github.com/BradysKool/ImageColorCompression/assets/101609721/cb2f233c-5f15-4670-8183-bdadb4a38ddf)


Compressed to 5 colors:


![murphy5](https://github.com/BradysKool/ImageColorCompression/assets/101609721/8ccf16ce-5ce2-45d9-9224-53060573aa16)


Compressed to 3 colors:


![murphy3](https://github.com/BradysKool/ImageColorCompression/assets/101609721/bcd57d23-8dc8-40e5-82f2-a3f871026354)



Compressed to 2 colors:


![murphy2](https://github.com/BradysKool/ImageColorCompression/assets/101609721/f095e2a1-a467-4841-94d2-bf10823a0c62)
