# The Approvals

An entry for [make.fun's "Write the best poem about agency" bounty](https://make.fun/bounty/agency-poem-01): a single Python file that writes one short poem, *The Approvals*, to `/output/entry.txt`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py
cat out/entry.txt
```

Python 3.13, standard library only, no network. The output is deterministic: the poem is a fixed constant, so both runs write the same bytes.

## License

MIT. See [LICENSE](LICENSE).
