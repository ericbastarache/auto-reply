## Auto Reply Bot

This simple script will allow you to automate replying to messages on LinkedIn based on receiving a certain text string. For example, if you want to reply to certain messages on LinkedIn which contain a certain phrase, you'd be able to add your check for that string easily. Simply update the `TEXT_TO_SEARCH` environment variable and you're good to go!

### Environment Variables

- Copy .env.example to .env (don't worry this is never committed to git!)

`LINKEDIN_EMAIL` - This is your LinkedIn email address, required to log you into your account so the bot can access your messages
`LINKEDIN_PASSWORD` - This is your LinkedIn password, self explanatory why this is needed
`TEXT_TO_SEARCH` - This is the text string you want to search by in order to have the bot send an automated reply to the sender. The message is currently pre-filled but you can edit this and place it somewhere else (or create a collection of responses to use) to make it more customizable. 

