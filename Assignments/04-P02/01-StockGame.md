## Stock Simulation Game

**Implement a stock market simulation game** for several human players and several computer players.
You are to create a fast-paced on-line interactive game of stock market, which has many of the
characteristics of electronic commerce. The entities in the game are a bank, a stock exchange,
several companies and several players. The time between events has been significantly accelerated to
make the game more challenging and interesting.

**Bank** : The one bank holds the cash of any player.  
A player can request a new account, deposit and withdraw money from the account. The bank has a
maximum of 10 accounts. Once every minute during the game, all money in an account accumulates 1%
interest.

**Company** : A company has a name and issues stock. Once a minute, the company’s price of the stock
is adjusted based on a random process and the law of supply and demand. Initially each company has
1000 shares of stock, which starts at $30 a share. There are several companies for example three to
ten in the game. A company buys or sells shares to a player by accepting or rejecting the player’s
bid. The process of deciding to accept or reject may be random or based on sound business practices.

**Player** : There can be two types of players – human and computer. A player starts with $1000 and
buys and sells stock from companies or other players by trading through the stock exchange. The goal
of a player is to make money. A player buys or sells shares from another player or a company by
posting bids on the stock exchange. The company or the other player may accept or reject the
player’s bid. The process of deciding how the computer-based player accepts or rejects may be
random or based on sound business practices. There are two to ten players.

**Stock Exchange** : Players and companies must register with the stock exchange. All trading of
stocks must go through the centralized stock exchange. The stock exchange posts current bids and the
prices of recent transactions on each stock.

The winner is the player with the highest total value in cash and stock value after a certain period
of time. Of course, a player can not buy shares of stock that don’t exist and he or she must have
enough cash to purchase the desired shares. The bank, stock exchange, companies and computer players
are trusted entities, i.e., they don’t cheat.
