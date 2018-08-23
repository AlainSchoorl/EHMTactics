A scipt that tries out different tactical options in Eastside Hockey Manager, reads the results with pytesseract, and uses a genetic algorithm to improve itself.

Classes.py - Simple classes to define what an individual is and what a population is. Has code for mutation and breeding populations/individuals.
runtime.py - Sets the tactics, tells the game to run a month of simulations, reads the screen, and outputs data to csvs.

Classes2 and runtime2 are a new version of the script with adjustments to the method to return more interpretable data and to speed up the process.
Players are grouped instead of being modified individually, so with the reduction in moving parts as well as various adjustments to reduce randomness the hope is that data will be more reliable and the algorithm will find solutions faster.
AssistantEditor.py is a script that edits game data via a helper program. Used in the new version to try out different player types.
