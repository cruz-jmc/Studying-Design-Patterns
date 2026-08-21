from codec import Codec
from video_file import VideoFile


class BitrateReader:

    @staticmethod
    def read(video_file: VideoFile, codec: Codec):
        print(
            f"[BitrateReader] lendo com codec {codec.type()}"
        )

        return f"buffer de {video_file.name}"

    @staticmethod
    def convert(buffer, codec: Codec):
        print(
            f"[BitrateReader] convertendo para {codec.type()}"
        )

        return f"{buffer} convertido para {codec.type()}"