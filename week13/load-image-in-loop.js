//example code for Matthew 
var imgArray = [];
var numOfImages = 16; //make sure you name files img0.jpg, img1.jpg, img2.jpg, etc - otherwise you need to count in loop beginning at 1, not 0

function preload(){
  for (var i=0; i<numOfImages; i++{
	  //MAKE SURE ALL IMAGES ARE CONVERTED TO SAME TYPE AND HAVE SAME SPELLING OF THE EXTENSION
    imgArray[i] = loadImage('H'+i+'.jpg');
  }
}

function setup(){
  //display a random image
  var pickAnImage = round(random(numOfImages));
  
  image(imgArray[pickAnImage],0,0); //display that image at 0,0
}
