TITLE: Getting Authenticated User Info (Python)
DESCRIPTION: Implements a Python function using the `requests` library to fetch details of the user associated with the provided access token. It makes a GET request to the Discord API's `/users/@me` endpoint, including the access token in the `Authorization` header with the `Bearer` prefix.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/discord-social-sdk/development-guides/using-with-discord-apis.mdx#_snippet_3

LANGUAGE: python
CODE:
```
def get_user_info(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
    return response.json()
```

----------------------------------------

TITLE: Authenticating API Request with Bearer Token (curl)
DESCRIPTION: Demonstrates making a GET request to the Discord API `/users/@me` endpoint to fetch information about the currently authenticated user. It requires setting the `Authorization` header with the `Bearer` prefix followed by the user's access token, typically obtained through the OAuth2 flow.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/discord-social-sdk/development-guides/using-with-discord-apis.mdx#_snippet_1

LANGUAGE: curl
CODE:
```
curl -X GET https://discord.com/api/v10/users/@me \
  -H "Authorization: Bearer USER_ACCESS_TOKEN"
```

----------------------------------------

TITLE: Example Full Discord Guild Object JSON
DESCRIPTION: This JSON object provides a detailed example of the structure and properties of a Discord Guild object as returned by the API. It includes basic information like ID, name, icon, and features, as well as configuration details like verification level, notification settings, and channel IDs. It demonstrates the various fields developers can expect when retrieving guild data.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/resources/guild.mdx#_snippet_0

LANGUAGE: JSON
CODE:
```
{
  "id": "197038439483310086",
  "name": "Discord Testers",
  "icon": "f64c482b807da4f539cff778d174971c",
  "description": "The official place to report Discord Bugs!",
  "splash": null,
  "discovery_splash": null,
  "features": [
    "ANIMATED_ICON",
    "VERIFIED",
    "NEWS",
    "VANITY_URL",
    "DISCOVERABLE",
    "MORE_EMOJI",
    "INVITE_SPLASH",
    "BANNER",
    "COMMUNITY"
  ],
  "emojis": [],
  "banner": "9b6439a7de04f1d26af92f84ac9e1e4a",
  "owner_id": "73193882359173120",
  "application_id": null,
  "region": null,
  "afk_channel_id": null,
  "afk_timeout": 300,
  "system_channel_id": null,
  "widget_enabled": true,
  "widget_channel_id": null,
  "verification_level": 3,
  "roles": [],
  "default_message_notifications": 1,
  "mfa_level": 1,
  "explicit_content_filter": 2,
  "max_presences": 40000,
  "max_members": 250000,
  "vanity_url_code": "discord-testers",
  "premium_tier": 3,
  "premium_subscription_count": 33,
  "system_channel_flags": 0,
  "preferred_locale": "en-US",
  "rules_channel_id": "441688182833020939",
  "public_updates_channel_id": "281283303326089216",
  "safety_alerts_channel_id": "281283303326089216"
}
```

----------------------------------------

TITLE: Acknowledging Discord PING Interaction Python
DESCRIPTION: This Python snippet, likely within a Flask application, demonstrates how to acknowledge an incoming Discord interaction request of type 1 (PING). It checks the interaction type and returns a 200 OK response with a JSON payload containing {"type": 1}, which is required by Discord for endpoint validation.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/interactions/overview.mdx#_snippet_0

LANGUAGE: Python
CODE:
```
@app.route('/', methods=['POST'])
def my_command():
    if request.json["type"] == 1:
        return jsonify({
            "type": 1
        })
```

----------------------------------------

TITLE: Exposing Local Server with ngrok (Shell)
DESCRIPTION: This command uses ngrok to create a secure tunnel from a public URL to a local server running on port 3000. This allows Discord's API to send interaction requests to the local application server, bypassing the need for a publicly hosted server during development. It requires ngrok to be installed and running, and the application server must be listening on the specified port.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/quick-start/getting-started.mdx#_snippet_5

LANGUAGE: Shell
CODE:
```
ngrok http 3000
```

----------------------------------------

TITLE: Receiving Modal Submission Interaction Payload - Discord API JSON
DESCRIPTION: This JSON object represents the payload received by a Discord application when a user submits a modal. It includes details about the application, channel, guild, user/member, and importantly, the submitted `data` containing component values, such as the text input value ('John' for 'custom_id': 'name'). This payload is used to process the user's input from the modal.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/components/reference.mdx#_snippet_7

LANGUAGE: json
CODE:
```
{
    "application_id": "845027738276462632",
    "channel": {
        "flags": 0,
        "guild_id": "772904309264089089",
        "id": "772908445358620702",
        "last_message_id": "113817814796417433",
        "name": "general",
        "nsfw": false,
        "parent_id": "1113560261366927532",
        "permissions": "281474976710655",
        "position": 0,
        "rate_limit_per_user": 0,
        "topic": null,
        "type": 0
    },
    "channel_id": "772908445358620702",
    "data": {
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "custom_id": "name",
                        "type": 4,
                        "value": "John"
                    }
                ]
            }
        ],
        "custom_id": "cool_modal"
    },
    "guild_id": "772904309264089089",
    "id": "847587388497854464",
    "member": {
        "avatar": null,
        "deaf": false,
        "is_pending": false,
        "joined_at": "2020-11-02T19:25:47.248000+00:00",
        "mute": false,
        "nick": null,
        "pending": false,
        "permissions": "17179869183",
        "premium_since": null,
        "roles": ["785609923542777878"],
        "user": {
            "avatar": "a_d5efa99b3eeaa7dd43acca82f5692432",
            "global_name": "Mason",
            "discriminator": "0",
            "id": "53908232506183680",
            "public_flags": 131141,
            "username": "Mason"
        }
    },
    "token": "UNIQUE_TOKEN",
    "type": 5,
    "version": 1
}
```

----------------------------------------

TITLE: Handling Profile Command with Context - JavaScript
DESCRIPTION: This JavaScript snippet demonstrates how to handle the `/profile` command by checking the `interactionContext` from the request body. If the interaction occurs outside of a direct message with the bot (context !== 1), the response is made ephemeral using flags=64 and a 'Share Profile' button component is added. It constructs the response payload dynamically based on the context before sending it back.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/tutorials/developing-a-user-installable-app.mdx#_snippet_6

LANGUAGE: javascript
CODE:
```
// "profile" command
if (name === 'profile') {
  const profile = getFakeProfile(0);
  const profileEmbed = createPlayerEmbed(profile);

  // Use interaction context that the interaction was triggered from
  const interactionContext = req.body.context;

  // Construct `data` for our interaction response. The profile embed will be included regardless of interaction context
  let profilePayloadData = {
    embeds: [profileEmbed],
  };

  // If profile isn't run in a DM with the app, we'll make the response ephemeral and add a share button
  if (interactionContext !== 1) {
    // Make message ephemeral
    profilePayloadData['flags'] = 64;
    // Add button to components
    profilePayloadData['components'] = [
      {
        type: 1,
        components: [
          {
            type: 2,
            label: 'Share Profile',
            custom_id: 'share_profile',
            style: 2,
          },
        ],
      },
    ];
  }

  // Send response
  return res.send({
    type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
    data: profilePayloadData,
  });
}
```

----------------------------------------

TITLE: Validating Discord Signature JavaScript
DESCRIPTION: This JavaScript snippet uses the tweetnacl library to verify the authenticity of a Discord interaction request by validating the X-Signature-Ed25519 header against the X-Signature-Timestamp and raw request body. It requires the application's public key and responds with a 401 Unauthorized error if the signature is invalid.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/interactions/overview.mdx#_snippet_1

LANGUAGE: JavaScript
CODE:
```
const nacl = require("tweetnacl");

// Your public key can be found on your application in the Developer Portal
const PUBLIC_KEY = "APPLICATION_PUBLIC_KEY";

const signature = req.get("X-Signature-Ed25519");
const timestamp = req.get("X-Signature-Timestamp");
const body = req.rawBody; // rawBody is expected to be a string, not raw bytes

const isVerified = nacl.sign.detached.verify(
    Buffer.from(timestamp + body),
    Buffer.from(signature, "hex"),
    Buffer.from(PUBLIC_KEY, "hex")
);

if (!isVerified) {
    return res.status(401).end("invalid request signature");
}
```

----------------------------------------

TITLE: Responding to Discord Slash Command (JavaScript)
DESCRIPTION: This JavaScript code snippet handles the '/test' Discord slash command. It checks if the received command name is 'test' and, if true, sends an interaction response of type 'CHANNEL_MESSAGE_WITH_SOURCE' to the channel where the command was triggered. The response includes a simple 'hello world' message appended with a random emoji obtained from a helper function.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/quick-start/getting-started.mdx#_snippet_6

LANGUAGE: javascript
CODE:
```
// "test" command
if (name === 'test') {
    // Send a message into the channel where command was triggered from
    return res.send({
    type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
    data: {
        // Fetches a random emoji to send from a helper function
        content: 'hello world ' + getRandomEmoji(),
    },
    });
}
```

----------------------------------------

TITLE: Example Guild Member JSON Object
DESCRIPTION: This JSON snippet provides a sample representation of a Discord Guild Member object, illustrating the typical structure and data types for its fields as returned by the API. It serves as a reference for understanding how member data is formatted.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/resources/guild.mdx#_snippet_5

LANGUAGE: json
CODE:
```
{
  "user": {},
  "nick": "NOT API SUPPORT",
  "avatar": null,
  "banner": null,
  "roles": [],
  "joined_at": "2015-04-26T06:26:56.936000+00:00",
  "deaf": false,
  "mute": false
}
```

----------------------------------------

TITLE: Authenticating API Request with Bot Token (curl)
DESCRIPTION: Demonstrates making a GET request to the Discord API `/users/@me` endpoint to fetch information about the bot user. It requires setting the `Authorization` header with the `Bot` prefix followed by the bot token. This is typically used for server-to-server interactions.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/discord-social-sdk/development-guides/using-with-discord-apis.mdx#_snippet_0

LANGUAGE: curl
CODE:
```
curl -X GET https://discord.com/api/v10/users/@me \
  -H "Authorization: Bot YOUR_BOT_TOKEN"
```

----------------------------------------

TITLE: Importing and Instantiating Discord SDK in JavaScript
DESCRIPTION: Shows how to import the `DiscordSDK` class and create a new instance, passing the Discord client ID as a constructor argument, which is necessary to initialize the SDK for use in an embedded application.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/developer-tools/embedded-app-sdk.mdx#_snippet_1

LANGUAGE: javascript
CODE:
```
import { DiscordSDK } from "@discord/embedded-app-sdk";

const discordSdk = new DiscordSDK(DISCORD_CLIENT_ID);
```

----------------------------------------

TITLE: Implementing Discord Social SDK Integration - C++
DESCRIPTION: This C++ code snippet provides a complete example of integrating the discordpp SDK. It covers initializing the client, setting up logging and status callbacks, performing the OAuth2 authorization code flow, updating the access token, connecting to Discord, accessing relationships, updating rich presence, and running the main loop to process SDK callbacks.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/discord-social-sdk/getting-started/using-c++.mdx#_snippet_12

LANGUAGE: cpp
CODE:
```
#define DISCORDPP_IMPLEMENTATION
#include "discordpp.h"
#include <iostream>
#include <thread>
#include <atomic>
#include <string>
#include <functional>
#include <csignal>

// Replace with your Discord Application ID
const uint64_t APPLICATION_ID = 1349146942634065960;

// Create a flag to stop the application
std::atomic<bool> running = true;

// Signal handler to stop the application
void signalHandler(int signum) {
    running.store(false);
}

int main() {
    std::signal(SIGINT, signalHandler);
    std::cout << "🚀 Initializing Discord SDK...\n";

    // Create our Discord Client
    auto client = std::make_shared<discordpp::Client>();

    // Set up logging callback
    client->AddLogCallback([](auto message, auto severity) {
      std::cout << "[" << EnumToString(severity) << "] " << message << std::endl;
    }, discordpp::LoggingSeverity::Info);

    // Set up status callback to monitor client connection
    client->SetStatusChangedCallback([client](discordpp::Client::Status status, discordpp::Client::Error error, int32_t errorDetail) {
      std::cout << "🔄 Status changed: " << discordpp::Client::StatusToString(status) << std::endl;

      if (status == discordpp::Client::Status::Ready) {
        std::cout << "✅ Client is ready! You can now call SDK functions.\n";

        // Access initial relationships data
        std::cout << "👥 Friends Count: " << client->GetRelationships().size() << std::endl;

        // Configure rich presence details
        discordpp::Activity activity;
        activity.SetType(discordpp::ActivityTypes::Playing);
        activity.SetState("In Competitive Match");
        activity.SetDetails("Rank: Diamond II");

        // Update rich presence
        client->UpdateRichPresence(activity, [](discordpp::ClientResult result) {
          if(result.Successful()) {
            std::cout << "🎮 Rich Presence updated successfully!\n";
          } else {
            std::cerr << "❌ Rich Presence update failed";
          }
        });

      } else if (error != discordpp::Client::Error::None) {
        std::cerr << "❌ Connection Error: " << discordpp::Client::ErrorToString(error) << " - Details: " << errorDetail << std::endl;
      }
    });

    // Generate OAuth2 code verifier for authentication
    auto codeVerifier = client->CreateAuthorizationCodeVerifier();

    // Set up authentication arguments
    discordpp::AuthorizationArgs args{};
    args.SetClientId(APPLICATION_ID);
    args.SetScopes(discordpp::Client::GetDefaultPresenceScopes());
    args.SetCodeChallenge(codeVerifier.Challenge());

    // Begin authentication process
    client->Authorize(args, [client, codeVerifier](auto result, auto code, auto redirectUri) {
      if (!result.Successful()) {
        std::cerr << "❌ Authentication Error: " << result.Error() << std::endl;
        return;
      } else {
        std::cout << "✅ Authorization successful! Getting access token...\n";

        // Exchange auth code for access token
        client->GetToken(APPLICATION_ID, code, codeVerifier.Verifier(), redirectUri,
          [client](discordpp::ClientResult result,
          std::string accessToken,
          std::string refreshToken,
          discordpp::AuthorizationTokenType tokenType,
          int32_t expiresIn,
          std::string scope) {
            std::cout << "🔓 Access token received! Establishing connection...\n";
            // Next Step: Update the token and connect
            client->UpdateToken(discordpp::AuthorizationTokenType::Bearer,  accessToken, [client](discordpp::ClientResult result) {
              if(result.Successful()) {
                std::cout << "🔑 Token updated, connecting to Discord...\n";
                client->Connect();
              }
            });
        });
      }
    });

    // Keep application running to allow SDK to receive events and callbacks
    while (running) {
      discordpp::RunCallbacks();
      std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }

    return 0;
}
```

----------------------------------------

TITLE: Sending Nested Components (Action Row with Buttons) (JSON)
DESCRIPTION: Example JSON payload demonstrating how to nest components using an Action Row (type 1) containing Button components (type 2). It sets the IS_COMPONENTS_V2 flag (32768) and shows a Text Display component followed by an Action Row containing two buttons with labels, styles, and custom IDs.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/components/using-message-components.mdx#_snippet_2

LANGUAGE: json
CODE:
```
{
  "flags": 32768,
  "components": [
    {
      "type": 10,
      "content": "This is a message with v2 components"
    },
    {
      "type": 1,
      "components": [
        {
          "type": 2,
          "style": 1,
          "label": "Click Me",
          "custom_id": "click_me_1"
        },
        {
          "type": 2,
          "style": 2,
          "label": "Click Me Too",
          "custom_id": "click_me_2"
        }
      ]
    }
  ]
}
```

----------------------------------------

TITLE: Client-side Authorization and Authentication - Discord SDK
DESCRIPTION: Initializes the Discord SDK, requests user authorization with specified scopes (`identify`, `guilds`, `applications.commands`) to obtain an authorization code. It then sends this code to the backend server's `/api/token` endpoint (via a proxy `/.proxy`) to exchange it for an access token and finally authenticates the user with the SDK using the obtained token.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/activities/building-an-activity.mdx#_snippet_13

LANGUAGE: JavaScript
CODE:
```
import { DiscordSDK } from "@discord/embedded-app-sdk";

import rocketLogo from '/rocket.png';
import "./style.css";

// Will eventually store the authenticated user's access_token
let auth;

const discordSdk = new DiscordSDK(import.meta.env.VITE_DISCORD_CLIENT_ID);

setupDiscordSdk().then(() => {
  console.log("Discord SDK is authenticated");

  // We can now make API calls within the scopes we requested in setupDiscordSDK()
  // Note: the access_token returned is a sensitive secret and should be treated as such
});

async function setupDiscordSdk() {
  await discordSdk.ready();
  console.log("Discord SDK is ready");

  // Authorize with Discord Client
  const { code } = await discordSdk.commands.authorize({
    client_id: import.meta.env.VITE_DISCORD_CLIENT_ID,
    response_type: "code",
    state: "",
    prompt: "none",
    scope: [
      "identify",
      "guilds",
      "applications.commands"
    ],
  });

  // Retrieve an access_token from your activity's server
  // Note: We need to prefix our backend `/api/token` route with `/.proxy` to stay compliant with the CSP.
  // Read more about constructing a full URL and using external resources at
  // https://discord.com/developers/docs/activities/development-guides/networking#construct-a-full-url
  const response = await fetch("/.proxy/api/token", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      code,
    }),
  });
  const { access_token } = await response.json();

  // Authenticate with Discord client (using the access_token)
  auth = await discordSdk.commands.authenticate({
    access_token,
  });

  if (auth == null) {
    throw new Error("Authenticate command failed");
  }
}

document.querySelector('#app').innerHTML = `
  <div>
    <img src="${rocketLogo}" class="logo" alt="Discord" />
    <h1>Hello, World!</h1>
  </div>
`;
```

----------------------------------------

TITLE: Example JSON for Container Component with Nested Components
DESCRIPTION: Shows a complete JSON structure for a Discord message payload using a container component (`type: 17`). The example demonstrates nesting text display (`type: 10`), media gallery (`type: 12`), and an action row (`type: 1`) containing button components (`type: 2`) within the container. It also shows how to set the `accent_color` for the container. Requires the `IS_COMPONENTS_V2` message flag.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/components/reference.mdx#_snippet_17

LANGUAGE: json
CODE:
```
"components": [
  {
    "type": 17,
    "accent_color": 703487,
    "components": [
      {
        "type": 10,
        "content": "# You have encountered a wild coyote!"
      },
      {
        "type": 12,
        "items": [
          {
            "media": {"url": "https://websitewithopensourceimages/coyote.png"}
          }
        ]
      },
      {
        "type": 10,
        "content": "What would you like to do?"
      },
      {
        "type": 1,
        "components": [
          {
            "type": 2,
            "custom_id": "pet_coyote",
            "label": "Pet it!",
            "style": 1
          },
          {
            "type": 2,
            "custom_id": "feed_coyote",
            "label": "Attempt to feed it",
            "style": 2
          },
          {
            "type": 2,
            "custom_id": "run_away",
            "label": "Run away!",
            "style": 4
          }
        ]
      }
    ]
  }
]
```

----------------------------------------

TITLE: Defining Modal with Text Input Component JSON
DESCRIPTION: Provides a JSON example demonstrating the structure for defining a Discord modal containing a text input component within an action row. It specifies the modal's title and custom ID, and the text input's type, custom ID, label, style, length constraints, placeholder, and required status.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/components/reference.mdx#_snippet_6

LANGUAGE: json
CODE:
```
// this is a modal
{
  "title": "My Cool Modal",
  "custom_id": "cool_modal",
  "components": [{
    "type": 1,
    "components": [{
      "type": 4,
      "custom_id": "name",
      "label": "Name",
      "style": 1,
      "min_length": 1,
      "max_length": 4000,
      "placeholder": "John",
      "required": true
    }]
  }]
}
```

----------------------------------------

TITLE: Authenticating with Bearer Token using HTTP Header (Text)
DESCRIPTION: Demonstrates the format for the `Authorization` HTTP header when using an OAuth2 bearer token. The header value consists of the "Bearer" token type followed by the actual bearer token, separated by a space.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/reference.mdx#_snippet_5

LANGUAGE: text
CODE:
```
Authorization: Bearer CZhtkLDpNYXgPH9Ml6shqh2OwykChw
```

----------------------------------------

TITLE: Example HTTP 429 Rate Limit Response
DESCRIPTION: Shows a complete HTTP response returned when a user or bot exceeds a rate limit, including the 429 status code, relevant rate limit headers, and the JSON body containing `message`, `retry_after`, and `global` fields.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/topics/rate-limits.md#_snippet_1

LANGUAGE: HTTP
CODE:
```
< HTTP/1.1 429 TOO MANY REQUESTS
< Content-Type: application/json
< Retry-After: 65
< X-RateLimit-Limit: 10
< X-RateLimit-Remaining: 0
< X-RateLimit-Reset: 1470173023.123
< X-RateLimit-Reset-After: 64.57
< X-RateLimit-Bucket: abcd1234
< X-RateLimit-Scope: user
{
  "message": "You are being rate limited.",
  "retry_after": 64.57,
  "global": false
}
```

----------------------------------------

TITLE: Calculating and Checking Permissions - Discord API - Python
DESCRIPTION: Demonstrates how to calculate a combined permission value by using the bitwise OR operator (|) on individual permission flag integers. It also shows how to check if a specific permission flag is set within the combined value using the bitwise AND operator (&).
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/topics/permissions.md#_snippet_0

LANGUAGE: python
CODE:
```
# Permissions value that can Send Messages (0x800) and Add Reactions (0x40):
permissions = 0x40 | 0x800 # 2112

# Checking for flags that are set:
(permissions & 0x40) == 0x40   # True
(permissions & 0x800) == 0x800 # True

# Kick Members (0x2) was not set:
(permissions & 0x2) == 0x2 # False
```

----------------------------------------

TITLE: Example Identify Payload JSON
DESCRIPTION: Illustrates a minimal JSON payload sent to the Discord Gateway (opcode 2) to identify the client and establish a session after receiving the Hello event and starting heartbeats. It requires the bot `token`, desired `intents`, and client `properties` like OS and browser/library.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/events/gateway.mdx#_snippet_3

LANGUAGE: json
CODE:
```
{
  "op": 2,
  "d": {
    "token": "my_token",
    "intents": 513,
    "properties": {
      "os": "linux",
      "browser": "my_library",
      "device": "my_library"
    }
  }
}
```

----------------------------------------

TITLE: Implementing OAuth2 Token Exchange Endpoint - Express.js
DESCRIPTION: Sets up an Express server with a POST route `/api/token`. This route receives a Discord authorization code from the client, securely exchanges it for an access token using the Discord API, and returns the access token to the client. Requires `express`, `dotenv`, `node-fetch`, and Discord API credentials as environment variables.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/activities/building-an-activity.mdx#_snippet_11

LANGUAGE: JavaScript
CODE:
```
import express from "express";
import dotenv from "dotenv";
import fetch from "node-fetch";
dotenv.config({ path: "../.env" });

const app = express();
const port = 3001;

// Allow express to parse JSON bodies
app.use(express.json());

app.post("/api/token", async (req, res) => {

  // Exchange the code for an access_token
  const response = await fetch(`https://discord.com/api/oauth2/token`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      client_id: process.env.VITE_DISCORD_CLIENT_ID,
      client_secret: process.env.DISCORD_CLIENT_SECRET,
      grant_type: "authorization_code",
      code: req.body.code,
    }),
  });

  // Retrieve the access_token from the response
  const { access_token } = await response.json();

  // Return the access_token to our client as { access_token: "..."}
  res.send({access_token});
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
```

----------------------------------------

TITLE: Example Discord Command Interaction Payload (JSON)
DESCRIPTION: This JSON object represents the data structure received by a Discord bot's interaction endpoint when a user invokes a slash command (`type: 2`). It provides comprehensive details about the interaction, including the invoking user, guild and channel context, application ID, and specific command data such as the command name and any provided options.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/tutorials/upgrading-to-application-commands.md#_snippet_1

LANGUAGE: json
CODE:
```
{
    "type": 2,
    "token": "A_UNIQUE_TOKEN",
    "member": {
        "user": {
            "id": "A_USER_ID",
            "username": "A_USERNAME",
            "avatar": "GUILD_AVATAR_HASH",
            "discriminator": "1337",
            "public_flags": 131141
        },
        "roles": ["12345678"],
        "premium_since": null,
        "permissions": "2147483647",
        "pending": false,
        "nick": null,
        "mute": false,
        "joined_at": "2019-04-14T12:14:14.000000+00:00",
        "is_pending": false,
        "deaf": false
    },
    "id": "INTERACTION_ID",
    "application_id": "YOUR_APP_ID",
    "app_permissions": "442368",
    "guild_id": "A_GUILD_ID",
    "guild_locale": "en-US",
    "locale": "en-US",
    "data": {
        "options": [{
            "name": "Igneous",
            "value": "rock_igneous"
        }],
        "name": "rock",
        "id": "APPLICATION_COMMAND_ID"
    },
    "channel_id": "ASSOCIATED_CHANNEL_ID"
}
```

----------------------------------------

TITLE: Registering Global CHAT_INPUT Command (Python)
DESCRIPTION: This Python snippet demonstrates how to register a global CHAT_INPUT (slash) command with the Discord API using an HTTP POST request. It requires the `requests` library and shows how to structure the JSON payload for the command, including options and choices. Authorization can be done with a Bot token or a Client Credentials token.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/interactions/application-commands.mdx#_snippet_0

LANGUAGE: Python
CODE:
```
import requests


url = "https://discord.com/api/v10/applications/<my_application_id>/commands"

# This is an example CHAT_INPUT or Slash Command, with a type of 1
json = {
    "name": "blep",
    "type": 1,
    "description": "Send a random adorable animal photo",
    "options": [
        {
            "name": "animal",
            "description": "The type of animal",
            "type": 3,
            "required": True,
            "choices": [
                {
                    "name": "Dog",
                    "value": "animal_dog"
                },
                {
                    "name": "Cat",
                    "value": "animal_cat"
                },
                {
                    "name": "Penguin",
                    "value": "animal_penguin"
                }
            ]
        },
        {
            "name": "only_smol",
            "description": "Whether to show only baby animals",
            "type": 5,
            "required": False
        }
    ]
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot <my_bot_token>"
}

# or a client credentials token for your app with the applications.commands.update scope
headers = {
    "Authorization": "Bearer <my_credentials_token>"
}

r = requests.post(url, headers=headers, json=json)
```

----------------------------------------

TITLE: Example Application Command with Localization (JSON)
DESCRIPTION: This snippet shows the structure of a Discord application command object including `name_localizations` and `description_localizations` fields to provide multilingual names and descriptions for the command and its options. These fields are dictionaries mapping locale codes to localized strings.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/interactions/application-commands.mdx#_snippet_12

LANGUAGE: json
CODE:
```
{
  "name": "birthday",
  "type": 1,
  "description": "Wish a friend a happy birthday",
  "name_localizations": {
    "zh-CN": "生日",
    "el": "γενέθλια"
  },
  "description_localizations": {
    "zh-CN": "祝你朋友生日快乐"
  },
  "options": [
    {
      "name": "age",
      "type": 4,
      "description": "Your friend's age",
      "name_localizations": {
        "zh-CN": "岁数"
      },
      "description_localizations": {
        "zh-CN": "你朋友的岁数"
      }
    }
  ]
}
```

----------------------------------------

TITLE: Handling Select Menu and Button Interactions (JavaScript)
DESCRIPTION: Handles MESSAGE_COMPONENT interactions, specifically checking for custom IDs starting 'accept_button_' (button click) or 'select_choice_' (select menu selection). For select menu interactions, it retrieves the user's choice, calculates the game result using helper functions, removes the game state from memory, sends the result as a follow-up message, and updates/deletes the ephemeral select menu message.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/quick-start/getting-started.mdx#_snippet_9

LANGUAGE: javascript
CODE:
```
if (type === InteractionType.MESSAGE_COMPONENT) {
// custom_id set in payload when sending message component
const componentId = data.custom_id;

  if (componentId.startsWith('accept_button_')) {
    // get the associated game ID
    const gameId = componentId.replace('accept_button_', '');
    // Delete message with token in request body
    const endpoint = `webhooks/${process.env.APP_ID}/${req.body.token}/messages/${req.body.message.id}`;
    try {
      await res.send({
        type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        data: {
          content: 'What is your object of choice?',
          // Indicates it'll be an ephemeral message
          flags: InteractionResponseFlags.EPHEMERAL,
          components: [
            {
              type: MessageComponentTypes.ACTION_ROW,
              components: [
                {
                  type: MessageComponentTypes.STRING_SELECT,
                  // Append game ID
                  custom_id: `select_choice_${gameId}`,
                  options: getShuffledOptions(),
                },
              ],
            },
          ],
        },
      });
      // Delete previous message
      await DiscordRequest(endpoint, { method: 'DELETE' });
    } catch (err) {
      console.error('Error sending message:', err);
    }
  } else if (componentId.startsWith('select_choice_')) {
    // get the associated game ID
    const gameId = componentId.replace('select_choice_', '');

    if (activeGames[gameId]) {
      // Interaction context
      const context = req.body.context;
      // Get user ID and object choice for responding user
      // User ID is in user field for (G)DMs, and member for servers
      const userId = context === 0 ? req.body.member.user.id : req.body.user.id;

      // User's object choice
      const objectName = data.values[0];

      // Calculate result from helper function
      const resultStr = getResult(activeGames[gameId], {
        id: userId,
        objectName,
      });

      // Remove game from storage
      delete activeGames[gameId];
      // Update message with token in request body
      const endpoint = `webhooks/${process.env.APP_ID}/${req.body.token}/messages/${req.body.message.id}`;

      try {
        // Send results
        await res.send({
          type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
          data: { content: resultStr },
        });
        // Update ephemeral message
        await DiscordRequest(endpoint, {
          method: 'PATCH',
          body: {
            content: 'Nice choice ' + getRandomEmoji(),
            components: []
          }
        });
      } catch (err) {
        console.error('Error sending message:', err);
      }
    }
  }
  return;
}
```

----------------------------------------

TITLE: Cloning Discord Activity Sample Project - Shell
DESCRIPTION: Clones the `getting-started-activity` sample project repository from GitHub into the current directory. This repository contains the foundational code for building a Discord Activity, including both client and server components.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/activities/building-an-activity.mdx#_snippet_0

LANGUAGE: shell
CODE:
```
git clone git@github.com:discord/getting-started-activity.git
```

----------------------------------------

TITLE: Initializing Discord Embedded App SDK and Authenticating (JavaScript)
DESCRIPTION: This snippet demonstrates the initial setup and authentication flow for a Discord Activity using the Embedded App SDK. It initializes the SDK, waits for the 'READY' state, requests OAuth authorization from the user, fetches an access token from a backend server using the obtained code, and finally authenticates the SDK instance with the access token.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/activities/how-activities-work.md#_snippet_0

LANGUAGE: javascript
CODE:
```
import {DiscordSDK} from '@discord/embedded-app-sdk';
const discordSdk = new DiscordSDK(YOUR_OAUTH2_CLIENT_ID);

async function setup() {
  // Wait for READY payload from the discord client
  await discordSdk.ready();

  // Pop open the OAuth permission modal and request for access to scopes listed in scope array below
  const {code} = await discordSdk.commands.authorize({
    client_id: YOUR_OAUTH2_CLIENT_ID,
    response_type: 'code',
    state: '',
    prompt: 'none',
    scope: ['identify'],
  });

  // Retrieve an access_token from your application's server
  const response = await fetch('/.proxy/api/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      code,
    }),
  });
  const {access_token} = await response.json();

  // Authenticate with Discord client (using the access_token)
  auth = await discordSdk.commands.authenticate({
    access_token,
  });
}
```

----------------------------------------

TITLE: Example Message Create Dispatch Payload (JSON)
DESCRIPTION: Documents the structure of the JSON payload dispatched when a message is created. It includes the `channel_id` and the full `message` object within the data field, containing details like content, author, timestamp, etc. This event provides comprehensive information about a new message.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/topics/rpc.md#_snippet_40

LANGUAGE: json
CODE:
```
{
  "cmd": "DISPATCH",
  "data": {
    "channel_id": "199737254929760256",
    "message": {
      "id": "199743874640379904",
      "blocked": false,
      "content": "test",
      "content_parsed": [
        {
          "content": "test",
          "type": "text"
        }
      ],
      "author_color": "#ffffff",
      "edited_timestamp": null,
      "timestamp": "2016-07-05T04:30:50.776Z",
      "tts": false,
      "mentions": [],
      "mention_roles": [],
      "mention_everyone": false,
      "embeds": [],
      "attachments": [],
      "type": 0,
      "pinned": false,
      "author": {
        "id": "190320984123768832",
        "username": "test user 2",
        "discriminator": "7479",
        "avatar": "b004ec1740a63ca06ae2e14c5cee11f3",
        "bot": false
      }
    }
  },
  "evt": "MESSAGE_CREATE"
}
```

----------------------------------------

TITLE: Example JSON suppressing all mentions using parse empty array
DESCRIPTION: Shows how to suppress all potential mentions (`@everyone`, `@here`, users, roles) within a message by providing an empty array `[]` for the `allowed_mentions.parse` field. This overrides default parsing behavior.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/resources/message.mdx#_snippet_3

LANGUAGE: JSON
CODE:
```
{
  "content": "@everyone hi there, <@&123>",
  "allowed_mentions": {
    "parse": []
  }
}
```

----------------------------------------

TITLE: Full Discord SDK Integration Example (C++)
DESCRIPTION: A complete example demonstrating a basic Discord SDK integration in C++. It initializes the SDK, sets up logging and status callbacks, performs the OAuth2 authorization flow for account linking, and runs the SDK's event loop.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/discord-social-sdk/getting-started/using-c++.mdx#_snippet_7

LANGUAGE: cpp
CODE:
```
#define DISCORDPP_IMPLEMENTATION
#include "discordpp.h"
#include <iostream>
#include <thread>
#include <atomic>
#include <string>
#include <functional>
#include <csignal>

// Replace with your Discord Application ID
const uint64_t APPLICATION_ID = 123456789012345678;

// Create a flag to stop the application
std::atomic<bool> running = true;

// Signal handler to stop the application
void signalHandler(int signum) {
    running.store(false);
}

int main() {
    std::signal(SIGINT, signalHandler);
    std::cout << "🚀 Initializing Discord SDK!\n";

    // Create our Discord Client
    auto client = std::make_shared<discordpp::Client>();

    // Set up logging callback
    client->AddLogCallback([](auto message, auto severity) {
      std::cout << "[" << EnumToString(severity) << "] " << message << std::endl;
    }, discordpp::LoggingSeverity::Info);

    // Set up status callback to monitor client connection
    client->SetStatusChangedCallback([client](discordpp::Client::Status status, discordpp::Client::Error error, int32_t errorDetail) {
      std::cout << "🔄 Status changed: " << discordpp::Client::StatusToString(status) << std::endl;

      if (status == discordpp::Client::Status::Ready) {
        std::cout << "✅ Client is ready! You can now call SDK functions.\n";
      } else if (error != discordpp::Client::Error::None) {
        std::cerr << "❌ Connection Error: " << discordpp::Client::ErrorToString(error) << " - Details: " << errorDetail << std::endl;
      }
    });

    // Generate OAuth2 code verifier for authentication
    auto codeVerifier = client->CreateAuthorizationCodeVerifier();

    // Set up authentication arguments
discordpp::AuthorizationArgs args{};
args.SetClientId(APPLICATION_ID);
args.SetScopes(discordpp::Client::GetDefaultPresenceScopes());
args.SetCodeChallenge(codeVerifier.Challenge());

    // Begin authentication process
    client->Authorize(args, [client, codeVerifier](auto result, auto code, auto redirectUri) {
      if (!result.Successful()) {
        std::cerr << "❌ Authentication Error: " << result.Error() << std::endl;
        return;
      } else {
        std::cout << "✅ Authorization successful! Getting access token!\n";

        // Exchange auth code for access token
        client->GetToken(APPLICATION_ID, code, codeVerifier.Verifier(), redirectUri,
          [client](discordpp::ClientResult result,
          std::string accessToken,
          std::string refreshToken,
          discordpp::AuthorizationTokenType tokenType,
          int32_t expiresIn,
          std::string scope) {
            std::cout << "🔓 Access token received! Establishing connection!\n";
            // Next Step: Update the token and connect
        });
      }
    });

    // Keep application running to allow SDK to receive events and callbacks
    while (running) {
      discordpp::RunCallbacks();
      std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }

    return 0;
}
```

----------------------------------------

TITLE: Authorizing with Discord SDK (JavaScript)
DESCRIPTION: This snippet demonstrates how to initiate the OAuth2 authorization flow using the Discord Embedded App SDK. It requires specifying the client ID, response type, and desired scopes. The `identify` and `guilds` scopes are requested here.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/developer-tools/embedded-app-sdk.mdx#_snippet_7

LANGUAGE: javascript
CODE:
```
await discordSdk.commands.authorize({
  client_id: DISCORD_CLIENT_ID,
  response_type: "code",
  state: "",
  prompt: "none",
  scope: [
    // "applications.builds.upload",
    // "applications.builds.read",
    // "applications.store.update",
    // "applications.entitlements",
    // "bot",
    "identify",
    // "connections",
    // "email",
    // "gdm.join",
    "guilds",
    // "guilds.join",
    // "guilds.members.read",
    // "messages.read",
    // "relationships.read",
    // 'rpc.activities.write',
    // "rpc.notifications.read",
    // "rpc.voice.write",
    // "rpc.voice.read",
    // "webhook.incoming",
  ],
});
```

----------------------------------------

TITLE: Registering Slash Commands via Script (NPM/Shell)
DESCRIPTION: This command executes a script (`register`) defined in the project's `package.json` to install global slash commands. It typically uses a tool like `node-fetch` to make a PUT request to the Discord API's `/applications/<APP_ID>/commands` endpoint, registering the commands listed in the `ALL_COMMANDS` constant. Requires the project to be set up with defined commands and API credentials.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/quick-start/getting-started.mdx#_snippet_3

LANGUAGE: Shell
CODE:
```
npm run register
```

----------------------------------------

TITLE: Access Token Exchange Response Example (JSON)
DESCRIPTION: Shows the structure and content of the JSON response received from the Discord token endpoint after successfully exchanging an authorization code. It includes the `access_token`, its type (`Bearer`), expiration time (`expires_in`), a `refresh_token`, and the authorized `scope`.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/topics/oauth2.mdx#_snippet_3

LANGUAGE: JSON
CODE:
```
{
  "access_token": "6qrZcUqja7812RVdnEKjpzOL4CvHBFG",
  "token_type": "Bearer",
  "expires_in": 604800,
  "refresh_token": "D43f5y0ahjqew82jZ4NViEr2YafMKhue",
  "scope": "identify"
}
```

----------------------------------------

TITLE: Example Get Guild Response JSON
DESCRIPTION: Provides a complete example of the JSON object returned by the GET `/guilds/{guild.id}` API endpoint. It details the structure and potential values for various guild properties, including id, name, icon, features, emojis, roles, and configuration settings.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/resources/guild.mdx#_snippet_12

LANGUAGE: json
CODE:
```
{
  "id": "2909267986263572999",
  "name": "Mason's Test Server",
  "icon": "389030ec9db118cb5b85a732333b7c98",
  "description": null,
  "splash": "75610b05a0dd09ec2c3c7df9f6975ea0",
  "discovery_splash": null,
  "approximate_member_count": 2,
  "approximate_presence_count": 2,
  "features": [
    "INVITE_SPLASH",
    "VANITY_URL",
    "COMMERCE",
    "BANNER",
    "NEWS",
    "VERIFIED",
    "VIP_REGIONS"
  ],
  "emojis": [
    {
      "name": "ultrafastparrot",
      "roles": [],
      "id": "393564762228785161",
      "require_colons": true,
      "managed": false,
      "animated": true,
      "available": true
    }
  ],
  "banner": "5c3cb8d1bc159937fffe7e641ec96ca7",
  "owner_id": "53908232506183680",
  "application_id": null,
  "region": null,
  "afk_channel_id": null,
  "afk_timeout": 300,
  "system_channel_id": null,
  "widget_enabled": true,
  "widget_channel_id": "639513352485470208",
  "verification_level": 0,
  "roles": [
    {
      "id": "2909267986263572999",
      "name": "@everyone",
      "permissions": "49794752",
      "position": 0,
      "color": 0,
      "hoist": false,
      "managed": false,
      "mentionable": false
    }
  ],
  "default_message_notifications": 1,
  "mfa_level": 0,
  "explicit_content_filter": 0,
  "max_presences": null,
  "max_members": 250000,
  "max_video_channel_users": 25,
  "vanity_url_code": "no",
  "premium_tier": 0,
  "premium_subscription_count": 0,
  "system_channel_flags": 0,
  "preferred_locale": "en-US",
  "rules_channel_id": null,
  "public_updates_channel_id": null,
  "safety_alerts_channel_id": null
}
```

----------------------------------------

TITLE: Authorization Code Grant Redirect URL Example
DESCRIPTION: Shows the URL the user is redirected to after successfully authorizing the application using the Authorization Code grant. It demonstrates how the authorization `code` and the original `state` parameter are returned as query parameters.
SOURCE: https://github.com/discord/discord-api-docs/blob/main/docs/topics/oauth2.mdx#_snippet_1

LANGUAGE: URL
CODE:
```
https://nicememe.website/?code=NhhvTDYsFcdgNLnnLijcl7Ku7bEEeee&state=15773059ghq9183habn
```