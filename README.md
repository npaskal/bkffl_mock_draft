# bkffl_mock_draft
Command line mock draft tool for BKFFL fantasy football league.

## Usage
* Run the "mock_draft.py" python file with no arguments. Instructions are provided in the script.
* Only required external librarys are numpy, pandas and openpyxl.
* If you don't know how to run python code and are on Windows, text me and I'll share an executable file. 

## Description
* Loads current keepers, historical draft data, tendencies tuned to our league, etc.
* Provides default rankings (FantasyPros OP rankings).
* CPU drafts as opponents, with randomly perturbed rankings. Realistic CPU behavior is a work in progress.
* Provides post-draft analysis (using FantasyPros projections).
* Supports draft pick trades.
* Input data for league history, rankings, and projections are in the 'input' folder. 
* In the future, I'll have it automatically pull from other rankings, ADP and projections, but FantasyPros was the easiest to get started with.
