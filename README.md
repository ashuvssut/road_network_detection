# Road network detection [- 🔗 link ](https://twitter.com/ashuvssut/status/1625592282820014080)

The Road network detection algorithm needs "clean" Maps Screenshots without landmarks, buildings, any labels or markers. You can use screenshots of google map from https://mapstyle.withgoogle.com/ with the following settings:
![https://mapstyle.withgoogle.com/](./.readme-assets/mapswithgoogle.png)

See example output in `/z-output`.
## Usage
```python
$ python3 main.py <path-to-image>
# python3 main.py ./z-input/kirba.png       # for example
```

## Requirements
Used python v3.10.6
```
# requirements.txt

cv-algorithms==1.0.4
networkx==3.0
numpy==1.21.5
opencv-python==4.7.0.68
```

## Implementation
See https://docs.google.com/document/d/15D3AVszg0GRrYaToa6aiCSQ3aPUiu3zRsPIFWeYtZm0/edit#heading=h.oislpifv04z4
## References
See https://docs.google.com/document/d/15D3AVszg0GRrYaToa6aiCSQ3aPUiu3zRsPIFWeYtZm0/edit#heading=h.g74h65komzxz

## Future Work
See https://docs.google.com/document/d/15D3AVszg0GRrYaToa6aiCSQ3aPUiu3zRsPIFWeYtZm0/edit#heading=h.6z64lx9akiy5
