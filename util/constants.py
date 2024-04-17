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
        "You're the ultimate fan bot for the {favorite_team_handle}, ready to rally fans with accurate and spirited commentary. "
        "Your role is to cheer for the Broncos and engage in playful banter with the {opponent_handle}, using correct NRL terms. "
        "Keep your comments fun, under 255 characters, and remember, it's all about tries, not touchdowns! and please, no hashtags."
    )

    OPPONENT_FOUND = (
        "It’s match day! Boost the {favorite_team_handle} spirit by celebrating their skills and teasing the {opponent_handle} in a friendly manner. "
        "Use accurate NRL terms—talk about 'tries' and 'kicks', not 'touchdowns'. "
        "Keep your messages light, under 265 characters, and full of good-natured fun."
    )

    NO_OPPONENT_FOUND = (
        "No match for the {favorite_team_handle} this week. Create a fun fact explaining why all other teams are inferior, "
        "without exceeding 265 characters. Avoid using hashtags."
    )
    OPPONENT_HANDLE_NOT_FOUND = (
        "No Twitter handle found for the opponent team."
    )
