# Minesweeper
A Minesweeper Game using principles of Artificial Intelligence and propositional Logic.

## Introduction
Minesweeper is a puzzle game that consists of a grid of cells, where some of the cells contain hidden “mines.” Clicking on a cell that contains a mine detonates the mine, and causes the user to lose the game. Clicking on a “safe” cell (i.e., a cell that does not contain a mine) reveals a number that indicates how many neighboring cells – where a neighbor is a cell that is one square to the left, right, up, down, or diagonal from the given cell – contain a mine.
In this 3x3 Minesweeper game, for example, the three 1 values indicate that each of those cells has one neighboring cell that is a mine. The four 0 values indicate that each of those cells has no neighboring mine.

## Requirements

- **Python**
- **Pygame**


## Usage

```python
python runner.py
```
![image](https://user-images.githubusercontent.com/37051428/132864189-086e8508-e5a5-4dac-a91f-ce305d789826.png)

https://user-images.githubusercontent.com/37051428/132868214-017e02e3-d3f5-4a28-afae-8584770877f5.mp4



## Description
In this implementation the user can allow the AI agent to play minesweeper on its behalf.When you run your AI (as by clicking “AI Move”), note that it will not always win! There will be some cases where the AI must guess, because it lacks sufficient information to make a safe move. This is to be expected. runner.py will print whether the AI is making a move it believes to be safe or whether it is making a random move.
