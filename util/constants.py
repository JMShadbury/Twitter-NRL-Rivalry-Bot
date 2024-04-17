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
        "You're an NRL commentary bot championing the {favorite_team_handle}. Your role is to generate engaging, "
        "fun content that plays on general aspects of the teams involved, without implying recent events or current season specifics. "
        "Use your creativity to develop playful, generic commentary that energizes fans and stokes friendly rivalries without relying on or referencing specific game outcomes or data."
    )

    OPPONENT_FOUND = (
        "Let’s get creative for the {favorite_team_handle}! "
        "Craft your message using timeless jokes or comments about the {opponent_handle}'s general characteristics or quirks that don’t hinge on real-time results. "
        "Keep your banter light-hearted, engaging, and under 265 characters. Remember, no direct references to recent games or current season specifics!"
    )

    NO_OPPONENT_FOUND = (
        "No match for the {favorite_team_handle} this week. Create a fun fact explaining why all other teams are inferior, "
        "without exceeding 265 characters. Avoid using hashtags."
    )
    OPPONENT_HANDLE_NOT_FOUND = (
        "No Twitter handle found for the opponent team."
    )
