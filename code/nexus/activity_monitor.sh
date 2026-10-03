#!/usr/bin/env bash
# Needpedia production activity monitor  --  Session N37
# Read-only. Queries production, writes counts into the Nexus web root.
# Lives OUTSIDE the web root because it holds a password.

set -uo pipefail

DB_HOST="18.223.241.10"
DB_USER="nexus_reader"
DB_NAME="needpedia_production"
export PGPASSWORD='REPLACE_ME'

OUT="/home/clearcrow/Nexus_private/data/activity.json"
TMP="$(mktemp)"
ERR="$(mktemp)"

SQL="
SELECT json_build_object(
 'ok', true,
 'generated_at', round(extract(epoch from now())),
 'last_action_key', (SELECT key FROM activities ORDER BY created_at DESC LIMIT 1),
 'last_action_at',  (SELECT round(extract(epoch from created_at)) FROM activities ORDER BY created_at DESC LIMIT 1),
 'total_users',      (SELECT count(*) FROM users),
 'total_posts',      (SELECT count(*) FROM posts),
 'total_activities', (SELECT count(*) FROM activities),
 'signups', json_build_object(
   'h24',(SELECT count(*) FROM users WHERE created_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM users WHERE created_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM users WHERE created_at > now()-interval '30 days')),
 'confirmed', json_build_object(
   'h24',(SELECT count(*) FROM users WHERE confirmed_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM users WHERE confirmed_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM users WHERE confirmed_at > now()-interval '30 days')),
 'logins', json_build_object(
   'h24',(SELECT count(*) FROM login_attempts WHERE success AND attempted_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM login_attempts WHERE success AND attempted_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM login_attempts WHERE success AND attempted_at > now()-interval '30 days')),
 'posts', json_build_object(
   'h24',(SELECT count(*) FROM posts WHERE created_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM posts WHERE created_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM posts WHERE created_at > now()-interval '30 days')),
 'edits', json_build_object(
   'h24',(SELECT count(*) FROM post_versions WHERE created_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM post_versions WHERE created_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM post_versions WHERE created_at > now()-interval '30 days')),
 'comments', json_build_object(
   'h24',(SELECT count(*) FROM comments WHERE created_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM comments WHERE created_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM comments WHERE created_at > now()-interval '30 days')),
 'machine_hits', json_build_object(
   'h24',(SELECT count(*) FROM guests WHERE created_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM guests WHERE created_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM guests WHERE created_at > now()-interval '30 days')),
 'ai_questions', json_build_object(
   'h24',(SELECT count(*) FROM chat_messages WHERE role='user' AND created_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM chat_messages WHERE role='user' AND created_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM chat_messages WHERE role='user' AND created_at > now()-interval '30 days')),
 'last_ai_question_at', (SELECT round(extract(epoch from created_at)) FROM chat_messages WHERE role='user' ORDER BY created_at DESC LIMIT 1),
 'failed_logins', json_build_object(
   'h24',(SELECT count(*) FROM login_attempts WHERE NOT success AND attempted_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM login_attempts WHERE NOT success AND attempted_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM login_attempts WHERE NOT success AND attempted_at > now()-interval '30 days')),
 'unconfirmed_signups', json_build_object(
   'h24',(SELECT count(*) FROM users WHERE confirmed_at IS NULL AND created_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM users WHERE confirmed_at IS NULL AND created_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM users WHERE confirmed_at IS NULL AND created_at > now()-interval '30 days')),
 'blocked_addresses', (SELECT count(*) FROM blocked_ips),
 'groups_new', json_build_object(
   'h24',(SELECT count(*) FROM groups WHERE created_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM groups WHERE created_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM groups WHERE created_at > now()-interval '30 days')),
 'groups_edited', json_build_object(
   'h24',(SELECT count(*) FROM groups WHERE updated_at > created_at AND updated_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM groups WHERE updated_at > created_at AND updated_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM groups WHERE updated_at > created_at AND updated_at > now()-interval '30 days')),
 'tasks_activity', json_build_object(
   'h24',(SELECT count(*) FROM tasks WHERE updated_at > now()-interval '24 hours'),
   'd7', (SELECT count(*) FROM tasks WHERE updated_at > now()-interval '7 days'),
   'd30',(SELECT count(*) FROM tasks WHERE updated_at > now()-interval '30 days')),
 'series', json_build_object(
 'newbies',(SELECT json_agg(c ORDER BY d) FROM (SELECT d,(SELECT count(*) FROM users WHERE created_at>=d AND created_at<d+interval '1 day')+(SELECT count(*) FROM users WHERE confirmed_at>=d AND confirmed_at<d+interval '1 day') c FROM generate_series(date_trunc('day',now())-interval '29 days',date_trunc('day',now()),interval '1 day') d) t),
 'ai',(SELECT json_agg(c ORDER BY d) FROM (SELECT d,(SELECT count(*) FROM chat_messages WHERE role='user' AND created_at>=d AND created_at<d+interval '1 day') c FROM generate_series(date_trunc('day',now())-interval '29 days',date_trunc('day',now()),interval '1 day') d) t),
 'logins_groups',(SELECT json_agg(c ORDER BY d) FROM (SELECT d,(SELECT count(*) FROM login_attempts WHERE success AND attempted_at>=d AND attempted_at<d+interval '1 day')+(SELECT count(*) FROM groups WHERE created_at>=d AND created_at<d+interval '1 day')+(SELECT count(*) FROM groups WHERE updated_at>created_at AND updated_at>=d AND updated_at<d+interval '1 day') c FROM generate_series(date_trunc('day',now())-interval '29 days',date_trunc('day',now()),interval '1 day') d) t),
 'posts',(SELECT json_agg(c ORDER BY d) FROM (SELECT d,(SELECT count(*) FROM posts WHERE created_at>=d AND created_at<d+interval '1 day') c FROM generate_series(date_trunc('day',now())-interval '29 days',date_trunc('day',now()),interval '1 day') d) t),
 'edits',(SELECT json_agg(c ORDER BY d) FROM (SELECT d,(SELECT count(*) FROM post_versions WHERE created_at>=d AND created_at<d+interval '1 day')+(SELECT count(*) FROM comments WHERE created_at>=d AND created_at<d+interval '1 day') c FROM generate_series(date_trunc('day',now())-interval '29 days',date_trunc('day',now()),interval '1 day') d) t),
 'tasks',(SELECT json_agg(c ORDER BY d) FROM (SELECT d,(SELECT count(*) FROM tasks WHERE updated_at>=d AND updated_at<d+interval '1 day') c FROM generate_series(date_trunc('day',now())-interval '29 days',date_trunc('day',now()),interval '1 day') d) t),
 'strange',(SELECT json_agg(c ORDER BY d) FROM (SELECT d,(SELECT count(*) FROM login_attempts WHERE NOT success AND attempted_at>=d AND attempted_at<d+interval '1 day')+(SELECT count(*) FROM users WHERE confirmed_at IS NULL AND created_at>=d AND created_at<d+interval '1 day')+(SELECT count(*) FROM guests WHERE created_at>=d AND created_at<d+interval '1 day') c FROM generate_series(date_trunc('day',now())-interval '29 days',date_trunc('day',now()),interval '1 day') d) t))
)"

if psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -Atc "$SQL" > "$TMP" 2>"$ERR" && [ -s "$TMP" ]; then
  mv "$TMP" "$OUT"
  chmod 644 "$OUT"
  echo "ok  $(date)"
else
  echo "FAILED  $(date)" >&2
  cat "$ERR" >&2
fi
rm -f "$TMP" "$ERR"
