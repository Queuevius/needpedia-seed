NEEDPEDIA REPO MAP 1.0
Where things live in the codebase

Version 1.0 — 14 September 2026
Companion to Needpedia Capabilities 1.1. That document says what the site does;
this one says where in the code it does it.
Repository: https://github.com/Queuevius/Needpedia
Verified against the repository at commit 26563af, 11 September 2026.

Code changes need the lead developer's review before merging. Documentation
does not.


================================================================
READ THIS BEFORE TRUSTING ANY OF IT
================================================================

The GitHub wiki at https://github.com/Queuevius/Needpedia/wiki was written in
January 2023 and is missing roughly half the current codebase — groups, task
cards, topics, version history, the AI assistants, fediverse, webhooks, and
more. Several of its links point at a repository named Needpedia2 rather than
Needpedia. Use it for background, not for facts.

The live site has not been deployed in some time, so the code described here is
ahead of needpedia.org.


================================================================
SHAPE OF THE PROJECT
================================================================

Ruby on Rails. Roughly the standard layout:

  app/models/        one file per kind of thing the site stores
  app/controllers/   one file per kind of request the site handles
  app/views/         the actual pages, one folder per controller
  app/services/      the heavier logic, pulled out of controllers
  app/jobs/          work that happens in the background
  config/routes.rb   every URL the site answers, in one file
  db/schema.rb       every database table and column, in one file

Two files are worth more than any documentation when you need a fact fast:
config/routes.rb tells you every address the site responds to, and db/schema.rb
tells you every piece of data it stores. Read those before asking anyone.


================================================================
WHERE EACH FEATURE LIVES
================================================================

POSTS — subjects, problems, ideas, layers, and the rest
  app/models/post.rb             all nine post types, the parent rules, the
                                 privacy and curation rules
  app/controllers/posts_controller.rb
  app/views/posts/
  app/views/posts/_idea_post.html.erb   the distinct idea post layout
  app/services/post_search_service.rb
  app/services/posts_service.rb
  app/services/delete_post_service.rb

  The nine types, all in one database table, told apart by a type field:
  subject, problem, idea, layer, geomaxing, social_media, have, want,
  quick_share.

TOKENS — note, question, debate
  app/models/post_token.rb
  app/models/token_ans_debate.rb        the for/against/neutral replies
  app/controllers/post_tokens_controller.rb
  app/controllers/token_ans_debates_controller.rb

VERSION HISTORY
  app/models/post_version.rb
  app/controllers/post_versions_controller.rb

OBJECTIVES, INTERESTED USERS, RELATED CONTENT
  app/models/objective.rb, interested_user.rb, related_content.rb
  and the matching controllers and view folders

RATINGS AND THE LOL VOTE
  app/models/rating.rb                  the scale is 0-5 plus Lol, stored as 6
  app/controllers/ratings_controller.rb the mutual-exclusion bug lives here

GROUPS, TOPICS, TASK CARDS
  app/models/group.rb, topic.rb, task.rb
  app/models/membership.rb, invitation.rb, request.rb
  app/controllers/groups_controller.rb, topics_controller.rb,
    tasks_controller.rb

TIME BANK
  app/models/gig.rb, transaction.rb, user_gig.rb
  app/services/transaction_service.rb
  app/controllers/gigs_controller.rb, transactions_controller.rb

AI ASSISTANTS
  Prompts are NOT in the code. They live in the database and are edited from the
  admin page at master_admin/ai_prompts. Versioned — activating a new version
  deactivates the old one.
  app/models/ai_prompt.rb               the versioning rules
  app/models/ai_token.rb                the per-user and per-guest usage budget
  app/models/chat_thread.rb, chat_message.rb    stored conversations
  app/controllers/api/v1/chat_messages_controller.rb
  app/services/ai_prompt_activator.rb
  app/models/user_assistant_document.rb reference PDFs for the assistants

NOTIFICATIONS AND PUSH
  app/models/notification.rb, notification_setting.rb, device.rb
  app/services/notification_service.rb, send_notification_service.rb
  app/services/push_notification_service.rb, fcm_service.rb
  app/controllers/api/v1/device_registration_controller.rb
  app/jobs/send_notifications_job.rb

MESSAGES AND CONNECTIONS
  app/models/conversation.rb, message.rb
  app/models/connection.rb, connection_request.rb, blocked_user.rb

SEARCH
  app/services/post_search_service.rb
  app/services/user_search_service.rb
  the tab-choosing bug is in app/controllers/posts_controller.rb, in the
  search_result action

LOGIN, SIGNUP, TWO-FACTOR
  app/controllers/users/sessions_controller.rb   also where failed login
                                                 attempts are recorded
  app/controllers/users/registrations_controller.rb
  app/controllers/users/omniauth_callbacks_controller.rb
  app/controllers/otp_verifications_controller.rb
  app/models/login_attempt.rb, blocked_ip.rb
  app/models/service.rb                 outside-account sign-in

FEDIVERSE
  app/controllers/activity_pub/         the account, inbox, outbox, webfinger
  app/services/activity_pub/
  app/services/federated_posts_fetcher.rb
  app/models/remote_follow.rb
  app/controllers/federated_posts_controller.rb, remote_follows_controller.rb
  The line that would publish new posts outward is in app/models/post.rb and is
  commented out.

PUBLIC AND APP INTERFACES
  app/controllers/api/                  v1 is the phone app, v2 is public
  app/controllers/webhooks/
  app/models/webhook_configuration.rb, webhook_setting.rb
  Documentation is generated automatically and served at /apipie

ADMIN
  app/controllers/admin/                admin tier
  app/controllers/master_admin/         master admin tier, sees everything
  app/dashboards/                       what each admin screen shows
  app/models/setting.rb                 the freeze switches and the nuclear note
  app/models/banned_term.rb

HOMEPAGE AND STATIC PAGES
  app/views/home/index.html.erb         homepage text
  app/controllers/home_controller.rb    about us, privacy, terms, faq, careers,
                                        time bank, contact
  app/models/home_video.rb, how_to.rb, button_image.rb

FEEDBACK SURVEY
  app/controllers/feedbacks_controller.rb
  app/models/feedback.rb, feedback_question.rb, feedback_question_option.rb,
    feedback_response.rb
  The questions are stored in the database, not the code. If none have been
  entered, the page renders empty.

DEPLOYMENT
  config/deploy.rb                      currently points at the STAGING folder,
                                        with the production line commented out
  config/deploy/production.rb           names server 18.223.241.10
  config/deploy/staging.rb              names the same server

  These two facts together mean a deploy could overwrite staging while looking
  like it updated production. Do not deploy until the lead developer confirms
  which folder is live and the exact command.


================================================================
NOTABLE OUTSIDE PIECES
================================================================

  Devise           login and accounts
  Administrate     the admin panels
  Ransack          search
  Kaminari         paging
  ActionText       the rich text editor and stored content
  ActiveStorage    uploaded images
  ActionCable      real-time messaging, via Redis
  PublicActivity   the activity feed
  Sidekiq          background jobs, viewable at /sidekiq for admins
  Capistrano       deployment
  Apipie           the generated API documentation


================================================================
HOW TO ANSWER A QUESTION ABOUT THIS CODEBASE
================================================================

  What addresses exist?            config/routes.rb
  What data is stored?             db/schema.rb
  What are the rules for a thing?  its file in app/models/
  What happens on a request?       its file in app/controllers/
  What does a page look like?      the matching folder in app/views/

Read the file. Do not infer behaviour from a file name or a branch name — the
names in this codebase are not always accurate, and at least one feature is
referred to by three different words in three different places.