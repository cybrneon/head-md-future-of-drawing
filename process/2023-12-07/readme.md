# 🔁 Mini-Reset with Douglas

## All the steps to build the thing

### What it needs to do?
- Detect the pen getting lifted and put back from the pen holder.

### Form
- 3D Modeling (Fusion360) of 1 object
    - 1 box composed of 2 Bodies (Pen Holder + Speaker and Micro-controller Base)
    - 210mm x 80mm x 80mm (H x W x L)

![Screenshot](/process/2023-12-05/sketch4.png)
- Exhibition Table/structure?

### Materials
- 3D Printing (Speaker and Micro-controller Base)
- Metal (Pen Holder)
- Fabrics (easy to get as I work at IKEA in the textile dep.)

### Electronics
- Raspberry Pi Zero 2 W
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
            - Speaker
            - Adafruit I2S 3W Stereo Speaker Bonnet for Raspberry Pi
- Dimensions
    - Raspberry Pi Zero 2 W: 65mm x 30mm (+Height of around 35mm with the Speaker Bonnet) (H x W x L)
- Wiring
    - The micro-switch is connected to the RP as an input.
    - The Speaker is connected to the Adafruit I2S.
    - The Adafruit I2S is connected to the RP as an output.
- Power (wall adapter)
- APIs?


## Ideas for the stories that will be narrated
- Old Times
- Futuristic Stories
- StellarAI's take on the world

## Preparing for Test Day
- Session 1: Interaction
- Session 2: A/B testing of two stories.