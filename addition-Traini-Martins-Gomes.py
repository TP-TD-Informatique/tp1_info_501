#!/usr/bin/env python3


def xor3(r, x, y, z):
    # TODO
    ...


def carry3(r, x, y, z):
    print(f"{x} {y} {z} ~{r}")
    print(f"{x} {y} ~{z} ~{r}")
    print(f"{x} ~{y} {z} ~{r}")
    print(f"~{x} {y} {z} ~{r}")
    print(f"~{x} ~{y} {z} {r}")
    print(f"~{x} {y} ~{z} {r}")
    print(f"{x} ~{y} ~{z} {r}")
    print(f"~{x} ~{y} ~{z} {r}")


if __name__ == "__main__":
    from sys import argv, exit, stderr

    try:
        n = int(argv[1])
    except (ValueError, IndexError):
        print("expect one (or two) number(s) as argument", file=stderr)
        exit(1)

    try:
        s = int(argv[2])
    except IndexError:
        from random import randrange
        s = randrange(0, randrange(0, 2**n))
        print(f"no 's' number given, using {s}", file=stderr)
    except ValueError:
        print(f"invalid 's' number: {s}", file=stderr)
        exit(1)

    # pas de retenue sur le premier bit
    print("~r1")

    # pas de depassement de capacité
    print(f"~r{n+1}")

    for i in range(1, n+1):
        if s % 2:
            print(f"s{i}")
        else:
            print(f"~s{i}")
        s = s//2

    for i in range(1, n+1):
        xor3(f"s{i}", f"a{i}", f"b{i}", f"r{i}")
        carry3(f"r{i+1}", f"a{i}", f"b{i}", f"r{i}")

