# Week 7

- Critique drawing tools
- Grids (review)
 - using arrays of arrays
- Pixel array
- Tribute to Carolee Schneeman

# Nested For Loops / To Make a Grid

Last week we covered nested for loops

Can you explain what happens?

[Example code of minimal nested for loop](https://editor.p5js.org/2sman/sketches/XdV_uJonn)

```
function setup() {
  createCanvas(400, 400);

  background(220);

  for (let x=0;x<width;x+=20){
    for (let y=0;y<height;y+=20){
      //fill(random(255));
   		rect(x,y,20,20);
    }
  }
}
```

# More complex array examples

We discussed the basics of arrays. Arrays let you hold a list of variables.

![array](array.png)

```
//from Getting Started with p5.js 11-8
var num = 60;
var x = [];
var y = [];

function setup() {
  createCanvas(400, 400);
  noStroke();

  for (var i = 0; i < num; i++){
   	x[i] = 0;
    y[i] = 0;
  }
}

function draw() {
  background(0);

  //Copy array values from back to front
  for (var i = num-1; i > 0; i--){
   	x[i] = x[i-1];
    y[i] = y[i-1];
  }

  x[0] = mouseX; //set the first element
  y[0] = mouseY; //set the first element

  for (var i = 0; i < num; i++){
     fill(i * 4);
      ellipse(x[i], y[i], 40, 40);
  }
}
```

## Multidimensional arrays

Arrays can be multidimensional. So far we have talked about a 1-dimensional array.

Each element in the array has a single number that assigns where it is location. 0 is the first element in the array. 1 is the next element. And so on.

![chessboard](chessboard.jpg)

A chessboard is 2-dimensional. There is a X, Y position for every space on the chessboard. So we need to give two numbers to identify a space in this 2-dimensional array.

## Pixel Array

Our pixel array is even more complex. For each individual pixel in our canvas sketch, there is a X and Y location.

We can change grab and change a pixel individually with get() and set().

Additionally, p5js gives us a pixels array. It is very long, and it corresponds to all of our canvas pixels.

The pixel array is 1-dimensional but our canvas is 2-dimensional.

```pixels = [_, _, _, _, _, _, _, .........]```

How does this work? Each pixel has a number for its red, green and blue value as well as its alpha (transparency). So the very first pixel, the pixel located at 0,0 in our grid are the first four values in the pixel array.

```pixels = [R, G, B, A, ..........]```


The formula for going from a 2d grid to a one-dimensional array is ```(x + y * width) * 4```.

Playing with pixels

```
function setup() {
  createCanvas(320, 240);
  pixelDensity(1);
}

function draw() {
  background(51);

  loadPixels();
  for (var y = 0; y < height; y++) {
    for (var x = 0; x < width; x++) {
      var index = (x + y * width)*4;
      pixels[index+0] = x;
      pixels[index+1] = 0;
      pixels[index+2] = y;
      pixels[index+3] = 255;      
    }
  }
  updatePixels();

}
```

# Image capture

Our laptops have built-in webcams, and we can access them with p5.js. The video we get from the camera we call a capture.

```
var capture;
function setup() {
  createCanvas(400, 400);
  capture = createCapture(VIDEO);
  capture.hide();
  imageMode(CENTER);
}
function draw() {
  background(50);
  image(capture, mouseX, mouseY, 160, 120);
}
```

[code](https://editor.p5js.org/2sman/sketches/OY8WGsMh3)

# Carolee Schneeman

Carolee Schneeman passed away this week. She was a multidisciplinary artist whose work explored gender, sexuality, the body and society, among other subjects. She challenged audiences and institutions, expressing herself and her own body as author rather than subject. She is sometimes described as a painter, as that was her first medium, but she is also considered an artist working within realms of Fluxus, certainly performance art, and happenings.

- [Groundbreaking Feminist Artist Carolee Schneeman Has Died](https://jezebel.com/groundbreaking-feminist-artist-carolee-schneemann-has-d-1833122858)
- [interview](https://www.youtube.com/watch?v=smo4OR3Gvq8) with Schneeman on her 1973 exhibition *Up To and Including Her Limits*
- [video of an installation by Schneeman](https://www.youtube.com/watch?v=tIakIRENhtc)
- article [Challenging Boundaries With Her Naked Body](https://www.nytimes.com/2016/10/30/arts/design/carolee-schneemann-challenges-boundaries-with-her-naked-body.html)
-


# Homework
- Watch [The Pixel Array](https://www.youtube.com/watch?v=nMUMZ5YRxHI) on The Coding Train on YouTube
- [Create Capture](https://www.youtube.com/watch?v=bkGf4fEHKak) to get a live image from the webcam
- [Painting With Pixels](https://www.youtube.com/watch?v=0V3uYA1hafk)

## Make a work using grids

Using nested for loops and optionally the camera, make an interactive work that uses grids in the creation of the work.

- The work should be able to work fullscreen in present mode. Use

```
createCanvas(windowWidth, windowHeight);
```

- The work needs to be interactive (with keypresses or mouse action, for example)

[Example code](https://editor.p5js.org/2sman/sketches/gBJmcnutD)
