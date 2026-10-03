[Document](https://docs.google.com/document/d/1I8r55bufq-oT_5jf5otkucac9rpgK5Wz6gFIFTizYNI/edit?usp=sharing)
# NeedPedia Documentation


## Module 1: Homepage
The home page of needpedia contains a search for posts and users, an intro video and a "how to section".
The template file can be found [here](https://github.com/Queuevius/Needpedia2/blob/master/app/views/home/index.html.erb) and its controller action is [here](https://github.com/Queuevius/Needpedia2/blob/master/app/controllers/home_controller.rb#L3)



1. **Managing video:** \
The links for video are saved in Database, so if in future needs to be changed just need to create a record or update the existing from Admin dashboard. \
The _model_ for videos is [home_video.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/home_video.rb)
2. **Managing “How To” section:** \
The _model_ for “How To” is [how_to.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/how_to.rb) \
There are two fields _question_ and _answer _containing the text for question and answer. Both question and answer also can have an image attached.
3. **Search:**
    For search the [ransack](https://github.com/activerecord-hackery/ransack) gem is used. The search form is submitted to [search_result](https://github.com/Queuevius/Needpedia2/blob/master/app/controllers/posts_controller.rb#L178) action. The template for the search on Homepage is[ _search.html.erb](https://github.com/Queuevius/Needpedia2/blob/master/app/views/home/_search.html.erb). \
The search function would find both the posts and users based on the provided query parameters. Service classes are used to lift the heavy weight of finding records in DB. for users filtering [user_search_service.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/services/user_search_service.rb) and for filtering posts records the [post_search_service.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/services/post_search_service.rb) is used. \

4. **Image buttons (on home page for new posts):** \
The images for image buttons are saved in Database, so if in future needs to be changed just need to create a record or update the existing from Admin dashboard.


## Module 2: Nav Bar

The navbar template is [_navbar.html.erb](https://github.com/Queuevius/Needpedia2/blob/master/app/views/shared/_navbar.html.erb).


## Module 3: Search Page

For search the [ransack](https://github.com/activerecord-hackery/ransack) gem is used. The search form is submitted to [search_result](https://github.com/Queuevius/Needpedia2/blob/master/app/controllers/posts_controller.rb#L178) action. The template for the search on Homepage is[ _search.html.erb](https://github.com/Queuevius/Needpedia2/blob/master/app/views/home/_search.html.erb). \
The search function would find both the posts and users based on the provided query parameters. Service classes are used to lift the heavy weight of finding records in DB. for users filtering [user_search_service.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/services/user_search_service.rb) and for filtering posts records the [post_search_service.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/services/post_search_service.rb) is used.


## Module 4: Wiki Posts

Posts are the fundamental part of Needpedia, there are 4 primary types of post and 2 secondary types of posts. The Primary post are:

* Subject (or Area)
* Problem
* Idea
* Quick Share


The secondary types are:

* Social media
* Layer

There is only one database table used for all types of posts, for differentiating different types, a field named post_type is used, which must be populated with the post type (Area/Problem/Proposal/Idea/Layer/Social Media). All the types are managed in the [post.rb ](https://github.com/Queuevius/Needpedia2/blob/master/app/models/post.rb)model.



1. Area is the root of the hierarchy
2. Area has two immediate childrens 1) Problem 2) Proposal. Problem and proposal can’t exist without an Area post.
3. and then Problem has one immediate child “Idea”. Idea can’t exists without Problem post
4. All posts can have many layers. 
5. Social media posts can exist without any parent.

For [Area-Problem/Proposal](https://github.com/Queuevius/Needpedia2/blob/master/app/models/post.rb#L37:L38) relationship a field named _area_id _is used containing the id of parent Area post and then we can figure out if a post is Problem or Proposal based on the _post_type _field.

For [Problem-Idea](https://github.com/Queuevius/Needpedia2/blob/master/app/models/post.rb#L40:L41) relationship a field named _problem_id _is used containing the id of parent Problem post.

For [Any post-Layer](https://github.com/Queuevius/Needpedia2/blob/master/app/models/post.rb#L43:L44) relationship a field named _post_id _is used containing the id of parent Problem post.

There are also Private posts and Curated posts, Private posts are as its name explains are private and only people given the access can view these posts, while curated posts are the ones where only people given access can edit. Its related code is [here](https://github.com/Queuevius/Needpedia2/blob/master/app/models/post.rb#L61:L65).

Further, posts can have many [likes](https://github.com/Queuevius/Needpedia2/blob/master/app/models/like.rb), [flags](https://github.com/Queuevius/Needpedia2/blob/master/app/models/flag.rb), [shares](https://github.com/Queuevius/Needpedia2/blob/master/app/models/share.rb), [comments](https://github.com/Queuevius/Needpedia2/blob/master/app/models/comment.rb), [ratings](https://github.com/Queuevius/Needpedia2/blob/master/app/models/rating.rb) \


Here is the link for the [post_controller.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/controllers/posts_controller.rb) and its related views can be found [here](https://github.com/Queuevius/Needpedia2/tree/master/app/views/posts)

### Idea post:
 (December 2022)Idea post would looks different from now on and has more features than the rest of the Post types.
The file for the view of idea post can be found here [_idea_post.html.erb](https://github.com/Queuevius/Needpedia/blob/master/app/views/posts/_idea_post.html.erb). 
Idea posts has more features and are listed as below:

* UI is different from normal posts, file: [_idea_post.html.erb](https://github.com/Queuevius/Needpedia/blob/master/app/views/posts/_idea_post.html.erb)
* for images there is a separate carousal introduced, file: [_idea_post.html.erb](https://github.com/Queuevius/Needpedia/blob/master/app/views/posts/_idea_post.html.erb)
* Resource tags has a separate area and also these tags can be updated.
* Objectives: The idea behind "Objectives" is that experts on their own layers will come up with objectives for the community, which they can post on the public layer. The files for it is here. [objective.rb](https://github.com/Queuevius/Needpedia/blob/master/app/models/objective.rb), related views folder: [objectives](https://github.com/Queuevius/Needpedia/tree/master/app/views/objectives) and controller [objectives_controller.rb](https://github.com/Queuevius/Needpedia/blob/master/app/controllers/objectives_controller.rb)
* Interested Users: represents if someone's interested in being a part of a project. Related files:
model: [interested_user.rb](https://github.com/Queuevius/Needpedia/blob/master/app/models/interested_user.rb), views folder: [interested_users](https://github.com/Queuevius/Needpedia/tree/master/app/views/interested_users) and controller: [interested_users_controller.rb](https://github.com/Queuevius/Needpedia/blob/master/app/controllers/interested_users_controller.rb)
* Related contents: on this area users would be commenting with related content. Related files:
model: [related_content.rb](https://github.com/Queuevius/Needpedia/blob/master/app/models/related_content.rb), views folder: [related_contents](https://github.com/Queuevius/Needpedia/tree/master/app/views/related_contents) and controller: [related_contents_controller.rb](https://github.com/Queuevius/Needpedia/blob/master/app/controllers/related_contents_controller.rb)
* comments has also now a separate section on idea posts

### Quick share post:
 (January 2023) Quick share posts are quick Idea post and would look more like Idea post but it DOES NOT have parent problem and subject posts and also it does not have the functions like private/curated and geomaxxing.

Module 5: User Accounts

The model for users is [user.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/user.rb). We use the [devise](https://github.com/heartcombo/devise) gem for authentication. Any profile info is saved on this table.

[profile_controller.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/controllers/profile_controller.rb) is used to update user profile related data, and to navigate through different pages on the wall page.


## Module 6: Admin Accounts

In the users table, there is a field named _admin, _when this is true, the user is thought to be admin. We use [administrate](https://github.com/thoughtbot/administrate) gem for handling the admin section. Admin can see/manage the Post Tokens, Tokens ans debates, Connections, User gigs, Flags, Comments, Gigs, Posts, Users and Notifications on Needpedia. Please go through the documentation of administrate gem to know more about the gem. \
 \
The controllers for handling actions on the Admin panel are [here](https://github.com/Queuevius/Needpedia2/tree/master/app/controllers/admin), mainly this section is used when custom functions are required, otherwise everything else can be achieved by the gem’s configurations for models. [dashboards](https://github.com/Queuevius/Needpedia2/tree/master/app) are used for handling CRUD operations on models.


## Module 7: Token system

Tokens are clickable links that can be added to any post text when editing it. The model used for the tokens is [post_token.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/post_token.rb). As a common practise a post_token_type field is used to differentiate between tokens while using a common table/model for the tokens.There are three types of tokens: \




1. **Note Token** \
 Note token just a simple note, it just a simple text
2. **Question Token** \
Question token is a question, users are able to add question tokens and then can be answered by other users.
3. **Debate Token**

    Debate token an argument where users can provide three kinds of answers for it. In favour of the main argument, against the argument and a neutral for neither supporting nor opposing the argument.


    The three types of keywords used for argument types are

1. against
2. for
3. neutral

The model used for the debate arguments is [here](https://github.com/Queuevius/Needpedia2/blob/master/app/models/token_ans_debate.rb).

The controller used for tokens is [post_tokens_controller.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/controllers/post_tokens_controller.rb), and for debate argument the controller used is [here](https://github.com/Queuevius/Needpedia2/blob/master/app/controllers/token_ans_debates_controller.rb).

We use [summernote](https://summernote.org/) as our WYSIWYG editor.


##  \
Module 9: Time Bank

The related models used for Time banks are: \




1. **Gig**

    The model for gigs is [gig.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/gig.rb), gigs have fields like a title, tags, body amount. A Gig goes through different states, which are:

1. Pending
2. Active
3. Progress
4. Awarded
5. Disabled

	Gigs have by default a “Pending” state.

	The controller for gigs is [gigs_controller.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/controllers/gigs_controller.rb) and its related templates are in the [gigs](https://github.com/Queuevius/Needpedia2/tree/master/app/views/gigs) folder.


     



2. **Transaction** \
The [transaction.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/transaction.rb) model is responsible for keeping track of the credits each user has. Every time a gig is offered or rewarded, the credits are calculated and saved in DB in this _transactions_ table.  By default every user has 1 credit hour and they can further increase or decrease this amount by offering gigs or completing gigs. The default credits are assigned here in the [user.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/user.rb#L71) model.

    [transaction_service.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/services/transaction_service.rb) is used for lifting the heavy weight of creating transactions.


    The [transactions_controller.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/controllers/transactions_controller.rb) is responsible for CRUD operation of the transactions.



## Module 10: Messages

Users can use the chat system to communicate and engage with each other on the platform. The related models are: \
[conversation.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/conversation.rb) and [message.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/message.rb), usually a conversation record is created for two users and then messages are associated with that conversation record. \
 \
To provide real time messaging experience, action cable is used for it, which uses redis.

The [conversations_controller.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/controllers/conversations_controller.rb) is used for CRUD on conversations and for handling messages, the [messages_controller.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/controllers/messages_controller.rb) is used.


## Module 11: Notifications

Different types of notifications are shown on different events, for example when a user receives a new message, when their post is edited and so on. The model for notifications is [notification.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/notification.rb), its related view files are in the [notifications](https://github.com/Queuevius/Needpedia2/tree/master/app/views/notifications) folder.

Here are some of the notifications that are working currently:



1. If someone posts something to your /wall.
2. If you've dropped a token and someone interacts with it.
3. If you've added an answer to a question token, or an argument to a debate token, and someone upvoted or downvoted it.
4. If you've made a post (anywhere) and someone comments on it.
5. If you've made a comment (anywhere) and someone replies to it.
6. If you've replied to a comment and someone else replied to it too.
7. If you're tracking a post and someone creates a new layer to it.
8. If someone added you as a friend.


## Module 12: Connections and Friend Requests

Users can connect with each other via the “Friends” feature of the platform, the related models are [connection.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/connection.rb) and [connection_request.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/connection_request.rb), the controller can be found [here](https://github.com/Queuevius/Needpedia2/blob/master/app/controllers/connection_requests_controller.rb).

Module 13: Comments and Replies

Users will be able to add comments on other user posts for that he must be login. Each comment can have multiple replies and if the comment is changed all their repliers will be notified regarding that comment change. By this way each replier can know if the comment is still related to on which they replied. Also users are able to Edit and delete their comments and replies and they can also mark other audience comments and replies as flagged. Admin will have all access to view which user flag which comment and the reason for flagging. On each comment and reply a user will be notified that his comment is being replied by the user. Also if a user tries to delete a comment it will be soft deleted from the system for which we are mainlining the status column in table **comments**. For replies we are using self relation with comments and **parent_id** for referencing. Comments that have **parent_id** are replies to comments with that **parent_id**. The related models are [comment.rb](https://github.com/Queuevius/Needpedia2/blob/master/app/models/comment.rb) and controllers used for this are [comments_controller.rb](https://github.com/Queuevius/Needpedia/blob/master/app/controllers/comments_controller.rb), its related view files are located here [comments](https://github.com/Queuevius/Needpedia/tree/master/app/views/comments) (this also include the **_reply_form.html.erb** and **reply.html.erb **for replies). 

Module 14: Have and Want Posts

Users can create have and want posts, on each user profile there are options for **Have** and **Want** posts (on the left sidebar [_sidebar.rb](https://github.com/Queuevius/Needpedia/blob/master/app/views/shared/_sidebar.html.erb)) by clicking those there will be posts listing for **Have** and **Want** respectively. For Have and Want posts we are using the same post model [post.rb](https://github.com/Queuevius/Needpedia/blob/master/app/models/post.rb) with post_type **`have`** and **`want`**. Each post in the **Have** and **Want** section will have the ability to edit, delete and also comment like on other posts. We are using the existing post code structure for this. The related models are [post.rb](https://github.com/Queuevius/Needpedia/blob/master/app/models/post.rb) and controllers used for this are [posts_controller.rb](https://github.com/Queuevius/Needpedia/blob/master/app/controllers/posts_controller.rb), its related view files are located here [posts](https://github.com/Queuevius/Needpedia/tree/master/app/views/posts).When we click on **`Create Have Post`** it calls the controller action `**new` **and initialize the post form with post_type ‘have’ or ‘want’, same on create/update and destroy it calls the create, update and destroy action respectively.

Module 15: Freeze Accounts and Posts

Admin has the ability to freeze accounts activity (e.g Sign in, Sign up) also he can disable activity on posts (e.g Post creation, Post updation). For this we are maintaining a table named **Settings **in the database that will handle this. The model for setting can be found here [setting.rb](https://github.com/Queuevius/Needpedia/blob/master/app/models/setting.rb). Here are the files that are initializing **settings** to show in master admin [settings_controller.rb](https://github.com/Queuevius/Needpedia/blob/master/app/controllers/master_admin/settings_controller.rb) and [setting_dashboard.rb](https://github.com/Queuevius/Needpedia/blob/master/app/dashboards/setting_dashboard.rb) and for admin panel [settings_controller.rb](https://github.com/Queuevius/Needpedia/blob/master/app/controllers/admin/settings_controller.rb) and [setting_dashboard.rb](https://github.com/Queuevius/Needpedia/blob/master/app/dashboards/setting_dashboard.rb).


## Module 16: Master Admin Accounts

In the users table, there is a field named _master_admin, _when this is true, the user is thought to be master admin. We use [administrate](https://github.com/thoughtbot/administrate) gem for handling the master admin section. Master Admin can see/manage everything on this Needpedia. Please go through the documentation of administrate gem to know more about the gem. \
 \
The controllers for handling actions on the Master Admin panel are [here](https://github.com/Queuevius/Needpedia2/tree/master/app/controllers/master_admin), mainly this section is used when custom functions are required, otherwise everything else can be achieved by the gem’s configurations for models. [dashboards](https://github.com/Queuevius/Needpedia2/tree/master/app) are used for handling CRUD operations on models.


## Module 17: Nuclear Note

If something forces you to take Needpedia down there is an option in the admin and master admin Settings section by name `Nuclear Note` Once activated, it simply loads the message for anyone trying to visit the site instead of loading anything else. The controller used for this is [nuclear_note_controller.rb](https://github.com/Queuevius/Needpedia/blob/master/app/controllers/nuclear_note_controller.rb). We added a `**nuclear_note**` column in our settings table in the database that turns on and off this behaviour. We have a function named **`check_nuclear_note` **[application_controller.rb](https://github.com/Queuevius/Needpedia/blob/master/app/controllers/application_controller.rb)** **that checks with each request that this nuclear note option is on/off and if it's on it redirects to [nuclear_note_controller.rb](https://github.com/Queuevius/Needpedia/blob/master/app/controllers/nuclear_note_controller.rb) index action that shows the page by rendering [nuclear_note_view](https://github.com/Queuevius/Needpedia/blob/master/app/views/nuclear_note/index.html.erb).


## Module 17: User Feedback

Users will have the ability to provide feedback to Needpedia. For that we created a Feedbacks table in the database, User can go to his profile setting (/users/edit) and can provide feedback by submitting the form. Admin/Master Admin can view the user feedback in the Admin / Master Admin Panel. The related models for these are [feedback_question_option.rb](https://github.com/Queuevius/Needpedia/blob/master/app/models/feedback_question_option.rb), [feedback_question.rb](https://github.com/Queuevius/Needpedia/blob/master/app/models/feedback_question.rb), [feedback_response.rb](https://github.com/Queuevius/Needpedia/blob/master/app/models/feedback_response.rb), [feedback.rb](https://github.com/Queuevius/Needpedia/blob/master/app/models/feedback.rb). We are pre populating questions and responses for each question for that **feedback_question** and **feedback_question_option** model used. A rake task is added in [populate_feedback_data](https://github.com/Queuevius/Needpedia/blob/master/lib/tasks/populate_feedback_data.rake) for data populating initially. Each feedback has many responses by the user that are stored in the **feedback_responses** table. The controller used for feedback action is [feedbacks_controller](https://github.com/Queuevius/Needpedia/blob/master/app/controllers/feedbacks_controller.rb) and views are located at [feedbacks](https://github.com/Queuevius/Needpedia/tree/master/app/views/https://github.com/Queuevius/Needpedia/tree/master/app/views/feedbacks).


## Other Important Gems used:



1. [Public_activity](https://github.com/chaps-io/public_activity): it is used to track the activity that is shown on the feed page
2. [Kaminari](https://github.com/kaminari/kaminari): used for pagination
3. [Capistrano](https://github.com/capistrano/capistrano):   for deployments
4. [Letter_opener](https://github.com/ryanb/letter_opener): for emails of development


## Deployment Details

The server used for Needpedia production is on AWS, you need to be authorized and must have a .pem file to access the production server. We use passengers with ngnix on production.

We use [Capistrano](https://github.com/capistrano/capistrano) gem for deployments, please go through its documentation to understand further. We have only one environment i.e production.

Deploying command is:

_cap deploy production_

This will do everything (bundle install, run migrations, versioning deployed and assets compiling etc) for you.
