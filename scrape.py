from modules.scraper import EspnScraper
from modules.analyzer import Analyzer
from modules.thresholds import THRESHOLD_DEFINITIONS

TEST_LINK = "https://www.espn.com/nba/scoreboard/_/date/20200817"
if __name__ == "__main__":
    espn_scraper = EspnScraper()
    espn_scraper.populate_games(print_summary=False, include_completed=True)

    if not espn_scraper.games:
        print("No ongoing games.")
        exit(0)

    analyzer = Analyzer()
    for idx, wanted_game in enumerate(espn_scraper.games):
        print("\nAnalyzing game {}: {}".format(idx+1, wanted_game))
        for definition in THRESHOLD_DEFINITIONS:
            if analyzer.compare_stats(wanted_game, definition["comparisons"]):
                print(definition["description"], "\n")
