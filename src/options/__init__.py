import duckdb 
import logging as _log
import os
from pathlib import Path

def main():
    _log.basicConfig(level=_log.DEBUG)

    path_db = Path(os.environ["DUCKDB_PATH"])
    con = duckdb.connect(str(path_db))
    _log.info("Connected to database, getting setup")

    tick_df = con.sql("SELECT t.* FROM ticker t WHERE t.include_options_eod = true;").df()
    _log.debug(tick_df)

    for t in tick_df["symbol"]:
        _log.debug(f"Fetching options info for {t}")
        get_current_options_info(
            symbol=t
        )

def get_current_options_info(
        symbol: str
) -> None:
    pass

if(__name__=="__main__"):
    main()
