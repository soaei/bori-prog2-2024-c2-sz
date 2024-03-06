import datetime as dt
import re
import time
from pathlib import Path

import pandas as pd

limit = 60 * 60 * 3

cols = [
    "solution",
    "input_size",
    "query_size",
    "setup_time",
    "preproc_time",
    "run_time",
]
types = [int, int, float, float, float]

if __name__ == "__main__":

    recs = []
    for f in Path("runs").iterdir():
        try:
            tss, sol = re.findall(r"([\d|\.]+)-(.*)", f.name)[0]
        except IndexError:
            continue
        if float(tss) > (time.time() - limit):
            recs.append([sol, *[t(v) for t, v in zip(types, f.read_text().split(","))]])

    lines = [f"# {dt.date.today().isoformat()}"]
    gcols = cols[1:3]
    for (ni, nq), gdf in pd.DataFrame(recs, columns=cols).groupby(gcols, sort=True):
        lines.append(f"## Inputs: {ni}, Queries {nq}")
        lines.append(
            gdf.drop(gcols, axis=1).sort_values("run_time").to_markdown(index=False)
        )

    Path("runs/README.md").write_text("\n\n".join(lines))
