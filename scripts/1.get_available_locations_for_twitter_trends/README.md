```bash
cat available_locations.json | jq 'map(. | select(.placeType.name=="Country"))' > available_locations_countries.json
```
