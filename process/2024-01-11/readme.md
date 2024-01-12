#  Progress of the day

The software is done. I just need to work on the story and push it through Text-To-Speech.

The presentation is almost done, I only need images of the device and small refinements here and there.

## Check-up with Douglas at noon
I'm on the right track, here's what's remaining to do.
- Find a better solution for the pen detection, putting weight into the top of the pen like lead (plomb), and not using ugly wood.
- Story generation with AI.
- Software corrections and boot setup.
- Finding how to hide the RPI.
- Presentation and finish Project Documentation
- Back up sd card!
- Label the cables so I can recognize which cable is which.


## Other
Here are settings for Google's TTS:

![](/process/2024-01-11/google-tts-settings.png)

I then go to the browser's Dev Tools > Get to the Network Tab > filter "proxy" and look for "proxy texttospeech" > reveal source > and get the JSON. Most important is the "audioContent" part, that I then put in a Base64 to mp3 decoder (https://www.ipvoid.com/base64-to-mp3/), or do it local on my machine!