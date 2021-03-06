import povsprites
import uctypes
import imagenes

sprite_struct = {
    "x": uctypes.UINT8 | 0,
    "y": uctypes.INT8 | 1,
    "image_strip": uctypes.UINT8 | 2,
    "frame": uctypes.INT8 | 3,
}

PIXELS=52
DISABLED_FRAME = -1

povsprites.init(PIXELS, imagenes.palette_pal)

def create_sprite(num_sprite):
    data = povsprites.getaddress(num_sprite)
    sp = uctypes.struct(data, sprite_struct) #, uctypes.LITLE_ENDIAN)
    return sp

def set_imagestrip(n, stripmap):
    povsprites.set_imagestrip(n, stripmap)

def debug(s):
    print("nave@%d (%d,%d,%d,%d) %d" % (s.image_strip, s.x, s.y, 0, 0, s.frame))
