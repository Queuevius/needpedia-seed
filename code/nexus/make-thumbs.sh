#!/bin/bash
VIDEO_DIR="/home/clearcrow/Needpedia_Nexus/Videos"
for f in "$VIDEO_DIR"/*.mp4 "$VIDEO_DIR"/*.webm "$VIDEO_DIR"/*.mov "$VIDEO_DIR"/*.avi "$VIDEO_DIR"/*.mkv "$VIDEO_DIR"/*.m4v; do
  [ -f "$f" ] || continue
  thumb="${f%.*}.thumb.jpg"
  [ -f "$thumb" ] && continue
  ffmpeg -ss 00:00:03 -i "$f" -frames:v 1 -q:v 2 "$thumb" -y -loglevel quiet
  echo "Thumbed: $(basename "$f")"
done
echo "Done."
