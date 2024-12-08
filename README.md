# neuron world! 
a game where you are a neuron in a developing brain 

# rules! 
## neuron
1. spawn randomly on screen (x,y) (range of 0 to 100 pixles)
2. connect randomly to other neuron (missing clock in here)
3. disconnect after a period of time (missing code in here**)
4. inner timer of 30 second counting down (missing count-down yet)
5. activation of neuron add 10 sec to the inner tiemer
6. inactivate after a period of time (missing code in here**)
   
## player
1. spawn in the middle of the screen (50,50)
2. action space (action is an integer):
      a. 0 = move right 1px
      b. 1 = move left 1px
      c. 2 = move up 1px
      d. 3 = move down 1px
      e. 4 = connect to closest neuron
3. have an inner activation if connected to other activated neurons
4. disconnect all neurons function (missing code in here **)
5. time_to_die (take the global timer of the game)

## world (game)
1. initate a number of spawn neuron (6 currently would be recommended to increase to 100 for intresting game)
2. initate player at 50,50
3. initate timer to 60 sec (dependce on the time nedded to reach neuron and connect to them this might changed for a playable game)
0. while is_game_over true
4. decrease timer in 10 sec each round - players choose action event (env.step(action)) (also might want to change the timing for playable game)
5. render a graph of current connection - player is in purple, neuron in grey, activated player of neuron in yellow, connection in white (using nx library and matplotlib)
6. reset function (if it was written in js it was a set interval but since i moved to python i need to determine somehow that interval)
7. is_game_over? if timer reaches 0 or under.


** reset function should do both 6 and 3 of neuron and 4 of player
