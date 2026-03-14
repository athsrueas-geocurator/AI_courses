# Geo API Error Log

> ADD-ONLY LOG: never remove historical errors from this file. If an issue is resolved, keep the original entry and set `solved: true` with a resolution note.

## Error entries

### ERR-2026-03-13-001
- `solved`: false
- `surface`: `functions.geo-api` tool (`spaceInfo` helper)
- `context`: Attempted to pass `spaceId` for target space lookup.
- `request`:
  - `{"helper":"spaceInfo","endpoint":"https://testnet-api.geobrowser.io/graphql","spaceId":"3be38bb922bc80c6a6503fbbba28d2b0","raw":true}`
- `observed error`:
  - `Invalid input: expected string, received undefined`
  - error path: `spaceId`
- `impact`: The helper appears to ignore provided `spaceId`, so space detail lookup had to be done via direct GraphQL calls.
- `workaround`: Use direct GraphQL query in `bash`:
  - `query($id:UUID!){ space(id:$id){ ... } }`

### ERR-2026-03-13-002
- `solved`: false
- `surface`: `functions.geo-api` tool (`searchSpaces` helper)
- `context`: Attempted keyword search for candidate related spaces (term=`ai`).
- `request`:
  - `{"helper":"searchSpaces","endpoint":"https://testnet-api.geobrowser.io/graphql","term":"ai","raw":true}`
- `observed behavior`:
  - Response metadata showed `"term": null`.
  - Returned generic first-page results instead of term-filtered matches.
- `impact`: Keyword-driven filtering from the helper is not reliable in current state.
- `workaround`: Enumerate spaces through direct GraphQL pagination and filter in-client by `page.name`/`page.description`.

## Resolved entries

- None yet.

## Geo style guide source of truth

- Source of truth: https://www.geobrowser.io/space/3be38bb922bc80c6a6503fbbba28d2b0/dd5546417d00442fb353c7b10f8b7163
- Always check every URL before publishing; replace broken or outdated links with working canonical URLs.
