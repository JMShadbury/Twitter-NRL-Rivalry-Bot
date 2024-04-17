from enum import Enum, auto


class URL(Enum):
    NRL_DRAW = "https://www.nrl.com/draw"


class Team(Enum):
    FAVORITE_TEAM = "Broncos"


class AccountHandle(Enum):
    BRONCOS = "@brisbanebroncos"
    PANTHERS = "@PenrithPanthers"
    SHARKS = "@cronullasharks"
    STORM = "@storm"
    RAIDERS = "@RaidersCanberra"
    COWBOYS = "@nthqldcowboys"
    DOLPHINS = "@dolphinsnrl"
    WARRIORS = "@NZWarriors"
    SEA_EAGLES = "@SeaEagles"
    ROOSTERS = "@sydneyroosters"
    EELS = "@TheParraEels"
    WESTS_TIGERS = "@WestsTigers"
    DRAGONS = "@NRL_Dragons"
    KNIGHTS = "@NRLKnights"
    BULLDOGS = "@NRL_Bulldogs"
    TITANS = "@GCTitans"
    RABBITOHS = "@SSFCRABBITOHS"


class Messages(Enum):
    SYSTEM_PROMPT = (
    "You're an NRL reporter bot supporting the {favorite_team_handle}. Your task is to provide accurate and humorous commentary that mocks the {opponent_handle}. "
    "Refer to verifiable events before 2017 or after 2021 and avoid discussing grand finals or major trophies directly. "
    "Keep your messages under 255 characters. Focus on factual accuracy in your humor, and when discussing the upcoming game, simply mention 'this weekend'."
)

    OPPONENT_FOUND = (
    "Time to support the {favorite_team_handle}! Create a fact that celebrates them without diving into league standings or finals. "
    "Got something funny on the {opponent_handle} for their game this weekend? Share it, but keep it under 265 characters and hashtag-free. "
    "Remember, we're here to make smiles, not frowns, so keep it light and fun!"
)

    NO_OPPONENT_FOUND = (
        "No match for the {favorite_team_handle} this week. Create a fun fact explaining why all other teams are inferior, "
        "without exceeding 265 characters. Avoid using hashtags."
    )
    OPPONENT_HANDLE_NOT_FOUND = (
        "No Twitter handle found for the opponent team."
    )

