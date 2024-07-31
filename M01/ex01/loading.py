#!python3

from time import sleep, time
from decimal import Decimal


def ft_progress(lst):
    size = len(lst)
    start = time()
    now = start

    for i, e in enumerate(lst):
        step = i + 1
        perc = Decimal(step / size * 100)

        elapsed = Decimal(now - start).quantize(Decimal('0.00'))
        eta = (elapsed * (100 - perc) / perc).quantize(Decimal('0.00'))

        bar_size = int(perc / 10)
        bar = "".join(["[", "=" * bar_size, ">", " " * (10 - bar_size), "]"])

        end = "\n" if step == size else "\r"
        print(
            (
                f"ETA: {eta}s [ {int(round(perc, 0))}%]{bar} {step}/{size}"
                f" | elapsed time {elapsed}s"
            ),
            end=end
        )

        yield e
        now = time()

    print("...", end="")


if __name__ == "__main__":
    a_list = range(1000)
    ret = 0
    for elem in ft_progress(a_list):
        ret += (elem + 3) % 5
        sleep(0.001)
    print()
    print(ret)
