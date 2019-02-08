# week 3

- Homework review - bouncing balls
- Questions!
- if statements review
  - flow control
  - scope with {}
  - if
  - else
  - else if
- events
  - mousePressed()
  - keyPressed()
  - an aside: builtin variable: mouseIsPressed
  - how is it different from the method mousePressed() ?
- booleans! (true or false)
- loops
- images!

# Control the flow with if statements

### Simple if statement

- "If this is true, then do this"

```
if (age <= 16){
  print("You're awfully young to be in college");
}
```


### Else

- "If this is true, then do this. OTHERWISE, do that."

```
if (age <= 16){
    print("You're awfully young to be in college");
} else {
  print("You're old enough for college.");
}
```

### Else if

- "If this is true, then do this. OTHERWISE IF this other thing is true, do that instead. Otherwise, if none of the above are true, do this last thing."

```
if (age <= 16){
    print("You're awfully young to be in college.");
} else if (age <= 23){
    print("You're old enough for college.");
} else {
    print("Did you go back to school? I salute you!");
}
```


# Events

An event is triggered by a time, or by an action. It is something your web browser does or something the user of your software does which indicates interaction. Examples are pressing a mouse button, dragging the cursor across the screen, tilting a phone, or pressing a key. p5.js gives a number of built-in functions to make it easier to work with events.

A full list of events can be found in the p5.js Reference [section on events](http://p5js.org/reference/#group-Events)

### mousePressed


```
function mousePressed(){
  //this code will run anytime the mouse is Pressed
  print('you clicked');
}
```

### keyPressed

```
function keyPressed(){
  //this function runs anytime you press a key
   if (keyCode === LEFT_ARROW) {
    //move left
   } else if (keyCode === RIGHT_ARROW) {
    //move right
  }
}
```

## Booleans

A boolean is a variable that is set to ```true``` or ```false```. This is a binary choice.

Example


```
var iMadeMyBedToday = false;
```


### Builtin in boolean: mouseIsPressed

Don't confuse mousePressed() with ```mouseIsPressed```.

mouseIsPressed is a builtin variable (like mouseX, or width) that we can use in our programs. We normally use it in our draw loop to detect if a key is building held down. If any key is being held down, then ```mouseIsPressed = true```

example

```
function draw() {
  background(237, 34, 93);
  fill(0);

  if (mouseIsPressed) {
    ellipse(50, 50, 50, 50);
  } else {
    rect(25, 25, 50, 50);
  }

  print(mouseIsPressed);
}
```

# Looping

Sometimes we want to do something many times. Over and over again.

We use loops to do this.

What kinds of things need to happen lots of lots of times? Drawing a lot of something is a good example.

### For loop

Use the for loop to specify having an action occur a set number of times.

```
for (var i = 0; i < 65; i++){
    print("My age is "+i);
}
```

There are 3 sections in the for loop statement. First we initialize the temporary variable. Then we test to see if the statement is valid. Then we increment the temporary variable at the end of each loop.

Another example

```
for (var i = 99; i >= 0; i--){
  print(i+" bottles of beer on the wall, "+i+" bottles of beer...");
}
```

## When to use an if statement or for loop

 **If you are testing whether something is true**

When you are asking a question, use an if statement.

Examples: Is my ball off screen? Is the color black?

**If you need to make lots of things, use a for a loop**

Examples: I need 300 circles.

## Images

Okay, we can draw ellipses, and rects, lines, points, triangles, or use ```beginShape()``` to make your own shape.
We can draw part of a circles with ```arc```.

This is great. But sometimes you want to work with images directly. p5.js can load and display images: png, jpg, gif.

To do so, we need to do four things:

1. Import the image into our sketch's folder.
2. Create a variable to hold the image.
3. Add a ```preload()``` function section to our code sketch and preload the image.
4. draw the image to the window with ```image(imageVariableName,x,y);```, usually in our draw function.

Example

```
var fluffyCatImg; //the variable to hold our imageFile

function preload(){
    fluffyCatImg = loadImage('cat.jpg');
}

function setup(){
  createCanvas(200,200);
}

function draw(){
  //this draws the fluffyCatImg at 0,0 in our sketch window
  image(fluffyCatImg,0,0);
}
```

You can also optionally specify the image's width and height.

```
image(fluffyCatImg,0,0,100,200);
//the image is drawin at 0,0 and is 100 wide, 200 high
```

## Text

Specify the string or a string variable, followed by the x and y coordinate.

```
text("Here is some text",100,100);
```

Text is affected by stroke, fill and strokeWeight.

There are [many options](http://p5js.org/reference/#group-Typography), including loading fonts, and setting size and style.

#### Change font size

```textSize(18);```

## Homework

## Read
- Review Getting Started With p5.js chapters 5 and 6

## Attend
- [Processing Community Day NYC](http://processing.nyc)
- Pick one of the talks or workshops you attend and write a short 1-3 paragraph post describing what you learned or thought about.
- Those not attending: Read Chapter 1, What Is Poetic About Computation?, and Chapter 2, Memory: To Remember and To Forget, in [Poetic Computation Reader](http://poeticcomputation.info/).
- Write a page response. Think about what you have read and form your own answer to what is poetic about computation?

## Digital Zine
- create a Canvas that is at least 600 by 600 pixels
- Create an abstract collage
- Build it up from at least 3 images, or as many as you would like
- You can use text as well
- At the top of the draw, set a tint

tint example

```  tint(0, 153, 204, 126); // Tint blue and set transparency```

This will be a work we'll critique, so spend time refining your image.
