import math
import struct
from machine import I2S
from machine import Pin

mode = 0   # 0: array_demo , other : math_demo

sine_wave_table = [
 0x7FFF,0x8323,0x8647,0x896A,0x8C8B,0x8FAA,0x92C7,0x95E1,0x98F8,0x9C0A,0x9F19,0xA223,0xA527,0xA826,0xAB1E,0xAE10
,0xB0FB,0xB3DE,0xB6B9,0xB98C,0xBC55,0xBF16,0xC1CD,0xC47A,0xC71C,0xC9B3,0xCC3F,0xCEBF,0xD132,0xD39A,0xD5F4,0xD842
,0xDA81,0xDCB3,0xDED6,0xE0EB,0xE2F1,0xE4E7,0xE6CE,0xE8A5,0xEA6C,0xEC23,0xEDC9,0xEF5E,0xF0E1,0xF254,0xF3B4,0xF503
,0xF640,0xF76B,0xF883,0xF989,0xFA7C,0xFB5C,0xFC28,0xFCE2,0xFD89,0xFE1C,0xFE9C,0xFF08,0xFF61,0xFFA6,0xFFD7,0xFFF5
,0xFFFE,0xFFF5,0xFFD7,0xFFA6,0xFF61,0xFF08,0xFE9C,0xFE1C,0xFD89,0xFCE2,0xFC29,0xFB5C,0xFA7C,0xF989,0xF883,0xF76B
,0xF640,0xF503,0xF3B4,0xF254,0xF0E1,0xEF5E,0xEDC9,0xEC23,0xEA6C,0xE8A5,0xE6CE,0xE4E7,0xE2F1,0xE0EB,0xDED6,0xDCB3
,0xDA81,0xD842,0xD5F4,0xD39A,0xD132,0xCEBF,0xCC3F,0xC9B3,0xC71C,0xC47A,0xC1CD,0xBF16,0xBC55,0xB98C,0xB6B9,0xB3DE
,0xB0FB,0xAE10,0xAB1E,0xA826,0xA527,0xA222,0x9F19,0x9C0A,0x98F8,0x95E1,0x92C7,0x8FAA,0x8C8B,0x8969,0x8647,0x8323
,0x7FFF,0x7CDB,0x79B7,0x7694,0x7373,0x7054,0x6D37,0x6A1D,0x6706,0x63F4,0x60E5,0x5DDB,0x5AD7,0x57D8,0x54E0,0x51EE
,0x4F03,0x4C20,0x4945,0x4672,0x43A8,0x40E8,0x3E31,0x3B84,0x38E2,0x364B,0x33BF,0x313F,0x2ECB,0x2C64,0x2A0A,0x27BC
,0x257D,0x234B,0x2128,0x1F13,0x1D0D,0x1B17,0x1930,0x1759,0x1592,0x13DB,0x1235,0x10A0,0x0F1D,0x0DAA,0x0C49,0x0AFB
,0x09BE,0x0893,0x077B,0x0675,0x0582,0x04A2,0x03D5,0x031C,0x0275,0x01E2,0x0162,0x00F6,0x009D,0x0058,0x0027,0x0009
,0x0000,0x0009,0x0027,0x0058,0x009D,0x00F6,0x0162,0x01E2,0x0275,0x031C,0x03D6,0x04A3,0x0583,0x0675,0x077B,0x0893
,0x09BE,0x0AFB,0x0C4A,0x0DAA,0x0F1D,0x10A1,0x1236,0x13DB,0x1592,0x1759,0x1930,0x1B17,0x1D0E,0x1F13,0x2128,0x234B
,0x257D,0x27BD,0x2A0A,0x2C64,0x2ECC,0x3140,0x33C0,0x364B,0x38E3,0x3B85,0x3E31,0x40E8,0x43A9,0x4673,0x4945,0x4C21
,0x4F04,0x51EE,0x54E0,0x57D9,0x5AD7,0x5DDC,0x60E5,0x63F4,0x6707,0x6A1D,0x6D37,0x7054,0x7374,0x7695,0x79B8,0x7CDB]


PIN_BCK = 27
PIN_LRCK = 28
PIN_DATA = 26
I2S_ID = 0
PICO_AUDIO_FREQ = 22_050
BUFFER_LENGTH_IN_BYTES = 2000

if mode == 0:
    SAMPLE_SIZE_IN_BITS = 16
    FORMAT = I2S.STEREO
else:
    SAMPLE_SIZE_IN_BITS = 16
    FORMAT = I2S.MONO 

def array_demo():
    samples = bytearray(len(sine_wave_table) * 2)
    for i in range(0, len(sine_wave_table)-1):
        samples[i*2+1] = ((sine_wave_table[i] - 0x7fff) >> 8) & 0xFF
        samples[i*2] = (sine_wave_table[i] - 0x7fff) & 0xFF
    return samples

def math_demo(rate, bits, frequency):
    # create a buffer containing th e pure tone samples
    samples_per_cycle = rate // frequency
    sample_size_in_bytes = bits // 8
    samples = bytearray(samples_per_cycle * sample_size_in_bytes)
    volume_reduction_factor = 32
    range = pow(2, bits) // 2 // volume_reduction_factor
    
    if bits == 16:
        format = "<h"
    else:  # assume 32 b its
        format = "<l"
    
    for i in range(samples_per_cycle):
        sample = range + int((range - 1) * math.sin(2 * math.pi * i / samples_per_cycle))
        struct.pack_into(format, samples, i * sample_size_in_bytes, sample)
        
    return samples


audio_out = I2S(
    I2S_ID,
    sck=Pin(PIN_BCK),
    ws=Pin(PIN_LRCK),
    sd=Pin(PIN_DATA),
    mode=I2S.TX,
    bits=SAMPLE_SIZE_IN_BITS,
    format=FORMAT,
    rate=PICO_AUDIO_FREQ,
    ibuf=BUFFER_LENGTH_IN_BYTES,
)

if mode == 0:
    buf = array_demo()
else:
    buf = math_demo(PICO_AUDIO_FREQ, SAMPLE_SIZE_IN_BITS, 440)
    
    
try:
    while True:
        audio_out.write(buf)

except (KeyboardInterrupt, Exception) as e:
    print("caught exception {} {}".format(type(e).__name__, e))

# cleanup
audio_out.deinit()
print("Done")