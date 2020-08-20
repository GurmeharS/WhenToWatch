from modules.scraper import EspnScraper

if __name__ == "__main__":
    espn_scraper = EspnScraper()
    espn_scraper.populate_games()
