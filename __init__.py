from .node import *
from .install import *

NODE_CLASS_MAPPINGS = {
    'SDVN SAMModelLoader': SAMModelLoader,
    'SDVN DinoModelLoader': GroundingDinoModelLoader,
    'SDVN DinoSAMSegment': GroundingDinoSAMSegment,
    'SDVN InvertMask': InvertMask,
    "SDVN IsMaskEmpty": IsMaskEmptyNode,
    "SDVN SegmentAnything": SegmentAnything,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    '🧩 SAMModel Loader': 'SDVN SAMModelLoader',
    '🧩 DinoModel Loader': 'SDVN DinoModelLoader',
    '🧩 Dino SAMSegment': 'SDVN DinoSAMSegment',
    '🧩 Invert Mask': 'SDVN InvertMask',
    "🧩 Is Mask Empty": 'SDVN IsMaskEmpty',
    "🧩 Segment Anything": 'SDVN SegmentAnything',
}

__all__ = ['NODE_CLASS_MAPPINGS']


