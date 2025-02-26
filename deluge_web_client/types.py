from typing import TypedDict, Optional


class ParamArgs(TypedDict):
    """"""

    add_paused: bool
    seed_mode: bool
    auto_managed: bool
    download_location: Optional[str]
    move_completed: bool
    move_completed_path: optional[str]
