# bkffl_mock_draft
Command line mock draft tool for BKFFL fantasy football league.

## Usage
* Run the "mock_draft.py" python file with no arguments. Instructions are provided in the script.
* If you don't know how to run python code, now's a good time to learn.
* Only required external librarys are numpy, pandas and openpyxl.

## Description
* Loads current keepers, historical draft data, tendencies tuned to our league, etc.
* Provides default rankings (FantasyPros OP rankings).
* CPU drafts as opponents, with randomly perturbed rankings, in a way consistent with our league history - I'm still working on setting realistic CPUs so it sometimes still does some wonky stuff.
* Provides post-draft analysis (using FantasyPros projections).
* Supports draft pick trades.
* Input data for league history, rankings, and projections are in the 'input' folder. 
* To update for trades, you can make the trade following the software prompt (preferred) or you can change the 'BKFFL  Draft History.xlsx' file directly.
