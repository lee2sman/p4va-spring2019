# Week 13

- checkin
- text-manipulation: dada text projects
- p5js in the ecosystem of the web
- Processing and its relation to p5js
- The basics of Processing and when you may want to use it
- Final project proposals
- studio time and one-on-one feedback
- Josh Davis/Praystation lecture

# The Ecosystem of the web

So far we have been using p5js in the context of the web editor. The web editor makes it easy to code in p5js, host and share your code and sketches online. It abstracts away having to deal with some of the details of presenting the work.

When you pop out the sidebar on the left side of the editor there is a file selector. This is where you can add files such as images, sound, text for example - which we've been doing throughout the semester. We've noticed the index.html file and the style.css file, but we haven't used it so far. Today we'll dive further into those and what they are for.

![sidebar in the p5js editor](sidebar.png)

We have been coding our p5js code in a file called sketch.js. Now let's look at the index.html and style.css files. Web Design is a huge realm and is covered extensively in the New Media foundation course Intro to Web, so we'll just touch on the basics, enough to understand the underlying ecosystem supporting our p5js sketches.

#### HTML

HTML stands for HyperText Markup Language. 

**Hypertext - text that has the ability to link - to make a connection in the page to another webpage elsewhere on the internet.**

**Markup Language - instructions in standardized notation to specify the structure of a document and its presentation. In text one specifies data or content and how it will be displayed.**

If you click on the ```index.html``` file inside the web editor, you will see basic webpage.

```
<!DOCTYPE html>
<html>
  <head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.3/p5.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.3/addons/p5.dom.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.3/addons/p5.sound.min.js"></script>
    <link rel="stylesheet" type="text/css" href="style.css">
    <meta charset="utf-8" />

  </head>
  <body>
    <script src="sketch.js"></script>
  </body>
</html>
```

We'll go through each line.

The first line specifies that our document is HTML. You'll notice that HTML is written with what are called tags. They are words inside angle brackets (aka greater than, and less than symbols). HTML is written in a branching manner. The whole rest of the document is nested inside of an html tag. The <html> tag starts on the second line. Everything that comes after will be HTML code, which will end with the enclosing </html> tag on the last line. We call tags that begin with ```/``` a closing tag. Inside the html section are two main sub-sections on almost every webpage. There is a ```<head></head>``` section, and a ```<body></body>``` section. 

The ```<head></head>``` section contains links to the p5js library, a collection of pre-written code with builtin variables, functions, methods for example. This is what allows us to write a preload(), setup() and draw() and the web browser to know to load preload first, setup once at the beginning, and then run draw in a loop, among many other things.
After loading p5js, we load in two other things:p5sound and p5dom. p5sound let's us work with sound. In other words, this is what allows us to use p5's sound methods. p5dom is an additional library to let us write code in p5js to affect other parts of a website. 

We have been coding our projects to visually present on a canvas. A canvas is a digital element on a webpage. It sits in a webpage but it is not the entire web page. This is why if you create a canvas at a set pixel dimension (for example 400 by 400) you'll see your canvas in the top left corner of a big white screen. 

##### windowWidth, windowHeight
To set your canvas to be the size of the entire window, we have used ```createCanvas(windowWidth, windowHeight);```. 

But our canvas is still sitting as an element within the website. p5dom let's us also address other parts of the web outside of the canvas. For example, We could make a traditional regular website, and then have our canvas as one of the additional elements on the webpage. 

The ```<body></body>``` section contains all of the content that gets seen visually on a website. In the body section of our index.html page we load up the script sketch.js. Inside this sketch, we create a canvas and draw things to that canvas. We could also add other content outside of the canvas, things like text, video, images that do not have to be just on the canvas. 


### Final Project work

