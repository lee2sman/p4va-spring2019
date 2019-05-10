define d = Character("Dani", color="#dd6e80")
define t = Character("Troy", color="#a80101")
define e = Character("Eggbert", color="#3cdcff")
define f = Character("Fox", color="#500799")
define p = Character("Pricniple Takahata (over loudspeaker)")
image dunk = Movie(play="dunk.ogg",  xpos=0, ypos=0, xanchor=0, yanchor=0)

#intro
label start:
    $ renpy.movie_cutscene("comp 1.ogv")

    play music "crushtheme.ogg"
    scene crush start
    scene crush start
    with Dissolve(.5)

    "{b}Click anywhere in the game to proceed through.{/b}"

    window hide
    pause
    window show

#part 1 of game: meeting Dani
    stop music fadeout 1.0
    play music "maintheme.ogg"
    scene crush start
    scene school building1
    with Dissolve(.5)

    "{cps=50}So this is it..."

    "{cps=50}My new school..."

    show dani0
    with Dissolve(.5)

    "???" "{cps=50}Hey what's the big idea just standing there!? I almost bumped into you."

    hide dani0
    show dani1
    with Dissolve(.5)

    menu:
        "???" "{cps=50}Wait a sec... are you new here?"

        "You bet! And I'm excited for my first day.":
            jump choice1_yes

        "Uh... yeah.":
            jump choice1_yesshy

    label choice1_yes:
        $ menu_flag = True

        hide dani1
        show dani8
        with Dissolve(.5)

        "???" "{cps=50}Haha very enthusiastic! I like that. Well, welcome to {color=#aa0d6b}Kurasshu High{/color}!"

        jump choice1_done

    label choice1_yesshy:
        $ menu_flag = False

        hide dani1
        show dani8
        with Dissolve(.5)

        "???" "{cps=50}You seem a little shy. Don't worry! Everyone here at {color=#aa0d6b}Kurasshu High{/color} is just as nice as I am!"

        jump choice1_done

    label choice1_done:

    d "{cps=50}Anyway, I'm {color=#dd6e80}Dani{/color}. What's your name?"
    python:
        name = renpy.input("What's your name?")

    hide dani8
    show dani
    with Dissolve(.5)

    d "{cps=50}Nice to meet you [name]. I think you and me are gonna be best friends!{/cps}"

    hide dani
    show dani7
    with Dissolve(.5)

    menu:
        d "{cps=50}So, I know it's only the very start of day one, but have you seen anyone you find cute yet?"

        "{cps=50}Well... not yet":
            jump choice2_no

        "{cps=50}Oh yeah! This place is filled with cute people.":
            jump choice2_yes

    label choice2_no:
        $ menu_flag = False

        hide dani7
        show dani
        with Dissolve(.5)

        d "{cps=50}Not to worry! I'll show you around and I'm sure we'll find you a crush in no time!"

        jump choice2_done

    label choice2_yes:
        $ menu_flag = True

        hide dani7
        show dani
        with Dissolve(.5)

        d "{cps=50}Haha if you think they look good out here, you should see some of our students inside!"

        jump choice2_done
    label choice2_done:

    hide dani
    show dani1
    with Dissolve(.5)

    d "{cps=50}Let me show you around!"

    scene school building1
    with Dissolve(.5)

    scene gym building
    with Dissolve(.5)
    show dani2
    d "{cps=50}This is the Gym."
    scene gym building
    with Dissolve(.5)

    scene science lab
    with Dissolve(.5)
    show dani3
    d "{cps=50}This is the Science Lab."
    scene science lab
    with Dissolve(.5)

    scene out back
    with Dissolve(.5)
    show dani9
    d "{cps=50}And this is out back behind the school."
    scene out back
    with Dissolve(.5)

#hallway. this is where you decide which place to go. You navigate back here numerous times throughout the game
    scene hall way
    with Dissolve(.5)

    show dani

    menu:
        d "{cps=50} Let me know where you wanna go and I'll take you there! Your crush awaits."

        "Gym":
            jump choice3_gym

        "Science Lab":
            jump choice3_lab

        "Behind the School":
            jump choice3_back

#Troy in the gym
    label choice3_gym:
        stop music fadeout 1.0
        scene hall way
        with Dissolve(.5)

        play music "troytheme.ogg"

        scene gym building
        with Dissolve(.5)


        show troy0:
            xpos -.25
        show dani5
        with Dissolve(.5)

        d "{cps=50} Omg!"

        hide troy0
        show troy1:
            xpos -0.25
        with Dissolve(.5)


        d "{cps=50} That's the superstar of our Basketball team {color=#a80101}Troy Eversmith.{/color}"

        menu:
            d "{cps=50}You should go talk to him!"

            "He is pretty cute... I guess I will.":
                jump choice4_yes

            "I think I'll try another place.":
                jump choice4_back

        label choice4_back:
            hide dani5
            show dani6
            with Dissolve(.5)

            d "{cps=50} If you say so. You don't really seem like you'd be into jocks anyway."

            stop music fadeout 1.0
            hide dani6
            hide troy1
            scene gym building
            with Dissolve(.5)

            play music "maintheme.ogg"

            scene hall way
            with Dissolve(.5)

            show dani
            with Dissolve(.5)

            menu:
                d "{cps=50}Let me know where you wanna go and I'll take you there! Your crush awaits."

                "Gym":
                    jump choice3_gym

                "Science Lab":
                    jump choice3_lab

                "Behind the School":
                    jump choice3_back

        label choice4_yes:
            d "{cps=50}That's what I thought! Good luck [name]"

            hide dani5
            hide troy1
            show troy2
            with Dissolve(.5)

            menu:
                t "{cps=50}Oh, hey I was just dunking some hoops... Would you grab me some water?"

                "Yeah sure":
                    jump choice5_yes

                "Uh...no":
                    jump choice5_no

            label choice5_yes:
                t "{cps=50}Thanks."

                hide troy2
                show troy4
                with Dissolve(.5)


                "{cps=50}*......*"
                hide troy4
                show troy2
                with Dissolve(.5)

                jump choice5_done

            label choice5_no:
                t "{cps=50}You're right. That's what {color=#3cdcff}Eggbert's{/color} for."
                hide troy2
                show troy3
                with Dissolve(.5)

                t "{cps=50}{color=#3cdcff}Eggbert{/color}! Water!"
                stop music fadeout 1.0
                play music "eggberttheme.ogg"

                hide troy3
                show troy2
                show eggbert2:
                    xpos 0.35
                with Dissolve(.5)

                e "{cps=50}Here you go {color=#a80101}Troy{/color}! Sorry I was late."

                hide troy2
                show troy4
                with Dissolve(.5)


                "{cps=50}*......*"

                "{cps=50}*......*"

                "{cps=50}*......*"

                hide troy4
                show troy5
                with Dissolve(.5)

                t "{cps=50}Alright you can scram."

                e "{cps=50}Right, sorry!"
                stop music fadeout 1

                hide eggbert2
                hide troy5
                show troy2
                with Dissolve(.5)
                play music "troytheme.ogg"

            label choice5_done:


            menu:
                t "{cps=50}So, you're new here right?"

                "Yeah, I just moved here.":
                    jump choice6_yes

                "...":
                    jump choice6_fail

            label choice6_fail:
                hide troy2
                show troy6
                with Dissolve(.5)

                t "{cps=50}Uh...ok I'm gonna get back to practicing."

                show dani10
                hide troy6
                with Dissolve(.5)


                d "{cps=50}Agh! You froze up!! And after only talking to him for a minute!"

                hide dani10
                show dani6
                with Dissolve(.5)

                d "{cps=50}Oh well, I guess jocks might not be your thing. Lets try to find another crush for you."
                stop music fadeout 1.0
                scene gym building
                with Dissolve(.5)

                play music "maintheme.ogg"

                scene hall way
                with Dissolve(.5)

                show dani

                menu:
                    d "{cps=50}Let me know where you wanna go and I'll take you there! Your crush awaits."

                    "Gym":
                        jump choice3_gym

                    "Science Lab":
                        jump choice3_lab

                    "Behind the School":
                        jump choice3_back

            label choice6_yes:
                menu:
                    t "{cps=50}Cool, my name's {color=#a80101}Troy{/color}."

                    "I know.":
                        jump choice7_bad

                    "Nice to meet you. My name is [name]":
                        jump choice7_good

            label choice7_bad:
                hide troy2
                show troy6
                with Dissolve(.5)

                menu:
                    t "{cps=50}Uh..."

                    "Not cuz I'm like a stalker or anything hahahahaha":
                        jump choice8_fail

                    "...Becasue everyone talks about how you're the superstar of the team!":
                        jump choice8_good

            label choice7_good:
                t "{cps=50}Good to meet ya [name]."

                hide troy2
                show troy9
                with Dissolve(.5)

                menu:
                    t "{cps=50}So, what brings you to the gym?"

                    "I heard there was a star player playing down here and I wanted to check it out.":
                        jump choice8_good

                    "Well... I heard you were good at Basketball so... I wanted to see.":
                        jump choice8_good


                label choice8_fail:
                    hide troy6
                    show troy7
                    with Dissolve(.5)

                    t "{cps=50}Um."

                    t "{cps=50}Word. I gotta get back to... Basketball."

                    show dani10
                    hide troy7
                    with Dissolve(.5)

                    d "{cps=50}What was that!!! You sounded like a total creep!"

                    hide dani10
                    show dani6
                    with Dissolve(.5)

                    d "{cps=50}You're hopeless... Well! There's always more cuties out there! Lets find 'em."
                    stop music fadeout 1.0
                    scene gym building
                    with Dissolve(.5)

                    play music "maintheme.ogg"

                    scene hall way
                    with Dissolve(.5)

                    show dani

                    menu:
                        d "{cps=50} Let me know where you wanna go and I'll take you there! Your crush awaits."

                        "Gym":
                            jump choice3_gym

                        "Science Lab":
                            jump choice3_lab

                        "Behind the School":
                            jump choice3_back
                label choice8_good:
                        hide troy6
                        show troy9
                        with Dissolve(.5)

                        t "{cps=50}Haha, I guess I am pretty impressive."
                        t "{cps=50}..."

                        menu:
                            t "{cps=50}Wanna watch me dunk?"

                            "Yeah":
                                jump choice9_yes

                            "Uh, not really":
                                jump choice9_no

                        label choice9_no:
                            hide troy9
                            show troy6
                            with Dissolve(.5)

                            t "{cps=50}Whatever, you're ugly anyway. Peace."

                            show dani10
                            hide troy6
                            with Dissolve(.5)

                            d "{cps=50}Woah! What a dick."
                            hide dani10
                            show dani6
                            with Dissolve(.5)

                            d "{cps=50}You're too good for that meathead anyway. Let's keep looking for your perfect crush."
                            stop music fadeout 1.0
                            scene gym building
                            with Dissolve(.5)

                            play music "maintheme.ogg"

                            scene hall way
                            with Dissolve(.5)

                            show dani

                            menu:
                                d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                                "Gym":
                                    jump choice3_gym

                                "Science Lab":
                                    jump choice3_lab

                                "Behind the School":
                                    jump choice3_back

                        label choice9_yes:
                            t "{cps=50}Ok. Stand back and enjoy the show."

                            $ renpy.movie_cutscene("dunk.ogv")

                            menu:
                                t "{cps=50}So? What'd you think of that?"

                                "Woah! Impressive! Would you teach me to play basketball sometime?":
                                    jump choice10_yes

                                "Uh... cool I guess...":
                                    jump choice10_no

                            label choice10_no:
                                hide troy9
                                show troy7
                                with Dissolve(.5)

                                t "{cps=50}Whatever. Can you get outta here I need to be alone to practice."

                                show dani1
                                hide troy7
                                with Dissolve(.5)

                                d "{cps=50}Jeez what a fragile ego. He's a waste of your time, who needs an oversensitive lug like that? Lets keep looking around for the perfect crush."
                                stop music fadeout 1.0
                                scene gym building
                                with Dissolve(.5)

                                play music "maintheme.ogg"

                                scene hall way
                                with Dissolve(.5)

                                show dani

                                menu:
                                    d "{cps=50}Let me know where you wanna go and I'll take you there! Your crush awaits."

                                    "Gym":
                                        jump choice3_gym

                                    "Science Lab":
                                        jump choice3_lab

                                    "Behind the School":
                                        jump choice3_back
                            label choice10_yes:
                                hide troy9
                                show troy8
                                with Dissolve(.5)

                                t "{cps=50}Haha sure, here's my number."
                                t "{cps=50}let's get together sometime. It was awesome talking to you, but I gotta get back to practice for the big game."
                                t "{cps=50}{color=#aa0d6b}Hopefully I'll see ya there <3.{/color}"

                                show dani5
                                hide troy8
                                with Dissolve(.5)

                                d "{cps=50}Woah!! Dude!"
                                d "{cps=50}He gave you his number without you even asking. You're something else..."
                                d "{cps=50}Lets go flirt with more people! You can never have too many Crushes."
                                stop music fadeout 1.0
                                scene gym building
                                with Dissolve(.5)

                                play music "maintheme.ogg"

                                scene hall way
                                with Dissolve(.5)

                                show dani

                                menu:
                                    d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                                    "Gym":
                                        jump choice3_gym

                                    "Science Lab":
                                        jump choice3_lab

                                    "Behind the School":
                                        jump choice3_back
#Eggbert's lab
    label choice3_lab:
        scene hall way
        with Dissolve(.5)
        stop music fadeout 1.0
        play music "eggberttheme.ogg" fadein 1.0


        scene science lab
        with Dissolve(.5)

        show dani9
        show eggbert0:
            xpos -0.25
        with Dissolve(.5)

        d "{cps=50}Oh. This is {color=#3cdcff}Eggbert{/color}. He's really..."

        show dani8
        hide dani9
        hide eggbert0
        show eggbert1:
            xpos -0.25
        with Dissolve(.5)

        d "{cps=50}Kind!"

        d "{cps=50}Well, crushes come in all forms. Who, knows maybe there's something under that meek exterior."
        hide dani8
        show dani1
        with Dissolve(.5)

        menu:
            d "{cps=50}Wanna talk to him?"

            "Yeah. There's something about him...":
                jump choice11_yes

            "Um... let's look somewhere else maybe.":
                jump choice11_back

        label choice11_back:

            hide dani1
            show dani6
            hide eggbert1
            with Dissolve(.5)

            d "{cps=50}No judgement there!"
            stop music fadeout 1.0

            scene science lab
            with Dissolve(.5)

            play music "maintheme.ogg"

            scene hall way
            with Dissolve(.5)

            show dani
            with Dissolve(.5)
            menu:
                    d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                    "Gym":
                        jump choice3_gym

                    "Science Lab":
                        jump choice3_lab

                    "Behind the School":
                        jump choice3_back
        label choice11_yes:
            menu:
                d "{cps=50}Go get him, tiger"

                "Hey, {color=#3cdcff}Eggbert{/color}!":
                    jump choice12_spook

                "*Tap {color=#3cdcff}Eggbert{/color} on the shoulder*":
                    jump choice12_spook

        label choice12_spook:
            hide dani1
            hide eggbert1
            show eggbert7
            with Dissolve(.5)

            e "{cps=100}AHH!"

            hide eggbert7
            show eggbert8
            with Dissolve(.5)

            e "{cps=50}I- *gasp*"
            menu:
                e "{cps=50}I need my- *cough*"
                "Are you okay!? Do you need help?":
                    jump choice13_help

                "I'll- I'll go get the nurse!":
                    jump choice13_die
        label choice13_die:
            hide eggbert8
            show eggbert9
            with Dissolve(.5)

            e "{cps=50}W- *gasp* wait!"

            hide eggbert9
            with Dissolve(.5)

            "{cps=50}I gotta get to the nurse, and fast!"


            scene black
            with Dissolve(.5)
            stop music fadeout 1.0

            "{cps=50}*.............*"

            scene science lab
            with Dissolve(.5)

            "{cps=50}*Huf Huf* I'm back with the nurse! {color=#3cdcff}Eggbert{/color}! Hey... where's {color=#3cdcff}Eggbert{/color}?"
            show dani9
            with Dissolve(.5)

            d "{cps=50}[name]... you took too long. {color=#3cdcff}Eggbert{/color} he..."

            d "{cps=50}He died of an asthma attack. Apparently he had an inhaler somewhere in this room but he couldnt communicate."

            "{cps=50}Oh..."

            hide dani9
            show dani6
            with Dissolve(.5)

            d "{cps=50}Jeez... I mean, talk about a rough start!"
            d "{cps=50}He probably wasnt your ideal crush anyway. Let's go look for another one!"
            "{cps=50}Ok..."
            scene science lab
            with Dissolve(.5)

            play music "maintheme.ogg"

            scene hall way
            with Dissolve(.5)

            show dani
            with Dissolve(.5)
            menu:
                d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                "Gym":
                    jump choice3_gym

                "Science Lab":
                    jump choice3_lab

                "Behind the School":
                    jump choice3_back

        label choice13_help:
            e "{cps=50}Get my- *cough* my inhaler! *cough* In the *gasp* desk!"

            "{cps=50}*......*"

            hide eggbert8
            show eggbert10
            with Dissolve(.5)

            e "{cps=50}That was a close one!"

            hide eggbert10
            show eggbert11
            with Dissolve(.5)


            menu:
                e "{cps=50}Sorry about that, I guess you scared me when you got my attention."

                "I should be the one apologizing.":
                    jump choice14_sorry

                "You should be more brave!":
                    jump choice14_no

        label choice14_sorry:
            hide eggbert11
            show eggbert3
            with Dissolve(.5)

            e "{cps=50}Don't worry about it! It's forgotten!"

            label choice14_no:
                hide eggbert11
                show eggbert3
                with Dissolve(.5)


                e "{cps=50}I really do spook too easy... That's why I prefer to stay in here and do my work."

                e "{cps=50}Ack! How rude of me not to introduce myself!"

                hide eggbert3
                show eggbert2
                with Dissolve(.5)

                menu:
                    e "{cps=50}I'm {color=#3cdcff}Eggbert{/color}, and on behalf of all the students here at {color=#aa0d6b}Kurasshu High{/color}, Welcome!"

                    "Thanks, {color=#3cdcff}Eggbert{/color}! I'm [name]":
                        jump choice15_yes

                    "How did you know I'm new here?":
                        jump choice15_how

            label choice15_how:
                hide eggbert2
                show eggbert5
                with Dissolve(.5)


                e "{cps=50}Well I keep a tally of all 796 students currently enrolled at the school to calculate our attendance average."

                e "{cps=50}I finished my tally this morning with 797, indicating there was one new student."

                e "{cps=50}And I've never seen you before so... It had to be you."

                with Dissolve(.5)

                menu:
                    e "{cps=50}What's your name?"

                    "[name]":
                        jump choice15_yes

                    "It's [name]":
                        jump choice15_yes


                label choice15_yes:
                    hide eggbert5
                    show eggbert2
                    with Dissolve(.5)
                    e "{cps=50}I don't make too many friends, so It's nice to meet you!"

                    hide eggbert2
                    show eggbert3
                    with Dissolve(.5)

                    e "{cps=50}....."

                    menu:
                        e "{cps=50}Do you wanna see what I'm working on?"

                        "Sure!":
                            jump choice16_yes

                        "Uh... ok":
                            jump choice16_yes

                label choice16_yes:
                    hide eggbert3
                    show eggbert5
                    with Dissolve(.5)


                    e "{cps=50}Well, it's all only theoretical at this stage but the math checks out..."

                    e "{cps=50}I had to substitute a few outdated theorems for one's I concieved myself."

                    menu:
                        e "{cps=50}If you just take a look at my computer screen the data speaks for itself."

                        "{color=#3cdcff}Eggbert{/color}! You've cracked the code to interdimensional space travel with a self-generating clean energy source! This is ground breaking!":
                            jump choice17_wow

                        "{color=#3cdcff}Eggbert{/color}, This is Pornography":
                            jump choice17_porn

                    label choice17_porn:
                        hide eggbert5
                        show eggbert11
                        with Dissolve(.5)

                        e "{cps=50}It's- what!? No-no that's just- That's not mine-"

                        hide eggbert11
                        show eggert14
                        with Dissolve(.5)

                        e "{cps=50}That's a- a- a virus I-"

                        e "{cps=50}I gotta go- I'm late for computing club!"

                        show dani11
                        hide eggert14
                        with Dissolve(.5)

                        d "{cps=50}That was... unfortunate. What a perv!"

                        hide dani11
                        show dani6
                        with Dissolve(.5)

                        d "{cps=50}I do feel bad for the little guy but, oh well. Why don't we try somewhere else."
                        stop music fadeout 1.0
                        scene science lab
                        with Dissolve(.5)

                        play music "maintheme.ogg"

                        scene hall way
                        with Dissolve(.5)

                        show dani
                        with Dissolve(.5)
                        menu:
                            d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                            "Gym":
                                jump choice3_gym

                            "Science Lab":
                                jump choice3_lab

                            "Behind the School":
                                jump choice3_back

                    label choice17_wow:
                        hide eggbert5
                        show eggbert11
                        with Dissolve(.5)

                        e "{cps=50}Keep your voice down! No one else knows about this yet!"

                        menu:
                            e "{cps=50}Will you keep this a secret please?"


                            "Of course. I would never tell anyone":
                                jump choice18_yes

                            "Eggbert I have to tell the press... or Nasa or MIT":
                                jump choice18_no

                    label choice18_no:
                        stop music fadeout 1.0
                        hide eggbert11
                        show eggbert12
                        with Dissolve(.5)
                        play music "foxtheme.ogg" fadein 1.0

                        e "{cps=50}Then... I'm afraid you leave me no choice."

                        e "{cps=50}I have to erase your memory."


                        e"{cps=50}It was nice talking to you... goodbye [name]"


                        hide eggbert12
                        with Dissolve(.5)

                        show eggbert13
                        with Dissolve(.5)



                        scene white
                        with Dissolve(1.5)

                        "{cps=50}*......*"

                        "*Blink Blink*"

                        hide eggbert13
                        with Dissolve(1)

                        scene science lab
                        with Dissolve(.5)
                        stop music fadeout 1.0

                        "{cps=50}This is... the science lab."

                        "{cps=50}How did I get here?"

                        "{cps=50}Where's {color=#dd6e80}Dani?{/color}"

                        "{cps=50}Weird... I guess I'll just go back to the hallway."
                        scene science lab
                        with Dissolve(.5)

                        play music "maintheme.ogg"

                        scene hall way
                        with Dissolve(.5)

                        show dani
                        with Dissolve(.5)
                        menu:
                            d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                            "Gym":
                                jump choice3_gym

                            "Science Lab":
                                jump choice3_lab

                            "Behind the School":
                                jump choice3_back

                    label choice18_yes:
                        hide eggbert11
                        show eggbert3
                        with Dissolve(.5)

                        e "{cps=50}Wow... thanks."

                        e "{cps=50}You're so... nice to me."

                        e "{cps=50}Everybody at this school treats me like I'm invisible or like I'm some freak."

                        e "{cps=50}But you talk to me like a person."

                        e "{cps=50}Listen... I uh... well I have a mathlete competition this sunday..."

                        menu:
                            e "{cps=50}If you wanted to come and... well If you wanted to come it would mean a lot."

                            "Oh, {color=#3cdcff}eggbert{/color} of course I'll come!":
                                jump choice19_yes

                            "Oh... {color=#3cdcff}Eggbert{/color} thank you for inviting me but...":
                                jump choice19_no

                    label choice19_no:
                        hide eggbert3
                        show eggbert12
                        with Dissolve(.5)

                        e "{cps=50}That's ok... I get it."

                        e "{cps=50}You should just have fun with your friends. I should get back to work. It was nice talking to you."

                        show dani6
                        hide eggbert12
                        with Dissolve(.5)

                        d "{cps=50}Oof that wasa little cold, but ya gotta be honest."
                        d "{cps=50}Let's go back out in the hallway and look for a different crush."
                        stop music fadeout 1.0
                        scene science lab
                        with Dissolve(.5)

                        play music "maintheme.ogg"

                        scene hall way
                        with Dissolve(.5)

                        show dani
                        with Dissolve(.5)
                        menu:
                            d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                            "Gym":
                                jump choice3_gym

                            "Science Lab":
                                jump choice3_lab

                            "Behind the School":
                                jump choice3_back

                    label choice19_yes:
                        hide eggbert3
                        show eggbert15
                        with Dissolve(.5)

                        e "{cps=50}You will!?"

                        e "{cps=50}Oh boy, this is great!"

                        e "{cps=50}Well that all reminds me I have to run to mathlete practice!"

                        hide eggbert15
                        show eggbert16
                        with Dissolve(.5)

                        e "{cps=50}{color=#aa0d6b}Goodbye [name] <3.{/color}"



                        e "{cps=50}I'll see you at the competition!"

                        show dani8
                        hide eggbert16
                        with Dissolve(.5)

                        d "{cps=50}Well whaddaya know. The kid's pretty sweet!"

                        d "{cps=50}This whole crush thing is pretty exciting. Let's go find some more!"
                        stop music fadeout 1.0
                        scene science lab
                        with Dissolve(.5)

                        play music "maintheme.ogg"

                        scene hall way
                        with Dissolve(.5)

                        show dani
                        with Dissolve(.5)
                        menu:
                            d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                            "Gym":
                                jump choice3_gym

                            "Science Lab":
                                jump choice3_lab

                            "Behind the School":
                                jump choice3_back

        #Fox behind the school
        label choice3_back:
            stop music fadeout 1.0
            scene hall way
            with Dissolve(.5)

            play music "foxtheme.ogg"

            scene out back
            with Dissolve(.5)

            show dani12
            show fox0:
                xpos -0.25
            with Dissolve(.5)

            d "{cps=50}Oh boy... that's..."

            hide fox0
            show fox1:
                xpos -0.25
            with Dissolve(.5)

            d "{cps=50}{color=#500799}Fox Tanner{/color}."

            d "{cps=50}[name], this guy is trouble. I hear he has a gang of 100 bad guys that'll beat anybody up just for looking at them!!"

            hide dani12
            show dani6
            with Dissolve(.5)

            menu:
                d "{cps=50}If I were you I'd steer clear but... maybe you like trouble."

                "Wait here, I'm gonna say hi":
                    jump choice20_yes

                "You're right we should get outta here":
                    jump choice20_no

        label choice20_no:


            hide dani6
            show dani8
            hide fox1
            with Dissolve(.5)
            d "{cps=50}Good call. Let's find somebody with a little less edge."
            stop music fadeout 1.0
            scene out back
            with Dissolve(.5)

            play music "maintheme.ogg"

            scene hall way
            with Dissolve(.5)

            show dani
            with Dissolve(.5)
            menu:
                d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                "Gym":
                    jump choice3_gym

                "Science Lab":
                    jump choice3_lab

                "Behind the School":
                    jump choice3_back

        label choice20_yes:

            hide dani6
            show dani12
            with Dissolve(.5)
            d "{cps=50}Alright, be careful."

            hide dani12
            hide fox1
            show fox2
            with Dissolve(.5)

            f "{cps=50}......"

            menu:
                f "{cps=50}you want somethin?"

                "Yeah, I just wanted to say your jacket is really cool":
                    jump choice21_yes

                "Um no...":
                    jump choice21_no

        label choice21_no:

            f "{cps=50}..."
            hide fox2
            show fox5
            with Dissolve(.5)

            menu:
                f "{cps=50} wanna go to third base?"

                "Ok":
                    jump choice22_ok

                "Um, no thanks":
                    jump choice22_no

            label choice22_no:

                hide fox5
                show fox4
                with Dissolve(.5)

                f "{cps=50}whatever, I'll find someone else."

                f "{cps=50}beat it."

                show dani11
                hide fox4
                with Dissolve(.5)

                d "{cps=50}Jeez what a pig! and a jerk!"

                d "{cps=50}Lets go find someone with a little class. No loss here."
                stop music fadeout 1.0
                scene out back
                with Dissolve(.5)

                play music "maintheme.ogg"

                scene hall way
                with Dissolve(.5)

                show dani
                with Dissolve(.5)
                menu:
                    d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                    "Gym":
                        jump choice3_gym

                    "Science Lab":
                        jump choice3_lab

                    "Behind the School":
                        jump choice3_back

            label choice22_ok:
                scene out back
                with Dissolve(.5)

                scene black
                with Dissolve(.5)

                "{cps=50}*...........*"

                scene black
                with Dissolve(.5)

                scene out back
                with Dissolve(.5)

                show fox3
                with Dissolve(.5)

                f "{cps=50}That was cool..."

                f "{cps=50}I gotta bail."

                f "{cps=50}See ya"

                show dani7
                hide fox3
                with Dissolve(.5)

                d "{cps=50}What did you guys do back there?"
                hide dani7
                show dani6
                with Dissolve(.5)

                d "{cps=50}Tell me about it on the way back inside. There's more potential crushes in there!"
                stop music fadeout 1.0
                scene out back
                with Dissolve(.5)

                scene hall way
                with Dissolve(.5)

                play music "maintheme.ogg"

                show dani
                with Dissolve(.5)
                menu:
                    d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                    "Gym":
                        jump choice3_gym

                    "Science Lab":
                        jump choice3_lab

                    "Behind the School":
                        jump choice3_back

        label choice21_yes:
            hide fox2
            show fox4
            with Dissolve(.5)

            f "{cps=50}whatever. It's a piece of shit."

            menu:
                f "{cps=50}i found it in a dumpster."

                "Well, I really like it":
                    jump choice23_like

                "Really cuz I see the tag right there... it's from Banana Republic":
                    jump choice23_tag

                    label choice23_tag:
                    hide fox4
                    show fox6
                    with Dissolve(.5)

                    f "{cps=50}huh?"

                    hide fox6
                    show fox9
                    with Dissolve(.5)

                    f "{cps=50}that's nothing!"

                    hide fox9
                    show fox2
                    with Dissolve(.5)

                    f "{cps=50}just get out of here, kid. i'm doin big boy stuff"

                    show dani1
                    hide fox2
                    with Dissolve(.5)

                    d "{cps=50}Haha, sensitive fella. Seems the tough Fox Tanner might be an act. Lets go find someone else inside."
                    stop music fadeout 1.0
                    scene out back
                    with Dissolve(.5)

                    scene hall way
                    with Dissolve(.5)

                    play music "maintheme.ogg"

                    show dani
                    with Dissolve(.5)
                    menu:
                        d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                        "Gym":
                            jump choice3_gym

                        "Science Lab":
                            jump choice3_lab

                        "Behind the School":
                            jump choice3_back

        label choice23_like:
            hide fox4
            show fox8
            with Dissolve(.5)

            f "{cps=50}heh...weirdo."

            menu:
                f "{cps=50}want a cig?"

                "Sure, thanks":
                    jump choice24_sure

                "No thanks, I'm good":
                    jump choice24_no

            label choice24_no:
                hide fox8
                show fox2
                with Dissolve(.5)

                f "{cps=50}whatever, square."
                hide fox2
                show fox5
                with Dissolve(.5)

                jump choice21_no

        label choice24_sure:
            hide fox8
            show fox7
            with Dissolve(.5)

            f "{cps=50}*Pensive silence*"

            menu:
                f "{cps=50}..."

                "So, do you like going to school here?":
                    jump choice25_school

                "Why do you hang out here by yourelf?":
                    jump choice25_alone

            label choice25_school:
                hide fox7
                show fox11
                with Dissolve(.5)

                f "{cps=50}are you nuts!?"

                jump choice25_alone

        label choice25_alone:
            hide fox11
            hide fox7
            show fox2
            with Dissolve(.5)

            f "{cps=50}everyone in this place sucks crud!"

            f "{cps=50}the students are all pretentious, self obsessed morons."

            hide fox2
            show fox9
            with Dissolve(.5)

            f "{cps=50}and the teachers are just bullies who always pick on me... especially when I show up!"

            hide fox9
            show fox11
            with Dissolve(.5)

            menu:
                f "{cps=50}would {i}{b}you{/b}{/i} wanna spend time in a place with people like that?"

                "No way. I'm sorry this place sucks so much":
                    jump choice25_sorry

                "Well maybe if you had a better attitude, you'd have a different experience":
                    jump choice25_attitude

            label choice25_attitude:

                hide fox11
                show fox9
                with Dissolve(.5)

                f "{cps=50}i knew it! You're just like those other assholes!"

                f "{cps=50}this blows, now I gotta ditch my spot."

                hide fox9
                show fox4
                with Dissolve(.5)

                f "{cps=50}later, loser."

                show dani12
                hide fox4
                with Dissolve(.5)

                d "{cps=50}woah! I told you he had a short fuse!"

                d "{cps=50}let's get out of here before he comes back!"
                stop music fadeout 1.0
                scene out back
                with Dissolve(.5)

                play music "maintheme.ogg"

                scene hall way
                with Dissolve(.5)

                show dani
                with Dissolve(.5)
                menu:
                    d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                    "Gym":
                        jump choice3_gym

                    "Science Lab":
                        jump choice3_lab

                    "Behind the School":
                        jump choice3_back

        label choice25_sorry:

            hide fox11
            show fox2
            with Dissolve(.5)

            f "{cps=50}whatever."

            hide fox2
            show fox7
            with Dissolve(.5)

            f "{cps=50}i'm fine. those jerks don't get to me anyway."

            f "{cps=50}all i need is a cigarette and a nice spot to skip class."

            p "{cps=50}FOX TANNER. PLEASE REPORT TO THE PRINCIPLES OFFICE IMMEDIATELY."

            hide fox7
            show fox10
            with Dissolve(.5)

            f "{cps=50}aw man. and i was just getting comfortable."

            f "{cps=50}i guess that's my cue to bail."
            hide fox10
            show fox12
            with Dissolve(.5)

            f "{cps=50}hey listen..."

            f "{cps=50}don't tell anyone else i hang out back here but..."

            f "{cps=50}if you wanted to come back tomorrow and smoke..."
            f "{cps=50}I might be here."

            f "{cps=50}{color=#aa0d6b}later, loser <3.{/color}"

            show dani7
            hide fox12
            with Dissolve(.5)

            d "{cps=50}Do my eyes decieve me or was Fox Tanner kind of..."
            hide dani7
            show dani5
            with Dissolve(.5)

            d "{cps=50}Dreamy!"

            d "{cps=50}Wow! and he invited you back tomorrow!"
            hide dani5
            show dani3
            with Dissolve(.5)

            d "{cps=50}Why don't we head inside and celebrate our victory."
            stop music fadeout 1.0
            scene out back
            with Dissolve(.5)


            scene hall way
            with Dissolve(.5)

            play music "maintheme.ogg"

            show dani
            with Dissolve(.5)
            menu:
                d "Let me know where you wanna go and I'll take you there! Your crush awaits."

                "Gym":
                    jump choice3_gym

                "Science Lab":
                    jump choice3_lab

                "Behind the School":
                    jump choice3_back
