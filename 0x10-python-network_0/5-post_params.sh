#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -sd "email=test@gmailcom&subject=I will always be here for PLD" "$1"
