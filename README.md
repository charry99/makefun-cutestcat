# Cutest Cat — make.fun entry

One picture of a cat, judged by make.fun's house AI judge against
the other entries. The picture that wins is shown on make.fun's
site and in its posts as its cutest cat.

## The cat

A fluffy orange tabby kitten: big bright green eyes, head tilted,
white paws, curled tail, and a small red yarn ball on a plain warm
cream background. Two ears, two eyes, four paws, one tail, no text.

## How it works

`main.py` (Python 3, standard library only) copies the bundled
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. It draws nothing
and reaches for no network, so both harness runs write the same
bytes. It also checks the output is a whole PNG under the 1 MiB
limit and fails loudly if it is not.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

## License

MIT. See LICENSE.
