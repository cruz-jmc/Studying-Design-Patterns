# this is the Facade, a simplified entry point.
# the most important class, without this, the system crash.

from video_file import VideoFile
from codec_factory import CodecFactory
from codec import OggCompressionCodec, MPEG4CompressionCodec
from bitrate_reader import BitrateReader
from audio_mixer import AudioMixer
# import all classes we are using


class VideoConverter: # -> Facade

    def convert(self, filename: str, format: str):

        file = VideoFile(filename) # VideoFile object

        codec_origin = CodecFactory.extract(file) # descovering codec

        if format == "mp4":
            codec_destination = MPEG4CompressionCodec()

        elif format == "ogg":
            codec_destination = OggCompressionCodec()

        else:
            raise ValueError(
                f"Formato de destino '{format}' não suportado"
            )
        # -> logic convertion above

        buffer = BitrateReader.read( # reading
            file,
            codec_origin
        )

        result = BitrateReader.convert( # converting
            buffer,
            codec_destination
        )

        result = AudioMixer.fix(result) # instancing the result

        print("[VideoConverter] conversão concluída")

        return result # -> showing result