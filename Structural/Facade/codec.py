from abc import ABC, abstractmethod


class Codec(ABC):

    @abstractmethod
    def type(self): # every codec requires a type (mp4 / ogg / etc.)
        raise NotImplementedError


class OggCompressionCodec(Codec):

    def type(self):
        return "ogg" # defining the "ogg" type


class MPEG4CompressionCodec(Codec):

    def type(self):
        return "mp4" # defining the "mp4" type