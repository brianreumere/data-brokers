import logging
import os
import yaml


# Set up logging
logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel("DEBUG")

# May move these to args later
data_broker_dir = "data"
out_file = "index.md"

data_brokers = {}
data_broker_files = os.scandir(data_broker_dir)
for data_broker_file in data_broker_files:
    if data_broker_file.is_file():
        logger.debug(f"Loading {data_broker_file.path}")
        with open(data_broker_file, "r") as f:
            data_broker = yaml.safe_load(f)
            data_broker_key = list(data_broker)[0]
            data_brokers[data_broker_key] = data_broker[data_broker_key]

data_brokers = dict(sorted(data_brokers.items()))

md_output = (
    "| Data broker | URL | Opt-out URL | Process | Help links | Status |\n"
    "| ----------- | --- | ----------- | ------- | ---------- | ------ |\n"
)
for key, data_broker in data_brokers.items():
    print(data_broker)
    name = data_broker["names"][0]
    url = data_broker["url"]
    opt_out_url = data_broker.get("removal-url", None)
    process = data_broker.get("process", None)
    help_links = "<br />".join(data_broker.get("help-links", []))
    if "status" in data_broker:
        status = data_broker["status"].get("working", None)
    else:
        status = None
    if status is not None:
        if status:
            status = "Working"
        else:
            status = "Not working"
    else:
        status = "Unknown"
    md_output += f"| {name} | {url} | {opt_out_url} | {process} | {help_links} | {status} |\n"

with open(out_file, "w") as f:
    f.write(md_output)
