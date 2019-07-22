# graphql-exploration
A toy project to look at how graphql and REST concepts differ.

## Getting this running
`docker-compose up` should give you most of it.

You'll have to manually create a `personal_shopper` table in the postgres DB, though.

## Some notes on GraphQL

### Advantages
* Decoupling frontend from backend - you don't have to write endpoints for specific uses on the frontend
* Don't fetch more than you need to - if your REST API isn't tailored specifically to your frontend, there's probably data that you don't need
* Transformations at querytime: future/past example, aliasing, changing units
* Documentation of API comes built-in

### Disadvantages
* Complexity shifted to frontend
* Setup cost: new technologies to learn for both frontend and backend
* Losing some of the niceties of REST: verbs, URLs describe resources, etc
