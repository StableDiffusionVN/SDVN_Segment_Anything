from .node import *
from .install import *

NODE_CLASS_MAPPINGS = {
    '🧩 SAMModelLoader': SAMModelLoader,
    '🧩 DinoModelLoader': GroundingDinoModelLoader,
    '🧩 DinoSAMSegment': GroundingDinoSAMSegment,
    '🧩 InvertMask': InvertMask,
    "🧩 IsMaskEmpty": IsMaskEmptyNode,
    "🧩 SegmentAnything": SegmentAnything,
}

__all__ = ['NODE_CLASS_MAPPINGS']


