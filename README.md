# chess-pgn-reader

## Purpose

Speech synthesis engine that reads aloud chess games supplied in pgn format. 

The engine is written in **Python3** and requires the library **pyttsx3**.


## Installation

Install the key dependency **pyttsx3** with:

```
pip install pyttsx3

```

## Usage

Run the <tt>main.py</tt> script within a proper environment

```
python main.py --pgn chessgame-example.pgn --step 5

```

The <tt>--steps</tt> argument indicates the number of moves the engine must read in a row before pausing; 
then press <tt>Enter</tt> to resume reading.

