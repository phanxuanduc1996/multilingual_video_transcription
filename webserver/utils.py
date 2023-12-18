import os
import re
import json
# from supabaseClient import getTranscription


def is_youtube_url(url):
    # Regular expression pattern for a YouTube video URL
    pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?([a-zA-Z0-9_-]{11})'

    # Match the URL pattern against the input string
    match = re.match(pattern, url)

    # Return True if the pattern matches, otherwise False
    return match is not None


# def is_already_transcribed(url):
#     data = getTranscription(url)
#     print(data)
#     if not all(data):
#         return False

#     return True


PREFIX = 'Bearer '


def get_token(header):
    if not header.startswith(PREFIX):
        raise ValueError('Invalid token')

    return header[len(PREFIX):]


def write_json(data_key, data_value, filename="logs/log_transcript_output.json"):
    if not os.path.exists(filename):
        with open(filename, "w", encoding='utf-8') as file:
            json.dump({"OUTPUT": "LOGS_TRANSCRIPT"}, file, ensure_ascii=False)

    with open(filename, 'r+', encoding='utf-8') as file:
        file_data = json.load(file)
        file_data[data_key] = data_value
        file.seek(0)
        json.dump(file_data, file, indent=4, ensure_ascii=False)
