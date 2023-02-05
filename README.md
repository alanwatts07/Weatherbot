This is a Ron Burgundy Weather bot I am testing out using open ai and the NWS.
Requires almost nothing to run this.

This will basically use the link inside (which can be updated) and bs4 to locate it based on being "div" with attr "xxxx" (which you can change). This will run through openai and make a summary with the voice of ron burgundy from davinci-003. It then uses google text to speech to make an mp3 file called weather.mp3 and plays it with mpg321 on linux machines.