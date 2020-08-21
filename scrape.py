from modules.scraper import EspnScraper
import modules.thresholds as th

if __name__ == "__main__":
    espn_scraper = EspnScraper()
    espn_scraper.populate_games(print_summary=False, include_completed=True)
    wanted_game = espn_scraper.games[-1]
    for definition in th.THRESHOLD_DEFINITIONS:
        if th.compare_stats(wanted_game, definition["comparisons"]):
            print(definition["description"])
