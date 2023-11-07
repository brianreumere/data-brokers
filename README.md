# Data Brokers

A repo of data brokers to help with opt outs. Each data broker has a YAML file in the `data/` directory.

## Schema

A full schema for the YAML files is below. All fields other than the top-level key, `names`, and `url` are optional and should be treated as unknown if they are absent. See [Opt-out process types](#opt-out-process-types) for valid values for the `process` field.

```yaml
some-site:
  names:
    - Some Site
    - SomeSite.com
  url: https://example.com
  removal-url: https://example.com/remove-me
  process: search-for-removal
  required-verification:
    - email
    - sms
    - phone
  help: |
    These are some helpful notes about how to opt out of this site.
    1. First do this.
    2. Then do this.
    3. Now you're done!
  help-links:
    - https://example.net/help-for-opting-out-of-some-site
  status:
    working: yes
    as-of: 2023-10-01
  notes:
    2023-10-01: These are some notes about this opt out experience.
```

The special `joins.yml` file in the data directory keeps track of relationships between data brokers. The lists of `similar` brokers are distinct sites with their own opt out processes, but there may be some underlying relationship between them (for example, their sites function almost identically, just with different styling).

## Fronts vs. 

## Services

[DeleteMe](https://joindeleteme.com/) and [Optery](https://www.optery.com/) seem to be solid and trustworthy options (Optery seems to cover more but I don't have any personal experience with it). Optery provides a decent free offering that will at least link you to various data brokers' search results for your name.

OneRep seems sketchy for various reasons; see an old [PrivacyDuck review of OneRep](https://web.archive.org/web/20210727095131/https://www.privacyduck.com/comparisons/privacyduck-vs-onerep-com-the-eastern-european-privacy-company/) and a more current [review of OneRep (plus a few other services) from Optery](https://www.optery.com/can-we-trust-onerep-helloprivacy-dataseal-and-brandyourself/), both of which raise valid concerns. If no other help links for opting out of a site are available, links to OneRep's site may be included.

## Other lists

These are some other lists of data brokers that might be useful to source from.

* [https://joindeleteme.com/sites-we-remove-from/](https://joindeleteme.com/sites-we-remove-from/) (Note that most sites on this list are only covered by custom requests or other premium plans. Check the legend at the bottom of the page.)
* [https://www.optery.com/pricing#data-brokers-we-cover](https://www.optery.com/pricing#data-brokers-we-cover)
* [https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List](https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List)

## Other guides

Links to guides from these sites may be included in the YAML data for each data broker.

* [https://joindeleteme.com/blog/opt-out-guides/](https://joindeleteme.com/blog/opt-out-guides/)
* [https://www.optery.com/opt-out-guides/](https://www.optery.com/opt-out-guides/)
* [https://wiki.onerep.com/](https://wiki.onerep.com/)

## Opt-out process types

There are various processes that data brokers use to allow you to opt out. For exmample, some require you to submit a "profile URL" or the URL of the search result you want to remove, and some have a special search process that reveals a "remove" option on the search results. This table documents the different types of processes (indicated by the `process` field in a data broker's YAML file) and what they entail.

| Process | Description |
| ------- | ----------- |
| `search-for-removal` | Use the removal search directly to see if there are results to remove. |
| `search-then-opt-out` | Search to see if data is available first and then use the opt out URL for removal. |
| `control` | Search for a profile that matches your data and then request to "control" it. |
