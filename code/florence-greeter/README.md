# Florence, Needpedia's greeter

Florence is the AI assistant that greets visitors to needpedia.org who are
not logged in. She answers their questions and helps them decide whether
to join. She is one of Needpedia's three assistants, Florence, Lotte and
Adele, named after librarians who resisted fascism.

She is a small website app (built with Next.js) that runs on Vercel, a
website hosting service. Every change to this project's main branch goes
live automatically.

Needpedia: https://needpedia.org
Every Needpedia system, including this one:
https://github.com/Queuevius/Needpedia/wiki/Needpedia-Inventory

## Which AI service she uses

OpenRouter, one account that reaches many AI models. No OpenAI account
is needed.

This project began as OpenAI's "Assistants API Quickstart" template and
still uses OpenAI's free, open-source software toolkit ("openai" in
package.json). That toolkit is only a ready-made way of writing messages
to an AI service, and it is pointed at OpenRouter's address with an
OpenRouter key (see app/openai.ts). Nothing is sent to OpenAI.

To use a different AI service: any service that accepts the same kind of
messages works. Change three settings: OPENROUTER_BASE_URL (the
service's address), OPENROUTER_API_KEY (its key) and OPENROUTER_MODEL
(the model's name). No code change is needed.

Needpedia recommends DeepSeek V4 v0813: very cheap, and it can run on
European servers that protect user data.

## Her settings

Set these in the Vercel project's settings (or in a file named .env when
running her on your own computer; copy .env.example to start).

Settings whose names start with NEXT_PUBLIC_ are visible to anyone using
Florence in their browser. Never put a key or token in one of those.

AI service:
- OPENROUTER_API_KEY: the AI service's key. Required.
- OPENROUTER_BASE_URL: the AI service's address. If left empty, she uses
  OpenRouter's, https://openrouter.ai/api/v1
- OPENROUTER_MODEL: which AI model to use.
- NEXT_PUBLIC_APP_URL: Florence's own web address. Sent to the AI service
  to say which app is calling.

The Needpedia site she works with:
- NEXT_PUBLIC_API_BASE_URL: the Needpedia site's address, for example
  https://needpedia.org . She uses it to load her instructions, look up
  posts, and in the chat screen itself (the example settings file lists
  usage tokens, conversation threads and her master instructions).
- PROMPT_API_TOKEN: the token she uses to load her instructions from the
  Needpedia site. It must match the prompt token set on the Needpedia
  server.
- PROMPT_AI_TYPE: which set of instructions to load. Instructions are
  written and versioned on the Needpedia site's admin pages (master admin,
  AI KBs). If left empty, she asks for "Florence".
- BEARER_TOKEN: the token she uses when looking up posts on the Needpedia
  site (app/api/posts/route.ts). Without it, post lookups return an error.

The chat screen:
- NEXT_PUBLIC_INITIAL_MESSAGE_TEXT: her first message to a visitor. If
  left empty: "👋Welcome! How can I help you today with Needpedia?"
- NEXT_PUBLIC_MAX_TOKENS: a limit the chat screen uses. If left empty,
  2000.

## Running her on your own computer

You need Node.js. Then, in this project's folder:

    npm install
    cp .env.example .env
    (fill in .env)
    npm run dev

She opens at http://localhost:3000

## Running her online

Connect this project to a Vercel account, add the settings above in the
Vercel project's settings, and deploy. Any other host that runs Next.js
apps works too.

## History

- Started from OpenAI's Assistants API Quickstart template.
- Rebuilt by Murtaza, Needpedia's lead developer, to use OpenRouter and
  to take her instructions from the Needpedia site.
- 20 August 2026: conversation saving added, so her conversations appear
  in the Needpedia site's AI chat transcripts.
- 1 October 2026: this document rewritten to match the code. The old one
  was still the template's instructions for setting up an OpenAI
  account.

## Licence

See LICENSE.
