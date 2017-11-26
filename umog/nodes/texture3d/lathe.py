from ..umog_node import *

import threading
import sys
import bpy
import copy
import numpy as np
#import pyximport
#pyximport.install()


class UMOGTexture3LatheNode(UMOGNode):
    bl_idname = "umog_Texture3LatheNode"
    bl_label = "Lathe Node"
    
    def init(self, context):
        self.inputs.new("TextureSocketType", "A")
        self.outputs.new("TextureSocketType", "A'")
        

    def draw_buttons(self, context, layout):
        pass

            
    def get_operation(self, input_types):
        resolution = 256
        types.assert_type(input_types[0], types.ARRAY)
        return engine.Operation(
            engine.LATHE_GPU,
            [types.Array(resolution, resolution, resolution, 0, 0, 0)],
            [],
            [engine.Argument(engine.ArgumentType.SOCKET, 0)
             ],
            [resolution])

    def get_buffer_values(self):
        return []
