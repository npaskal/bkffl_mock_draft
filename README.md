# bkffl_mock_draft
Command line mock draft tool for BKFFL fantasy football league.

## Usage
* If you can run python, just run "mock_draft.py" directly.
* Otherwise, if you're on Windows, run the much slow executable "mock_draft.exe" (it takes a few minutes to start-up).
* If you can't run python and are also on Mac, you're on your own.
* Instructions are provided in the prompt.

## Description
* Loads current keepers, historical draft data, tendencies tuned to our league, etc.
* Provides default rankings (FantasyPros OP rankings).
* CPU drafts as opponents, with randomly perturbed rankings, in a way consistent with our league history - I'm still working on setting realistic CPUs so it sometimes still does some wonky stuff.
* Provides post-draft analysis (using FantasyPros projections).
* Supports draft pick trades.
* Input data for league history, rankings, and projections are in the 'input' folder. 
* To update for trades, you can make the trade following the software prompt (preferred) or you can change the 'BKFFL  Draft History.xlsx' file directly.
