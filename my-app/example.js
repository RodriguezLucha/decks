// require { normalize, schema } from "normalizr";
const normalizr = require('normalizr')
const normalize = normalizr.normalize
const schema = normalizr.schema

let originalData = {
  data: [
    {
      id: 683,
      name: 'name'
    },
    {
      id: 684,
      name: 'name'
    }
  ]
}

const deck = new schema.Entity('deck')

const normalizedData = normalize(originalData, { decks: [deck] })
console.log(JSON.stringify(normalizedData, null, 2))
