import {
  createSlice,
  createAsyncThunk,
  createEntityAdapter
} from '@reduxjs/toolkit'
import { normalize } from 'normalizr'
import { cardSchema } from '../../schema.js'

export const fetchCardsById = createAsyncThunk(
  'card/fetchCardsById',
  async (deck_id, thunkApi) => {
    const response = await fetch(`/decks/${deck_id}/cards/`)
    const data = await response.json()
    const normalized = normalize(data, { data: [cardSchema] })
    return { entities: normalized.entities }
  }
)

export const toggleCardById = createAsyncThunk(
  'card/toggleCardById',
  async (card, thunkApi) => {
    let deck_id = card.deck_id
    let card_id = card.id
    const response = await fetch(`/decks/${deck_id}/cards/${card_id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        hidden: !card.hidden
      })
    })
    const data = await response.json()
    const normalized = normalize(data, cardSchema)

    return { entities: normalized.entities }
  }
)

const cardAdapter = createEntityAdapter()

export const cardSlice = createSlice({
  name: 'card',
  initialState: cardAdapter.getInitialState(),
  reducers: {},
  extraReducers: {
    [fetchCardsById.fulfilled]: (state, action) => {
      cardAdapter.upsertMany(state, action.payload.entities.card)
    },
    [toggleCardById.fulfilled]: (state, action) => {
      cardAdapter.upsertOne(state, action.payload.entities.card)
    }
  }
})

export const {} = cardSlice.actions

export const {
  selectById: selectCardById,
  selectIds: selectCardIds,
  selectEntities: selectCardEntities,
  selectAll: selectAllCards,
  selectTotal: selectTotalCards
} = cardAdapter.getSelectors(state => state.card)

export default cardSlice.reducer
