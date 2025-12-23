# Higher Lower Game

This project is inspired by the classic Higher or Lower concept. The player is shown two different personalities along with short descriptions and must decide which one has a higher follower count. Each correct answer increases the score and continues the game with a new comparison.

**Technologies Used**

+ ```Python```
+ ```random``` module for number generation
+ Functions to separate game logic
+ data source (```game_data```)

**Features**

+ Randomized comparison between two entities
+ Ensures two different options are always compared
+ Score tracking for correct answers
+ Game ends when the player makes a wrong guess
+ Clear console output for comparisons and results

**What Users Can Do**

+ Compare two public figures based on follower count
+ Guess which option has more followers
+ Accumulate points for correct answers
+ Continue playing until an incorrect guess ends the game

**The Process / How It’s Built**

+ The game starts by randomly selecting two different options from the dataset.
+ Each round displays the two options with their names, descriptions, and countries.
+ The player inputs whether A or B has more followers.
+ The answer is checked using a helper function.
+ If correct, the score increases and a new comparison is generated.
+ If incorrect, the game ends and the final score is displayed.

