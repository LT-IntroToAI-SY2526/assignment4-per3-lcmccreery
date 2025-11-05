# Assignment 4 Rubric - Tic Tac Toe

**Total Points: 10**

---

## Grading Notes

You'll be graded on your TTTBoard class implementation, testing approach, and reflection on object-oriented programming. I'm looking for:

* Correct implementation of all required methods with proper OOP principles
* Working game logic that handles all win conditions and edge cases
* Thoughtful reflection on programming challenges and design decisions
* Evidence of testing beyond the provided asserts

Remember: This assignment introduces object-oriented programming concepts that we'll use throughout the rest of the course - focus on understanding how classes work and how to design good methods.

---

## Grading Table

| Criteria | Points Possible | Points Earned | Comments |
|----------|----------------|---------------|----------|
| **Programming Implementation** | | | |
| TTTBoard Class Methods | 4 |4 | |
| Test Cases Passing | 3 |3 | |
| **Reflection & Understanding** | | | |
| Programming Challenge Reflection | 1 |1 | |
| Design & Strategy Understanding | 2 |2 | |
| **TOTAL** | **10** |10 | Great work! |

---

## Programming Implementation (7 points)

### TTTBoard Class Methods (4 points)

* **4 points:** All six required methods (`__init__`, `__str__`, `make_move`, `has_won`, `game_over`, `clear`) correctly implemented with proper logic, handles all edge cases
* **3 points:** Most methods work correctly but 1-2 have minor issues or missing edge case handling
* **2 points:** Basic structure in place for all methods but significant logic errors in `has_won` or `make_move`
* **1 point:** Attempted implementation of class but major flaws in multiple methods
* **0 points:** Class not implemented or completely incorrect

### Test Cases Passing (3 points)

* **3 points:** All provided assert statements pass correctly
* **2 points:** 5-6 of the provided asserts pass
* **1 point:** 3-4 of the provided asserts pass
* **0 points:** Fewer than 3 assert statements pass

---

## Reflection & Understanding (3 points)

### Programming Challenge Reflection (1 point)
**Question:** "What was the most difficult part to tic-tac-toe?"

* **1 point:** Thoughtful reflection on specific challenges (e.g., checking win conditions, board indexing, method design) with evidence of learning
* **0.5 points:** General reflection acknowledging challenges but minimal specific detail
* **0 points:** No response or completely generic answer

### Design & Strategy Understanding (2 points)

**Question 2:** "Explain how you would add a computer player to the game." (1 point)
* **1 point:** Clear explanation with specific implementation ideas (e.g., random moves, calling make_move, handling turns)
* **0.5 points:** General explanation but lacking implementation details
* **0 points:** No response or shows fundamental misunderstanding

**Question 3:** "How you might get the computer player to play the best move every time." (1 point)
* **1 point:** Thoughtful explanation of strategy concepts (e.g., checking for wins/blocks, minimax idea, center/corner strategy)
* **0.5 points:** Basic understanding with vague strategy ideas
* **0 points:** No response or shows fundamental misunderstanding of game strategy