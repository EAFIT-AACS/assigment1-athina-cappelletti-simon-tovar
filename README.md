Athina Cappelletti
Simón Tovar

Wednesday classes SI2002-2 (7309)

OS: Windows

Programming language: Python

Instructions for execution:

1) Open your code editor (preferably VSCode)
2) Go to the options to run Python file
3) The console will open, where you can see the required inputs.
The data to enter will be requested by the console.
The format of the transitions is as follows:

  state symbol1 destination1 symbol2 destination2
  
It will depend on whether the automaton is with two equivalent states,
with inaccessible states or more equivalent states.

    Example: Simple automaton with two equivalent states:
    
    State and its transitions: 0 0 1 1 2
    
    Example: Automaton with inaccessible states
    
    State and its transitions: 0 a 1 b 3
    
    Example: Automaton with more equivalent states
    
    State and its transitions: 0 0 1 1 2

Explanation of the algorithm:

This program reads and minimizes a deterministic finite automaton (DFA). First, it asks the user for the states, alphabet, transitions, and final states of the automaton. Then, it identifies which states are reachable from the initial state and applies the minimization algorithm to find equivalent states, i.e., those that can be combined without changing the behavior of the automaton. Finally, it returns the equivalent state pairs for each test case entered.

Bibliography:

https://es.stackoverflow.com/questions/76447/aut%C3%B3mata-finito-determinista-en-python

https://ellibrodepython.com/diccionarios-en-python

https://www.studocu.com/co/document/universidad-pedagogica-y-tecnologica-de-colombia/psicopedagogia/taller-diseno-af-python-java/31462029

https://pythondiario.com/2015/06/afd-en-python-automata-finito.html


[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/95BWY5mA)
