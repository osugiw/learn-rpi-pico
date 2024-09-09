/*****************************************************************************
* | File: Readme_EN. TXT
* | the Author:
* | Function: Help with use
* | Info:
* -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -
* | This version: V1.0
* | Date: 2021-09-13
* | Info: provide here USES a Chinese version of the document, for your quick use
******************************************************************************/
This file is to help you use this routine.
Here is a brief description of the use of this project:

1. Basic information:
This routine uses the corresponding module matching PICO for verification;

2. Pin connection:
Audio_data. h Pin connection You can view the audio_data.h in the \lib\audio_data directory, and again here:
PCM5101A     =>   	Pico
DIN		 26
BCK 		 27
LRCK	 	 BCK + 1

3. Basic use:
You need to execute:
    1): Press and hold the button on the Pico board, connect Pico to the USB port of the 
        Raspberry Pi through the Micro USB cable, and then release the button.
        After connecting, the computer will automatically recognize a removable disk (RPI-RP2)
        
    2): Copy the rp2-pico-20220618-v1.19.1.uf2 file in the python directory to the recognized 
        removable disk (RPI-RP2)
    
    3): Update Thonny IDE
        sudo apt upgrade thonny
        
    4): Open Thonny IDE （Click raspberry logo -> Programming -> Thonny Python IDE ）
        select Tools -> Options... -> Interpreter
        select MicroPython(Raspberry Pi Pico  and ttyACM0 port
        
    5): Open the Audio_PIO.py/Hardware_I2S.py file in Thonny IDE
        Then run the current script (green triangle)
