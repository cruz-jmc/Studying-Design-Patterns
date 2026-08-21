class VideoFile: # represents literally a video file.

    def __init__(self, name: str):
        self.name = name
        self.codec_name = name.split(".")[-1] # Separate the file from . (dot) and pick de last part
        # example: video.mp4 = [video(0), mp4(1 or -1)]

        print(f"[VideoFile] arquivo '{name}' aberto")