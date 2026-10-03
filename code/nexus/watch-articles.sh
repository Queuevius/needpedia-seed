#!/bin/bash
WATCH_DIR="/home/clearcrow/Needpedia_Nexus/articles"
VIDEO_DIR="/home/clearcrow/Needpedia_Nexus/Videos"
inotifywait -m -r -e close_write -e moved_to "$WATCH_DIR" "$VIDEO_DIR" --format '%w%f' |
while read FILEPATH; do
  FILENAME=$(basename "$FILEPATH")
  DIR=$(dirname "$FILEPATH")
  EXT="${FILENAME##*.}"
  BASE="${FILENAME%.*}"
  if [[ "$EXT" == "docx" || "$EXT" == "odt" || "$EXT" == "doc" ]]; then
    echo "Converting: $FILENAME"
    libreoffice --headless --convert-to html "$FILEPATH" --outdir "$DIR/"
    rm "$FILEPATH"
    /home/clearcrow/Needpedia_Nexus/rebuild-index.sh
  fi
  if [[ "$EXT" == "mp4" || "$EXT" == "webm" || "$EXT" == "mov" || "$EXT" == "avi" || "$EXT" == "mkv" || "$EXT" == "m4v" ]]; then
    THUMB="$DIR/$BASE.thumb.jpg"
    if [ ! -f "$THUMB" ]; then
      echo "Thumbnailing: $FILENAME"
      ffmpeg -ss 00:00:03 -i "$FILEPATH" -frames:v 1 -q:v 2 "$THUMB" -y -loglevel quiet
    fi
  fi
done
