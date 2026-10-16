# bb Factory demo: tip calculator

A tiny project used to demonstrate the [Software Factory](https://github.com/lpbaril/bb-plugin-factory)
plugin for bb: a Lead agent plans the tasks, specialist agents build them, and
independent agents review every pull request.

```sh
python3 tip.py 100             # 15.00
python3 tip.py 80 20           # 16.00
python3 tip.py 100 --split 4   # 3.75 (tip per person)
python3 -m unittest -v         # run the tests
```
