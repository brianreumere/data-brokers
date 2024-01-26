# Data brokers

A repo of data brokers to help with opt outs. Each data broker has a YAML file in the `data` directory.

## Schema

A full schema for the YAML files is below. The top-level key, `names`, and `url` are required. All other keys are optional and should be treated as unknown if they are absent. Generally if keys are included they should also have **all** of their subkeys. See [Opt-out process types](#opt-out-process-types) for valid values for the `process` field.

```yaml
someSite:
  names:
    - Some Site
    - SomeSite.com
  url: https://example.com
  removalUrl: https://example.com/remove-me
  process: search-for-removal
  helpLinks:
    - site: Example
      url: https://example.net/help-for-opting-out-of-some-site
  status:
    working: false
    asOf: 2023-10-01
    workaround: |
      Email `someone@example.com` indicating that the opt out is broken. Include the profile URL in the email.
  notes:
    - note: These are some notes about the opt out experience. You can use **Markdown**.
      date: 2023-10-01
```

## Fronts and similar sites

"Fronts" are sites that use other data brokers' data or APIs on their backend, and do not have their own opt out process. These are included in the `joins/fronts.yml` file. Top-level keys are the backend sites that actually host the data and opt out processes. The lists of sites under the top-level keys are the fronts.

Similar sites are data brokers that look and function in suspiciously similiar ways. The styling of their sites may be slightly different but otherwise have identical or very similar functionality. For example, [Optery says Councilon "falls under the umbrella of Radaris"](https://www.optery.com/councilon-how-to-remove-councilon-step-by-step-instructions/) (I haven't been able to confirm how). They maintain separate opt out processes, but their sites function nearly identically.

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
| `opt-out-search` | Use the special removal/opt-out search directly to see if there are results to remove. |
| `search-first` | Search to see if data is available first and then use the opt out URL for removal. |
| `control` | Search for a profile that matches your data and then request to "control" it. |
