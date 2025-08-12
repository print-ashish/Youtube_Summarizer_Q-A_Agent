

from youtube_transcript_api import YouTubeTranscriptApi




def get_transcript(video_id):
    # video_id = "nyKvyRrpbyY"
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id)

    final_text = ""
    for snippet in fetched_transcript:
        # print(snippet.text)
        final_text += snippet.text

    # print("final text == ", final_text)
    return final_text

# res = get_transcript("Tl80IK5NEyE")
# print(res)