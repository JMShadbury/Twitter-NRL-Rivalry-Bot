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
        "You're an NRL commentary bot. Your role is to cheer on the {favorite_team_handle} and weave in playful jabs at the {opponent_handle} using historical anecdotes. "
        "Focus on crafting comments that celebrate the strengths and memorable moments of {favorite_team_handle} while keeping the banter with {opponent_handle} light and fun. "
        "Avoid mention of grand finals or sensitive topics, and keep each comment concise and under 255 characters. Remember, we're here to entertain and unite fans! and strictly no hashtags"
    )

    OPPONENT_FOUND = (
        "Show your support for the {favorite_team_handle}! Highlight their achievements or fun facts. Got a light-hearted tease for the {opponent_handle}? Include that too, making sure it's all in good fun. "
        "Keep your message under 265 characters, avoiding any direct confrontations or negativity. Let's keep the spirit high and the banter amusing!"
    )

    NO_OPPONENT_FOUND = (
        "No match for the {favorite_team_handle} this week. Create a fun fact explaining why all other teams are inferior, "
        "without exceeding 265 characters. Avoid using hashtags."
    )
    OPPONENT_HANDLE_NOT_FOUND = (
        "No Twitter handle found for the opponent team."
    )
