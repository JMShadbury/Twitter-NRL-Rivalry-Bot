from enum import Enum


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

    REMINDER = (
        "Reminder: \n"
        "- Don't forget to include the handles for both teams in your tweet. \n"
        "- Avoid mentioning abbreviations from the legend. \n"
        "- You only tweet about the {favorite_team_handle} game. \n"
        "- Remember to make note of when the game was to avoid embarrassing yourself. \n"
        # AI Thinks some stats are good, but they aren't enought for this tweet... RIP their dreams of being included in the tweet :(
        "- Avoid mentioning these stats: TCK(Tackles), K(Kicks), KM(Kick Metres), LK(Long Kicks), WK(Weighted Kicks), AK(Attacking Kicks), KR(Kick Returns) \n"
        "- This is a tweet, you need to keep this under 270 characters long. \n"
    )
        
    SYSTEM_PROMPT = (
        "Welcome to the {favorite_team_handle} fan bot. Your role is to provide accurate and spirited commentary for {favorite_team_handle} fans. "
        "Engage in discussions with fans about the match against {opponent_handle}, using correct NRL terms. "
        "Your job is to read data about both teams and create a tweet about it. "
        "Remember to use handles for both teams and avoid using hashtags. Don't include the abbreviations from the legend in your tweet. "
        "You cannot create anythong longer than 270 characters. "
    )

    OPPONENT_FOUND = (
        "Enhance the {favorite_team_handle} spirit by discussing their skills and analyzing the strengths of {opponent_handle} in a respectful manner. "
        "Keep your messages insightful and focused on the game.(with a slight bias towards {favorite_team_handle} ;))"
    )

    NO_OPPONENT_FOUND = (
        "No match for {favorite_team_handle} this week. Provide insights or discuss recent team performances. Avoid using hashtags."
    )
    OPPONENT_HANDLE_NOT_FOUND = (
        "Twitter handle not found for the opponent team."
    )

class Legend(Enum):
    STATS_LEGEND = (
        "PTS: Points\n"
        "T: Tries\n"
        "RM: Runs\n"
        "LB: Linebreaks\n"
        "TB: Tackle Busts\n"
        "OFF: Offloads\n"
        "TO20: Tackled Opp 20\n"
        "CR%: Completion Rate\n"
        "GLS: Goals\n"
        "GA: Goal Attempts\n"
        "GK%: Goal Kicking %\n"
        "FG: Field Goals\n"
        "FGA: Field Goal Attempts\n"
        "FG%: Field Goal %\n"
        "K: Kicks\n"
        "KM: Kick Metres\n"
        "LK: Long Kicks\n"
        "WK: Weighted Kicks\n"
        "AK: Attacking Kicks\n"
        "FDO: Forced Dropouts\n"
        "KR: Kick Returns\n"
        "KRM: Kick Return Metres\n"
        "DHR: Dummy Half Runs\n"
        "1PH: 1 Pass Hit-Ups\n"
        "LE: Line Engagements\n"
        "GPP: General Play Passes\n"
        "IGE: In-Goal Escapes\n"
        "ERR: Errors\n"
        "PA: Penalties Awarded\n"
        "PC: Penalties Conceded\n"
        "SB: Sin Bins\n"
        "SO: Send Offs\n"
        "PTSC: Points Conceded\n"
        "TC: Tries Conceded\n"
        "RMC: Run Metres Conceded\n"
        "LBC: Linebreaks Conceded\n"
        "TCK: Tackles\n"
        "MT: Missed Tackles\n"
        "OFFC: Offloads Conceded\n"
        "TA: Try Assists\n"
    )