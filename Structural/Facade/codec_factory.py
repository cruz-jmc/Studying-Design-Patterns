from codec import OggCompressionCodec, MPEG4CompressionCodec #importing all codecs
from video_file import VideoFile # importing the file we are working


class CodecFactory:

    @staticmethod # static because we don't need keep any state
    def extract(video_file: VideoFile):
        print(f"[CodecFactory] codec {video_file.codec_name} extraído") # show which codec was extracted

        if video_file.codec_name == "ogg": # -> verification
            return OggCompressionCodec()

        if video_file.codec_name == "mp4": # same here
            return MPEG4CompressionCodec()

        raise ValueError( # -> ValueError, obviously
            f"Codec '{video_file.codec_name}' não suportado"
        )