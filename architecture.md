## Pub quiz

## Objective

To be able to generate a dynamic multi-category quiz with questions and answers with the help of an LLM. This way we can play the game near infinite times without getting board with the same questions


## Basic approach

1) Generate questions and answers in a repeatable format
   which can be stored and used by the game logic module. This generation can be done via the LLM-backend module.

   a) This module should be highly configurable:
      - categories
      - num of questions per category
      - difficulty

   b) Storing questions and answers in appropriate format
      for game logic module to handle

2) The questions and answers should be handled by the game
   logic module which uses the questions and answers to build the game structure that can then be used by the front end.

   a) Should take the questions-answers and create the
      game structure, take care of the game state:
      - teams name and score
      - user answers validation (strict or fuzzy)

3) The user-experience module should present the questions
   to the user so they they can answer them.

    a) Should provide the user to configure the game
    b) Provide interface for team creation
    c) Update the interface based on the games state
