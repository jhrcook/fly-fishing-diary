#!/usr/bin/env python3

import argparse
from datetime import datetime
from pathlib import Path

TEMPLATE = """---
title: "Title"
date: {{DATE}}
description: ""
tags: []
draft: false

cover:
    image: "featured.jpeg" # image path/url
    alt: ""
    caption: ""
    relative: true
    hidden: false
---

...

---

{{< chat {{DATE}} >}}

"""


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="New post",
        description="Create a new blog post.",
    )
    parser.add_argument("-d", "--date", type=str, default=None)
    args = parser.parse_args()
    post_date: datetime
    if args.date is None:
        post_date = datetime.today()
    else:
        post_date = datetime.strptime(args.date, "%Y-%m-%d")
    date_str = post_date.strftime("%Y-%m-%d")
    posts_dir = Path("./content/posts/") / date_str
    if not posts_dir.exists():
        posts_dir.mkdir()

    index_file = posts_dir / "index.md"
    if index_file.exists():
        res = input(
            f"Index file {index_file} already exists - overwrite?\n[Anything for 'Yes', blank for 'No']:"
        ).strip()
        if not res:
            print("Exiting early.")
            return

    text = TEMPLATE.replace("{{DATE}}", date_str)
    with open(index_file, "w") as fh:
        fh.write(text)
    print(index_file)


if __name__ == "__main__":
    main()
