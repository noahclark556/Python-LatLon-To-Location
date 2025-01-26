# Python Lat/Lon to City, County and State

**Written by**: Noah Clark 

**Date Created**: ~2022-02-02

**Language**: Python

**Target Platform**: Local Machine

**Development Environment**: macOS Sequoia 15.2, MacBook M2 Pro 2023 14-inch

## Description
This repository is a GeoCoding script that takes Lat/Lon points as input and will output the City, County and State.
All of this is something can be easily accomplished using Google, but I wrote this a few years ago for a project and never created a repo.
This script can be hosted on a Docker container and adjusted to create a simple and free GeoCoding API, this was the original functionality.

## Getting Started

### Prerequisites

- Python 3
- GeoPy python library
- OpenCage API Key (https://opencagedata.com/)

### Installation

1. Install the above pre-requisites

### Usage

1. Fill the GeoPoints list in main.py with Lat/Lon pairs
2. Run the following:
    ```bash
    python3 main.py
    ```
3. Check the console output