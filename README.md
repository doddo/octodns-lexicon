[![PyPi](https://img.shields.io/pypi/v/octodns_lexicon.svg)](https://pypi.org/project/octodns-lexicon/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/octodns-lexicon)
[![Build Status](https://travis-ci.org/doddo/octodns-lexicon.svg?branch=master)](https://travis-ci.org/doddo/octodns-lexicon)

# octodns-lexicon
Use Lexicon providers in OctoDNS

## Introduction
octodns_lexicon is a provider for OctoDNS which by acting as a wrapper, it lets you to use [Lexion](https://github.com/AnalogJ/lexicon) providers in [OctoDNS](https://github.com/github/octodns) and thus you can manage your DNS records as code across even more providers.

## Getting started
### Installation

    pip install octodns-lexicon
    
### Extra dependencies

Some providers has extra dependencies. These are not installed by default.

See [here](https://github.com/AnalogJ/lexicon#setup) for instructions on how to install extra dependencies for such providers.


### Config
From OctoDNS, this provider can be [configured](https://github.com/github/octodns#config) pretty much like any other, 

* `class`: `octodns_lexicon.LexiconProvider`
* `raise_on_unknown`: if `True`, raise RuntimeError on unhandled record
                        types (default `False`)
* `lexicon_config`: lexicon config. This dictionary gets sent staight into the wrapped Lexicon provider as a [DictConfigSource](https://github.com/AnalogJ/lexicon/blob/master/lexicon/config.py#L269)

Furthermore: this provider also uses the Lexicon [EnvironmentConfigSource](https://github.com/AnalogJ/lexicon/blob/57a90f2c2992cb7c68371e05fb6d361c4b076374/lexicon/config.py#L217), so that you can put your lexicon dns providers settings into environment variables, just like in Lexicon.


#### Example Configuration
```yaml
providers:
  gandi:
    class: octodns_lexicon.LexiconProvider
    lexicon_config:
      provider_name: gandi
      domain: blodapels.in
      gandi:
        auth_token: "better kept in environment variable"
        api_protocol: rest

    namecheap:
      class: octodns_lexicon.LexiconProvider
      lexicon_config:
        provider_name: namecheap
        domain: example.com
        namecheap:
          auth_sandbox: True
          auth_username: foobar
          auth_client_ip: 127.0.0.1
          auth_token: "better kept in environment variable"
```

### Some words of caution.

### On Lexicon providers

Some Lexicon providers is not well suited for use in OctoDNS. For example, not all providers support updating TTL, some do not handle multi value records. Others yet might have other unknown shortcomings which makes them unsuitable.

Because of the sheer amount of providers available for Lexicon, it is very hard to test them all and therefore, some sandboxing is recommended before committing to using OctoDNS with a particular LexiconProvider.

A good test case can be creating a multi-value A record (or whichever, really), and then to applying it with OctoDNS multiple times. Only the first run should apply any changes.

Second step could be to change some of the values for that record, and maybe add one or two values, but keep some intact, and then change TTL and apply that a couple of times. Only the first run should apply any changes.

#### On SRV, MX and other record typpes with multi-value values

There are some inconsistencies in how lexicon providers handle these types of records. Some treats the additional value fields as extra options which they read from a Lexicon Config source while others handle them as single space separated value.

This provider uses the latter case, ie multi value values are treated as one joined with spaces, as this seems to be the most common case. 

#### On native OctoDNS providers

If there is a native OctoDNS provider available for a particular provider, then it is advisable to use that one and to not use the wrapped Lexicon equivalent, because some OctoDNS providers handle their DNS updates in atomic transactions, and others has geo DNS support. 
Also some providers handle updating a multi value record as a single operation whereas octodns_lexicon performs an update/create/create+delete per value.
