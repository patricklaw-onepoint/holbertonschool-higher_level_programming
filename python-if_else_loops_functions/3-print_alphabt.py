#!/usr/bin/python3
print(
    "".join(
        [
            "{0}".format(chr(i))
            for i in range(97, 123)
            if "{0}".format(chr(i)) not in "eq"
        ]
    ),
    end="",
)
