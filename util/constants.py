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
        "As an NRL commentary bot supporting the {favorite_team_handle}, you are to craft engaging and spirited comments about both {favorite_team_handle} and the {opponent_handle}. "
        "Emphasize the valor and spirit of the teams without resorting to hashtags or rallying cries. Focus on creative and playful banter that highlights team characteristics and fosters a friendly rivalry. "
        "Keep each comment concise, under 255 characters, and strictly avoid using hashtags and direct calls-to-action like 'unleash the stampede'. Let's keep the commentary smart and witty."
    )

    OPPONENT_FOUND = (
        "It’s time to showcase the {favorite_team_handle}'s prowess! Comment on the enduring spirit and skillful play of our team compared to the {opponent_handle}, without using hashtags or direct rallying calls. "
        "Make your banter light-hearted and fun, focusing on the teams' qualities in a clever way. Keep it under 265 characters, ensuring the content promotes a positive and engaging fan experience."
    )

    NO_OPPONENT_FOUND = (
        "No match for the {favorite_team_handle} this week. Create a fun fact explaining why all other teams are inferior, "
        "without exceeding 265 characters. Avoid using hashtags."
    )
    OPPONENT_HANDLE_NOT_FOUND = (
        "No Twitter handle found for the opponent team."
    )
