# CS361_Microservice

#########################################################
                    INSTRUCTIONS
#########################################################

########## HOW TO REQUEST DATA ##########

### Save ###

You can send a POST request with JSON data. The microservice will then respond to that POST being sent and create a folder and write the save file.

"POST /save"

Parameters: username, slot, game_data

Example (JavaScript*)
fetch("http://localhost:5000/save", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username: "Ralsei",
    slot: "slot1",
    game_data: {
      hp: 35,
      inventory: ["Fiber Scarf", "Bandage"],
      location: "Castle Town"
    }
  })
})
.then(response => response.json())
.then(data => console.log("Save response:", data))
.catch(error => console.error("Error saving game:", error));

### Load ###

This is a request to load game data.

"GET /load/:username/:slot"


########## HOW TO RECEIVE DATA ##########

These are responses to send back to the microservice.

### LOAD ###

"GET /load/<username>/<slot>"

Parameters: username (letters, numbers, hyphens, and underscores only) and slot (Save slot identifier (Ex. "slot1")

Example (JavaScript*)
fetch("http://localhost:5000/load/evan123/slot1")
  .then(response => response.json())
  .then(data => {
    console.log("Received game data:", data);
  })
  .catch(error => console.error("Error loading save:", error));

*Any language with HTTP clients work. Like Python, this is just another example.

### SAVE SUCCESSFULL ###

This is confirmation that data was successfully saved.

Example: 
{
  "message": "Game saved successfully.",
  "username": "evan123",
  "slot": "slot1"
}

#########################################################
                  UML SEQUENCE DIAGRAM
#########################################################

![UML Sequence Diagram](images/sequence_diagram.jpg)

#########################################################
                  COMMUNICATION CONTRACT
#########################################################

A. For which teammate did you implement “Microservice A”?

Evan Johnson.

B. What is the current status of the microservice? Hopefully, it’s done!

The microservice is complete and fully functional. 

C. If the microservice isn’t done, which parts aren’t done and when will they be done?

N/A

D. How is your teammate going to access your microservice?

-Clone the repository from Github (gh repo clone kyofyufufufufufufufu/CS361_Microservice)
-Run locally, install Flask, and execute file as usual
- Make HTTP requests to the microservice (examples shown above in Instructions)

E. If your teammate cannot access/call YOUR microservice, what should they do?

They should contact me directly ASAP. I'm available mostly through Teams. Times available are after 5PM on weekdays.

F. By when do they need to tell you if they can't access the microservice?

Tuesday, May 20th at 11:59 PM.

G. Is there anything else your teammate needs to know?

Nope.



The microservice sends back a JSON file when the request is successful. If the save doesn't exist or input is invalid, it throws an error.
