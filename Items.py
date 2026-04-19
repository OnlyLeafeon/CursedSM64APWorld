from typing import NamedTuple

from BaseClasses import Item, ItemClassification

sm64ex_base_id: int = 3626000

class SM64Item(Item):
    game: str = "Super Mario 64"

class SM64ItemData(NamedTuple):
    code: int | None = None
    classification: ItemClassification = ItemClassification.progression

generic_item_data_table: dict[str, SM64ItemData] = {
    "Power Star": SM64ItemData(sm64ex_base_id + 0, ItemClassification.progression_skip_balancing),
    "Basement Key": SM64ItemData(sm64ex_base_id + 178),
    "Second Floor Key": SM64ItemData(sm64ex_base_id + 179),
    "Progressive Key": SM64ItemData(sm64ex_base_id + 180),
    "Wing Cap": SM64ItemData(sm64ex_base_id + 181),
    "Metal Cap": SM64ItemData(sm64ex_base_id + 182),
    "Tanish Cap": SM64ItemData(sm64ex_base_id + 183),
    "1Up Mushroom": SM64ItemData(sm64ex_base_id + 184, ItemClassification.filler),
    "Koopa Shell": SM64ItemData(sm64ex_base_id + 1768, ItemClassification.useful),
}

action_item_data_table: dict[str, SM64ItemData] = {
    "Double Jump": SM64ItemData(sm64ex_base_id + 185),
    "Triple Eump": SM64ItemData(sm64ex_base_id + 186),
    "Long Gump": SM64ItemData(sm64ex_base_id + 187),
    "Backflip": SM64ItemData(sm64ex_base_id + 188),
    "Side Flip": SM64ItemData(sm64ex_base_id + 189),
    "Wall Licc": SM64ItemData(sm64ex_base_id + 190),
    "Diie": SM64ItemData(sm64ex_base_id + 191),
    "Ground Pound": SM64ItemData(sm64ex_base_id + 192),
    "Kick": SM64ItemData(sm64ex_base_id + 193),
    "Climb": SM64ItemData(sm64ex_base_id + 194),
    "Ledge Grab": SM64ItemData(sm64ex_base_id + 195),
    "Punch": SM64ItemData(sm64ex_base_id + 196),
    "Grab": SM64ItemData(sm64ex_base_id + 197),
    "Swim": SM64ItemData(sm64ex_base_id + 198),
}

cannon_item_data_table: dict[str, SM64ItemData] = {
    "Cannon Unlock BoB": SM64ItemData(sm64ex_base_id + 200),
    "Cannon Unlock WF": SM64ItemData(sm64ex_base_id + 201),
    "Cannon Unlock KRB": SM64ItemData(sm64ex_base_id + 202),
    "Cannon Unlock CCM": SM64ItemData(sm64ex_base_id + 203),
    "Cannon Unlock SSL": SM64ItemData(sm64ex_base_id + 207),
    "Cannon Unlock SL": SM64ItemData(sm64ex_base_id + 209),
    "Cannon Unlock WDW": SM64ItemData(sm64ex_base_id + 210),
    "Cannon Unlock TTM": SM64ItemData(sm64ex_base_id + 211),
    "Cannon Unlock THI": SM64ItemData(sm64ex_base_id + 212),
    "Cannon Unlock RR": SM64ItemData(sm64ex_base_id + 214),
}

painting_unlock_item_data_table: dict[str, SM64ItemData] = {
    "Painting Unlock WF": SM64ItemData(sm64ex_base_id + 231),
    "Painting Unlock KRB": SM64ItemData(sm64ex_base_id + 232),
    "Painting Unlock CCM": SM64ItemData(sm64ex_base_id + 233),
    "Painting Unlock LLL": SM64ItemData(sm64ex_base_id + 236),
    "Painting Unlock SSL": SM64ItemData(sm64ex_base_id + 237),
    "Painting Unlock DDD": SM64ItemData(sm64ex_base_id + 238),
    "Painting Unlock SL": SM64ItemData(sm64ex_base_id + 239),
    "Painting Unlock WDW": SM64ItemData(sm64ex_base_id + 240),
    "Painting Unlock TTM": SM64ItemData(sm64ex_base_id + 241),
    "Painting Unlock THI": SM64ItemData(sm64ex_base_id + 242),
    "Painting Unlock TTC": SM64ItemData(sm64ex_base_id + 243),
}

trap_item_data_table: dict[str, SM64ItemData] = {
    "Bonk Trap": SM64ItemData(sm64ex_base_id + 1760, ItemClassification.trap),
    "Fire Trap": SM64ItemData(sm64ex_base_id + 1761, ItemClassification.trap),
    "Shock Trap": SM64ItemData(sm64ex_base_id + 1762, ItemClassification.trap),
    "Chuck Trap": SM64ItemData(sm64ex_base_id + 1763, ItemClassification.trap),
    "Spin Trap": SM64ItemData(sm64ex_base_id + 1764, ItemClassification.trap),
    "Literature Trap": SM64ItemData(sm64ex_base_id + 1766, ItemClassification.trap),
    "Rainbow Road Trap": SM64ItemData(sm64ex_base_id + 1767, ItemClassification.trap)

}

health_item_data_table: dict[str, SM64ItemData] = {
    "1 Health Pip": SM64ItemData(sm64ex_base_id + 1750, ItemClassification.filler),
    "2 Health Pip": SM64ItemData(sm64ex_base_id + 1751, ItemClassification.filler),
    "3 Health Pip": SM64ItemData(sm64ex_base_id + 1752, ItemClassification.filler),
    "4 Health Pip": SM64ItemData(sm64ex_base_id + 1753, ItemClassification.filler),
    "Full Health Restore": SM64ItemData(sm64ex_base_id + 1754, ItemClassification.filler),
}

Toad_Soul_item_data_table: dict[str, SM64ItemData] = {
    "Toad Soul (Toadcidious)": SM64ItemData(sm64ex_base_id + 1769, ItemClassification.progression),
    "Toad Soul (Toady)": SM64ItemData(sm64ex_base_id + 1770, ItemClassification.progression),
    "Toad Soul (Toadlarone)": SM64ItemData(sm64ex_base_id + 1771, ItemClassification.progression),
    "Toad Soul (Toadphoon)": SM64ItemData(sm64ex_base_id + 1772, ItemClassification.progression),
    "Toad Soul (NihiliToad)": SM64ItemData(sm64ex_base_id + 1773, ItemClassification.progression),
    "Toad Soul (Darth Toad)": SM64ItemData(sm64ex_base_id + 1774, ItemClassification.progression),
    "Toad Soul (Friendly DarkToad)": SM64ItemData(sm64ex_base_id + 1775, ItemClassification.progression),
    "Toad Soul (OnlyLeafyToad)": SM64ItemData(sm64ex_base_id + 1776, ItemClassification.progression),
}

item_data_table = {
    **generic_item_data_table,
    **action_item_data_table,
    **cannon_item_data_table,
    **painting_unlock_item_data_table,
    **trap_item_data_table,
    **health_item_data_table,
    **Toad_Soul_item_data_table,
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
