# Python-Exercise-1

## Introduction

This exercise is designed to help you practice your Python programming skills by creating a simple application. You will implement a program that reads a text file, counts the frequency of each word, and displays the top 10 most frequent words along with their counts. This exercise will help you practice file handling, string manipulation, and data structures in Python.

## Requirements

1. Input:
  - A text file (you can use any sample text file or create one).
2. Output:
  - A list of the top 10 most frequent words in the file, along with their frequency counts.
3. Functionality:
  - Read the content of the text file.
  - Normalize the text by converting it to lowercase and removing punctuation.
  - Count the frequency of each word.
  - Identify and display the top 10 most frequent words.
4. Implementation Details:
  - Use a dictionary to store the word counts.
  - Use string methods to normalize and clean the text.
  - Use sorting or a priority queue to determine the top 10 most frequent words.
  - Handle any potential errors gracefully, such as file not found.

## Scope

1. Environment:
- This exercise should be completed in a Python environment. Standard libraries such as os, string, and collections can be used.

2. Steps:
  - Define a function to read and clean the text file.
  - Define a function to count word frequencies.
  - Define a function to find and display the top 10 most frequent words.

## Sample Solution Architecture

```
 +-------------------+
 |     Read File     |
 +---------+---------+
           |
           v
 +---------+---------+
 |   Clean Text      |
 +---------+---------+
           |
           v
 +---------+---------+
 | Count Word Frequency|
 +---------+---------+
           |
           v
 +---------+---------+
 | Find Top 10 Words  |
 +---------+---------+
           |
           v
 +---------+---------+
 | Display Results    |
 +-------------------+
```

## Exercise Question

1. Introduction

You are tasked with creating a Python program that reads a text file, counts the frequency of each word, and displays the top 10 most frequent words. This will help you practice file handling, string manipulation, and the use of data structures in Python.

2. Requirements

  - Write a Python program that:
    - Reads a text file provided by the user.
    - Normalizes the text by converting it to lowercase and removing punctuation.
    - Counts the frequency of each word in the text.
    - Displays the top 10 most frequent words along with their counts.
   
3. Scope

  - Implement the solution in Python using standard libraries.
  - Ensure the program is well-documented and includes error handling for potential issues such as file not found.
