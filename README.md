# Podcast Intelligence Pipeline

Build a pipeline that follows a YouTube podcast, analyzes new episodes, and surfaces insights over time.

## The challenge

New episodes arrive every **n days**, where **n can vary**. We want to capture each episode as soon as it is published and run analysis on it. Do not assume a fixed weekly release schedule.

### Per-episode analysis

Extract:

- **TL;DR:** a concise summary of the episode.
- **Topics discussed:** the main themes and discussions.
- **Insightful learnings:** interesting takeaways, ideas, or observations.
- **Top quotes and opinions:** notable statements and viewpoints.

### Week-over-week analysis

Look across episodes to understand:

- Which topics are consistently addressed week over week?
- How do individual panelists' opinions on those topics evolve, shift, or stay consistent over time?

## Your approach

This exercise is deliberately open-ended. Choose any podcast you want, and use whichever tools, models, and technologies you think fit. There is no prescribed architecture or output format.

Explore the data, experiment, and do some testing. Decide what to prioritize and how far to take the implementation. Be ready to explain your choices, assumptions, and tradeoffs.

## Example data

The repository includes All-In podcast transcripts to explore and test with. You can use these or choose another podcast.

- **All-In YouTube channel:** https://www.youtube.com/channel/UCESLZhusAkFfsNsApnjF_Cg
- **Channel ID:** `UCESLZhusAkFfsNsApnjF_Cg`

The checked-in dataset can be used without network access or API keys:

- `transcripts/` contains 11 text files.
- `w1.txt` through `w9.txt` include an episode title, YouTube source link, and timestamped captions.
- `w0.txt` and `w0.5.txt` are additional transcript samples.

Formatting varies between files. Captions may contain transcription errors.

## Fetch transcripts programmatically

One option is [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api), which retrieves existing YouTube captions, including automatically generated captions. No YouTube API key is required. You are free to use another approach.

Set up a Python environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install youtube-transcript-api
```

### Command line

Download the captions for the episode used in `transcripts/w1.txt`:

```bash
youtube_transcript_api KcmMOZKnKAk --languages en --format json > transcript.json
```

JSON output preserves each caption's text, start time, and duration.

### Python

```python
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "KcmMOZKnKAk"
transcript = YouTubeTranscriptApi().fetch(video_id, languages=["en"])

for snippet in transcript:
    print(f"{snippet.start:.3f}s: {snippet.text}")
```

Pass the video ID, not the full URL. For `https://www.youtube.com/watch?v=KcmMOZKnKAk`, the ID is `KcmMOZKnKAk`.

Fetching requires network access and available captions. YouTube may block or rate-limit requests, especially from cloud IP addresses. The checked-in files let you explore and test the analysis without live downloads.
