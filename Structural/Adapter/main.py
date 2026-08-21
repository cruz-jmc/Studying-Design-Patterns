from player import AudioPlayer, MediaPlayer
from video_adapter import VideoAdapter
from video_player import VideoPlayer
# importing all pieces we need

MediaPlayer(AudioPlayer()).execute()
# without Adapter, native player.
MediaPlayer(VideoAdapter(VideoPlayer())).execute()
# 1. instace "videoAdapter" (incompatible);
# 2. Encapsulates in videoAdapter;
# 3. pass videoAdapter to MediaPlayer;
# 4. when execute, MediaPlayer call .play(), the adapter receives the command then call .play_mp4() in VideoPlayer.