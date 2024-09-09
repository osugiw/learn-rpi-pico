/*****************************************************************************
* | File      	:   Readme_CN.txt
* | Author      :   
* | Function    :   Help with use
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2022-09-13
* | Info        :   在这里提供一个中文版本的使用文档，以便你的快速使用
******************************************************************************/
这个文件是帮助您使用本例程。
在这里简略的描述本工程的使用：

1.基本信息：
本例程使用相对应的模块搭配Pico进行了验证;

2.管脚连接：
管脚连接您可以在\lib\audio_data目录下查看audio_data.h中查看，这里也再重述一次：
PCM5101A    =>    Pico
DIN		26
BCK 		27
LRCK		BCK + 1


3.基本使用：
你需要执行：
    1): 按住Pico板上的按键，将pico通过Micro USB线接到树莓派的USB接口，然后松开按键。
        接入之后，电脑会自动识别到一个可移动盘（RPI-RP2）
        
    2): 将python目录中rp2-pico-20220618-v1.19.1.uf2文件复制到识别的可移动盘（RPI-RP2）中
    
    3): 更新Thonny IDE
        sudo apt upgrade thonny
        
    4): 打开Thonny IDE （点击树莓logo -> Programming -> Thonny Python IDE ）
        选择Tools -> Options... -> Interpreter
        选择MicroPython(Raspberry Pi Pico 和ttyACM0端口
        
    5): 在Thonny IDE中打开Audio_PIO.py/Hardware_I2S.py文件
        然后运行当前脚本（绿色小三角）即可


