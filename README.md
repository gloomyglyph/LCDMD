# Python Implementation of LCDMD

## This project implements the concepts and algorithms described in the article “Local community detection algorithm based on local modularity density
” (Local community detection algorithm based on local modularity density - Scientific Figure on ResearchGate. Available from: https://www.researchgate.net/figure/Illustration-of-the-two-stage-community-detection-process-of-LCDMD_fig3_351662412 [accessed 11 Feb, 2024]) using Python.

## Features
    1. Implements core algorithms from the article.
    2. Provides clear and concise code with comments.
    3. Includes strike graph example demonstrating usage.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/gloomyglyph/LCDMD.git
   ```

## Usage
### Do the things below just like the strike_etst.py file which includes a complete step by step usage of this project
1. Make a list implementation of your graph.
2. Make an LCDMD instance for executing the article's algorithms.
3. Given a node, find the core area and its extended community using the LCDMD instance.
4. Make the true communities list for validation.
5. Use f1 score for measurement.
