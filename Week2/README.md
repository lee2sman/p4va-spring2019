# Week 2

- Questions/challenges?
- Review of assignments
- Presentation on artist research
- Variables!
- Debugging with print
- Conditionals
- Loops
- Events
- Homework

## Variables

Variables are symbolic containers. It is a symbol that contains a value that you want to change while your program is running. An example is age. I always have an age, but the value of age changes over time. Each year that I continue to *run*, the value of my age increases by 1. When I was born my age was 0. A year later on my birthday, 1 was added to my age. A year after that another 1 was added to my age. And so on.

In your code sketch, any value that you want to change over time should be a variable. You have already been working with built-in variables, mouseX and mouseY. As a test, let's print out the value of mouseX.

```
function setup(){
  createCanvas(200,200);
}

function draw(){
  print(mouseX);
}
```

Run the program and look in the console. As you move around the mouse, draw is continuously (approximately 60 times a second) printing the variable mouseX's value. Notice that if you hold the mouse in one spot the value doesn't change. What happens when you move the mouse off the canvas?

We can also create our own variables. There are two parts to create a variable: declaring and initializing.

### Declaring a variable

Declaring is when you name a variable. You are telling the program *"I want a variable. I'm calling it age."*

In some languages, you have to specify what kind of variable you want depending on what you want it to hold, like a decimal, a word, a whole number, or something else. In p5.js (and Javascript), you only have to say ```var``` to show you want a variable and follow it with the name of the variable you would like.

```
var age;
```

### Initializing a variable

After you declare a variable you need to set it to some value. This is called initializing a variable.

```
age = 22;
```

We can also set a variable equal to an equation, including with other variables.

```
var myAge
var mySistersAge;

myAge = 54;
mySistersAge = myAge - 3;
```

#### Initializing and Declaring together

You can initialize and declare a variable at the same time.

Example

```
var myAge = 28;
```

### A quick note on Debugging using print

When you get stuck while programming, you might be confused why your program is acting a certain way. Many times, it's because your variable is not set to what you think it should be set to. We can use the print command to tell us the value of a variable. You can print text and/or the value of a variable. It will appear in the console.

example

```
print("mouseX is "+mouseX);
```

### Local vs. Global Variables

In Javascript, the location where you *declare* your variable is important. It sets where you are allowed to use that variable's value in the rest of your program.

If you declare a variable inside a function then it cannot be used inside other functions.

**To be able to use a particular variable anywhere in your program, you need to declare it globally. By habit, most programmers will declare their variables at the very top of their program, before their setup.**

Example with a global variable, accessible everywhere

```
var mySistersAge = 24;

function setup(){
  noCanvas(); //use this when you don't need a canvas

  print("My sister's age is "+mySistersAge);
}
```

Example with a local variable, only accessible inside its own function

```
function setup(){
  noCanvas();

  var mySistersAge = 24;
}

function draw(){
  print("My sister's age is "+mySistersAge);
  //THIS WILL CREATE AN ERROR!
}
```

This will not work and instead create an error in the console. It does not work because the variable mySistersAge was created *inside* the setup function. This means it is a local variable that can only work inside setup and therefore will not work inside the draw function. To have it work in both, it needs to be created globally, outside of these functions, and best practices is to create it at the top of the program. Note: it is where the variable is *declared* (not initialized) that sets whether it is local or global.

### Moving Ball

We are used to reading from left to right.

But when you set the value of a variable you first take everything to the right of the equal sign and that value is placed in the variable.

Take the following example. What do you expect to see?

```
var ballX=0;

function setup(){
  createCanvas(200,200);
}

function draw(){
  ellipse(ballX,height/2,20,20);  
  ballX = ballX + 1;
}
```

The line ```ballX = ballX + 1``` may look strange but it's perfectly valid. We start on the right side of the equal sign, so we are taking the current value of ballX, whatever it is, and adding 1 to it. When the program starts, ballX has been set to 0. So 0 + 1 is 1. Finally, we look on the left side of the equal sign. We see ballX there, so we set ballX equal to that amount, 1. The next time we run draw we start on the right side of the equal sign. ballX is 1 and we add 1 to it, totalling 2. So we set ballX (which is on the left side of the equal sign) to be 2.

#### Shorthand way to increase or decrease a variable

There are some shorthand ways to increase or decrease a variable. To simplify writing ```someVariable = someVariable + 1;``` you can instead write ```someVariable++;``` Likewise, if you want to write ```someVariable = someVariable - 1;``` that can be simplified as ```someVariable--;```. The number doesn't always have to change by 1. If you want to increase a variable by the number 10 for example, instead of ```someVariable = someVariable+10;``` you can write ```someVariable += 10;```.

## Random

How do we get a random number? We can ask a friend, try to pick one without thinking too hard, or luck up a number in a book. In programming, there are a number of ways to generate a random number. p5.js has the ```random``` function.

By itself, random will generate a random decimal (called a float) between 0 and 1. Commonly, we will want to get a random number between a certain minimum and maximum value. We can specify this range and get a result.

```
var myNum = random(10,100);

print(myNum); //will print a number between 10 and 100, like 76.87680
```

If you want an integer, a whole number, you need to round it.

```
var myNum = round(random(10,100));

print(myNum); //will print a whole number between 10 and 100, like 76
```

**random must be used after setup starts and createCanvas runs.** If you want to create a random global variable you must first declare it globally at the start before setup, and then initialize it with random in the setup.


### Random Face Jam

Take your face you started last week and replace with variables. Try creating x and y variables such as eyeX, eyeY and width and height, like mouthWidth, mouthHeight. Create these as global variables and try running the program several times with different values based on using random.

# Conditionals

In the above section we created a ball, then changed its x location by having the ballX variable increase. The ball kept moving to the right and eventually moved off the screen. How do we get it back if the program keeps running?

A conditional is a test. We can state it like this: *If this thing is true, then do this:*

### If statement

The way we do this in code is with an **IF statement**.

In p5.js it looks like this.

```
var myName = 'Lee';

if (myName == 'Lee'){
  print('Hi Lee');
}
```

The *if* tells the software to evaluate whatever follows that in the *( )* parenthesis. If what is in the parenthesis is true, then it will do the action within the following *{ }* brackets.

What's with the double equal sign? Due to the way the software works, if you use a single equal sign, the program will immediately take anything to the right of the equal sign and place it in the variable on the left. And then since they are equal, the if statement will say, yes, it's true and then always perform the actions in the following { } brackets. To get around this issue, when we are coding we use the double equal sign == which means *test if they are equal*.


```
//NOTE THIS PROGRAM IS SHOWING A MISTAKE!
var myName = 'Pierre';

if (myName = 'Lee'){ //this line has a mistake! should be ==
  print('Hi Lee'); //This will print out because of the mistake above!
}
```

Now that we know about conditionals, we can fix our moving ball program from earlier. Now we will add a conditional statement. **If** the ball goes off screen to the right, let's have it appear again on the left side of the canvas. How do we do this? Let's check where the ball's x position is located.

```
var ballX = 0;

function setup(){
  createCanvas(200,200);
}

function draw(){
  ellipse(ballX,height/2,20,20);

  ballX++;

  if (ballX > 200){
    ballX = 0;
  }
}
```

We have already learned about the builtin variables mouseX and mouseY. There are also the builtin variables ```width``` and ```height```, that are set to the width and height of the canvas once createCanvas in setup runs. In our code above we can replace the line ```if (ballX > 200){ }``` with ```if (ballX > width){ }```


### Else Statement

Sometimes we need to be able to choose from several options. We use *else* and *else if* to create the options.

```
var parkingTickets = 120;

if (parkingTickets < 50){
  print("That's annoying, but you can pay that.");
} else if (parkingTickets < 80){
  print("Better pay off that bill and try to save some money.");
} else {
  print("That's so much money. Better wise up! You owe $"+parkingTickets);
}
```

*else* is the default. If nothing else is true in the if and else if statements then the else statement will be executed.


### Checking multiple things

Sometimes it's not enough to test one thing. You can use and,  or.

```&&``` = AND

```||``` = OR

example

```
if ((myName == 'Lee') && (myAge < 60)){
  print("that's probably him");
}

# Looping

Sometimes we want to do something many times. Over and over again.

We use loops to do this.


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

## Events

An event is something your web browser does or something the user of your software does which indicates interaction. Examples are pressing a mouse button, dragging the cursor across the screen or pressing a key. p5.js gives a number of built-in functions to make it easier to work with events.

A full list of events can be found in the p5.js Reference [section on events](http://p5js.org/reference/#group-Events)

```
function mousePressed(){
  //this code will run anytime the mouse is Pressed
  print('you clicked');
}

function keyPressed(){
  //this function runs anytime you press a key
   if (keyCode === LEFT_ARROW) {
    //move left
   } else if (keyCode === RIGHT_ARROW) {
    //move right
  }
}
```

Events happen independently of (outside) the draw loop.

# Homework

## Read

- Getting Started with p5.js Chapters 5 and 6

## Tutorials

- Watch The Coding Train tutorials
  - [Variables](https://www.youtube.com/watch?v=RnS0YNuLfQQ&list=PLRqwX-V7Uu6Zy51Q-x9tMWIv9cueOFTFA&index=7)
  - [Make your own variables](https://www.youtube.com/watch?v=Bn_B3T_Vbxs&index=8&list=PLRqwX-V7Uu6Zy51Q-x9tMWIv9cueOFTFA)
  - [If Statements](https://www.youtube.com/watch?v=1Osb_iGDdjk)
  - We didn't get to this in class but will cover next week: [For Loops](https://www.youtube.com/watch?v=cnRD9o6odjk&t)

## Research: Web as platform for programming and art

Check out this great [list](https://www.artsy.net/article/artsy-editorial-10-artistic-masterpieces-meant-experienced-online) of *10 Artistic Masterpieces Meant to Be Experienced Online*. Not all of these projects would be classified as artworks made with programming, but many are. One thing for us to consider, especially as we are learning to code, is how much we want to engage with the web. Is your work meant to be viewed in a gallery? online? outside? Where does the work lie? And based on this, what is the form your work should take? Select one of the works from the article and really experience it. What do you find meaningful in the work? How does the artwork really use the web as a platform? What can you learn from this work or any other projects here that will inform artwork you want to make?
- Write a short response (1 - 3 paragraphs) where you examine at least one of these projects from the list, describe it and your perceptions of it, and answer these questions about your own practice.

# Bouncing Ball

Take our bouncing ball starter code from [here](https://editor.p5js.org/2sman/sketches/77EtIEz_5). Duplicate the code sketch. Now add:

- when the ball bounces, change the color
- when the ball bounces, change the size of the ball
- when the ball bounces, change the speed of the ball

Hints: Think about what new variables you need. You'll need variables for the r, g and b color, for the width and height of the ball (could be the same), and the speed.

Post your link to Moodle.

# Your Face

Finish working on your face project. Have a variety of variables for your face, for its colors, locations of its features, etc. When you click or press a button, have the face get randomized. Post a link to Moodle.
