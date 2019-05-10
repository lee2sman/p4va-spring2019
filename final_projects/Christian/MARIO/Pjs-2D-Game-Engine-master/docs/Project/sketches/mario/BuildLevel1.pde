final int BLOCK = 16,
          screenWidth = 32*BLOCK,
          screenHeight = 27*BLOCK;

/**
 * Gravity
 */
float DOWN_FORCE = 1.1;
float ACCELERATION = 1.1;
float DAMPENING = .75;



void initialize() {
  frameRate(35);
  reset();
}

void reset() {
  clearScreens();
  addScreen("MainLevel", new MainLevel(4*width, height));  
}





class MainLevel extends Level {
  MainLevel(float levelWidth, float levelHeight) {
    super(levelWidth, levelHeight);
    addLevelLayer("background layer", new MainBackgroundLayer(this));
    addLevelLayer("main layer", new MainLevelLayer(this));
    setViewBox(0,0,screenWidth,screenHeight);
    // And of course some background music!
    SoundManager.load(this, "audio/bg/Overworld.mp3");
    SoundManager.play(this);
  }
}



class MainBackgroundLayer extends LevelLayer {
  Mario mario;
  MainBackgroundLayer(Level owner) {
    super(owner, owner.width, owner.height, 0,0, 0.75,0.75);
    setBackgroundColor(color(0, 100, 190));
    addBackgroundSprite(new TilingSprite(new Sprite("graphics/backgrounds/sky_2.gif"),0,0,width,height));
  }
  void draw() {
    super.draw();
    
    
    if(mario!=null && mario.active != null && mario.active.name!="dead" && mario.y>height) {
      reset();
    }
  }
}



class MainLevelLayer extends LevelLayer {
  Mario mario;
  
  MainLevelLayer(Level owner) {
    super(owner);
   
    addBackgroundSprite(new TilingSprite(new Sprite("graphics/backgrounds/sky.gif"),0,0,width,height));



    // Mario placement
    mario = new Mario();
    mario.setPosition(32, height-64);
    addPlayer(mario);

    // slanted hills
    addSlant(206, height-48);
    addSlant(1300, height-48);
    addSlant(1350, height-48);
    
    

  
    addBoundary(new Boundary(-1,0, -1,height));
    addBoundary(new Boundary(width+1,height, width+1,0));

    // add general ground
    addGround("ground", -32,height-48, -32 + 17*32,height);
    addBoundary(new Boundary(-32 + 17*32,height-48,-32 + 17*32,height));

    addInteractor(new Muncher(521, height-10));
    addInteractor(new Muncher(536, height-10));
    addInteractor(new Muncher(552, height-10));
    addInteractor(new Muncher(567, height-10));

    addBoundary(new Boundary(-31 + 19*32,height,-31 + 19*32,height-48));
    addGround("ground", -31 + 19*32,height-48, width+32,height);

    
    addBushes();


    //platforms    
    addGroundPlatform("ground", 928, height-224, 96, 112);
    addGroundPlatform("ground", 738, height-160, 96, 112);
    addCoins(717,height-170,128);
    addCoins(309,height-140,128);
    addGroundPlatform("ground", 312, height-128, 128, 80);
    addCoins(928,height-236,96);
    addGroundPlatform("ground", 920, height-176, 32, 64);
    addGroundPlatform("ground", 912, height-128, 128, 80);
    addCoins(912,height-140,128);
    addGroundPlatform("ground", 976, height-96, 128, 48);
    addGroundPlatform("ground", 1442, height-128, 128, 80);
    addCoins(1442,height-140,128);
    addGroundPlatform("ground", 1442+64, height-96, 128, 48);
    
   
    addForPlayerOnly(new DragonCoin(352,height-164));

   // Koopa koopa = new Koopa(254, height-178);
    Koopa koopa = new Koopa(204, height-178);
    addInteractor(koopa);

    addTriggers();
    addGoal(1920, height-48);
  }
  
  
  void addGround(String tileset, float x1, float y1, float x2, float y2) {
    TilingSprite groundline = new TilingSprite(new Sprite("graphics/backgrounds/"+tileset+"-top.gif"), x1,y1,x2,y1+16);
    addBackgroundSprite(groundline);
    TilingSprite groundfiller = new TilingSprite(new Sprite("graphics/backgrounds/"+tileset+"-filler.gif"), x1,y1+16,x2,y2);
    addBackgroundSprite(groundfiller);
    addBoundary(new Boundary(x1,y1,x2,y1));
  }
  
 
  void addSlant(float x, float y) {
    Sprite groundslant = new Sprite("graphics/backgrounds/ground-slant.gif");
    groundslant.align(LEFT, BOTTOM);
    groundslant.setPosition(x, y);
    addBackgroundSprite(groundslant);
    addBoundary(new Boundary(x, y + 48 - groundslant.height, x + 48, y - groundslant.height));
  }


  
  void addBushes() {
    int[] bush = {
      1, 3, 4, 5
    };
    for (int i=0, xpos=0, end=bush.length; i<end; i++) {
      Sprite sprite = new Sprite("graphics/backgrounds/bush-0"+bush[i]+".gif");
      xpos += sprite.width;
      sprite.align(CENTER, BOTTOM);
      sprite.setPosition(116 + xpos, height-48);
      addForegroundSprite(sprite);
    }

    // bush8S
    bush = new int[] {
      1, 2, 4, 2, 3, 4, 2, 5
    };
    for (int i=0, xpos=0, end=bush.length; i<end; i++) {
      Sprite sprite = new Sprite("graphics/backgrounds/bush-0"+bush[i]+".gif");
      xpos += sprite.width;
      sprite.align(CENTER, BOTTOM);
      sprite.setPosition(384 + xpos, height-48);
      addForegroundSprite(sprite);
    }

    // bush3
    bush = new int[] {
      1, 3, 4, 5
    };
    for (int i=0, xpos=0, end=bush.length; i<end; i++) {
      Sprite sprite = new Sprite("graphics/backgrounds/bush-0"+bush[i]+".gif");
      xpos += sprite.width;
      sprite.align(CENTER, BOTTOM);
      sprite.setPosition(868 + xpos, height-48);
      addForegroundSprite(sprite);
    }

    // bush4
    bush = new int[] {
      1, 2, 4, 3, 4, 5
    };
    for (int i=0, xpos=0, end=bush.length; i<end; i++) {
      Sprite sprite = new Sprite("graphics/backgrounds/bush-0"+bush[i]+".gif");
      xpos += sprite.width;
      sprite.align(CENTER, BOTTOM);
      sprite.setPosition(1344 + xpos, height-48);
      addForegroundSprite(sprite);
    }
  }

 
  void addGroundPlatform(String tileset, float x, float y, float w, float h) {
    Sprite lc = new Sprite("graphics/backgrounds/"+tileset+"-corner-left.gif");
    lc.align(LEFT, TOP);
    lc.setPosition(x, y);
    
    Sprite tp = new Sprite("graphics/backgrounds/"+tileset+"-top.gif");
    Sprite rc = new Sprite("graphics/backgrounds/"+tileset+"-corner-right.gif");
    rc.align(LEFT, TOP);
    rc.setPosition(x+w-rc.width, y);
    TilingSprite toprow = new TilingSprite(tp, x+lc.width, y, x+(w-rc.width), y+tp.height);

    addBackgroundSprite(lc);
    addBackgroundSprite(toprow);
    addBackgroundSprite(rc);

    // sides/filler
    TilingSprite sideleft  = new TilingSprite(new Sprite("graphics/backgrounds/"+tileset+"-side-left.gif"),  x,            y+tp.height, x+lc.width,     y+h);
    TilingSprite filler    = new TilingSprite(new Sprite("graphics/backgrounds/"+tileset+"-filler.gif"),     x+lc.width,   y+tp.height, x+(w-rc.width), y+h);
    TilingSprite sideright = new TilingSprite(new Sprite("graphics/backgrounds/"+tileset+"-side-right.gif"), x+w-rc.width, y+tp.height, x+w,            y+h);

    addBackgroundSprite(sideleft);
    addBackgroundSprite(filler);
    addBackgroundSprite(sideright);

    
    addBoundary(new Boundary(x, y, x+w, y));
  }

  
  void addCoins(float x, float y, float w) {
    float step = 16, i = 0, last = w/step;
    for(i=0; i<last; i++) {
      addForPlayerOnly(new Coin(x+8+i*step,y));
    }
  }

  
  void addGoal(float xpos, float hpos) {
    hpos += 1;
    // background post
    Sprite goal_b = new Sprite("graphics/assorted/Goal-back.gif");
    goal_b.align(CENTER, BOTTOM);
    goal_b.setPosition(xpos, hpos);
    addBackgroundSprite(goal_b);
    // foreground post
    Sprite goal_f = new Sprite("graphics/assorted/Goal-front.gif");
    goal_f.align(CENTER, BOTTOM);
    goal_f.setPosition(xpos+32, hpos);
    addForegroundSprite(goal_f);
    // the finish line rope
    addForPlayerOnly(new Rope(xpos, hpos-16));
  }
  
 
  void addTriggers() {
    addTrigger(new KoopaTrigger(412,0,5,height, 350, height-64, -0.2, 0));
    addTrigger(new KoopaTrigger(942,0,5,height, 350, height-64, -0.2, 0));
    addTrigger(new KoopaTrigger(392,0,5,height, 350, height-64, -0.2, 0));
    addTrigger(new KoopaTrigger(322,0,5,height, 350, height-64, -0.2, 0));
    addTrigger(new KoopaTrigger(12,0,5,height, 350, height-64, -0.2, 0));
    addTrigger(new KoopaTrigger(25,0,5,height, 350, height-64, -0.2, 0));
   addTrigger(new KoopaTrigger(562,0,5,height, 350, height-64, -0.2, 0));
   addTrigger(new KoopaTrigger(916,0,5,height, 350, height-64, -0.2, 0));
    addTrigger(new BanzaiBillTrigger(1446,310,5,74, 400, height-84, -6, 0));
  }




  void draw() {
    super.draw();
    viewbox.track(parent, mario);
   
    if(mario!=null && mario.active != null && mario.active.name!="dead" && mario.y>height) {
      reset();
    }
  }
}


class Mario extends Player {
  
  int score = 0;
  float speed = 2;

  Mario() {
    super("Mario");
    setStates();
    handleKey('W');
    handleKey('A');
    handleKey('S');
    handleKey('D');
    setImpulseCoefficients(DAMPENING, DAMPENING);
    setForces(0, DOWN_FORCE);
    setAcceleration(0, ACCELERATION);
  }
  
  
  void setStates() {
    
    addState(new State("idle", "graphics/mario/small/Standing-mario.gif"));

    
    addState(new State("running", "graphics/mario/small/Running-mario.gif", 1, 4));

   
    State dead = new State("dead", "graphics/mario/small/Dead-mario.gif", 1, 2);
    dead.setAnimationSpeed(0.25);
    
    
    dead.setDuration(100);
    addState(dead);   
    SoundManager.load(dead, "audio/Dead mario.mp3");
    
    
    State jumping = new State("jumping", "graphics/mario/small/Jumping-mario.gif");
    jumping.setDuration(15);
    addState(jumping);
    SoundManager.load(jumping, "audio/Jump.mp3");

 
 
 
    State won = new State("won", "graphics/mario/small/Standing-mario.gif");
    won.setDuration(240);
    addState(won);

  
    setCurrentState("idle");
  }
  

  void handleInput() {
    
    if(active.name=="dead" || active.name=="won") return;
    
    
    if(isKeyDown('A') || isKeyDown('D')) {
      if (isKeyDown('A'))
      {
       
        setHorizontalFlip(true);
        addImpulse(-speed, 0);
        setViewDirection(-1, 0);
      }
      if (isKeyDown('D')) {
       
        setHorizontalFlip(false);
      
        addImpulse(speed, 0);
        setViewDirection(1, 0);
      }
    }
    
  
    if(isKeyDown('W') && active.name!="jumping" && boundaries.size()>0) {
    
      addImpulse(0,-35);
     
      setCurrentState("jumping");
      SoundManager.play(active);
    }
    
  
    if (active.mayChange())
    {
     
      if(isKeyDown('A') || isKeyDown('D')) {
        setCurrentState("running");
      }
      
 
      else {
        setCurrentState("idle");
      }
    }
  }
  
 
  void handleStateFinished(State which) {
    if(which.name == "dead" || which.name == "won") {
      removeActor();
      reset();
    } else {
      setCurrentState("idle");
    }
  }
  
  
  //INTERACTIONS NOTE ENEMEY
  
  
  void overlapOccurredWith(Actor other, float[] direction) {
    if (other instanceof Koopa) {
      Koopa koopa = (Koopa) other;
      float angle = direction[2];

   
      float tolerance = radians(75);
      if (PI/2 - tolerance <= angle && angle <= PI/2 + tolerance) {
        koopa.squish();
        stop(0,0);
        setImpulse(0, -30);
        setCurrentState("jumping");
      }

      //WHEN YA DUN MESSED UP
      else { die(); }
    }
  }

 
 
  void die() {
    setCurrentState("dead");
    
    setInteracting(false);
    addImpulse(0,-30);
    setForces(0,3);
   
    SoundManager.stop(getLevelLayer().getLevel());
    SoundManager.play(active);
  }

  
  
  
  void pickedUp(Pickup pickup) {
    if (pickup.name=="Regular coin") {
      score++;
    }
    else if (pickup.name=="Dragon coin") {
      score+=100;
    }
    // winning
    
    else if (pickup.name=="Finish line") {
      setCurrentState("won");
    }
  }
  
}


class Koopa extends Interactor {

  Koopa(float x, float y) {
    super("Koopa Trooper");
    setStates();
    setForces(-0.25, DOWN_FORCE);    
    setImpulseCoefficients(DAMPENING, DAMPENING);
    setPosition(x,y);
  }
  
 
  void setStates() {
    
    State walking = new State("idle", "graphics/enemies/Red-koopa-walking.gif", 1, 2);
    walking.setAnimationSpeed(0.12);
    
    SoundManager.load(walking, "audio/Squish.mp3");
    
    addState(walking);
    
   
    State naked = new State("naked", "graphics/enemies/Naked-koopa-walking.gif", 1, 2);
    naked.setAnimationSpeed(0.12);
    SoundManager.load(naked, "audio/Squish.mp3");
    addState(naked);
    
    setCurrentState("idle");
  }
  
 //hes a smart boy now
  void gotBlocked(Boundary b, float[] intersection) {
    if (b.x==b.xw) {
      fx = -fx;
      setHorizontalFlip(fx > 0);
    }
  }
  
  void squish() {
    SoundManager.play(active);

    
    if (active.name != "naked") {
      setCurrentState("naked");
      return;
      
      
    }
    

    removeActor();
  }
}


class Muncher extends Interactor {

  Muncher(float x, float y) {
    super("Muncher");
    setPosition(x,y);
    setupStates();
  }

  void setupStates() {
    State munch = new State("munch","graphics/enemies/Muncher.gif", 1, 2);
    munch.setAnimationSpeed(0.20);
    addState(munch);
  }

  void overlapOccurredWith(Actor other, float[] overlap) {
    super.overlapOccurredWith(other, overlap);
    if (other instanceof Mario) {
      ((Mario)other).die();
    }
    
    
  }
  
}


class BanzaiBill extends Interactor {

  
  BanzaiBill(float mx, float my) {
    super("Banzai Bill", 1, 1);
    setPosition(mx, my);
    setImpulse(-0.5, 0);
    
    
    setForces(0, 0);
    setAcceleration(0, 0);
    
    setupStates();
  
    setPlayerInteractionOnly(true);
  }

  
  void setupStates() {
    State flying = new State("flying", "graphics/enemies/Banzai-bill.gif");
    SoundManager.load(flying, "audio/Banzai.mp3");
    addState(flying);
    setCurrentState("flying");
    SoundManager.play(flying);
  }

  
  void overlapOccurredWith(Actor other, float[] overlap) {
    super.overlapOccurredWith(other, overlap);
    if (other instanceof Mario) {
      ((Mario)other).die();
    }
  }
}


class MarioPickup extends Pickup {
  MarioPickup(String name, String spritesheet, int rows, int columns, float x, float y, boolean visible) {
    super(name, spritesheet, rows, columns, x, y, visible);
  }
  
  
  void gotBlocked(Boundary b, float[] intersection) {
    if (intersection[0]-x==0 && intersection[1]-y==0) {
      fx = -fx;
      active.sprite.flipHorizontal();
    }
  }
}



class Coin extends MarioPickup {
  Coin(float x, float y) {
    super("Regular coin", "graphics/assorted/Regular-coin.gif", 1, 4, x, y, true);
    SoundManager.load(this, "audio/Coin.mp3");
  }
  void pickedUp() { 
    SoundManager.play(this);
  }
}


class DragonCoin extends MarioPickup {
  DragonCoin(float x, float y) {
    super("Dragon coin", "graphics/assorted/Dragon-coin.gif", 1, 10, x, y, true);
    SoundManager.load(this, "audio/Dragon coin.mp3");
  }
  void pickedUp() { 
    SoundManager.play(this);
  }
}


class Rope extends MarioPickup {
  Rope(float x, float y) {
    super("Finish line", "graphics/assorted/Goal-slider.gif", 1, 1, x, y, true);
    Sprite s = getState("Finish line").sprite;
    s.align(LEFT, TOP);
    s.setNoRotation(true);
    s.addPathLine(0, 0, 1, 1, 0, 0, -116, 1, 1, 0, 50);
    s.addPathLine(0, -116, 1, 1, 0, 0, 0, 1, 1, 0, 50);
    s.setLooping(true);
    SoundManager.load(this, "audio/bg/Course-clear.mp3");
  }

  void pickedUp() {

    SoundManager.stop(getLevelLayer().getLevel());
    // victory
    SoundManager.play(this);
  }
}


class KoopaTrigger extends Trigger {
  float kx, ky, fx, fy;
  KoopaTrigger(float x, float y, float w, float h, float _kx, float _ky, float _fx, float _fy) {
    super("koopa", x, y, w, h);
    kx = _kx;
    ky = _ky;
    fx = _fx;
    fy = _fy;
  }
  void run(LevelLayer layer, Actor actor, float[] intersection) {
    Koopa k = new Koopa(x+kx, ky);
    if (fx>0) { 
      k.setHorizontalFlip(true);
    }
    layer.addInteractor(k);
   
    removeTrigger();
  }
}



class BanzaiBillTrigger extends Trigger {
  float kx, ky, fx, fy;
  BanzaiBillTrigger(float x, float y, float w, float h, float _kx, float _ky, float _fx, float _fy) {
    super("banzai bill", x, y, w, h);
    kx = _kx;
    ky = _ky;
    fx = _fx;
    fy = _fy;
  }
  
  
  
  void run(LevelLayer layer, Actor actor, float[] intersection) {
    BanzaiBill k = new BanzaiBill(x+kx, ky);
    k.setImpulse(fx, fy);
    layer.addInteractor(k);
    removeTrigger();
    
  }
  
}
