## Bugs

 * When puzzle changed, the cached scramble is still from the old puzzle
   * Maybe make a synchronous `fetchScramble` call, and then get two scrambles?
 * The scramble doesn't immediately change when the puzzle is changed
 * Inconsistent terminology of the datetime a solve was submitted. Should it be "date" or "time" ?
 * Add a data migration to automatically load the initial data
   * Also collapse previous migrations

## Other

 * Delete times
 * Get a better/{more compact} way to switch puzzles
 * Implement users (only use oauth?)
 * Statistics page ((Ao 5, 12), mean 100, past `n` days) (kind of done)
 * Random-state scrambles
 * Different formatting notations?
   * Could require sending the scramble as JSON and have the browser interpret it
 * Implement a proper pre-generation solution for scrambles (e.g. keep a set of at least 10 scrambles ready for each puzzle)
   * Maybe [Celery](http://celeryproject.org/) would work?
 * provide CSV exports of user data

## Far future

 * Mobile apps with syncronization with website
 * Social media something thing?
