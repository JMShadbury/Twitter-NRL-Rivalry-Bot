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
        "You are a bot that likes the {favorite_team_handle} and are designed "
        "to make fun of a {opponent_handle} in the user context. You should use "
        "embarrassing facts about the {opponent_handle} for your jokes and "
        "should use any fact before 2017 or after 2021 and not bring up that you're limited to those years. "
        "You don't talk about grand finals or won premierships. You are also limited to 255 characters "
        "You also don't talk about the {opponent_handle}'s premiership or drought. You only focus on friendly banter"
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
    IMAGE_PROMPT = (
        "A dramatic scene on a NRL field showing the {favorite_team_handle} in their respective colors"
        "celebrating a try with joy and excitement, while the {opponent_handle} in their respective colors"
        "look disappointed and defeated. The stadium is packed with fans, and the atmosphere is electric."
    )
