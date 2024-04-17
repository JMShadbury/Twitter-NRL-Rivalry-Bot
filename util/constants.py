from enum import Enum, auto


class URL(Enum):
    NRL_DRAW = "https://www.nrl.com/draw/?competition=111&round=13&season=2024"


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
    TIGERS = "@WestsTigers"
    DRAGONS = "@NRL_Dragons"
    KNIGHTS = "@NRLKnights"
    BULLDOGS = "@NRL_Bulldogs"
    TITANS = "@GCTitans"
    RABBITOHS = "@SSFCRABBITOHS"


class Messages(Enum):
    SYSTEM_PROMPT = (
        "You are a bot that likes the {favorite_team_handle} and are designed "
        "to make fun of a {opponent_handle} in the user context. You should use "
        "embarrassing facts about the {opponent_handle} for your jokes and "
        "should use any fact before 2017 or after 2021 and not bring up that you're limited to those years. "
        "We don't talk about grand finals or won premierships."
    )
    OPPONENT_FOUND = (
        "Can you come up with a funny historical fact about the {favorite_team_handle} "
        "that supports them for a tweet? Let's make fun of an embarrassing fact about "
        "the {opponent_handle} as they play them this weekend, staying under 265 characters? "
        "We really don't want hashtags."
    )
    NO_OPPONENT_FOUND = (
        "No opponent found for the {favorite_team_handle} this week - make an interesting "
        "fact about why all other teams but {favorite_team_handle} suck, staying under 265 characters? "
        "We really don't want hashtags."
    )
    OPPONENT_HANDLE_NOT_FOUND = (
        "No Twitter handle found for the opponent team."
    )
