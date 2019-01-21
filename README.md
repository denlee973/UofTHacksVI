# UofTHacksVI
## Inspiration
I have always been intrigued by the methods in which people overcome disabilities. I keep up with many disabled content creators, and I am constantly inclined to create something whenever they mention an obstacle in their daily lives.
I've been trying to learn ASL for many years, but all I can sign is "My name is Denny." There must be some other way I can communicate with the hard-of-hearing. Although there have been a few developments over the years regarding this topic, there hasn't been any widely available sign language interpreters which is where Diallogue comes in.
## What is Diallogue?
Diallogue is the easiest way to communicate with someone who is deaf. Download the app, hold your phone up to the signing person, and receive a text or speech response, and vice versa.
## How we built it
We used Microsoft's Azure Custom Vision API to train our own model to recognize numerical American Sign Language. With Python and Kivy we created the current user interface and processor.
## Challenges we ran into
This was our first time using cloud services of any kind, so implementing them into our code proved a bit difficult. However, through some troubleshooting and mentors' help, we were able to connect our Custom Vision trained model and the rest of our code.
## Accomplishments that we're proud of
Being able to dive into an unfamiliar framework! You'll never learn anything if you are not uncomfortable.
## What we learned
Keep going. Don't stop, even if your program doesn't work for a whole day, or you can't find any solutions to the error you're facing, or you've just run out of steam. It's always worth it to follow through. Plus, we learned two new frameworks; the Custom Vision API and Kivy!
## What's next for Diallogue
As this app is only a proof of concept, we hope to be able to interpret sign language more accurately and fluidly without needing to capture each sign, as more complex phrases tend to flow from one sign to the next. We would also like to be able to reverse the process to translate spoken English into sign language. Furthermore, we would like to improve the UI design and implementation with Python, as well as expand to different sign languages to support global signing.
