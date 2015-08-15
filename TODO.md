## Bugs

 * When puzzle changed, the cached scramble is still from the old puzzle
   * Maybe make a synchronous `fetchScramble` call, and then get two scrambles?
 * The scramble doesn't immediately change when the puzzle is changed

## Other

 * Get a better/{more compact} way to switch puzzles
 * Implement users (only use oauth?)
 * Statistics page ((Ao 5, 12), mean 100, past `n` days)
 * Random-state scrambles
 * Different formatting notations?
   * Could require sending the scramble as JSON and have the browser interpret it

## Far future

 * Mobile apps with syncronization with website
 * Social media something thing?
