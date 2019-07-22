# Get a single client
```graphql
{
  client(id:"Q2xpZW50Tm9kZTox") {
    name
  }
}
```

# Get client's shopping list
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

# Get shopping list for source
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
