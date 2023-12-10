# 🔁 Mini-Reset with Douglas

## All the steps to build the thing

### What it needs to do?
- Detect the pen getting lifted and put back from the pen holder.

### Form
3D Modeling (Fusion360) of 2 objects
- The device:
    - 1 box composed of 2 Bodies (Pen Holder + Speaker and Micro-controller Base)
    - 210mm x 80mm x 80mm (H x W x L)
![Screenshot](/process/2023-12-05/sketch4.png)
![Screenshot](/process/2023-12-05/handmade_sketch.jpg)

- A "back" box, where electronics are stored. Should be bigger than the RP.
    - It will contain the RP (88mm x 58mm x 19mm)
    - It will contain all the loose cables and +
- Exhibition Table/structure?

### Materials
- 3D Printing (Speaker and Micro-controller Base) + (Back Box)
- Metal (Pen Holder)
- Fabrics for the speaker grill (easy to get as I work at IKEA in the textile dep.)

### Electronics
- Raspberry Pi 4
    - Code
        - micro-switch detector
        - .mp3 or .wav player
        - Experimental AI stuff to try:
            - Giving the beggining to a story to an AI and letting it generate the end.
            - Giving the title of an episode to an AI and letting it generate each episode.
    - Components
        - INPUT
            - Micro-switch
        - OUTPUT
            - 2 speakers (each 40mm x 20mm x 8mm)
            - Adafruit I2S 3W Stereo Speaker Bonnet for Raspberry Pi
- Dimensions
    - Raspberry Pi 4: 88mm x 58mm x 19mm (+Height of around 35mm with the Speaker Bonnet) (H x W x L)
- Wiring
    - The micro-switch is connected to the RP as an input.
    - The Speakers are connected to the Adafruit I2S.
    - The Adafruit I2S is connected to the RP as an output.
- Power (wall adapter)
- APIs?


## Ideas for the stories that will be narrated
- Lemanus
- Futuristic Stories
- StellarAI's take on the world

## Preparing for Test Day
- Session 1: Interaction
- Session 2: A/B testing of two stories.