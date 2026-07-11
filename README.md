# Cortex

```bash
uv venv
source .venv/bin/activate

# this will take a second. also makes the project like 5 gigs right off the bat lmao
uv pip install -r requirements.txt
```

download MiniLM model:

DO THIS PEHLE SE. `test.py` runs in offline mode and will crash if you run it without running this first 
```
python cacheMiniLM.py
``` 
at `~/.cache/huggingface/hub/`

## current state

- `test.py` lets you keep typing queries in a while loop while returning results
- `config.toml`: add tracked paths here

when you MODIFY or CREATE a file it triggers the embedding. only use **markdown** (pls) for now

### to run:
start chroma server
```
chroma run --path ./chroma_db
```

start watchdog
```
python -m ingestion.watcher
```

finally
```
python test.py
```


###### ~~yeah you need three separate terminals just to get this working ill fix it later shut up~~