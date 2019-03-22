# Week 9

# Schedule today
- How is everyone doing?
- Big questions, concerns, confusions?

# Review Autonomous Drawing Objects Part 1
- pairs
- feedback



# Timers! using millis()

After learning about Classes/Objects, timers are much easier! :0

We've discussed a number of built-in variables with p5js such as *width* and *mouseIsPressed*. One of the other built-in variables is millis() which returns the number of milliseconds that have occurred since your program started. Keep in mind there are 1000 milliseconds per second.

```
var timeSinceStart = millis();

print(timeSinceStart);
```

#### How many milliseconds in.... 

##### an hour?

1000 milliseconds per second * 60 seconds per minute * 60 minutes in an hour

```1000 * 60 * 60 = 3600000```

### Simplest Timer

Let's suppose we want an alarm to go off in 5 seconds. 5 seconds is 5000 millis.

```
var alarmTime = 5000;

function setup(){
  noCanvas();
}

function draw(){
  if (millis() > alarmTime){
    print("RING RING RING");
  }
}
```

If we run this, we see nothing for 5 seconds, then we see a constant printing of "RING RING RING" in the console. Why?

### Alarm goes off every X number of seconds

```
var alarmTime = 5000;

function setup(){
  noCanvas();
}

function draw(){
  if (millis() > alarmTime){
    print("RING RING RING");
    alarmTime = alarmTime + 5000;
  }
}
```

Every 5000 millis, we print "RING RING RING" then add 5000 to the alarmTime. Since our draw is constantly running, in 5 seconds it will again print "RING RING RING" add more time to the alarmTime, and start checking again, etc etc



# Changing state

How do you have random events occur, such as a change in direction of motion?

We want to change the location of our objects. Our object has its own x and y position, and may have a speed and other changing values. Any value that needs to change over time is a variable. 

What parts do we need to make something change direction randomly at different times? We need a timer to tell us when to change the direction. Changing the direction can be its own method in the class. So first we'll make a timer. We can put this timer in a method inside our class. Each time we reach the timer value we'll run changeDirection, pick a new timer to count to, and begin counting to that timer again.

How do we create changeDirection? THis method is also in the class. There are several ways to change direction. One way is to change the speed in the x-direction and y-direction.

- in-class challenge

# Studio Time to work on Autonomous Drawing Objects

# Watch and Read

- watch this short [video](https://www.youtube.com/watch?v=AiVw8crgfB4) of Roxy Paine's Scumak No. 2
- Read this short [exhibition description](https://www.jamescohan.com/attachment/en/599f12405a4091c6048b4568/TextOneColumnWithFile/599f12855a4091c6048b5e82) of Roxy Paine's exhibit Machinations. 

## Creating an animation

In this example, we preload a number of images that go together in a sequence into an array. Using a timer, we test in our draw loop to see if enough time has elapsed greater than the total wait time, and if so we advance the number of our frame. We draw the image in the array corresponding to that frame number, making sure to reset the frame number to 0 first if we've advanced to a frame number beyond the highest image number in the array.

```
var numOfFrames = 6;
var frame = 0; // our starting frame number
var animation = [];
var timer = 1000; //how long are we waiting to change the image?

function preload(){
  for (var i = 0; i < numOfFrames; i++){
    animation[i] = loadImage(i+'.jpg');
  }
}

function setup(){
  createCanvas(400,400);
}

function draw(){
  if (millis() > timer){
    timer = millis() + 1000;
    frame++;
  }
  if (frame == numOfFrames){
    frame = 0;
  }
  
  image(animation[frame],0,0);
}

```

# Homework

## Finish Autonomous Drawing Machine

For this assignment, you are designing an autonomous drawing object. This is somewhat like a car that has driven through a puddle of paint, leaving a mark behind of its route. You must create a Class that will produce objects. The class will define an object with a shape, color, motion. Create a compelling class for objects that appear to have a mind of their own. Your class should contain enough variables so that each produced object has its own unique outcome, perhaps even making use of random, or perhaps using specified parameters, or both.

Part 2 - Due March 29

FINAL REQUIREMENTS:
- Create several classes, no fewer than 3. Each will produce a number of objects, using a for loop to create them in an array. Each class should have different colors, shapes, behavior, motions. The end result should be an interesting moving generative work.
- Your program must use sound as an essential part of an object's behavior! In other words, sound should be activated when an object collides, walks off screen, bounces or other event. You don't need to have sounds for all of these actions, but pick at least onefor each of your classes/objects.

#### Writing about your Autonomous Drawing Machine

- Read [No Man's Sky Is Like 18 Quintillion Bowls of Oatmeal](https://motherboard.vice.com/en_us/article/nz7d8q/no-mans-sky-review).  In your own words what is the "10,000 Bowls of Oatmeal" problem?
 - Show screenshots or saved images from your software during at least 2 earlier stages and in your final version. As you've worked on it, how have you modified your software over time to make more interesting outcomes?

 
