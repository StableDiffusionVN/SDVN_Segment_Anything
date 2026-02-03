from .node import *
from .install import *

NODE_CLASS_MAPPINGS = {
    '🧩 SAMModel Loader': SAMModelLoader,
    '🧩 DinoModel Loader': GroundingDinoModelLoader,
    '🧩 Dino SAMSegment': GroundingDinoSAMSegment,
    '🧩 Invert Mask': InvertMask,
    "🧩 Is Mask Empty": IsMaskEmptyNode,
    "🧩 Segment Anything": SegmentAnything,
}

__all__ = ['NODE_CLASS_MAPPINGS']


