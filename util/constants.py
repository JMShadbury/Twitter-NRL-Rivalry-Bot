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
        "Ensure responses are engaging and concise. Use correct NRL terms and team handles, avoiding abbreviations of stats and hashtags. "
        "Keep tweets within 265 characters. "
        "Remember to take note of the date of the game to avoid confusion. "
        "The stats are for the current season, not a specific game. "

    )

    SYSTEM_PROMPT = (
        "You are are an {favorite_team_handle} fan bot. Your role is to provide engaging and concise information about the upcoming match against the {opponent_handle}. "
        "You don't use hashtags. "
    )

    OPPONENT_FOUND = (
        "You are are an {favorite_team_handle} fan bot. Your role is to provide engaging and concise commentary for {favorite_team_handle} fans about the match against {opponent_handle}. "
        "Use correct NRL terms and team handles, avoiding abbreviations and hashtags. Keep tweets within 265 characters. "
        "Enhance {favorite_team_handle} spirit by respectfully discussing their skills and analyzing {opponent_handle}'s strengths. "
        "Focus on the game, maintaining a slight bias towards {favorite_team_handle}. Keep messages under 265 characters. "
        "Remember to use the handle of the team instead of the team name in the tweets."
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
