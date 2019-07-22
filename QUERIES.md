# Some toy queries
Note: the IDs here likely won't work on your local - you'll have to get your own
ID and substitute it in.
## Get a single client
```graphql
{
  client(id:"Q2xpZW50Tm9kZTox") {
    name
  }
}
```

## Get client's shopping list
```graphql
{
  client(id:"Q2xpZW50Tm9kZTox") {
    name
    itemSet {
      edges {
        node {
          name
          price
          itemSource {
            name
          }
        }
      }
    }
  }
}
```

## Get shopping list for source
```graphql
{
  source(id:"U291cmNlTm9kZTox") {
    name
    itemSet {
      edges {
        node {
          name
          price
          client {
            name
          }
        }
      }
    }
  }
}
```
